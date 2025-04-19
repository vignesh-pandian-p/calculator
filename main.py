from modules.addition import addition
from modules.subtraction import subtraction
from modules.multiplication  import multiplication
from modules.division import division
from modules.modulus import modulus

# main function
def main():
    print("")
    print("     ***** CALCULATOR *****")
    print("")
    print("     Choose any one of the operations: ")
    print("""
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Division
            5. Remainder (Modulo)
        """)
    a = int(input("     Enter the first number : "))
    b = int(input("     Enter the second number: "))

    choice = int(input("\n     Enter your choice : "))
    print()
    print(f"    **********************")
    print(f"    ***   Result : {choices(choice,a,b)}   ***")
    print(f"    **********************")


def choices(choice,a,b):
# if-else choices for arithmetic operations
    if(choice==1):
        return addition(a,b)
    
    elif(choice==2):
        return subtraction(a,b)
    
    elif(choice==3):
        return multiplication(a,b)

    elif(choice==4):
        return division(a,b)

    elif(choice==5):
        return modulus(a,b)


if __name__== "__main__":
    main()