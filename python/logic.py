# n = int(input("enter a number"))

# print("digit count : ", len(str(n)))
# count = 0
# while n > 0:
#     n = n//10
#     count +=1

# print("digit : ", count)

# n = int(input("enter a number : "))
# rev= 0
# while n > 0:
#     p = n % 10
#     rev = (rev*10) + p 
#     print(rev)
#     n = n // 10

str = input(" : ")
sub = ""
len = 0
curr = 0
for ch in str:
    if ch in sub:
        sub = ch
        print("sub : ", sub)
        print("ch : ", ch)
        curr = 1
    else:
        sub += ch
        print("unique sub : ",  sub)
        curr +=1
    if len < curr:
        len = curr
return len