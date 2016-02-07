"use strict";
// Copyright (C) 2016 Elad Alfassa <elad@fedoraproject.org>
var UI = require('ui');
var Vibe = require('ui/vibe');
var Light = require('ui/light');
var ajax = require('ajax');
var BASE_URL = 'https://cloud.eladalfassa.com/train/';
var stations = [];
var saved_schedule = [];
var nearest_station;
/* The following are personal settings for my commute, if I wanted to actually
   publish this app to the pebble appstore, I would make this user-configurable
   on runtime.

   For now, change the values here for your regular home station
   and destination station.*/
var dest_station = '3600';
var regular_dest = '3600';
var regular_home = '4170';

if (typeof Number.prototype.toRad == 'undefined') {
  Number.prototype.toRad = function() {
    return this * Math.PI / 180;
  };
}

function seconds_to_str(in_seconds) {
    in_seconds = Number(in_seconds);
    var ret = "";
    var hours = Math.floor(in_seconds / 3600);
    var minutes = Math.floor(in_seconds % 3600 / 60);
    if (hours > 0) {
       ret = hours + " hours";
    }
    if (minutes > 0) {
        if (ret != "") {
           ret+=', ';
        }
        ret += minutes + " mins";
    }
    if (minutes <= 1) {
    	ret = "Now";
    }
    return ret;
}



function approx_distance(lat1, lat2, lon1, lon2) {
    if (lat1 === undefined || lat2 === undefined || lon1 === undefined || lon2 === undefined)
        return;
    if (lat1 == "" || lat2 == "" || lon1 == "" || lon2 == "")
        return;
    var R = 6371; // Earth radius in km
    var x = (lon2-lon1).toRad() * Math.cos((lat1+lat2).toRad()/2);
    var y = (lat2-lat1).toRad();
    var d = Math.sqrt(x*x + y*y) * R;
    return d * 1000; //return in meters
}

function compare_distance(a,b) {
  if (a.distance < b.distance)
    return -1;
  else if (a.distance > b.distance)
    return 1;
  else
    return 0;
}

var searching_window = new UI.Card({
    title: 'Next Train',
    subtitle: 'Finding trains...'
});

var loading_window = new UI.Card({
  title: 'Next Train',
  subtitle: 'Finding nearest station...'
});

loading_window.show();

var main_window = new UI.Card({
    title: 'Next Train',
});

main_window.on('click', 'up', function(e) {
    // Select origin station
    var menuitems = [];
    for (var i=0; i<stations.length; i++) {
        menuitems.push({'title': stations[i].name});
    }
    var menu = new UI.Menu({
        sections: [{
            title: "Select origin station",
            items: menuitems
        }]
    });
    menu.on('select', function(e) {
        nearest_station = stations[e.itemIndex];
        searching_window.body('From ' + nearest_station.name);
        menu.hide();
        searching_window.show();
        find_trains();
    });
    menu.show();
});

main_window.on('click', 'select', function(e) {
    // Select destination station
    var menuitems = [];
    for (var i=0; i<stations.length; i++) {
        menuitems.push({'title': stations[i].name});
    }
    var menu = new UI.Menu({
        sections: [{
            title: "Select destination",
            items: menuitems
        }]
    });
    menu.on('select', function(e) {
        dest_station = stations[e.itemIndex].id;
        searching_window.body('From ' + nearest_station.name +'\nTo ' + e.item.title);
        menu.hide();
        searching_window.show();
        find_trains();
    });
    menu.show();
});

main_window.on('click', 'down', function(e) {
    // Show schedule
    var menuitems = [];
    for (var i=0; i<saved_schedule.length; i++) {
        var train = saved_schedule[i];
        var moreinfo = "";
        if (train.Transfers == "Without changing")
            moreinfo = "Direct";
        else
            moreinfo = train.Transfers + " transfers";
        moreinfo += "," + train.Duration;
        menuitems.push({'title': train.Departure,
                        'subtitle':  moreinfo});
    }
    var menu = new UI.Menu({
        sections: [{
            title: "Schedule",
            items: menuitems
        }]
    });
    menu.show();
});


var locationOptions = {
  enableHighAccuracy: true,
  maximumAge: 60000,
  timeout: 100000
};

