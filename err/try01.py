#!/usr/bin/python3
"""Review of try and except logic | Alta3 Research"""

#lab 73 https://live.alta3.com/content/tlg-sde-python/labs/content/pyb/LAB_try_except_else_finally.html

# Start with an infinite loop
while True:
    try:
        print("enter a file name: ")
        name = input()
        with open(name, "w") as myfile:
            myfile.write("No problems with that file name.")
        break
    except:
        print("Error with that file name! Try again...")