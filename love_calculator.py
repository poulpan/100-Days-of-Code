print("Welcome to the Love Calculator!\n")
name1 = input("What is your name? ")
name2 = input("What is their name? ")
# ***NOTE*** Better to combine the two strings prior, so you can have fewer code.
# i.e.: combine_names = name1 + name2
# lower_combine_names = combine_names.lower()
# t = lower_combine_names.count("t"), etc. etc.
lower_name1 = name1.lower()
lower_name2 = name2.lower()
t = lower_name1.count("t") + lower_name2.count("t")
print(f"#t={t}")
r = lower_name1.count("r") + lower_name2.count("r")
print(f"#r={r}")
u = lower_name1.count("u") + lower_name2.count("u")
print(f"#u={u}")
e = lower_name1.count("e") + lower_name2.count("e")
print(f"#e={e}")
l = lower_name1.count("l") + lower_name2.count("l")
print(f"#l={l}")
o = lower_name1.count("o") + lower_name2.count("o")
print(f"#o={o}")
v = lower_name1.count("v") + lower_name2.count("v")
print(f"#v={v}")
e = lower_name1.count("e") + lower_name2.count("e")
print(f"#e={e}")
score = str(t+r+u+e) + str(l+o+v+e)
# ***NOTE*** Or better make a string before the comparisons:
# score = int(str(t+r+u+e) + str(l+o+v+e))
# So I won't need to int each score below for the comparisons!
if int(score) < 10 or int(score) > 90:
    print(f"Your score is {score}%, you go together like coke and mentos.")
elif int(score) > 40 and int(score) < 50:
    print(f"Your score is {score}%, you are alright together.")
else:
    print(f"Your score is {score}%")
