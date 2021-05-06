import random as r

lst = ["snake", "water", "gun"]  # list is created
n = 0  # number of times loop to be run
c = 0  # computers score
m = 0  # human score
while n != 9:
    a = r.choice(lst)  # computer generates random string from given list
    n = n + 1
    b = input("Please choose from snake , water , gun : \n")  # takes input
    if b != lst[0] and b != lst[1] and b != lst[2]:
        print("invalid input !")
        n -= 1
        continue
    if (a == lst[0] and b == lst[1]) or (a == lst[1] and b == lst[2]) or (
            a == lst[2] and b == lst[0]):  # comparison between computer and humans choice
        print("you selected : ", b)
        print("computer selected : ", a)
        print("you lost !")
        c = c + 1
        print("your total score : ", m)
        print("computer's total score : ", c)
        continue
    elif (b == lst[0] and a == lst[1]) or (b == lst[1] and a == lst[2]) or (b == lst[2] and a == lst[0]):
        print("you selected : ", b)
        print("computer selected : ", a)
        print("you won")
        m = m + 1
        print("your total score : ", m)
        print("computer's total score : ", c)
        continue
    else:
        print("you selected : ", b)
        print("computer selected : ", a)
        print("tie")
        c = c + 1
        m = m + 1
        print("your total score : ", m)
        print("computer's total score : ", c)
        continue
if m > c:
    print("\nHooray, you won overall !")
elif m == c:
    print("tie overall !")
else:
    print("\nAlas ,computer won overall !")
