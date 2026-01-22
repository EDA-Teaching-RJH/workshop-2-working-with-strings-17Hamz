import math  

def main():
    A = int(input("A"))
    B = int(input("B")) 
    result = pythag(A,B)
    print(result)
def pythag(A,B):
    C = math.sqrt (A**2) + (B**2)
    return C 

main()
