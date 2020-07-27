iSum = 0
def Sum(iNo):
    iDigit = 0
    global iSum
    if(iNo != 0):
        iDigit = int(iNo%10)
        iSum = iSum+iDigit
        iNo = int(iNo/10)
        Sum(iNo)
    print(iSum)

def main():
    iValue = int(input("Enter no.: "))
    Sum(iValue)

if __name__=="__main__":
    main()