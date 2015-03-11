### About:

Musicbrainz_discid calculates the disc ID of a CD and then prints matching
releases from the MusicBrainz database.

### Dependencies:

* python2
* python-discid
* python-musicbrainzngs

### Usage:

Insert a CD, then run

	$ ./musicbrainz_discid.py

If python-discid does not select the correct drive automatically, you can pass
the device path:

	$ ./musicbrainz_discid.py /dev/sr1
