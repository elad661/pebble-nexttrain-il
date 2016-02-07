Next Train (Israel) for Pebble
==============================

This is a tiny app for the Pebble smartwatch for people who use trains in Israel.

It allows you to see when your next train home is due to leave directly from your watch,
instead of having to look at your phone.

By default, the app looks for trains form the nearest station, to a pre-defined destination.
If the nearest station is the pre-defined destination, it will instead search for trains to the pre-defined "home station", so on your daily commute you don't need to fiddle with the app to get information that is relevant to you.

While using the app, you can change the search parameters using the top and middle buttons.

Use the **top button** to select a different **origin station**. The station on the list will be sorted by distance from your current location.

Use the **middle button** to select a different **destination**. The station on the list will be sorted by distance from your current location.

Use the **lower button** to show a list of trains after this one.

It works okay, but the UI is not polished or colurful.

**Known Issues**

As of now, the app doesn't handle night trains very well if you opened it before midnight and the next train is after midnight. Since night trains are not very common in Israel, I didn't bother to implement this, but I might do so in the future.

There's no UI to configure the default "home" and "destination" stations. Instead, you have to manually edit `app.js`. I might add it in the future.

Because of these two issues and the lack of logo, the app is not published in the pebble app store.

Server
------

The server is a simple Python3 app based on cherrypy. It has the following dependencies:
 * BeautifulSoup4
 * cherrypy
 * dateutil
 * pytz
 * requests
 * requests_cache

to start it simply execute `python3 server/main.py`.
