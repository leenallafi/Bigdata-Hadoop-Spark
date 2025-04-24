#!/usr/bin/env python3
#There is another solution in the docstring; please take a look :)
#We searched and found that the first solution (A more advanced Reducer, using Python iterators and generators)
#first solution was inspired by a reference, where we got the idea(link) ( https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/ ):) :) 
#this solution (1st one was more complex.
#The second solution is simpler, so thanks alooooot for making things easier to understand. :)
import sys

def read_input(file):
    for line in file:
        try:
            # Assuming that the web page is represented as "/file_XX.html"
      
            line = line.strip()
            parts = line.split('\t')
            if len(parts) == 3:
                timestamp, ip_address, web_page = parts 
            else:
                raise ValueError("Invalid line format: Expected 3 elements.")
        except ValueError as e:
            # Handle the case where the line doesn't have the expected number of elements
            print(f"Error processing line: {line}. Reason: {e}")

        yield f"{web_page}\t1"

def main():
    data = read_input(sys.stdin)
    for result in data:
        print(result)

if __name__ == "__main__":
    main()

"""
#!/usr/bin/env python3
import sys

try:
	for line in sys.stdin:
	     line=line.strip()
	     timestamp, ip_address, web_page = line.split('\t')
	     print(f"{web_page}\t1") 
except ValueError as e:
        # Handle the case where the line doesn't have the expected number of elements
        print(f"Skipping invalid line: {line}. Error: {e}")
"""        

