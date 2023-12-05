#add import
import question_b
from question_b import get_most_likely_ancestor_consensus

while True:
    print("\nmenu")
    print("option 1 - compare strings")
    print("option 2 - exit menu")

    option =  str(input ("Pick a number: "))

    while option not in ("1" , "2"):
        option = str(input("ERROR pick 1 or 2: "))

    if option == "1":
        while True: 
            something = str(input("Create a string: "))
            if question_b.validate_string1(something) == "Invalid" :
                print("String not between 8-16 characters ")
            else:
                break

        while True:
            other_thing = str(input("create substring: ")) 
            if question_b.validate_substring(other_thing) == "Invalid" :
                print("String is not equal to 4 characters ")
            else:
                break

        result = get_most_likely_ancestor_consensus(something, other_thing) 
        print("results: ")

        for i in range(len(result)): 
            print(result [i])

    elif option == "2":
        print ("exiting program")
        break

    


