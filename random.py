import random
n=random.randrange(3)
print(n)
print(random.randrange(1,8))
print(random.randint(100,211))
mylist=["Rohit","Jadeja","Virat","Dhoni","Bumrah"]
mylist1={"Rohit","Jadeja","Virat","Dhoni","Bumrah"}
print(random.choice(mylist))
#print(random.choice(mylist1))
random.shuffle(mylist)
print(mylist)