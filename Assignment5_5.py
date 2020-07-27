iMult = 1
def Fact(iNo):
    global iMult
    if(iNo != 0):
        iMult = iMult*iNo
        iNo = iNo-1
        Fact(iNo)
    print(iMult)

def main():
    iValue = int(input("Enter no.: "))
    Fact(iValue)

if __name__=="__main__":
    main()