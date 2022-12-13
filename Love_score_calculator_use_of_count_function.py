# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_name=name1+name2
lower_case=combined_name.lower()
t=lower_case.count("t")
r=lower_case.count("r")
u=lower_case.count("u")
e=lower_case.count("e")
l=lower_case.count("l")
o=lower_case.count("o")
v=lower_case.count("v")
e=lower_case.count("e")
true=t+r+u+e
love=l+o+v+e
love_score=str(true)+str(love)
total_love_score=int(love_score)
if (total_love_score <10) or (total_love_score>90):
    print(f'Your score is, {total_love_score} you go together like coke and mentos.')
elif (total_love_score>=40) and (total_love_score<=50):
    print(f'Your score is, {total_love_score} you go together like coke and mentos.')
else:
    print(f"Your score is, {total_love_score}.")