### About:

Musicbrainz_discid calculates the disc ID of a CD and then prints matching
releases from the MusicBrainz database.

### Dependencies:

* python2
* python-discid
* python-musicbrainzngs

### Usage:

#### Synopsis:

	musicbrainz_discid.py [-hjJ] [-i list] [device]

#### Flags:

Flag      | Description
----------|------------
`-h`      | Show help text
`-j`      | Use compact JSON output format
`-J`      | Use pretty-printed JSON output format
`-i list` | Set extra includes (comma separated). Currently only useful with JSON output.

### Example:

	$ ./musicbrainz_discid.py
	Device:  /dev/cdrom
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

### JSON example:

	$ ./musicbrainz_discid.py -J
	{
	  "device": "/dev/cdrom", 
	  "search-type": "discid", 
	  "disc": {
		"sectors": "256287", 
		"offset-list": [
		  150, 
		  47852, 
		  101887, 
		  152325
		], 
		"release-list": [
		  {
			"status": "Official", 
			"artist-credit": [
			  {
				"name": "Rachmaninoff", 
				"artist": {
				  "sort-name": "Rachmaninoff, Sergei", 
				  "disambiguation": "Sergei Rachmaninoff", 
				  "id": "44b16e44-da77-4580-b851-0d765904573e", 
				  "name": "\u0421\u0435\u0440\u0433\u0435\u0439 \u0420\u0430\u0445\u043c\u0430\u043d\u0438\u043d\u043e\u0432"
				}
			  }, 
			  "; ", 
			  {
				"artist": {
				  "sort-name": "New York Philharmonic", 
				  "id": "7cdb68bc-c4f1-4a92-9bd2-739641c5eff0", 
				  "name": "New York Philharmonic"
				}
			  }, 
			  ", ", 
			  {
				"artist": {
				  "sort-name": "Bernstein, Leonard", 
				  "id": "fa39bc82-9b27-4bbb-9425-d719a72e09ac", 
				  "name": "Leonard Bernstein"
				}
			  }, 
			  ", ", 
			  {
				"artist": {
				  "sort-name": "Graffman, Gary", 
				  "id": "97816210-708e-4792-ac23-34d10c671e5d", 
				  "name": "Gary Graffman"
				}
			  }
			], 
			"barcode": "0074643672221", 
			"label-info-count": 1, 
			"label-info-list": [
			  {
				"catalog-number": "SNYC 36722", 
				"label": {
				  "sort-name": "Sony Classical", 
				  "label-code": "6868", 
				  "id": "10920823-9ed8-45d9-adb3-69fc22475ab0", 
				  "name": "Sony Classical"
				}
			  }
			], 
			"cover-art-archive": {
			  "count": "1", 
			  "front": "true", 
			  "back": "false", 
			  "artwork": "true"
			}, 
			"release-event-list": [
			  {
				"date": "1988-02-12", 
				"area": {
				  "sort-name": "United States", 
				  "iso-3166-1-code-list": [
					"US"
				  ], 
				  "id": "489ce91b-6658-3307-9877-795b68554c98", 
				  "name": "United States"
				}
			  }
			], 
			"text-representation": {
			  "language": "mul", 
			  "script": "Latn"
			}, 
			"date": "1988-02-12", 
			"quality": "normal", 
			"id": "7def89ca-e77b-4db0-84d7-760ea2592d96", 
			"release-event-count": 1, 
			"title": "CBS Great Performances, Volume 9: Piano Concerto no. 2 / Rhapsody on a Theme of Paganini", 
			"country": "US", 
			"medium-count": 1, 
			"artist-credit-phrase": "Rachmaninoff; New York Philharmonic, Leonard Bernstein, Gary Graffman", 
			"medium-list": [
			  {
				"position": "1", 
				"track-count": 4, 
				"format": "CD", 
				"disc-list": [
				  {
					"offset-list": [
					  150, 
					  47852, 
					  101887, 
					  152325
					], 
					"id": "0w58cOF1RX6itd.eIsnJ_trchiM-", 
					"sectors": "256287", 
					"offset-count": 4
				  }, 
				  {
					"offset-list": [
					  182, 
					  47897, 
					  101912, 
					  152367
					], 
					"id": "8grrsCnXv_3UFSYy3eQA2uUkYWs-", 
					"sectors": "256195", 
					"offset-count": 4
				  }
				], 
				"track-list": [
				  {
					"recording": {
					  "length": "633800", 
					  "id": "5db2c551-65fc-4ea2-b4ff-5387d29a8a96", 
					  "title": "Piano Concerto no. 2 in C minor, op. 18: I. Moderato"
					}, 
					"length": "636026", 
					"title": "Concerto No. 2 in C minor, Op. 18: I. Moderato", 
					"position": "1", 
					"track_or_recording_length": "636026", 
					"id": "ac9661dc-3225-39c8-80cb-7675f127fe8f", 
					"number": "1"
				  }, 
				  {
					"recording": {
					  "length": "720000", 
					  "id": "bb14fb9f-e3c3-4ea2-9a5e-40474060517e", 
					  "title": "Piano Concerto no. 2 in C minor, op. 18: II. Adagio sostenuto"
					}, 
					"length": "720466", 
					"title": "Concerto No. 2 in C minor, Op. 18: II. Adagio sostenuto", 
					"position": "2", 
					"track_or_recording_length": "720466", 
					"id": "b4742914-0dcb-3c66-832d-85c2f5f0f1ca", 
					"number": "2"
				  }, 
				  {
					"recording": {
					  "length": "672506", 
					  "id": "360dab86-f8a0-49b1-828b-1298879e12c5", 
					  "title": "Piano Concerto no. 2 in C minor, op. 18: III. Allegro scherzando"
					}, 
					"length": "672506", 
					"title": "Concerto No. 2 in C minor, Op. 18: III. Allegro scherzando", 
					"position": "3", 
					"track_or_recording_length": "672506", 
					"id": "4df32d88-6c3c-3572-89ed-dfb02c0a9f2a", 
					"number": "3"
				  }, 
				  {
					"number": "4", 
					"recording": {
					  "length": "1386160", 
					  "id": "fcacecbd-9667-4802-845a-06195b4683a6", 
					  "title": "Rhapsody on a Theme of Paganini, Op. 43"
					}, 
					"length": "1386160", 
					"position": "4", 
					"id": "4168cc82-f9e6-3b5c-b653-19897d21bc49", 
					"track_or_recording_length": "1386160"
				  }
				], 
				"disc-count": 2
			  }
			]
		  }
		], 
		"offset-count": 4, 
		"release-count": 1, 
		"id": "0w58cOF1RX6itd.eIsnJ_trchiM-"
	  }, 
	  "success": true
	}
