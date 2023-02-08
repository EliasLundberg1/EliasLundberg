
import random
#uppgift 1
x = []

for num in range(10):
    r = random.randint(30, 50)
    x.append(r)
print(x)

#uppgift 2
z = []

for num in range(5):
    u = random.uniform(1,10)
    z.append(u)
print(z)

#uppgift 3

for i in range(7):
   print(random.gauss(50,25))
import random as r

#uppgift 4

list1 = []
for i in range(5):
   list1.append(r.randint(1, 10))
for i in range(5):
   print(r.sample(list1, 2))
print(list1)

