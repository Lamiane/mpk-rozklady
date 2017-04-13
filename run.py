import urllib
import re
from collections import OrderedDict
import pandas as pd
import numpy as np

with open('linki.txt') as f:
    links = f.readlines()

schedules = OrderedDict()
line_numbers = []
for link in links:
    if link == '':
        continue

    line_number = re.search('line.[0-9]+', link).group(0)[5:]
    print 'przetwarzam linie', line_number
    
    f = urllib.urlopen(link)
    content = f.read()
    
    times = {}
    start = False
    for line in content.split('\n'):
        if "table margin-auto" in line:
            start = True
        if not start:
            continue
        
        if "first" in line:
            hour = re.search('[0-9]+', line).group(0)
            if hour not in times.keys():
                times[hour] = []
        if "href" in line:
            h_m = re.findall('time.[0-9]+.[0-9]+', line)
            for group in h_m:
                hour = group.split(':')[0][5:]
                minutes = group.split(':')[1]
                times[hour].append(minutes)
        if "footer-schedule" in line:
            break
    schedules[line_number] = times


# making times sorted and valid for pandas
data = np.chararray(shape=(24, len(schedules.keys())), itemsize=10, unicode=True )

for line_index, line in enumerate(sorted([int(i) for i in schedules.keys()])):
    times = schedules[str(line)]
    for hour in sorted([int(i) for i in times.keys()]):
        hour = str(hour)
        minutes = ' '.join(sorted(times[hour]))
        data[int(hour), line_index] =  minutes


#print schedules
df = pd.DataFrame(data, columns=schedules.keys(), index=range(24))
print df
df.to_csv('rozklady.csv')
print 'saved to file'

