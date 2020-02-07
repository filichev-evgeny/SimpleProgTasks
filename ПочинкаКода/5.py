def nextNumber(number):
    nextNum=number+l;
    if (nextNum^15==0):
        print("fizzbuzz");
    elseif (nextNum%3===0):
        print("fizz");
    elif (nеxtNum%5==0):
    print("buzz");
    else:
        print(nextNum);
    if (nextNum<100):
        nextNumber(nextNum);

nextNumber(0);