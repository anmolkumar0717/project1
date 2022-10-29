print("\t\t\t\t    -----welcome to the quiz game------ \n")
i=1
while i<2:
    score=0
    print("<1> Who is the current ceo of google ")
    print(" 1-- sundar puchai\t\t\t2-- nagarajan swami ")
    print(" 3-- satya nadela\t\t\t4-- rishab panth \n")
    out1=int(input("Enter your choice: "))
    if out1==1:
        print("congratulation you are right!!! ")
        score+=100
    else:
        print("better luck for next time!!! ")
    print("score = ",score,"\n")
    print("2 Who is the current ceo of microsoft?")
    print(" 1-- sundar puchai\t\t\t2-- nagarajan swami ")
    print(" 3-- satya nadela\t\t\t4-- rishab panth \n")
    out2 = int(input("Enter your choice: "))
    if out2 ==3:
        print("congratulation you are right ")
        score+=100
    else:
        print("better luck for next time ")
    print("score =",score,"\n")
    print("3.What is the full form of wi-fi")
    print(" 1-- Wireless funtion\t\t\t\t2-- wireless fidility")
    print(" 3-- without funtion\t\t\t\t4-- without money\n")
    ch1=int(input("Enter your choise: "))
    if ch1==2:
        print("congratulation you are right")
        score+=100
    else:
        print(" better luck next time")
    print("score =",score,"\n")
    print("3.what is the name of the first network?")
    print(" 1-- ARPANET\t\t\t2-- INTERNET")
    print(" 3-- IPNET\t\t\t4-- WEBNET\n")
    ch1=int(input("Enter your choise: "))
    if ch1==1:
        print("congratulation you are right")
        score+=100
    else:
        print(" better luck next time")
    print("score =",score,"\n")
    print("3.What is the name of the first car?")
    print(" 1--Benz Patent-Motorwagen\t\t2-- ford")
    print(" 3-- maruti\t\t\t4-- Tata")
    ch1=int(input("Enter your choise: "))
    if ch1==1:
        print("congratulation you are right")
        score+=100
    else:
        print(" better luck next time")
    print("score =",score,"\n")
    if score==500:
        print("Your all answer are right")
    print("\n1.For Play again")
    print("2.Exit")
    ch=int(input(" \nEnter your choise:-"))
    if ch==1:
        i-=1
    elif ch==2:
        i+=1
    else:
        print("invalid choise")
        i+=1
