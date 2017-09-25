def collatz(number):
    if number % 2 == 0:
        n = number // 2
        return n
    elif number % 2 == 1:
        n = number*3+1
        return (n)

##Run the function
while True:
    print ('Enter number (enter q to quit): ')
    s = input()
    if s == "q" : break
    try:
        i = int(s)
        print ("After collatz: " + str(collatz(i)) + "\n")
    except:
        print ("Please enter a valid number.\n")
    