#!/usr/bin/python3

import csv

result = []

for line in open('data-src/unihan/Unihan_RadicalStrokeCounts.txt').readlines():
	line = line.strip()
	if not len(line) or line[0] == '#':
		continue
	unicodeHex, prop, value = line.split('\t')
	if prop == 'kRSKangXi':
		radical, stroke = value.split('.')
		radical = int(radical)
		unicode = int(unicodeHex[2:], 16)
		result.append((chr(unicode), chr(0x2f00 + radical - 1), unicodeHex, unicode, radical, stroke))

writer = csv.writer(open('out/kangxi.csv', 'w'))
writer.writerow(('Character','Kangxi Radical Character', 'Unicode (hex)', 'Unicode (dec)', 'Kangxi Radical Index', 'Kangxi Stroke'))
writer.writerows(result)
