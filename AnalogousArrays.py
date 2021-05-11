diff=[-2,-1,-2,5]
lower=3
upper=10

def countAnalogousArrays(consecutiveDifference, lowerBound, upperBound):
    temp=[]
    while lowerBound < upperBound:
        for i in range(len(consecutiveDifference)):
            val=lowerBound-consecutiveDifference[i]
            temp.append(val)   
            lowerBound=val
        temp.insert(0,lowerBound)
        lowerBound+=1
        for values in temp:
            if values > upperBound:
                temp=[]
        if len(temp) > 0:
            print(temp)
        temp=[]

countAnalogousArrays(diff,lower,upper)