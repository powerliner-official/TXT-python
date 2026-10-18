just_name = input("enter your new name:")
with open('sample.txt', "w",encoding="utf-8") as f:
    f.write(just_name)