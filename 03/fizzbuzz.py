def fizzbuzz():
    for i in range (1,101):
        #Fizz Buzz: Divisible by 3 && 5
        if i % 3 == 0 and i % 5 == 0:
            print ('Fizz Buzz')
        #Fizz: Divisible by 3 ONLY
        elif i % 3 == 0:
            print ("Fizz")
        #Buzz: Divisible by 5 ONLY
        elif i % 5 == 0:
            print ("Buzz")
        #i: Divisible by neither 3 NOR 5
        else:
            print (i)

fizzbuzz()