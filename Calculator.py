from tkinter import *
import miniaudio

#Properties________________
okno = Tk()
okno.iconbitmap('susy.ico')
okno.title('Kalkulator')
okno.geometry('280x440')
okno.minsize(282, 440)
okno.maxsize(282, 440)

#integer________
aktualna = int(0)
wpisana = int(0)
znak = ""
stream = ""
znak_wykonaj = int(0)
n = int(0)
poprzedni = int(0)
ile_po_przecinku = int(0)
old_ile_po_przecinku = int(0)
ujemne = False
przecinek = False
second = False

#Functions________________
def play():
    global stream
    stream = miniaudio.stream_file("Click.wav")
    play_sound()

def equal_play():
    global stream
    stream = miniaudio.stream_file("Equal_click.wav")
    play_sound()

def second_play():
    global stream
    stream = miniaudio.stream_file("Nose_Click.mp3")
    play_sound()

def Boom_Play():
    global stream
    stream = miniaudio.stream_file("Explosion.wav")
    play_sound()

def action_play():
    global stream
    stream = miniaudio.stream_file("Action.wav")
    play_sound()

def play_sound():
    miniaudio.PlaybackDevice().start(stream)

#Znaki_____________________
def opposed():
    global aktualna
    global ujemne
    if aktualna != 0:
        if aktualna >= 0:
            ujemne = True
        elif aktualna < 0:
            ujemne = False
        aktualna = aktualna - aktualna - aktualna
    wyswitlacz.config(text=aktualna)

def comma():
    global przecinek
    global ile_po_przecinku
    if przecinek == False:
        ile_po_przecinku = 1
    przecinek = True
    wyswitlacz.config(text=aktualna)

def equal():
    global znak_wykonaj
    global znak
    global poprzedni
    global aktualna
    global ile_po_przecinku
    global przecinek
    global old_ile_po_przecinku
    blad = False
    if znak_wykonaj == 1:
        poprzedni += aktualna
    elif znak_wykonaj == 2:
        poprzedni -= aktualna
    elif znak_wykonaj == 3:
        poprzedni *= aktualna
    elif znak_wykonaj == 4:
        if aktualna == 0:
            wyswitlacz.config(text="Błąd")
            blad = True
        else: 
            poprzedni /= aktualna
    znak = ""
    wyswitlacz_znaku.config(text=znak)
    poprzedni = round(poprzedni, old_ile_po_przecinku)
    if blad == False:
        if poprzedni == 0 and znak_wykonaj == 4:
            wyswitlacz.config(text=aktualna)
        else:
            wyswitlacz.config(text=poprzedni)
    aktualna = poprzedni
    znak_wykonaj = 0
    poprzedni = 0
    ile_po_przecinku = 0
    old_ile_po_przecinku = 0
    przecinek = False

def z_n():
    global poprzedni
    global aktualna
    global ile_po_przecinku
    global przecinek
    global old_ile_po_przecinku
    przecinek = False
    poprzedni = aktualna
    aktualna = 0
    old_ile_po_przecinku = ile_po_przecinku
    ile_po_przecinku = 0

def wys_znak():
    global znak
    global second
    if second == False:
        wyswitlacz_znaku.config(text=znak)

def increase():
    global znak_wykonaj
    global znak
    global poprzedni
    global aktualna
    znak = "+"
    poprzedni = aktualna
    znak_wykonaj = 1
    wys_znak()
    z_n()

def decrease():
    global znak_wykonaj
    global znak
    global poprzedni
    global aktualna
    znak = "-"
    poprzedni = aktualna
    znak_wykonaj = 2
    wys_znak()
    z_n()

def multiplication():
    global znak_wykonaj
    global znak
    global poprzedni
    global aktualna
    znak = "×"
    poprzedni = aktualna
    znak_wykonaj = 3
    wys_znak()
    z_n()

def division():
    global znak_wykonaj
    global znak
    global poprzedni
    global aktualna
    znak = "÷"
    poprzedni = aktualna
    znak_wykonaj = 4
    wys_znak()
    z_n()

def C():
    global aktualna
    global wpisana
    global przecinek
    global ujemna
    aktualna = 0
    przecinek = False
    ujemna = False
    wpisana = 0
    wyswitlacz.config(text=aktualna)
    wyswitlacz_znaku.config(text=znak)

def CE():
    global znak
    global aktualna
    global wpisana
    global ujemna
    global przecinek
    global poprzedni
    global ile_po_przecinku
    ile_po_przecinku = 0
    ujemna = False
    przecinek = False
    znak = ""
    poprzedni = 0
    aktualna = 0
    wpisana = 0
    wyswitlacz.config(text=aktualna)
    wyswitlacz_znaku.config(text=znak)

def second_mode():
    global second
    if second == False:
        second = True
        Buttondecrease.config(text="²√x")
        Buttonincrease.config(text="x!")
        Buttonmultiplication.config(text="x²")
        Buttondivision.config(text="1/x")
    elif second == True:
        second = False
        Buttondecrease.config(text="-")
        Buttonincrease.config(text="+")
        Buttonmultiplication.config(text="×")
        Buttondivision.config(text="÷")

#Liczby______________________________________________
def liczba():
    global n
    global aktualna
    global przecinek
    global ujemne
    global ile_po_przecinku
    global poprzedni
    if przecinek == True:
        aktualna *= 10**ile_po_przecinku
        aktualna = round(aktualna, ile_po_przecinku)
        if aktualna >= 0:
            aktualna += wpisana
        elif aktualna < 0:
            #ujemna
            aktualna = aktualna - aktualna - aktualna
            aktualna += wpisana
            aktualna = aktualna - aktualna - aktualna
        aktualna /= 10**ile_po_przecinku
        ile_po_przecinku += 1
    else:
        aktualna *= 10
        if aktualna >= 0:
            aktualna += wpisana
        else:
            #ujemna
            aktualna = aktualna - aktualna - aktualna
            aktualna += wpisana
            aktualna = aktualna - aktualna - aktualna
    if znak_wykonaj != 0:
        wyswitlacz.config(text=aktualna)
    wyswitlacz.config(text=aktualna)

