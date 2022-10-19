print("Hello ,Welcome to Python Quiz")
x=input("If you are intersted in Quiz (Y/N) :")
x=x.upper()
if x=="Y":
    print("lets Rock the Quiz")
else:
    print("Ok,Try This Once You Will Love This")

    
y=input("Enter Your Name To Start The Quiz :")
print("ok",y,"lets start the quiz")

print("#------------------")
sum=0

question="1.WHO CREATED PYTHON"
print(question)
A="A.RAGAVENDIRAN"
B="B.RAGUVARAN"
C="C.MANIVEL"
D="D.GUIDO VAN ROSSUM"
print(A)
print(B)
print(C)
print(D)
ans=input("Enter (A ,B ,C , D) :")
ans=ans.upper()

if ans=="D":
    print("Correct Answer")
    sum=sum+25
else:
    print("Wrong Answer")
print("#------------------") 

question="2.WHAT YEAR WAS PYTHON CREATED"
print(question)
A="A.1989"
B="B.1991"
C="C.2000"
D="D.2016"
print(A)
print(B)
print(C)
print(D)
ans=input("Enter (A ,B ,C , D) :")
ans=ans.upper()

if ans=="B":
    print("Correct Answer")
    sum=sum+25
else:
    print("Wrong Answer")
print("#------------------")     

question="3.PYTHON IS TRIBUTED TO WHICH COMEDY GROUP"
print(question)
A="A.Lonely Island"
B="B.Smosh"
C="C.Monty Python"
D="D.SNL"
print(A)
print(B)
print(C)
print(D)
ans=input("Enter (A ,B ,C , D) :")
ans=ans.upper()
if ans=="C":
    print("Correct Answer")
    sum=sum+25
else:
    print("Wrong Answer")
print("#------------------")  
question="4.WHAT IS THE CORRENT PYTHON VERSION"
print(question)
A="A.3.10.7"
B="B.3.10.6"
C="C.3.09.7"
D="D.3.10.9"
print(A)
print(B)
print(C)
print(D)
ans=input("Enter (A ,B ,C , D) :")
ans=ans.upper()
if ans=="A":
    print("Correct Answer")
    sum=sum+25
else:
    print("Wrong Answer")
print("#------------------")  

print("your smarks is 100/",sum)