function locationError(err) {
  console.log('location error (' + err.code + '): ' + err.message);
  show_error('location error (' + err.code + '): ' + err.message);
}

// Request current position
ajax({url: BASE_URL + 'get_stations', type: 'json'},
     function(station_list) {
        // Success!
        console.log('Successfully fetched station list');
        navigator.geolocation.getCurrentPosition(function (position) {
            var nearest_distance = Infinity;
            console.log('Found location lat=' +  position.coords.latitude + ' lon=' +position.coords.longitude);
            for (var i=0; i<station_list.length; i++) {
                var distance = approx_distance(parseFloat(station_list[i].lat), position.coords.latitude, parseFloat(station_list[i].lon), position.coords.longitude);
                station_list[i].distance = distance || Infinity;
                if (distance < nearest_distance) {
                    nearest_station = station_list[i];
                    nearest_distance = distance;
                }
            }
            stations = station_list;
            stations.sort(compare_distance);
            // For debug: 3700 = Savidor center
            //nearest_station.id = '3700';
            // If we're at our "home" station, we probably want to get to our regular destination (In my case: Tel Aviv)
            // But if we're in some other place, we usually want to get home.
            if (nearest_station.id == regular_home)
                dest_station = regular_dest;
            else
                dest_station = regular_home;
            console.log("nearest station: " + nearest_station.name);
            loading_window.hide();
            searching_window.body('From ' + nearest_station.name);
            searching_window.show();
            find_trains();
        }, locationError, locationOptions);
     },
     function(error) {
        // Failure!
        console.log('Could not fetch station list: ' + error);
        show_error('Could not fetch station list: ' + error);
     }
);

function find_trains() {
    ajax(
      {
        url: BASE_URL + 'next_trains?origin_id='+nearest_station.id+'&dest_id='+dest_station,
        type: 'json'
      },
      function(schedule) {
        // Success!
        console.log('Successfully fetched schedule');
        saved_schedule = schedule;
        if(schedule.length === 0) {
            no_trains();
        }
        process_schedule(schedule);
      },
      function(error) {
        // Failure!
        console.log('Could not fetch schedule: ' + error);
        show_error('Could not fetch schedule: ' + error);
      }
    );
}
var time_update_interval = false;
function process_schedule(schedule) {
        if (time_update_interval) {
            clearInterval(time_update_interval);
            time_update_interval = false;
        }
        var now = Date.now() / 1000;
        var found_train = false;
        var our_train;
        for (var i=0; i<schedule.length; i++) {
            if (schedule[i].departure_timestamp >= now) {
                var waiting_time = seconds_to_str(schedule[i].departure_timestamp - now);
                var transfers = '';
                main_window.subtitle(waiting_time);
                if (schedule[i].Transfers != "Without changing") {
                    transfers = "\nWith " + schedule[i].Transfers + " transfer";
                    if (schedule[i].Transfers > 1)
                        transfers += 's';
                }

                main_window.body('\nPlatform ' +schedule[i].Platform + transfers);
                searching_window.hide();
                main_window.show();
                found_train = true;
                our_train = schedule[i];
                break;
            }
        }
        if (!found_train)
            no_trains();
        Vibe.vibrate('short');
        Light.trigger();
        var vibrated_for_this_train = false;
        time_update_interval = setInterval(function() {
            var now = Date.now() / 1000;
            var waiting_time;
            if (now > our_train.departure_timestamp) {
                process_schedule(schedule);
                return;
            } else if (our_train.departure_timestamp - now < 60) {
                waiting_time = "Now";
                if (!vibrated_for_this_train) {
                    Vibe.vibrate('double');
                    Light.trigger();
                    vibrated_for_this_train = true;
                }
            } else {
                waiting_time = seconds_to_str(our_train.departure_timestamp - now);
            }
            main_window.subtitle(waiting_time);
        }, 10000);

}
function no_trains() {
    if (time_update_interval) {
        clearInterval(time_update_interval);
        time_update_interval = false;
    }
    main_window.subtitle();
    main_window.body('No trains :(');
    searching_window.hide();
    main_window.show();
}

function show_error(error) {
    if (time_update_interval) {
        clearInterval(time_update_interval);
        time_update_interval = false;
    }
    main_window.subtitle("Error");
    main_window.body(error);
    searching_window.hide();
    loading_window.hide();
    main_window.show();
}
