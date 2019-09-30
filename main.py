from tkinter import*
def click(number):
    global op
    op=op+str(number)
    text_input.set(op)

def clrbt():
    global op
    op=""
    text_input.set("")
def Eq():
    global op
    equ=str(eval(op))
    text_input.set(equ)
    op=""
	
def onclick(event):
    global k
    b=event.widget
    if b==b0 or b==b1 or  b==b2 or b==b3 or b==b4 or b==b5 or b==b6 or b==b7 or b==b8 or b==b9:
        if k==0:
            txt.delete(0,"end")
            txt.insert("end",b.cget("text"))
            k=1
            
        else:
            txt.insert("end",b.cget("text"))
            
    elif b==bplus or b==bminus or b==bmultiply or b==bdivide:
        k=1
        op=b
        op1=txt.get()
        txt.delete(0,"end")
        
    elif b==bequals:
        op2=txt.get()
        calc
		
		
window=Tk()
window.title("Making a Goddamn Calculator")
op=""
text_input=StringVar()
display=Entry(window,font=("Times new roman",25),textvariable=text_input,bd=30,insertwidth=5,bg="grey",justify="right").grid(columnspan=6)
Button1=Button(window,padx=18,bd=10,fg="black",font=("Times new roman",20,"bold"),text=1,command=lambda:click(1)).grid(row=1,column=0)
Button2=Button(window,padx=18,bd=10,fg="black",font=("Times new roman",20,"bold"),text=2,command=lambda:click(2)).grid(row=1,column=1)
Button3=Button(window,padx=18,bd=10,fg="black",font=("Times new roman",20,"bold"),text=3,command=lambda:click(3)).grid(row=1,column=2)
Add=Button(window,padx=18,bd=10,fg="black",font=("Times new roman",20,"bold"),text="+",command=lambda:click("+")).grid(row=1,column=3)
Button4=Button(window,padx=18,bd=10,fg="black",font=("Times new roman",20,"bold"),text=4,command=lambda:click(4)).grid(row=2,column=0)
Button5=Button(window,padx=18,bd=10,fg="black",font=("Times new roman",20,"bold"),text=5,command=lambda:click(5)).grid(row=2,column=1)
Button6=Button(window,padx=18,bd=10,fg="black",font=("Times new roman",20,"bold"),text=6,command=lambda:click(6)).grid(row=2,column=2)
sub=Button(window,padx=18,bd=10,fg="black",font=("Times new roman",20,"bold"),text="-",command=lambda:click("-")).grid(row=2,column=3)
Button7=Button(window,padx=18,bd=10,fg="black",font=("Times new roman",20,"bold"),text=7,command=lambda:click(7)).grid(row=3,column=0)
Button8=Button(window,padx=18,bd=10,fg="black",font=("Times new roman",20,"bold"),text=8,command=lambda:click(8)).grid(row=3,column=1)
Button9=Button(window,padx=18,bd=10,fg="black",font=("Times new roman",20,"bold"),text=9,command=lambda:click(9)).grid(row=3,column=2)
Product=Button(window,padx=18,bd=10,fg="black",font=("Times new roman",20,"bold"),text="*",command=lambda:click("*")).grid(row=3,column=3)
Clear=Button(window,padx=18,bd=10,fg="black",font=("Times new roman",20,"bold"),text="C",command=lambda:clrbt()).grid(row=4,column=0)
Button0=Button(window,padx=18,bd=10,fg="black",font=("Times new roman",20,"bold"),text=0,command=lambda:click(0)).grid(row=4,column=1)
Equal=Button(window,padx=18,bd=10,fg="black",font=("Times new roman",20,"bold"),text="=",command=lambda:Eq()).grid(row=4,column=2)
Divide=Button(window,padx=18,bd=10,fg="black",font=("Times new roman",20,"bold"),text="/",command=lambda:click("/")).grid(row=4,column=3)


window.mainloop()
