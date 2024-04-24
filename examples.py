email="saima@gmail.com"
pwd=123456
otp=3546
uemail=str(input("enter email:"))
upwd=int(input("enter the pwd:"))
if(email==uemail):
    if(pwd==upwd):
        print("login success")
        uotp=int(input("enter otp:"))
        if(otp==uotp):
            print("successful transaction")
        else:
            print("transtion failed")
    else:
        print("login failed due to incorrect pwd")
else:
    print("login failed due to incorrect email")