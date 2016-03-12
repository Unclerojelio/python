# Just playing around with ElementTree. Parses the MyFounds list from GC.com and prints caches in order by date
# Roger Banks
# 25 Nov 2015

import xml.etree.ElementTree as ET
from datetime import date

count = 0
my_caches = []
tree = ET.parse('8255490.gpx')
root = tree.getroot()
print root.tag, root.attrib
for wpt in root.findall('{http://www.topografix.com/GPX/1/0}wpt'):
    gc_num = wpt.find('{http://www.topografix.com/GPX/1/0}name').text
    desc = wpt.find('{http://www.topografix.com/GPX/1/0}desc').text
    time = wpt.find('{http://www.topografix.com/GPX/1/0}time').text.split('T')
    date_str = time[0].split('-')
    find_date = date(int(date_str[0]), int(date_str[1]), int(date_str[2]))
    cache = wpt.find('{http://www.groundspeak.com/cache/1/0}cache')
    container = cache.find('{http://www.groundspeak.com/cache/1/0}container').text
    name = cache.find('{http://www.groundspeak.com/cache/1/0}name').text
    owner = cache.find('{http://www.groundspeak.com/cache/1/0}owner').text
    type = cache.find('{http://www.groundspeak.com/cache/1/0}type').text
    difficulty = cache.find('{http://www.groundspeak.com/cache/1/0}difficulty').text
    terrain = cache.find('{http://www.groundspeak.com/cache/1/0}terrain').text
    logs = cache.find('{http://www.groundspeak.com/cache/1/0}logs')
    log = logs.find('{http://www.groundspeak.com/cache/1/0}log')
    found_date = log.find('{http://www.groundspeak.com/cache/1/0}date').text
    format_dt = '(' + difficulty + '/' + terrain + ')'
#    print name, desc, find_date, time[1], wpt.attrib['lat'], wpt.attrib['lon'], container, found_date
#    print found_date, gc_num, name, owner, type, terrain, difficulty, container
    my_caches.append([found_date, gc_num, name, owner, type, format_dt, container])
    count += 1
my_caches.sort()
for cache in my_caches:
     print cache
print count

# print sorted list of found caches [(date_found, gc_num, name, owner, type, container, lat, lon)]