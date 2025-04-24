#!/usr/bin/env python3
#There is another solution in the docstring; please take a look :)
#We searched and found that the first solution (A more advanced Reducer, using Python iterators and generators)
#first solution was inspired by a reference, where we got the idea(link) ( https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/ ):) :) 
#this solution (1st one) was more complex.
#The second solution is simpler, so thanks a looooot for making things easier to understand. :) 

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator=' '):
    # Generator function to read and yield lines from the input file
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    # Input data comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    for web_page, group in groupby(data, itemgetter(0)):
        try:
            # Calculate the total count for the current web_page
            total_count = sum(int(count) for web_page, count in group)
            # Print the result in the format "<web_page><separator><total_count>"
            print(f"{web_page}{separator}{total_count}")
        except ValueError:
            # If count was not a number, silently discard this item
            print(f"Invalid count value for {web_page}. Skipping.")
        except Exception as e:
            # Handle other exceptions (if any) and print an informative message
            print(f"An error occurred for {web_page}: {str(e)}")

# Entry point for the script
if __name__ == "__main__":
    main()

""".
#!/usr/bin/env python3
import sys
current_web_page=None
current_count=0
web_page=None
for line in sys.stdin:
   line=line.strip()
   web_page,count=line.split('\t',1)
   count=int(count)
   if current_web_page==web_page:
       current_count+=count
   else:
       if current_web_page:
           print(current_web_page,"\t",current_count)
       current_count=count
       current_web_page=web_page
if current_web_page== web_page:
   print(current_web_page,current_count)     
"""    
