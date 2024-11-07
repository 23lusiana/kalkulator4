from tkinter import*
window=Tk()
window.geometry("400x450")

def click(item):
    global expression
    expression+=str(item)
    input_teks.set(expression)

def tmbl_clear(): 
    global expression 
    expression = "" 
    input_teks.set("")

def btn_equal():
    global expression
    try:
     	result = str(eval(expression.			replace('%','/100')))
     	input_teks.set(result)
    except:
     	input_teks.set("Error")
     	expression=""

def tombol_persen():
	global expression
	expression+="%"
	input_teks.set(expression)
	
def tombol_plus_minus():
	global expression
	if expression and expression[0]=='-':
			expression=expression[1:]    
	else:
			expression='-'+expression
	input_text.set(expression)
		
expression=""
input_teks=StringVar()

frame1=Frame(window, bg="black" )
frame1.pack()

frame2=Frame(window, bg="black" )
frame2.pack()

label3=Label(frame1, text=" Kalkulator Lusiana PPLG 1 ",anchor="w",width=50,font=("Arial", 10))
label3.pack()

label2=Label(frame1, text="", font=("Arial", 50),bg="black",fg="white",anchor="e",width=40,textvariable=input_teks)
label2.pack()

button1=Button(frame2, text="AC", width=5,height=0, bg="dimgrey", font=("arial",20), fg="white", command =lambda:tmbl_clear())
button1.grid(row=0, column=1)

button3=Button(frame2, width=5,height=0, text="+/-", bg="dimgrey", font=("arial",20), fg="white",command=lambda:tombol_plus_minus() )
button3.grid(row=0, column=2, pady=5, padx=5)

button3=Button(frame2, width=5,height=0, text="%", bg="dimgrey", font=("arial",20),fg="white",command=lambda:click("%"))
button3.grid(row=0, column=3, pady=5, padx=5)

button3=Button(frame2, width=5,height=0, text="/", bg="orange",font=("arial",20),fg="white",command=lambda:click("/") )
button3.grid(row=0, column=4, pady=5, padx=5)



button4=Button(frame2, width=5,height=0, text="x", bg="orange", font=("arial",20), fg="white",command=lambda:click("*") )
button4.grid(row=1, column=4, pady=5, padx=5)

button5=Button(frame2, width=5,height=0, text="7",bg="grey", font=("arial",20),fg="white", command=lambda:click("7"))
button5.grid(row=1, column=1, pady=5, padx=5)

button6=Button(frame2, width=5,height=0, text="8",bg="grey", font=("arial",20), fg="white", command=lambda:click("8"))
button6.grid(row=1, column=2, pady=5, padx=5)

button7=Button(frame2, width=5,height=0, text="9" ,bg="grey",font=("arial",20),fg="white",command=lambda:click("9"))
button7.grid(row=1, column=3, pady=5, padx=5)

button8=Button(frame2, width=5, height=0,text="+", bg="orange", font=("arial",20), fg="white", command=lambda:click("+"))
button8.grid(row=3, column=4, pady=5, padx=5)

button9=Button(frame2, width=5,height=0, text="4",bg="grey", font=("arial",20), fg="white",command=lambda:click("4"))
button9.grid(row=2, column=1, pady=5, padx=5)

button10=Button(frame2, width=5,height=0, text="5",bg="grey", font=("arial",20),fg="white",command=lambda:click("5") )
button10.grid(row=2, column=2, pady=5, padx=5)

button11=Button(frame2, width=5,height=0, text="6",bg="grey", font=("arial",20),fg="white", command=lambda:click("6"))
button11.grid(row=2, column=3, pady=5, padx=5)

button12=Button(frame2, width=5,height=0, text="-",bg="orange", font=("arial",20),fg="white",command=lambda:click("-") )
button12.grid(row=2, column=4, pady=5, padx=5)

button13=Button(frame2, width=5,height=0, text="1",bg="grey", font=("arial",20),fg="white", command=lambda:click("1"))
button13.grid(row=3, column=1, pady=5, padx=5)

button14=Button(frame2, width=5,height=0, text="2",bg="grey", font=("arial",20),fg="white",command=lambda:click("2"))
button14.grid(row=3, column=2, pady=5, padx=5)

button15=Button(frame2, width=5,height=0, text="3",bg="grey", font=("arial",20), fg="white",command=lambda:click("3") )
button15.grid(row=3, column=3, pady=5, padx=5)

button16=Button(frame2, width=5,height=0, text="=",bg="orange", font=("arial",20),fg="white", command = lambda:btn_equal())
button16.grid(row=4, column=4, pady=5, padx=5)

button17=Button(frame2, text="0",bg="grey",font=("arial",20), fg="white", width=5,height=0, command=lambda:click("0"))
button17.grid(row=4, column=2)

button19=Button(frame2, text="00",bg="grey", font=("arial",20), fg="white", width=5,height=0, command=lambda:click("00"))
button19.grid(row=4, column=1,  pady=5, padx=5)

button18=Button(frame2, width=5, height=0,text=".",bg="grey", font=("arial",20),fg="white",command=lambda:click(".") )
button18.grid(row=4, column=3, pady=5, padx=5)


window.mainloop()