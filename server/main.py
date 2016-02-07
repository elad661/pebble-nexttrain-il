#!/usr/bin/python3
# coding=utf-8
# Copyright (C) 2015 Elad Alfassa <elad@fedoraproject.org>
import argparse
import cherrypy
import dateutil.parser
import os.path
import pytz
import requests
import requests_cache
import stations
from bs4 import BeautifulSoup
from datetime import datetime

requests_cache.install_cache(expire_after=900)

tz = pytz.timezone('Asia/Jerusalem')
base_uri = "http://rail.co.il/EN/DrivePlan/Pages/DrivePlan.aspx"
base_query = {"DrivePlanPage": "true",
              "HoursDeparture": "all",
              "MinutesDeparture": 0,
              "GoingHourDeparture": "true",
              "ArrivalHourDeparture": "false",
              "GoingHourReturn": "true",
              "ArrivalHourReturn": "false",
              "IsReturn": "false",
              "IsFullURL": "true"}


def get_timetable(origin_id, dest_id):
    today = datetime.now(tz=tz).date().isoformat()
    query_params = {"OriginStationId": origin_id,
                    "OriginStationName": stations.by_id[origin_id],
                    "DestStationId": dest_id,
                    "DestStationName": stations.by_id[dest_id],
                    "GoingTrainCln": today,
                    "ReturnningTrainCln": today}
    query_params.update(base_query)
    session = requests.Session()
    session.get(base_uri, params=query_params)
    query_params['isExcel'] = 'true'  # actually not excel, but a bare HTML file which is easier to parse
    # Doing two queries because the website is not stateless :(
    timetable_html = session.get(base_uri, params=query_params).text
    parser = BeautifulSoup(timetable_html, "lxml")
    timetable = parser.find_all('table')[-1]  # Last table in the page is the timetable
    out = []
    column_names = ['Train#', 'Platform', 'Departure', 'Arrival', 'Duration', 'Transfers', 'extra', 'route_type']
    for row in timetable.find_all('tr'):
        out.append({col: cell.text.strip() for col, cell in zip(column_names, row.find_all('td'))})
    out.pop(0)  # remove column headers
    return(out)


class App(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.etags(autotags=True)
    def next_trains(self, origin_id, dest_id):
        if origin_id not in stations.by_id or dest_id not in stations.by_id:
            cherrypy.response.status = "404 Not Found"
            return {'error': 'invalid station'}
        now = datetime.now(tz=tz)
        timetable = get_timetable(origin_id, dest_id)
        out = []
        for train in timetable:
            departure = tz.localize(dateutil.parser.parse(train['Departure']))
            if departure >= now:
                train['departure_timestamp'] = departure.timestamp()
                out.append(train)
        return out

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.etags(autotags=True)
    def get_stations(self):
        return stations.stations


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', '-p', nargs='?', default=8080, help='Specify port number to listen on (default is 8080')
    args = parser.parse_args()

    if args.port is not None and int(args.port) > 65535 or int(args.port) < 0:
        print("Invalid port number %s!" % args.port)
        return
    elif args.port is not None:
        cherrypy.config.update({'server.socket_port': int(args.port)})
    cherrypy.quickstart(App())

if __name__ == '__main__':
    main()
