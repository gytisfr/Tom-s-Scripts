#Imports
import tkinter as tk
import pyperclip
import asyncio
import os
from collections import Counter

#Set
os.chdir("D:\Ridgeway\Tom's")
order = []

#Funcs
def welcomecopyfunc(self):
    pyperclip.copy("Hello! Welcome to Tom's Takeout! How may I take your order today?")

def isallcopyfunc(self):
    pyperclip.copy("Is that all for you today?")

def inoroutcopyfunc(self):
    pyperclip.copy("And is that eat-in or take-away?")

def eatincopyfunc(self):
    pyperclip.copy("Alright, have a seat and I'll be with you shortly!")

def takeoutcopyfunc(self):
    pyperclip.copy("Alright, I'll be just out with your food shortly!")

def pullupcopyfunc(self):
    pyperclip.copy("Alright, pull up to the next window and I'll bring your food to you shortly!")

def byecopyfunc(self):
    pyperclip.copy("Of course, have a very Tom's Takeout day!")

def gpdfunc(self):
    order.append("Garlic Pork Dumplings")

def samdfunc(self):
    order.append("Spinach and Mushroom Dumplings")

def shridfunc(self):
    order.append("Shrimp Dumplings")

def seadfunc(self):
    order.append("Seafood Dumplings")

def pfrfunc(self):
    order.append("Plain Fried Rice")

def cfrfunc(self):
    order.append("Chicken Fried Rice")

def sfrfunc(self):
    order.append("Shrimp Fried Rice")

def bfrfunc(self):
    order.append("Beef Fried Rice")

def fcfunc(self):
    order.append("Fortune Cookies")

def wrfunc(self):
    order.append("White Rice")

def fffunc(self):
    order.append("French Fries")

def erfunc(self):
    order.append("Egg Rolls")

def pgfunc(self):
    order.append("Pho Ga")

def pbvfunc(self):
    order.append("Pho Bo Vien")

def ptbvfunc(self):
    order.append("Pho Tai Bo Vien")

def crfunc(self):
    order.append("California Rolls")

def ssrfunc(self):
    order.append("Spicy Salmon Rolls")

def urfunc(self):
    order.append("Unagi Rolls")

def copyorderfunc(self):
    c = Counter(order)
    finalorder = ([(f'{n} ' if n > 1 else '') + item for item, n in c.items()])
    finalfinalorder = ""
    for el in finalorder:
        finalfinalorder = f"{finalfinalorder}, {el}"
    finalfinalorder = finalfinalorder.lstrip(', ')
    un, _, dos = finalfinalorder.rpartition(', ')
    finalfinalorder = un + ' & ' + dos
    if finalfinalorder[0] == ' ':
        finalfinalorder = finalfinalorder.lstrip(' & ')
    pyperclip.copy(finalfinalorder)

def clearorderfunc(self):
    globals()['order'] = []

def removeonefunc(self):
    del (globals()['order'])[-1]

def clearclipfunc(self):
    pyperclip.copy(" ")

def checktheguy(self):
    os.startfile('Group Checker.py')

#Window Setup
window = tk.Tk()
window.title("My App")
window.geometry("607x245")

#Content
welcomecopy = tk.Button(text="Welcome")
welcomecopy.grid(column=0, row=0)
welcomecopy.bind("<Button-1>", welcomecopyfunc)
isallcopy = tk.Button(text="All?")
isallcopy.grid(column=1, row=0)
isallcopy.bind("<Button-1>", isallcopyfunc)
inoroutcopy = tk.Button(text="In Out")
inoroutcopy.grid(column=0, row=1)
inoroutcopy.bind("<Button-1>", inoroutcopyfunc)
eatincopy = tk.Button(text="Eat In")
eatincopy.grid(column=1, row=1)
eatincopy.bind("<Button-1>", eatincopyfunc)
takeoutcopy = tk.Button(text="Takeout")
takeoutcopy.grid(column=2, row=1)
takeoutcopy.bind("<Button-1>", takeoutcopyfunc)
pullupcopy = tk.Button(text="Window")
pullupcopy.grid(column=4, row=1)
pullupcopy.bind("<Button-1>", pullupcopyfunc)
byecopy = tk.Button(text="Bye")
byecopy.grid(column=4, row=0)
byecopy.bind("<Button-1>", byecopyfunc)

