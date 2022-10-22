nums = list(input("Список: "))
a = "".join(nums) 
s = set(a)
if sorted(s) == sorted(a):
    print(False)
else:
    print(True)