def one():
    global wpisana
    wpisana = 1
    liczba()

def two():
    global wpisana
    wpisana = 2
    liczba()

def three():
    global wpisana
    wpisana = 3
    liczba()

def four():
    global wpisana
    wpisana = 4
    liczba()

def five():
    global wpisana
    wpisana = 5
    liczba()

def six():
    global wpisana
    wpisana = 6
    liczba()

def seven():
    global wpisana
    wpisana = 7
    liczba()

def eight():
    global wpisana
    wpisana = 8
    liczba()

def nine():
    global wpisana
    wpisana = 9
    liczba()

def zero():
    global wpisana
    wpisana = 0
    liczba()

font_size = 15

#Buttons_______________________________________________________________________
Buttonopposed = Button(okno, text = '+/-', font=('', font_size), bg='gray', fg='black', command=lambda: [play(), opposed()])
Buttonopposed.place(x=10, y=372, width = 58, height = 58)
Button0 = Button(okno, text = '0', font=('', font_size), bg='gray', fg='black', command=lambda: [play(), zero()])
Button0.place(x=78, y=372, width = 58, height = 58)
Buttoncomma = Button(okno, text = ',', font=('', font_size), bg='gray', fg='black', command=lambda: [play(), comma()])
Buttoncomma.place(x=146, y=372, width = 58, height = 58)
Buttonequal = Button(okno, text = '=', font=('', font_size), bg='gray', fg='black', command=lambda: [equal_play(), equal()])
Buttonequal.place(x=214, y=372, width = 58, height = 58)
Button1 = Button(okno, text = '1', font=('', font_size), bg='gray', fg='black', command=lambda: [play(), one()])
Button1.place(x=10, y=304, width = 58, height = 58)
Button2 = Button(okno, text = '2', font=('', font_size), bg='gray', fg='black', command=lambda: [play(), two()])
Button2.place(x=78, y=304, width = 58, height = 58)
Button3 = Button(okno, text = '3', font=('', font_size), bg='gray', fg='black', command=lambda: [play(), three()])
Button3.place(x=146, y=304, width = 58, height = 58)
Buttonincrease = Button(okno, text = '+', font=('', font_size), bg='gray', fg='black', command=lambda: [action_play(), increase()])
Buttonincrease.place(x=214, y=304, width = 58, height = 58)
Button4 = Button(okno, text = '4', font=('', font_size), bg='gray', fg='black', command=lambda: [play(), four()])
Button4.place(x=10, y=236, width = 58, height = 58)
Button5 = Button(okno, text = '5', font=('', font_size), bg='gray', fg='black', command=lambda: [play(), five()])
Button5.place(x=78, y=236, width = 58, height = 58)
Button6 = Button(okno, text = '6', font=('', font_size), bg='gray', fg='black', command=lambda: [play(), six()])
Button6.place(x=146, y=236, width = 58, height = 58)
Buttondecrease = Button(okno, text = '-', font=('', font_size), bg='gray', fg='black', command=lambda: [action_play(), decrease()])
Buttondecrease.place(x=214, y=236, width = 58, height = 58)
Button7 = Button(okno, text = '7', font=('', font_size),bg='gray', fg='black', command=lambda: [play(), seven()])
Button7.place(x=10, y=168, width = 58, height = 58)
Button8 = Button(okno, text = '8', font=('', font_size), bg='gray', fg='black', command=lambda: [play(), eight()])
Button8.place(x=78, y=168, width = 58, height = 58)
Button9 = Button(okno, text = '9', font=('', font_size), bg='gray', fg='black', command=lambda: [play(), nine()])
Button9.place(x=146, y=168, width = 58, height = 58)
Buttonmultiplication = Button(okno, text = '×', font=('', font_size), bg='gray', fg='black', command=lambda: [action_play(), multiplication()])
Buttonmultiplication.place(x=214, y=168, width = 58, height = 58)
ButtonCE = Button(okno, text = 'CE', font=('', font_size), bg='gray', fg='black', command=lambda: [Boom_Play(), CE()])
ButtonCE.place(x=10, y=129, width = 81, height = 29)
ButtonC = Button(okno, text = 'C', font=('', font_size), bg='gray', fg='black', command=lambda: [Boom_Play(), C()])
ButtonC.place(x=101, y=129, width = 80, height = 29)
Buttondivision = Button(okno, text = '÷', font=('', font_size), bg='gray', fg='black', command=lambda: [action_play(), division()])
Buttondivision.place(x=191, y=129, width = 81, height = 29)
wyswitlacz=Label(okno, text=aktualna, font=('Arial', 20), anchor="w")
wyswitlacz.place(x=10, y=10, width = 262, height = 99)
wyswitlacz_znaku=Label(okno, text="", font=('Arial', 12), anchor="e")
wyswitlacz_znaku.place(x=10, y=10, width = 262, height = 15)
Button2nd = Button(okno, text = '2nd', font=('', font_size - 2), bg='gray', fg='black', command=lambda: [second_play(), second_mode()])
Button2nd.place(x=10, y=100, width=262, height=22)

#l = Label(okno, text = "Calculate integers")
#l.config(font =("Courier", 14))
#l.pack()

okno.mainloop()
