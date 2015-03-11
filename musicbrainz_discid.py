#!/usr/bin/env python2

# Requires python-discid and python-musicbrainzngs

import os
import sys
import discid
import musicbrainzngs as ws

if len(sys.argv) > 2 or (len(sys.argv) == 2 and sys.argv[1] == "-h"):
	print("usage: {0:s} [device]".format(os.path.basename(sys.argv[0])))
	exit(1)
elif len(sys.argv) == 2:
	device = sys.argv[1]
else:
	device = discid.get_default_device();

print("Device: " + device)

disc = discid.read(device=device)
print("Disc ID: " + disc.id)
print("TOC:     " + disc.toc_string)

ws.set_useragent("musicbrainz_discid", "0.1")
r = ws.get_releases_by_discid(disc.id, toc=disc.toc_string, cdstubs=False, includes=["artists", "recordings", "labels"])

if 'disc' in r and r['disc']['release-count'] > 0:
	print("Disc ID found")
	releases = r['disc']['release-list']
elif 'release-list' in r and len(r['release-list']) > 0:
	print("TOC search succeeded")
	releases = r['release-list']
else:
	print("Release not found")
	exit(1)

rnum = 1
for x in releases:
	print("Release " + str(rnum) + ":")
	print("  ID:     " + x['id'])
	print("  URL:    http://musicbrainz.org/release/" + x['id'])
	print("  Title:  " + x['title'] + " ["
		+ (x['release-event-list'][0]['date'] if 'release-event-list' in x and 'date' in x['release-event-list'][0] else "<no date>")
		+ ", " + (x['country'] if 'country' in x else "<no country>")
		+ ", " + (x['label-info-list'][0]['label']['name'] if x['label-info-count'] > 0 else "<no label>") + "]")
	print("  Artist: " + x['artist-credit'][0]['artist']['name'])
	print("  Tracks:")
	for x in x['medium-list']:
		print("    " + x['format'] + " " + str(x['position']) + ":")
		tnum = 1
		for x in x['track-list']:
			print("      " + "{0:02d} ".format(tnum) + x['recording']['title'])
			tnum += 1
	rnum += 1
