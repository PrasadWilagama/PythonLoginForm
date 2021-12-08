from tkinter import *
root = Tk()
root.geometry("600x400")
def getvals():
    print("Accepted")

#Heading
Label(root, text="Python Login Form",font="ar 15 bold").grid(row=0,column=3)

#Field Name
name =Label(root, text="Name")
phone =Label(root, text="Phone")
gender =Label(root, text="Gender")
email =Label(root, text="Email")

#Packing Fields
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
email.grid(row=4,column=2)

#Vaariables for storing data
name=StringVar
phone=StringVar
gender=StringVar
email=StringVar

checkvalue=IntVar

#Creating entry field
nameentry=Entry(root,textvariable=name)
phoneentry=Entry(root,textvariable=phone)
genderentry=Entry(root,textvariable=gender)
emailentry=Entry(root,textvariable=email)

#Packing entry field
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emailentry.grid(row=4,column=3)

#Creating Checkbox
checkbtn = Checkbutton(text="remember me?",variable=checkvalue)
checkbtn.grid(row=6,column=3)

#Submit Button
Button(text="Submit", command=getvals).grid(row=7, column=3)

root.mainloop()