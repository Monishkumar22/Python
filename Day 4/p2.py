t=int(input("Enter total users="))
if(t==0):
    print("invalid input")
    t=t=int(input("Enter total users="))
elif(t<0):
        print("invalid input")
        t=t=int(input("Enter total users="))
s=int(input("Enter staff users="))
n=(s//3)
if(t<s):
    print("invalid input")
elif(t==s):
    print("student users are=",t-(s-n))
else:
    print("student users are=",t-s-n)
