# Just playing around with ElementTree. Parses the MyFounds list from GC.com and prints caches in order by date
# Roger Banks
# 25 Nov 2015

def format_date(str):
    temp = str.split('T')[0].split('-')
    return date(int(temp[0]), int(temp[1]), int(temp[2])).strftime('%Y-%m-%d')

import xml.etree.ElementTree as ET
from datetime import date

ns = {'gpx': 'http://www.topografix.com/GPX/1/0',
      'cache': 'http://www.groundspeak.com/cache/1/0/1'}

count = 0
my_caches = []
tree = ET.parse('8255490.gpx')
root = tree.getroot()

for wpt in root.findall('gpx:wpt', ns):
    gc_num = wpt.find('gpx:name', ns).text
    desc = wpt.find('gpx:desc', ns).text
    placed_date_str = wpt.find('gpx:time', ns).text
    cache = wpt.find('cache:cache', ns)
    container = cache.find('cache:container', ns).text
    name = cache.find('cache:name', ns).text
    owner = cache.find('cache:owner', ns).text
    type = cache.find('cache:type', ns).text
    difficulty = cache.find('cache:difficulty', ns).text
    terrain = cache.find('cache:terrain', ns).text
    country = cache.find('cache:country', ns).text
    state = cache.find('cache:state', ns).text
    logs = cache.find('cache:logs', ns)
    log = logs.find('cache:log', ns)
    found_date_str = log.find('cache:date', ns).text

    placed_date = format_date(placed_date_str)
    found_date = format_date(found_date_str)
    format_dt = '(' + difficulty + '/' + terrain + ')'

    my_caches.append([found_date, gc_num, name, owner, type, format_dt, container, country, state])
    count += 1
my_caches.sort()
for cache in my_caches:
    print(cache)
print(count)

#    print(root.tag, root.attrib)
#    print sorted list of found caches [(date_found, gc_num, name, owner, type, container, lat, lon)]
#    print(name, desc, find_date, time[1], wpt.attrib['lat'], wpt.attrib['lon'], container, found_date)
#    print found_date, gc_num, name, owner, type, terrain, difficulty, container
