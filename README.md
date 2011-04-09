Tulsa Transit Database - Prototype
==================================
This is a prototype of a database of Tulsa Transit information.  The end goal is to get Tulsa's buses onto Google Maps.  This hack is sponsored by [tulsa Web Devs](http://tulsawebdevs.org/).

Files
-----
The folder `tulsa-transit-proto` is a [Google App Engine](http://code.google.com/appengine/) project.  The live version runs at *todo*, but you can run it locally once you install the [SDK](http://code.google.com/appengine/downloads.html).

Google Transit Partner Program
------------------------------
The process as given on the [Google Transit Partner Program page]:

1. Prepare a data feed according to [General Transit Feed Specification](http://code.google.com/transit/spec/transit_feed_specification.html) and [Best Practices](http://maps.google.com/help/maps/transit/partners/bestpractices.html) document.
2. Validate the feed using the [Feed Validator](http://code.google.com/p/googletransitdatafeed/wiki/FeedValidator).
3. Inspect the feed in [Schedule Viewer](http://code.google.com/p/googletransitdatafeed/wiki/ScheduleViewer).
4. Zip the files in your feed. Name the zip file google_transit.zip.
5. [Host](http://maps.google.com/help/maps/transit/partners/participate.html#host) the feed on a web server for Google to fetch. We support both HTTP and HTTPS.
6. [Contact](http://maps.google.com/help/maps/transit/partners/contactus.html) the Google Transit team to sign-up for the partnership
7. Google will be in touch to setup a private preview and have the agency complete an online agreement before launch.
8. Agency will test the data in the private preview until the result is satisfactory.
9. Launch!

We're working with the Tulsa Transit Authority to get whatever data they have, and in order to ship Google Maps integration, we'll need their cooperation.

If Tulsa Transit Authority's data is unavailable or unsuitable for Google Maps, it appears that a small group of volunteers could do all the data collection, entry, and manipulation needed to get a valid data feed (up to step 6 in the process).  This project is an experiment to see how quickly and easily we can get there.

