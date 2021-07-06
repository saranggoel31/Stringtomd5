import hashlib
line=input("Enter any text or line")
Strmd5=hashlib.md5(line.encode())
print("The conversion of ",line," to md5 is ", end="")
print(Strmd5.hexdigest())