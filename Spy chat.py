import time
import random
print("***### WELCOME TO SPY CHAT ###***")
def spy():
    a=input("Enter Spy name:- ")
    while(len(a)<=3):
        print("Invalid name.")
        print("Name must be greater than 3 character")
        a=input("Re-enter name:- ")
    b=int(input("Enter Age:- "))
    while(70<b or b<18):
        b = int(input("Invalid Age..Re-enter Age:-"))
    c=input("Enter Spy ID:- ")
    while(3>=len(c)):
        print("Invalid Spy ID.")
        print("ID must be greater than 3 Numbers.")
        c=input("Re-enter Spy ID:- ")
    r = input("Enter Spy Experience(In Years):- ")
    print("Name:- "+a.upper())
    print("Age:- "+str(b))
    print("Spy ID:- "+str(c))
    if("r>=0"):
        print("Congratulations! We are happy to make you the candidate of aur organization we hope to see lots of passion and hardwork for our organization and we will surely support you till the period u connected to us.")
        print("Thank You!.")
    elif ("0<r>=1"):
        print("Congratulations!. We are glad to have you on our organization as per your experienced in our company we hope that you will keep it up futher in the future.")
        print("Thank You!.")
    elif ("1<r>=2"):
        print("Congratulations! We are so lucky to have you on our side. We appreciate your hardwork with us which is shown to us in this short time is great . And we hope we will make is more greater futher in future.")
        print("Thank You!.")
    elif ("2<r>=3"):
        print("Congratulations! We are so much glad to have you for this much longer time in our company as per its success. And we appreciate your hardwork which is so worthly to aur organization. we hope to see you more in future with this much energy and hardwork.")
        print("Thank You!.")
    elif ("3<r>=4"):
        print("Congratulations! We feels so much lucky for having the candidates like you with this much passion in this period of long time in our organization we really appreciate your hardwork and passion for us and hope to see you more working with us for long time in future.")
        print("Thank You!.")
    elif ("4<r<=5"):
        print("Congratulations! We feel so proud to have such a hard-working and passionfull candidate along with our organization. After that much long time with you with shares lots of success rate in this organization and we also hope to make this success greater and greater in future along with you.")
        print("Thank You!.")
def newspy():
    a=[]
    s=[]
    a.append(input("Enter friend's name:- "))
    age=int(input("Enter Friend Age:- "))
    while(70<age or age<18):
        age=int(input("Invalid Age..Re-enter Age:-"))
    print("New friend added..")
    print("Add friend's Status..")
    print("1.Add Status from friend..")
    print("2.Add Status from default..")
    print("3.Show Details..")
    print("4.Send Message..")
    print("5.Read Message..")
    print("6.Exit..")
    st=int(input("Enter your choice:- "))
    while(st>2 or st==0):
        print("Invalid Choice..\nRe-enter choice..")
        print("1.Add Status from friend..")
        print("2.Add Status from default..")
        print("3.Show Details..")
        print("4.Send Message..")
        print("5.Read Message..")
        print("6.Exit..")
        st=int(input("Enter Your Choice:- "))
    if(st==1):
        s.append(input("Enter your Status:- "))
    elif(st==2):
        print("Select Your status..")
        print("1.Working.")
        print("2.Student.")
        print("3.Free.")
        print("4.Part time Job.")
        b=int(input("Enter your choice from above:- "))
        while(b>4 or b==0):
            print("Wrong choice..\nTry again..")
            print("Select Your status..")
            print("1.Working.")
            print("2.Student.")
            print("3.Free.")
            print("4.Part time Job.")
            b = int(input("Enter your choice from above:- "))
        if(b==1):
            s.append("Working")
        elif(b==2):
            s.append("Student")
        elif(b==3):
            s.append("Free")
        elif(b==4):
            s.append("Part time Job")
    print("Friend list..")
    print(a)
    print("Status..")
    print(s)
def default():
    a=random.randint(10,99)
    b=random.randint(18,30)
    c=random.randint(1234,9876)
    print("Spy With default value..")
    print("Default Name:- Spy"+str(a))
    print("Age:- "+str(b))
    print("Spy Default ID:- "+str(c))
print("1.Default Value SPY")
print("2.New SPY..")
print("3.Existing SPY")
w=int(input("Enter Your Choice:- "))
while(w>4 or w==0):
    print("Invalid choice...\nTry again..")
    rint("1.Default Value SPY")
    print("2.New SPY..")
    print("3.Existing SPY")
    print("4.Exit")
    w = int(input("Enter Your Choice"))
if(w==1):
    print("Adding Default Value SPY")
    default()
    time.sleep(3)
    print("Default Value added")
if(w==2):
    print("Adding New SPY")
    newspy()
    time.sleep(3)
    print("New spy added")
elif(w==3):
    print("Adding new spy with default values..")
    default()
    print("Default value spy added")
elif(w==4):
    exit()