split1 = tk.Label(text=" ")
split1.grid(column=0, row=2)

dumplings = tk.Label(text="Dumplings")
dumplings.grid(column=0, row=4)
gpd = tk.Button(text="Garlic Pork Dumplings")
gpd.grid(column=0, row=5)
gpd.bind("<Button-1>", gpdfunc)
samd = tk.Button(text="Spinach and Mushroom Dumplings")
samd.grid(column=0, row=6)
samd.bind("<Button-1>", samdfunc)
shrid = tk.Button(text="Shrimp Dumplings")
shrid.grid(column=0, row=7)
shrid.bind("<Button-1>", shridfunc)
sead = tk.Button(text="Seafood Dumplings")
sead.grid(column=0, row=8)
sead.bind("<Button-1>", seadfunc)

friedrice = tk.Label(text="Fried Rice")
friedrice.grid(column=1, row=4)
pfr = tk.Button(text="Plain Fried Rice")
pfr.grid(column=1, row=5)
pfr.bind("<Button-1>", pfrfunc)
cfr = tk.Button(text="Chicken Fried Rice")
cfr.grid(column=1, row=6)
cfr.bind("<Button-1>", cfrfunc)
sfr = tk.Button(text="Shrimp Fried Rice")
sfr.grid(column=1, row=7)
sfr.bind("<Button-1>", sfrfunc)
bfr = tk.Button(text="Beef Fried Rice")
bfr.grid(column=1, row=8)
bfr.bind("<Button-1>", bfrfunc)

sideorders = tk.Label(text="Side Orders")
sideorders.grid(column=2, row=4)
fc = tk.Button(text="Fortune Cookies")
fc.grid(column=2, row=5)
fc.bind("<Button-1>", fcfunc)
wr = tk.Button(text="White Rice")
wr.grid(column=2, row=6)
wr.bind("<Button-1>", wrfunc)
ff = tk.Button(text="French Fries")
ff.grid(column=2, row=7)
ff.bind("<Button-1>", fffunc)
er = tk.Button(text="Egg Rolls")
er.grid(column=2, row=8)
er.bind("<Button-1>", erfunc)

vietnamesepho = tk.Label(text="Vietnamese Pho")
vietnamesepho.grid(column=3, row=4)
pg = tk.Button(text="Pho Ga")
pg.grid(column=3, row=5)
pg.bind("<Button-1>", pgfunc)
pbv = tk.Button(text="Pho Bo Vien")
pbv.grid(column=3, row=6)
pbv.bind("<Button-1>", pbvfunc)
ptbv = tk.Button(text="Pho Tai Bo Vien")
ptbv.grid(column=3, row=7)
ptbv.bind("<Button-1>", ptbvfunc)

sushi = tk.Label(text="Sushi")
sushi.grid(column=4, row=4)
cr = tk.Button(text="California Rolls")
cr.grid(column=4, row=5)
cr.bind("<Button-1>", crfunc)
ssr = tk.Button(text="Spicy Salmon Rolls")
ssr.grid(column=4, row=6)
ssr.bind("<Button-1>", ssrfunc)
ur = tk.Button(text="Unagi Rolls")
ur.grid(column=4, row=7)
ur.bind("<Button-1>", urfunc)

split2 = tk.Label(text=" ")
split2.grid(column=0, row=9)

copyorder = tk.Button(text="Copy")
copyorder.grid(column=0, row=10)
copyorder.bind("<Button-1>", copyorderfunc)
clearorder = tk.Button(text="Clear")
clearorder.grid(column=1, row=10)
clearorder.bind("<Button-1>", clearorderfunc)
removeone = tk.Button(text="Remove 1")
removeone.grid(column=2, row=10)
removeone.bind("<Button-1>", removeonefunc)
clearclip = tk.Button(text="Clpbrd")
clearclip.grid(column=3, row=10)
clearclip.bind("<Button-1>", clearclipfunc)

checkuser = tk.Button(text="Check")
checkuser.grid(column=4, row=10)
checkuser.bind("<Button-1>", checktheguy)

#Make Work
window.mainloop()