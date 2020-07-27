def Display(iNo):
    if(iNo != 0):
        print("*\t",end=" ")
        iNo = iNo-1
        Display(iNo)


def main():
    iValue = int(input("Enter no.: "))
    Display(iValue)

if __name__=="__main__":
    main()