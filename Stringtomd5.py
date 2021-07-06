import hashlib

line = input("Enter any word or sentence")
strtomd5 = hashlib.md5(line.encode())
print("The md5 conversion of ", line, " : ", end="")
print(strtomd5.hexdigest())
