# Made by Kavin Jindal
# Version : 1.1.0
# Compatible OS : Windows XP or above
# Python Version Support : Python 3
# Copying and MOdifying the code doesnt make it yours 
from tkinter import *
from tkinter import ttk
import sys
import re
import time
import tkinter.font as font
import tkinter.scrolledtext as ScrolledText
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
import math
import os
#from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile

#https://usefulwebtool.com/math-keyboard

root = Tk()
root.title("Equit by Kavin Jindal")
root.configure(bg='white')
root.geometry('1550x840')
root.resizable(False, False)


global open_status_name
open_status_name = False

#current_open_file = 'no_file'
global selected
selected = False



frame = Frame(root)
frame.grid(row=1, column=0)
#frame.config(bg='white')
#Menu


    
def cut_text(e):
    global selected
    if text.selection_get():
        selected = text.selection_get()
        text.delete('sel.first', 'sel.last')


def copy_text(e):
    global selected
    if text.selection_get():
        selected = text.selection_get()


def paste_text(e):
    if selected:
        position = text.index(INSERT)
        text.insert(position, selected)

def undo():
    text.edit_undo()

def redo():
    text.edit_redo()

def new_file():
    text.delete(1.0, END)
    root.title('New File - Equit')

    global open_status_name
    open_status_name = False

def open_file():
    text.delete('1.0', END)
    text_file = filedialog.askopenfilename(initialdir ='/', title = 'Open Files', filetypes=[('Text Files', "*.txt")])
    
    if text_file:
        global open_status_name
        open_status_name = text_file

        
    name = text_file
    name = name.replace('/', '')
    root.title(f'{name} -  Equit')

    text_file = open(text_file, 'r')
    stuff = text_file.read()
    text.insert(END, stuff)
    text_file.close()

    
def saveas_file():
    filetypes=[('Text Files', '*.txt')]
    text_file = filedialog.asksaveasfilename(initialdir ='/', title = 'Save as Files', filetypes=filetypes, defaultextension = filetypes)
    if text_file:
        name = text_file
        name = name.replace('/', '')
        root.title(f'{name} - Equit')
        text_file = open(text_file, 'w', encoding="utf8")
        text_file.write(text.get(1.0, END))
        text_file.close()

    

def save_file():
    global open_status_name
    open_status_name = True
    if open_status_name:
        text_file = open(open_status_name, 'w')
        text_file.write(text.get(1.0, END))
        text_file.close()

        messagebox.showinfo('Equit', 'Saved your File')
    else:
        saveas_file()

def app_info():
    global info
    info = Tk()
    info.title("Equit App Info")
    info.configure
    label1_info = Label(info, text='Equit App Info', fg='black', bg='white')

# Formattings commands def

def bold_text():
    text.tag_add("bt", "sel.first", "sel.last")
    text.tag_config("bt", font=("Arial", "16", "bold"))
'''
    current_tags = text.tag_names('sel.first')
    if "bt" in current_tags:
        text.tag_remove('bold', "sel.first", 'sel.last')
    else:
        text.tag_add('bold', 'sel.first', 'sel.last')

    
    bold_font = tkfont.Font(text, text.cget('font'))
    bold_font.configure(weight = 'bold')

    # configure a tag
    current_tags = text.tag_names('sel.first')
    text.tag_configure("bold", font=bold_font)
    if "bold" in current_tags:
        text.tag_remove('bold', "sel.first", 'sel.last')
    else:
        text.tag_add('bold', 'sel.first', 'sel.last')

    '''

def unbold():
    text.tag_add("bt", "sel.first", "sel.last")
    text.tag_config("bt", font=("Arial", "16"))

def italic():
    text.tag_add('bt', 'sel.first', 'sel.last')
    text.tag_config('bt', font=('Arial', "16", "italic"))

def r_italic():
    text.tag_add('bt', 'sel.first', 'sel.last')
    text.tag_config('bt', font=('Arial', "16"))
    

