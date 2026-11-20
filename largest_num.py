import sys
def largest_num(num1,num2,num3):
    if((num1 > num2) and (num1 > num3)):
        print("num1 is Largest")
    elif((num2 > num1) and (num2 > num3)):
        print("num2 is Largest")
    else:
        print("num3 is Largest")

if __name__ == "__main__":
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    num3 = sys.argv[3]

    print("Largest number is ", largest_num(21,24,16))