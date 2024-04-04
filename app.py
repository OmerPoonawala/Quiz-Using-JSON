import json

def add(x,y):
    return (x+y)

def subtract(x,y):
    return (x-y)

def multiply(x,y):
    return (x*y)

def divide(x,y):
    return int(x/y)



print("Choose 1 to Create Quiz")
print("Choose 2 to Take Quiz")

qnadict = {}

choice1 = input("Choose option (1/2): ")

if choice1 == "1":

    print("select calculation")
    print("select 1 for add")
    print("selct 2 to subtract")
    print("select 3 to multiply")
    print("select 4 to divide")
    print("select 5 to end")
    runstate = True


    while runstate == True:
    
        choice = input("select (1/2/3/4/5): ")
        key = ""
        value = ""
        

        if choice in ('1','2','3','4'):

            try:
                num1 = int(input("Enter your first number: "))
                num2 = int(input("Enter your second number: "))
            except ValueError:
                print("Invalid Input. Enter a number")
                continue

        

        if choice == '1':
            key += str(num1) + " + " + str(num2)
            value += str(add(num1, num2))
            qnadict[key] = value
            print ("question added")

        elif choice == '2':
            key += str(num1) + " - " + str(num2)
            value += str(subtract(num1, num2))
            qnadict[key] = value
            print ("question added")

        elif choice == '3':
            key += str(num1) + " x " + str(num2)
            value += str(multiply(num1, num2))
            qnadict[key] = value
            print ("question added")


        elif choice == '4':
            try:
                key += str(num1) + " / " + str(num2)
                value += str(divide(num1,num2))
                qnadict[key] = value
                print ("question added")
                
            except ZeroDivisionError:
                print("Cannot divide by 0")
        
        else:
            print("Ended")
            runstate = False
    
    print(qnadict)
    # dump qnadict here
    quiz = open("mathsquiz.json", "w")
    json.dump(qnadict, quiz)
    quiz.close()


elif choice1 == "2":
    quiz = open("mathsquiz.json", "r")
    outfromjson = (quiz.read())
    data = json.loads(outfromjson)
    for key in data.keys():
        print(key)
        userans = input("Enter your answer here (as whole number): ")
        if userans == str(data[key]):
            print("Answer is correct!")
            
        else:
            print("Wrong. The correct answer to", key, "is", data[key])

else:
    print("Invalid format")







