#!/usr/bin/env python

import os
import sys
import getopt
import discid
import musicbrainzngs as ws

use_json = False
compact_json = True
extra_includes = []
device = None

def usage():
	print("Usage: {0:s} [-hjJ] [-i list] [device]".format(os.path.basename(sys.argv[0])))
	print("Flags:")
	print("  -h       Show this help")
	print("  -j       Use compact JSON output format")
	print("  -J       Use pretty-printed JSON output format")
	print("  -i list  Set extra includes (comma separated)")

# note: calling json_print() more than once will result in invalid JSON output
def json_print(obj):
	import json
	if compact_json:
		print(json.dumps(obj, separators=(',', ':')))
	else:
		print(json.dumps(obj, separators=(',', ': '), indent=2))

def die(str):
	if use_json:
		json_print({"success": False, "message": str, "device": device})
	else:
		print("error: " + str)
	exit(1)

try:
	optlist, args = getopt.gnu_getopt(sys.argv[1:], "hjJi:")
except getopt.GetoptError as e:
	print("error: " + str(e))
	usage()
	exit(2)
for o, a in optlist:
	if o == "-h":
		usage()
		exit(1)
	elif o in ("-j", "-J"):
		use_json = True
		compact_json = (o == "-j")
	elif o == "-i":
		extra_includes = a.split(",")
device = discid.get_default_device() if len(args) == 0 else args[len(args) - 1]

if not use_json:
	print("Device:  " + device)
try:
	disc = discid.read(device=device)
except discid.DiscError as e:
	die(str(e))
if not use_json:
	print("Disc ID: " + disc.id)
	print("TOC:     " + disc.toc_string)

ws.set_useragent("musicbrainz_discid", "0.1")
includes = ["artists", "recordings", "labels"] + extra_includes
try:
	r = ws.get_releases_by_discid(disc.id, toc=disc.toc_string, cdstubs=False, includes=includes)
except ws.MusicBrainzError as e:
	die(str(e))
if 'disc' in r and len(r['disc']['release-list']) > 0:
	search_type = "discid"
	releases = r['disc']['release-list']
elif 'release-list' in r and len(r['release-list']) > 0:
	search_type = "toc"
	releases = r['release-list']
else:
	die("Release not found")

if use_json:
	toc = list(map(int, disc.toc_string.split(None)))
	response = {
		"success": True, "device": device, "search-type": search_type,
		"disc": {
			"release-list": releases, "sectors": str(disc.sectors), "offset-count": len(toc) - 3,
			"release-count": len(releases), "offset-list": toc[3:], "id": disc.id
		}
	}
	json_print(response)
else:
	if search_type == "discid":
		print("Disc ID found")
	elif search_type == "toc":
		print("Fuzzy TOC search succeeded")
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
			print("    " + (x['format'] if 'format' in x else "Medium") + " " + str(x['position']) + ":")
			tnum = 1
			for x in x['track-list']:
				print("      " + "{0:02d} ".format(tnum) + x['recording']['title'])
				tnum += 1
		rnum += 1
