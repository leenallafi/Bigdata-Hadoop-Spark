#!/usr/bin/env python3
#there is no DataFrame :) :)
#There is another solution in the docstring; please take a look :)
#We searched and found that the first solution (A more advanced Reducer, using Python iterators and generators)
#first solution was inspired by a reference, where we got the idea(link) ( https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/ )  :) :) 
#this solution (1st on) was more complex than the 2nd solution.
#The second solution is simpler, so thanks a looooot for making things easier to understand. :)
import sys

def read_input(file):
    for line in file:
        # Assuming that the web page is represented as "/file_XX.html"
        try:
            p1, p2, view_purchase, item = line.strip().split(',')
        except ValueError:
            # Handle the case where the line doesn't have enough elements
            print(f"Skipping invalid line: {line}")
            continue

        # Ignore "add_to_cart"
        if view_purchase == "add_to_cart":
            continue

        yield f"{item}\t{view_purchase}"

def main():
    data = read_input(sys.stdin)
    for result in data:
        print(result)

if __name__ == "__main__":
    main()

    
"""
#!/usr/bin/env python3
import sys

for line in sys.stdin:
    try:
        line = line.strip()
        p1, p2, view_purchase, item = line.split(',')
    except ValueError:
        # Handle the case where the line doesn't have enough elements
        print(f"Skipping invalid line: {line}")
        continue
        
    if view_purchase == "add_to_cart":
        continue

    print(f"{item}\t{view_purchase}")
"""    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

