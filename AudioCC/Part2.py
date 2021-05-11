number = 111110

def Part2(number):
    x=0
    values = []

    while x <= number:
        numlist = list(str(number))
        numtest = list(str(number))
        numtest.sort()
        if numtest == numlist:
            values.insert(0,number)
            break
        x+=1
        number -=1
    print(values[len(values)-1])

Part2(number)