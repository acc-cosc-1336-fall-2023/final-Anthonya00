#add import
import question_a

while True:
    print("\nmenu")
    print("option 1 - create table")
    print("option 2 - exit menu")

    option =  str(input ("Pick a number: "))

    while option not in ("1" , "2"):
        option = str(input("ERROR pick 1 or 2: "))

    if option ==  "1":
        Row = int(input("input a number for the number of rows : "))
        colum = int(input("input a number for the number of columns :  "))

        table = question_a.create_multiplication_table(Row, colum)
        
        question_a.display_multiplication_table(table)
    elif option == "2":
        print ("exiting program")
        break

    



    



