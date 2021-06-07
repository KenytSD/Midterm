#midTerm
#name:Kenyt
#date:6_1_21

def play():

    number1 = eval(input("What's your first number: "))
    number2 = eval(input("What's your second number: "))
    total = (number1+number2)
    print ("What is the result of:",number1, "+",number2)
    number_student = 0

    while number_student != total:
        number_student = int(input("Enter your guess: "))
        if number_student == total:
            print("Congratulations")
        else:
            print("No,Try again!")

another = "Y"
while another == "Y":
    play()
    another = input("How about another game(Y/N)? ")