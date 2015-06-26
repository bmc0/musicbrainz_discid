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

### Example:

	$ ./musicbrainz_discid.py
	Device: /dev/cdrom
	Disc ID: AMCnTAkHnIR4.T8GauRbPTFgFs4-
	TOC:     1 13 225659 150 24164 38599 56819 71757 86549 100811 117609 137264 150660 165797 188724 209446
	Disc ID found
	Release 1:
	  ID:     1e365079-6577-409d-b8eb-f9a08b1b01d6
	  URL:    http://musicbrainz.org/release/1e365079-6577-409d-b8eb-f9a08b1b01d6
	  Title:  Short Movie [2015-03-23, US, Ribbon Music]
	  Artist: Laura Marling
	  Tracks:
		CD 1:
		  01 Warrior
		  02 False Hope
		  03 I Feel Your Love
		  04 Walk Alone
		  05 Strange
		  06 Don’t Let Me Bring You Down
		  07 Easy
		  08 Gurdjieff’s Daughter
		  09 Divine
		  10 How Can I
		  11 Howl
		  12 Short Movie
		  13 Worship Me
	Release 2:
	  ID:     31602cb0-76e7-4741-8519-b3cbd72b6eb1
	  URL:    http://musicbrainz.org/release/31602cb0-76e7-4741-8519-b3cbd72b6eb1
	  Title:  Short Movie [2015-03-23, GB, Virgin]
	  Artist: Laura Marling
	  Tracks:
		CD 1:
		  01 Warrior
		  02 False Hope
		  03 I Feel Your Love
		  04 Walk Alone
		  05 Strange
		  06 Don’t Let Me Bring You Down
		  07 Easy
		  08 Gurdjieff’s Daughter
		  09 Divine
		  10 How Can I
		  11 Howl
		  12 Short Movie
		  13 Worship Me
