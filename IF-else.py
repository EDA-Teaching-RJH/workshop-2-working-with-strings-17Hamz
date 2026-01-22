import random

def main():
    secret_number = random.randint(1, 10)
    print (secret_number)
    x =  int(input("guess the number? "))
    function(x,secret_number)

def function (guess,sn):
    if guess > sn:
        print ("Too high")
    elif guess < sn:
        print("Too low")
    else:
        print("correct")
    
main()