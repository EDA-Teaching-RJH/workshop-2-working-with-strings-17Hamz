def main ():
    x = int(input("What is your age? "))
    function(x)

def function (x):
 if x > 18:
    print("you are an adult")
 if x < 18:
    print("you are a child")

main()