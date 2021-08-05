# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name_total = (name1 + name2)
name_total = name_total.lower()
l = name_total.count("l")
o = name_total.count("o")
v = name_total.count("v")
e = name_total.count("e")
love_total = l + o + v + e

t = name_total.count("t")
r = name_total.count("r")
u = name_total.count("u")
e = name_total.count("e")
true_total = t + r + u + e

name_total = str(true_total) + str(love_total)
name_total = int(name_total)
if (name_total > 40) and (name_total < 50):
  print(f"Your score is {name_total} \n You guys go great together!")
elif (name_total <= 10) or (name_total >= 90):
  print(f"Your score is {name_total} \n You go together like coke and mentos")
else: 
  print(f"Your score is {name_total}.")




