



import pandas as pd
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt



dec=int(input("enter a decimal number:"))

# --------------For Binary-------------------------------------------------
def convertToBinary(dec):
    if dec>1:
        convertToBinary(dec//2)
    print(dec%2,end ='')
print("Binary :",end='')
convertToBinary(dec)

print()

#-------------For Octal Conversion------------------------------------------
def dectoOct(dec):
    if(dec>0):
        dectoOct((int)(dec/8))
        print(dec%8,end='')
print("octal :", end='')
dectoOct(dec);

print()

#----------------For Hexa-Decimal-----------------------------------------------

def getHexChar(dec_digit):
    if dec_digit < 10:
        return dec_digit
    if dec_digit == 10:
        return "A"
    if dec_digit == 11:
        return "B"
    if dec_digit == 12:
        return "C"
    if dec_digit == 13:
        return "D"
    if dec_digit == 14:
        return "E"
    if dec_digit == 15:
        return "F"

def decToHex(dec):
    while dec > 0:
        hex_value=dec%16
        dec=dec//16
        print(getHexChar(hex_value),end="")


print("Hexa-Decimal :", end=" ")
decToHex(dec);





from tkinter import *
window=Tk()
window.title("Project")
window.geometry('450x400')
window.configure(bg='Pink')
lb1 = Label(window, text=".......Convertor..........")
lb1.grid(column=1, row=0)
lb2 = Label(window,text="...........Click Here for Results........")
lb2.grid(column=1, row = 3,pady=4)

def clickedB():
    lb1.configure(convertToBinary(dec))
print()

def clickedO():
    lb1.configure( dectoOct(dec))
print()


def clickedH():
    lb1.configure(decToHex(dec))
print()

btn =Button(window, text=" In_Binary",command=clickedB)
btn.grid(column=1, row=5, padx=4)
btn.configure(bg="yellow",fg="blue")



btn =Button(window, text="In_Octal",command=clickedO)
btn.grid(column=1, row=7, padx=5 ,pady=4)
btn.configure(bg="yellow",fg="blue")




btn =Button(window, text="Hexadecimal", command=clickedH)
btn.grid(column=1, row=9)
btn.configure(bg="yellow",fg="blue")





window.mainloop()


