#add import

import question_d
question_d.write_file("stocklist.txt")
dictionary = question_d.get_stock_list("stocklist.txt")

while True:
    print ("menu")
    print ("1 - Display purchase stock history ")
    print("2 - exit ")
    option = str(input("choose 1 or 2 "))
    while option not in ('1', '2'):
                         option = str(input("Invalid, Choose 1 or 2 "))
    if option == '1':
            print (" Stock purchase history ")
            for symbol, stocks in dictionary.items():
                    print(f"{str(stocks.get_company_name()).ljust(14)} {stocks.get_symbol()}")
            print("")

    elif option == '2':
            print ("Exiting")
            break