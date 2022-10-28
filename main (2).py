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
print("")
print(question)
A="A.RAGAVENDIRAN"
B="B.RAGUVARAN"
C="C.MANIVEL"
D="D.GUIDO VAN ROSSUM"
print(A)
print(B)
print(C)
print(D)
print("")
ans=input("Enter (A ,B ,C , D) :")
ans=ans.upper()

if ans=="D":
    print("Correct Answer")
    sum=sum+10
else:
    print("Wrong Answer")
print("#------------------") 

question="2.WHAT YEAR WAS PYTHON CREATED"
print("")
print(question)
A="A.1989"
B="B.1991"
C="C.2000"
D="D.2016"
print(A)
print(B)
print(C)
print(D)
print("")
ans=input("Enter (A ,B ,C , D) :")
ans=ans.upper()

if ans=="B":
    print("Correct Answer")
    sum=sum+10
else:
    print("Wrong Answer")
print("#------------------")     

question="3.PYTHON IS TRIBUTED TO WHICH COMEDY GROUP"
print("")
print(question)
A="A.Lonely Island"
B="B.Smosh"
C="C.Monty Python"
D="D.SNL"
print(A)
print(B)
print(C)
print(D)
print("")
ans=input("Enter (A ,B ,C , D) :")
ans=ans.upper()
if ans=="C":
    print("Correct Answer")
    sum=sum+10
else:
    print("Wrong Answer")
print("#------------------")  
question="4.WHAT IS THE CORRENT PYTHON VERSION"
print("")
print(question)
A="A.3.10.7"
B="B.3.10.6"
C="C.3.09.7"
D="D.3.10.9"
print(A)
print(B)
print(C)
print(D)
print("")
ans=input("Enter (A ,B ,C , D) :")
ans=ans.upper()
if ans=="A":
    print("Correct Answer :")
    sum=sum+10
else:
    print("Wrong Answer")
print("#------------------")  

question="5.WHAT IS THE CAPTIAL OF INDIA"
print("")
print(question)
A="A.DELHI"
B="B.CHENNAI"
C="C.HOSUR"
D="D.KALINGAVARAM"
print(A)
print(B)
print(C)
print(D)
print("")
ans=input("Enter (A ,B ,C , D) :")
ans=ans.upper()

if ans=="A":
    print("Correct Answer")
    sum=sum+10
else:
    print("Wrong Answer")
print("#------------------")     

question="6.How many letters are there in the English alphabet?"
print("")
print(question)
print("")
ans=int(input("Enter THE ANSWER :"))
if ans==26:
    print("Correct Answer")
    sum=sum+10
else:
    print("Wrong Answer")
print("#------------------")   

question=("7.How many hours are there in a day?")
print(question)
print("")
ans=int(input("Enter THE ANSWER :"))
if ans==24:
    print("Correct Answer")
    sum=sum+10
else:
    print("Wrong Answer")
print("#------------------")   

question=("8.How many days are there in a week?")
print(question)
print("")
ans=int(input("Enter THE ANSWER :"))
if ans==7:
    print("Correct Answer")
    sum=sum+10
else:
    print("Wrong Answer")
print("#------------------")  

question=("9.How many minutes are there in an hour?")
print(question)
print("")
ans=int(input("Enter THE ANSWER :"))
if ans==60:
    print("Correct Answer")
    sum=sum+10
else:
    print("Wrong Answer")
print("#------------------") 

question=("10.How many days are there in a year?")
print(question)
print("")
ans=int(input("Enter THE ANSWER :"))
if ans==365:
    print("Correct Answer")
    sum=sum+10
else:
    print("Wrong Answer")
print("#------------------")

print("Your Marks In This Quiz is  100 /",sum)

    




