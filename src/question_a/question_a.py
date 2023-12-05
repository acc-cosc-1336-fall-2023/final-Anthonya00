#write functions here, don't add input('') statements here!
def test_config():
    return True

def create_multiplication_table(X,Y): 
    numbers = []

    for list1 in range(1 , X + 1): 
        row = []
        list1 * 1 
        for i in range (1, Y + 1):
            product = list1 * i  

            row.append (product)

        numbers.append (row)

    return numbers 

def display_multiplication_table(numbers):
    for X in range(len(numbers)):  
        print("")
        for Y in range(len(numbers[X])):
            print (str(numbers[X][Y]).ljust(4) ,end = " " )