my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command= new_file)
file_menu.add_command(label='Open', command= open_file)
file_menu.add_separator()
file_menu.add_command(label='Save', command=save_file)
file_menu.add_command(label='Save As', command=saveas_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Cut', command =lambda: cut_text(False))
edit_menu.add_command(label='Copy', command =lambda: copy_text(False))
edit_menu.add_command(label='Paste',command =lambda: paste_text(False))
edit_menu.add_separator()
edit_menu.add_command(label='Undo', command =undo)
edit_menu.add_command(label='Redo', command =redo)

'''
help_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='App Info', command=app_info)
'''
format_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Format', menu=format_menu)
format_menu.add_command(label='Bold', command=bold_text)
format_menu.add_command(label='Remove Bold', command=unbold)
format_menu.add_command(label = 'Italics', command=italic)
format_menu.add_command(label = 'Remove Italics', command=r_italic)

# Status Bar
##status_bar = Label(root, text='Ready  ', anchor=E)
#status_bar.grid(row=1, column=0, side=BOTTOM, ipady=5)




#exponents = [math.pow('0', 5)]



#Functions:
# Equations
def sq_root_cmd():
	text.insert(INSERT, '√()')

def unequal_cmd():
    text.insert(INSERT, '≠')

def large_cmd():
    text.insert(INSERT, '>')

def small_cmd():
    text.insert(INSERT, '<')

def square():
    text.insert(INSERT, '²')

def cube():
    text.insert(INSERT, '³')

def cube_root():
    text.insert(INSERT, '3√')

# Number functions

def no_one():
    text.insert(INSERT, '₁')

def no_two():
    text.insert(INSERT, '₂')

def no_three():
    text.insert(INSERT, '₃')

def no_four():
    text.insert(INSERT, '₄')

def no_five():
    text.insert(INSERT, '₅')

def no_six():
    text.insert(INSERT, '₆')

def no_seven():
    text.insert(INSERT, '₇')

def no_eight():
    text.insert(INSERT, '₈')

def no_nine():
    text.insert(INSERT, '₉')

def no_zero():
    text.insert(INSERT, '₀')

def equal_cmd():
    text.insert(INSERT, '=')

def plus_cmd():
    text.insert(INSERT, '+')

def minus_cmd():
    text.insert(INSERT, '-')

def multiply_cmd():
    text.insert(INSERT, 'x')

def divide_cmd():
    text.insert(INSERT, '÷')

def tri_cmd():
    text.insert(INSERT, '∆')

def half_cmd():
    text.insert(INSERT, '½')

def quarter_cmd():
    text.insert(INSERT, '¼')

def bracket_cmd():
    text.insert(INSERT, '()')

def backspace_cmd():
    text.insert(INSERT, 'α')

def angle_cmd():
    text.insert(INSERT, '∠')

def pie_cmd():
    text.insert(INSERT, 'π')

def perp_cmd():
    text.insert(INSERT, '⊥')

def parallel_cmd():
    text.insert(INSERT, '||')

def clear_cmd():
    text.delete(1.0, END)

def prop_cmd():
    text.insert(INSERT , '∝')

def cong_cmd():
    text.insert(INSERT, '≅')

def box_cmd():
    text.insert(INSERT, '□')

def pm_cmd():
    text.insert(INSERT, '±')

def deg_cmd():
    text.insert(INSERT, '°')

def percent_cmd():
    text.insert(INSERT, '%')

def slash_cmd():
    text.insert(INSERT, 'γ')

def onep_cmd():
    text.insert(INSERT, '¹')

def fourp_cmd():
    text.insert(INSERT, '⁴')

def fivep_cmd():
    text.insert(INSERT, '⁵')

def sixp_cmd():
    text.insert(INSERT, '⁶')

def sevenp_cmd():
    text.insert(INSERT, '⁷')

def eightp_cmd():
    text.insert(INSERT, '⁸')

def ninep_cmd():
    text.insert(INSERT, '⁹')

def zerop_cmd():
    text.insert(INSERT, '⁰')

def therep_cmd():
    text.insert(INSERT, '∴')

def bcozp_cmd():
    text.insert(INSERT, '∵')

def propo_cmd():
    text.insert(INSERT, '⋮')

def beta_cmd():
    text.insert(INSERT, 'β')
# Variables

borderwidth = 1
font = ('Arial', 14)
backspace_font = ('Arial', 20)
padx = 30
pady= 22
ex_font = ('Arial', 14)
min_font = ("Arial", 16)
brack = ('Arial', 15)
# Elements
text = ScrolledText.ScrolledText(frame, width=101, height=18, font=("Arial", 20), selectbackground='yellow',
 selectforeground='black', borderwidth=1, undo=True)


# Functions

#cut = Button(frame, text='✂', padx=5, pady=5, fg='white', bg='black', command=cut_text(False), borderwidth=borderwidth, font=ex_font)




# Numbers
one = Button(frame, text='x₁', padx=30, pady=pady, fg='white', bg='black', command=no_one, borderwidth=borderwidth, font=ex_font)
two = Button(frame, text='x₂', padx=padx, pady=pady, fg='white', bg='black', command=no_two, borderwidth=borderwidth, font=ex_font)
three = Button(frame, text='x₃', padx=padx, pady=pady, fg='white', bg='black', command=no_three, borderwidth=borderwidth, font=ex_font)
four = Button(frame, text='x₄', padx=padx, pady=pady, fg='white', bg='black', command=no_four, borderwidth=borderwidth, font=ex_font)
five = Button(frame, text='x₅', padx=padx, pady=pady, fg='white', bg='black', command=no_five, borderwidth=borderwidth, font=ex_font)
six = Button(frame, text='x₆', padx=padx, pady=pady, fg='white', bg='black', command=no_six, borderwidth=borderwidth, font=ex_font)
seven = Button(frame, text='x₇', padx=padx, pady=pady, fg='white', bg='black', command=no_seven, borderwidth=borderwidth, font=ex_font)
eight = Button(frame, text='x₈', padx=padx, pady=pady, fg='white', bg='black', command=no_eight, borderwidth=borderwidth, font=ex_font)
nine = Button(frame, text='x₉', padx=padx, pady=pady, fg='white', bg='black', command=no_nine, borderwidth=borderwidth, font=ex_font)
zero = Button(frame, text='x₀', padx=padx, pady=pady, fg='white', bg='black', command=no_zero, borderwidth=borderwidth, font=ex_font)
bracket = Button(frame, text='()', padx=padx, pady=pady, fg='white', bg='red', command=bracket_cmd, borderwidth=borderwidth, font=brack  )

#operators

triangles = Button(frame, text='∆', padx=padx, pady=pady, fg='white', bg='black', command=tri_cmd, borderwidth=borderwidth, font=ex_font)
angle = Button(frame, text='∠', padx=padx, pady=pady, fg='white', bg='black', command=angle_cmd, borderwidth=borderwidth, font=ex_font)
perp = Button(frame, text='⊥', padx=padx, pady=pady, fg='white', bg='black', command=perp_cmd, borderwidth=borderwidth, font=ex_font)
parallel = Button(frame, text='||', padx=padx, pady=pady, fg='white', bg='black', command=parallel_cmd, borderwidth=borderwidth, font=ex_font)
box = Button(frame, text='□', padx=32, pady=pady, fg='white', bg='black', command=box_cmd, borderwidth=borderwidth, font=ex_font)


half = Button(frame, text='½', padx=padx, pady=pady, fg='black', bg='white', command=half_cmd, borderwidth=borderwidth, font=ex_font)
quarter = Button(frame,  text='¼', padx=padx, pady=pady, fg='black', bg='white', command=quarter_cmd, borderwidth=borderwidth, font=ex_font)
divide = Button(frame, text='÷', padx=33, pady=pady, fg='white', bg='red', command=divide_cmd, borderwidth=borderwidth, font=ex_font)
multiply = Button(frame, text='x', padx=padx, pady=pady, fg='white', bg='red', command=multiply_cmd, borderwidth=borderwidth, font=ex_font)
minus = Button(frame, text='-', padx=34, pady=20, fg='white', bg='red', command=minus_cmd, borderwidth=borderwidth, font=min_font)
plus = Button(frame, text='+', padx=padx, pady=pady, fg='white', bg='red', command=plus_cmd, borderwidth=borderwidth, font=ex_font)
equal = Button(frame, text='=', padx=padx, pady=pady, fg='white', bg='red', command=equal_cmd, borderwidth=borderwidth, font=ex_font)
pm = Button(frame, text='±', padx=padx, pady=pady, fg='white', bg='red', command=pm_cmd, borderwidth=borderwidth, font=ex_font)
degree = Button(frame, text='°', padx=padx, pady=pady, fg='black', bg='white', command=deg_cmd, borderwidth=borderwidth, font=ex_font)

pie = Button(frame, text='π', padx=33, pady=pady, fg='black', bg='white', command=pie_cmd, borderwidth=borderwidth, font=font)
cong = Button(frame, text='≅', padx=32, pady=22, fg='black', bg='white', command=cong_cmd, borderwidth=borderwidth, font=ex_font)

percent = Button(frame, text='%', padx=32, pady=22, fg='black', bg='white', command=percent_cmd, borderwidth=borderwidth, font=font)
slash = Button(frame, text='γ', padx=33, pady=22, fg='black', bg='white', command=slash_cmd, borderwidth=borderwidth, font=font)

sq_root = Button(frame, text='√', padx=32, pady=22, fg='black', bg='white', command=sq_root_cmd, borderwidth=borderwidth, font=font)
unequal = Button(frame, text='≠', padx=32, pady=22, fg='black', bg='white', command=unequal_cmd, borderwidth=borderwidth, font=font)
larger_than = Button(frame, text='>', padx=32, pady=22, fg='black', bg='white', command=large_cmd, borderwidth=borderwidth, font=font)
smaller_than = Button(frame, text='<', padx=32, pady=22, fg='black', bg='white', command=small_cmd, borderwidth=borderwidth, font=font)
square = Button(frame, text='x²', padx=padx, pady=pady, fg='black', bg='white', command=square, borderwidth=borderwidth, font=ex_font)
cube = Button(frame, text='x³', padx=padx, pady=pady, fg='black', bg='white', command=cube, borderwidth=borderwidth, font=ex_font)
cube_root = Button(frame, text='3√', padx=padx, pady=pady, fg='black', bg='white', command=cube_root, borderwidth=borderwidth, font=backspace_font)
prop = Button(frame, text='∝', padx=padx, pady=pady, fg='black', bg='white', command=prop_cmd, borderwidth=borderwidth, font=('Arial', 16))
propo = Button(frame, text='⋮', padx=padx, pady=pady, fg='black', bg='white', command=propo_cmd, borderwidth=borderwidth, font=('Arial', 16))

# Functions
clear = Button(frame, text='Clear', padx=60, pady=27, fg='white', bg='green', command=clear_cmd, borderwidth=borderwidth, font=font )
onep = Button(frame, text='x¹', padx=padx, pady=pady, fg='black', bg='white', command=onep_cmd, borderwidth=borderwidth, font=ex_font)
fourp = Button(frame, text='x⁴', padx=padx, pady=pady, fg='black', bg='white', command=fourp_cmd, borderwidth=borderwidth, font=ex_font)
fivep = Button(frame, text='x⁵', padx=padx, pady=pady, fg='black', bg='white', command=fivep_cmd, borderwidth=borderwidth, font=ex_font)
sixp = Button(frame, text='x⁶', padx=padx, pady=pady, fg='black', bg='white', command=sixp_cmd, borderwidth=borderwidth, font=ex_font)
sevenp = Button(frame, text='x⁷', padx=padx, pady=pady, fg='black', bg='white', command=sevenp_cmd, borderwidth=borderwidth, font=ex_font)
eightp = Button(frame, text='x⁸', padx=padx, pady=pady, fg='black', bg='white', command=eightp_cmd, borderwidth=borderwidth, font=ex_font)
ninep = Button(frame, text='x⁹', padx=padx, pady=pady, fg='black', bg='white', command=ninep_cmd, borderwidth=borderwidth, font=ex_font)
zerop = Button(frame, text='x⁰', padx=padx, pady=pady, fg='black', bg='white', command=zerop_cmd, borderwidth=borderwidth, font=ex_font) 

therep = Button(frame, text='∴', padx=padx, pady=pady, fg='black', bg='white', command=therep_cmd, borderwidth=borderwidth, font=('Cambria', 17))
bcozp = Button(frame, text='∵', padx=padx, pady=pady, fg='black', bg='white', command=bcozp_cmd, borderwidth=borderwidth, font=('Cambria', 17))


backspace = Button(frame, text='α', padx=33, pady=pady, fg='white', bg='green', command=backspace_cmd, borderwidth=borderwidth, font=font)
beta = Button(frame, text='β', padx=33, pady=pady, fg='white', bg='green', command=beta_cmd, borderwidth=borderwidth, font=font)

#erase = Button(frame, text='←', padx=55, pady=pady, fg='white', bg='red', command=arrow_cmd, borderwidth=borderwidth, font=font )

# Grid Sys

#cut.grid(row=0, column=18)

text.grid(row=0, column=0, columnspan=120)

sq_root.grid(row=2, column=0)

onep.grid(row=3, column=2)
fourp.grid(row=3, column=3)
fivep.grid(row=3, column=4)
sixp.grid(row=3, column=5)
sevenp.grid(row=3, column=6)
eightp.grid(row=3, column=9)
ninep.grid(row=3, column=10)
zerop.grid(row=3, column=11)

therep.grid(row=3, column=12)
bcozp.grid(row=3, column=13)

propo.grid(row=3, column=16)
half.grid(row=3, column=17)
degree.grid(row=2, column=16)
quarter.grid(row=2, column=17)
pie.grid(row=2, column=6)
prop.grid(row=3, column=14)
cong.grid(row=2, column=9)
pm.grid(row=1, column=17)
unequal.grid(row=2, column=1)
larger_than.grid(row=2, column=2)
smaller_than.grid(row=2, column=3)
square.grid(row=3, column=1)
cube.grid(row=3, column=0)
equal.grid(row=1, column=13)
plus.grid(row=1, column=10)
minus.grid(row=1, column=11)
divide.grid(row=1, column=12)
multiply.grid(row=1, column=16)
triangles.grid(row=2, column=10)
angle.grid(row=2, column=11)
perp.grid(row=2, column=12)
parallel.grid(row=2, column=13)
box.grid(row=2, column=14)

percent.grid(row=2, column=4)
slash.grid(row=2, column=5)
backspace.grid(row=2, column=7)
beta.grid(row=2, column=8)
clear.grid(row=3, column=5,columnspan=6)


bracket.grid(row=1, column=14)
one.grid(row=1, column=0)
two.grid(row=1, column=1)
three.grid(row=1, column=2)
four.grid(row=1, column=3)
five.grid(row=1, column=4)
six.grid(row=1, column=5)
seven.grid(row=1, column=6)
eight.grid(row=1, column=7)
nine.grid(row=1, column=8)
zero.grid(row=1, column=9)


# Configuration
#text_scroll.config(command=Text.yview)
#root.mainloop()
# Alignment
#Text.grid(row=0, column=0)
#Text = Text(frame,width=97,height=10,font=('Arial', 20), selectbackground='yellow',
 #           selectforeground='black', undo=True, yscrollcommand=text_scroll.set)
#text_scroll = Scrollbar(frame)
root.mainloop()