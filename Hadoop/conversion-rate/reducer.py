#!/usr/bin/env python
#there is no DataFrame :) :)
#There is another solution in the docstring; please take a look :)
#We searched and found that the first solution (A more advanced Reducer, using Python iterators and generators)
#first solution was inspired by a reference, where we got the idea(link) ( https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/ )  :) :) 
#this solution (1st on) was more complex than the 2nd solution.
#The second solution is simpler, so thanks a looooot for making things easier to understand. :)
from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        try:
            item, view_purchase = line.strip().split(separator)
            yield item, view_purchase
        except ValueError:
            # Skip invalid lines
            print(f"Skipping invalid line: {line}")

def calculate_conversion_rates():
    data=read_mapper_output(sys.stdin, separator='\t')
    grouped_lines = groupby(data, itemgetter(0))

    for item, group in grouped_lines:
        views = 0
        purchases = 0

        for item, view_purchase in group:
            if view_purchase == 'view':
                views += 1
            elif view_purchase == 'purchase':
                purchases += 1

        try:
            conversion_rate = purchases / views
        except ZeroDivisionError:
            conversion_rate = 0

        print(f"Intermediate result: {item}\t{conversion_rate}")

def main(separator='\t'):
    calculate_conversion_rates()

if __name__ == "__main__":
    main()


"""
#solution2 
#!/usr/bin/env python3
import sys

current_item = None
views = 0
purchases = 0

for line in sys.stdin:
    line = line.strip()
    item, view_purchase = line.split('\t' )

    if current_item is None:
        current_item = item
       

    # Update counts for the current item
    if current_item == item:
        if view_purchase == 'view':
            views += 1
        elif view_purchase == 'purchase':
            purchases += 1
    else:
        # Output conversion rate when moving to a new item
        try:
            conversion_rate = purchases / views
        except ZeroDivisionError:
            # Handle division by zero
            conversion_rate = 0

        print(f"Intermediate result: {current_item}\t{conversion_rate}")

        # Start counting for the new item
        current_item = item
        views = 1 if view_purchase == 'view' else 0
        purchases = 1 if view_purchase == 'purchase' else 0

# Output the last item's conversion rate
try:
    conversion_rate = purchases / views
except ZeroDivisionError:
    # Handle division by zero
    conversion_rate = 0

print(f"Final result: {current_item}\t{conversion_rate}")
"""



