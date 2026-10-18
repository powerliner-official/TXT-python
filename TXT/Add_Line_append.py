new_name = input("enter your new name:")
with open('sample.txt', "a",encoding="utf-8") as f:
    f.write(new_name)