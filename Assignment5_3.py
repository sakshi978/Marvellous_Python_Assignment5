i = 5
def Display():
    global i
    if(i != 0):
        print(i, "\t", end=" ")
        i = i-1
        Display()


def main():
    Display()

if __name__=="__main__":
    main()