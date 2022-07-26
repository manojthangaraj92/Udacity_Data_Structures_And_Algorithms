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

def get_val(items):
    my_dict = {}     #O(1)
    for item in items:       #O(n)
        if item[0] in my_dict:
            my_dict[item[0]] += int(item[3])
        else:
            my_dict[item[0]] = int(item[3])
            
        if item[1] in my_dict:
            my_dict[item[1]] += int(item[3])
        else:
            my_dict[item[1]] = int(item[3])
            
    return my_dict

result = get_val(calls)

max_time = max(zip(result.values(), result.keys()))           #O(n)

print(f'{max_time[1]} spent the longest time, {max_time[0]} seconds, on the phone during September 2016.')