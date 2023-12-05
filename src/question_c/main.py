#add import
import question_c

while True:
    print("\nmenu")
    print("option 1 - display stock history")
    print("option 2 - exit menu")

    option =  str(input ("Pick a number: "))

    while option not in ("1" , "2"):
        option = str(input("ERROR pick 1 or 2: "))

    if option == "1":
        question_c.stock_purchase_history()

    if option == "2":
         print ("exiting program")
         break
