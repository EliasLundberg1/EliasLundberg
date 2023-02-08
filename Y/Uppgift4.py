
import random

try:
    number = int(input("Skriv valfritt heltal mellan 0-10: "))
    print(number)
except:
    print("Du skrev ej in ett tal")

try:
    while number <= 10 and number >= 0:
        print("tack")
        if number == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
            break
    else:
        print("Du skrev inte ett heltal mellan 0-10")
except:
    print("Försök igen")

x =[]

for num in range(1):
    r=random.randint(0,10)
    x.append(r)
print(x)

print("Tack för hjälpen (ps. hade du rätt?)")