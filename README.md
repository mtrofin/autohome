# autohome

Personal project for an electrified home with Powerwall. It enables automatic power outage detection, upon which it turns off all major power consumers - like heating/AC and water. This is particularly useful if an outage happens in the middle of the night or while on holiday.

It also supports time-based scheduling - e.g. avoid heating the water tank during the high cost period, as it adds little value (there's usually sufficient hot water in a tank for normal kitchen / bathroom use for a few hours).


Note: the "tests" aren't true unit tests. They are rather a convenient way to verify a local configuration.

Deployment: I have this deployed as a cron job running every 5 minutes on a raspeberry pi 4.
