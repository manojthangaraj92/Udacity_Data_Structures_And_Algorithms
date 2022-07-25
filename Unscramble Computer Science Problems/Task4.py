"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

outgoing_calls = set([item[0] for item in calls])  #O(n)
incoming_calls = set([item[1] for item in calls])   #O(n)
outgoing_texts = set([item[0] for item in texts])   #O(n)
incoming_texts = set([item[1] for item in texts])   #O(n)

telemarketing_num = []   #O(1)

for num in outgoing_calls:    #O(n)
    if (num not in outgoing_texts) and (num not in incoming_texts) and (num not in incoming_calls):
        telemarketing_num.append(num)
        
numbers = sorted(telemarketing_num)    # O(n log n)

print(f'These numbers could be telemarketers: \n')

for item in numbers:   # O(n)
    print(f'{item}\n')