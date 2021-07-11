import itertools
import string
import time
from tkinter import*
from tkinter import messagebox

root=Tk()
root.title("Pass-Cracker")
root.geometry("620x230")



def guess_common_password(password):
    with open("common_password.txt",'r') as passwords:
        data=passwords.read().splitlines()

    for i, match in enumerate(data):
        if match ==password:
            return f'The Password is {match} (Attempt #{i})'
    return 0

def Brute_Force(password,min_length=4,max_length=9):
    chars=string.ascii_lowercase+ string.digits #+string.punctuation +.ascii_uppercase or for both use ascii_letters
    attempts=0
    for password_length in range(min_length,max_length):
        for guess in itertools.product(chars,repeat=password_length):
            attempts+=1
            guess=''.join(guess)
            if guess==password:
                messagebox.showinfo("Cracked!!", f'The password is {guess} (Attempt #{attempts})')
                return f'The password is {guess} (Attempt #{attempts})'
            print(guess,attempts)

def get_password():
    #password=input("Enter Password: ")
    start_time=time.time()
    password=e.get()
    common=guess_common_password(password)
    if common==0:
        Brute_Force(password)
        timetaken=round(time.time()-start_time,2),'s'
        Label2=Label(root,text="Time to Crack: ",font='tmes 15 bold italic')
        Label2.grid(row=5,column=1,padx=10,pady=10)
        Label3=Label(root,text=timetaken,font='tmes 15 bold italic')
        Label3.grid(row=5,column=2,padx=10,pady=10)
    else:
        messagebox.showinfo("Cracked It's a Common Password",common)
        timetaken=round(time.time()-start_time,2),'s'
        Label2=Label(root,text="Time to crack :",font='tmes 15 bold italic')
        Label2.grid(row=5,column=1,padx=10,pady=10)
        Label3=Label(root,text=timetaken,font='tmes 15 bold italic')
        Label3.grid(row=5,column=2,padx=10,pady=10)

#start_time=time.time()
"""
choice=input("Want to check your password? y/n")
if(choice=='y'or choice=='Y'):
    get_password()
    timetaken=round(time.time()-start_time,2),'s'
else:
    print("Wrong Response!!")
"""


Label0=Label(root,text="Let's Check how strong is your Password",font='tmes 15 bold italic')
Label0.grid(row=1,column=1,padx=10,pady=10)


Label1=Label(root,text="Enter the Password * : ")
Label1.grid(row=2,column=1,padx=10,pady=10)

e=Entry(root,width=40,fg="blue",bg="white",borderwidth=7)
e.icursor(0)
e.grid(row=2,column=2,padx=10,pady=10)


Button1=Button(root,text="Let's Crack",font='times 10 bold',fg='black',bg='light blue',padx=50,command=get_password)
Button1.grid(row=4,column=1,padx=10,pady=10)


'''
Label3=Label(root,text=timetaken,font='tmes 15 bold italic')
Label3.grid(row=6,column=2,padx=10,pady=10)
'''
