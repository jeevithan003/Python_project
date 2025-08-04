c=input("enter the email: ")
l=len(c)
if l==0:
    print("email cannot be empty")

if "@" in c and "." in c:
    print("its a  valid emial ")
else:
    print("its is invlaid email")
    