user_line = int(input("enter the number of lines:"))
with open("sample.txt" , "r" , encoding="utf-8") as f:
    data= list(f)
    for i in range(0 , len(data)):
        if i == user_line:
            print(data[i])