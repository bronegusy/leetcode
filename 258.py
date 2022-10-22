num = int(input("число: "))
h = True
k = ""
while len(str(num)) != 1:
    stroka = str(num)
    num = 0
    for i in range(len(stroka)):
       num = num+int(stroka[i])
print(num)       
