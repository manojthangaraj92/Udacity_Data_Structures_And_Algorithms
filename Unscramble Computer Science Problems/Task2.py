"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def max_duration(items):                              
    max_item = max([int(item[3]) for item in items])    #O(n)
    for i in items:                                     #O(n)
        if int(i[3]) == max_item:
            return i
            break
        else:
            continue
result = max_duration(calls)
print(f'{result[1]} spent the longest time, {result[3]} seconds, on the phone during September 2016.')