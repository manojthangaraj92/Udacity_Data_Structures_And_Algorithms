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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
#Create an empty list to append all the numbers O(1)
tel_num = []

#loop through the text records   O(n)
for num in texts:
    tel_num.append(num[0])
    tel_num.append(num[1])

#Loop through the calls records   O(n)    
for num in calls:
    tel_num.append(num[0])
    tel_num.append(num[1])

#Loop through the final list and replace paranthesis and empty spaces inside the string   O(n)
tel_num = [num.replace('(','').replace(')','').replace(' ','') for num in tel_num]

print(f'There are {len(set(tel_num))} different telephone numbers in the records.')