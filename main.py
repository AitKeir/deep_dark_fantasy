import traceback
import tkinter as tk
import win32api
import math
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import StringVar
from datetime import datetime
from support import support
from formulas import *

class ChoiceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ChoRace = Toplevel(window)
        self.ChoRace.title('Раса персонажа')
        self.ChoRace.resizable(width=False, height=False)
        self.ChoRace.columnconfigure(0, pad=3)
        self.var = tk.StringVar()
        self.var.set("Человек")
        self.buttons = [self.create_radio(c) for c in OPTIONS]
        self.i = 0
        for button in self.buttons:
            self.ChoRace.rowconfigure(self.i, pad=3)
            button.grid(row = self.i, column = 0)
            self.i += 1

        self.okButt = tk.Button(self.ChoRace, command=change_race, text='Выбрать расу')
        self.okButt.grid(row = self.i, column = 0)

    def change_race(self):
        raceLabel2.config(text = self.var.get())

    def create_radio(self, option):
        text = value = option
        return tk.Radiobutton(self.ChoRace, text=text, value=value,
                              command=self.print_option,
                              variable=self.var)

    def print_option(self):
        print(self.var.get())

class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """
    def __init__(self, widget, text='widget info'):
        self.waittime = 500     #miliseconds
        self.wraplength = 300   #pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                       background="#ffffff", relief='solid', borderwidth=1,
                       wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()

def exit(): #Остановка скрипта
    window.destroy()

def change_main_window(window,list_obj):
    for object_name in list_obj:
        if object_name.winfo_viewable():
            object_name.grid_remove()

def new_exp():
    global expNow,lvlNow,allAtt
    if addExp.get():
        expNow = plus_exp(expNow,int(addExp.get()),learningAttInt)
        expNowAttLabel.config(text='{0}'.format(expNow))
        lastLVL = lvlNow
        lvlNow = what_lvl(list_lvl,expNow)
        if lvlNow > lastLVL:
            allAtt = allAtt+(lvlNow-lastLVL)
            levelLabel2.config(text='{0}'.format(lvlNow))
            availableAttNumb.config(text='{0}'.format(allAtt))
        addExp.delete(0, 'end')

def create_attribute_window():
    ChoAtt = Toplevel(window)
    ChoAtt.title('Характеристики персонажа')
    ChoAtt.resizable(width=False, height=False)

    ChoAtt.rowconfigure(0, pad=3)
    ChoAtt.rowconfigure(1, pad=3)
    ChoAtt.columnconfigure(0, pad=3)
    ChoAtt.columnconfigure(1, pad=3)
    ChoAtt.columnconfigure(2, pad=3)
    ChoAtt.columnconfigure(3, pad=3)

    frameStr=Frame(ChoAtt, relief=RAISED, borderwidth=1)
    frameAgi=Frame(ChoAtt, relief=RAISED, borderwidth=1)
    frameInt=Frame(ChoAtt, relief=RAISED, borderwidth=1)
    frameBody=Frame(ChoAtt, relief=RAISED, borderwidth=1)

    # str
    # config
    frameStr.rowconfigure(0, pad=3)
    frameStr.rowconfigure(1, pad=3)
    frameStr.rowconfigure(2, pad=3)
    frameStr.rowconfigure(3, pad=3)
    frameStr.rowconfigure(4, pad=3)
    frameStr.rowconfigure(5, pad=3)
    frameStr.rowconfigure(6, pad=3)
    frameStr.columnconfigure(0, pad=3)
    frameStr.columnconfigure(1, pad=3)
    frameStr.columnconfigure(2, pad=3)
    frameStr.grid(row=0, column=0)



    # labeles
    mainStrLabel = Label(frameStr, text=list(support['attributes'].keys())[0])
    meleFight = Label(frameStr, text='{0}:'.format(list(support['attributes'][list(support['attributes'].keys())[0]].keys())[0]))
    meleFightAtt = Label(frameStr, text='{0}'.format(meleFightAttInt))
    meleFightButt = Button(frameStr, command=lambda: add_att(0,meleFightAtt), text='+')
    shoot = Label(frameStr, text='{0}:'.format(list(support['attributes'][list(support['attributes'].keys())[0]].keys())[1]))
    shootAtt = Label(frameStr, text='{0}'.format(shootAttInt))
    shootButt = Button(frameStr, command=lambda: add_att(1,shootAtt), text='+')
    strongHits = Label(frameStr, text='{0}:'.format(list(support['attributes'][list(support['attributes'].keys())[0]].keys())[2]))
    strongHitsAtt = Label(frameStr, text='{0}'.format(strongHitsAttInt))
    strongHitsButt = Button(frameStr, command=lambda: add_att(2,strongHitsAtt), text='+')
    warBusiness = Label(frameStr, text='{0}:'.format(list(support['attributes'][list(support['attributes'].keys())[0]].keys())[3]))
    warBusinessAtt= Label(frameStr, text='{0}'.format(warBusinessAttInt))
    warBusinessButt = Button(frameStr, command=lambda: add_att(3,warBusinessAtt), text='+')
    tactics = Label(frameStr, text='{0}:'.format(list(support['attributes'][list(support['attributes'].keys())[0]].keys())[4]))
    tacticsAtt= Label(frameStr, text='{0}'.format(tacticsAttInt))
    tacticsButt = Button(frameStr, command=lambda: add_att(4,tacticsAtt), text='+')

    # tooltips
    CreateToolTip(meleFight,support['attributes'][list(support['attributes'].keys())[0]][list(support['attributes'][list(support['attributes'].keys())[0]].keys())[0]]['tooltip'])
    CreateToolTip(shoot,support['attributes'][list(support['attributes'].keys())[0]][list(support['attributes'][list(support['attributes'].keys())[0]].keys())[1]]['tooltip'])
    CreateToolTip(strongHits,support['attributes'][list(support['attributes'].keys())[0]][list(support['attributes'][list(support['attributes'].keys())[0]].keys())[2]]['tooltip'])
    CreateToolTip(warBusiness,support['attributes'][list(support['attributes'].keys())[0]][list(support['attributes'][list(support['attributes'].keys())[0]].keys())[3]]['tooltip'])
    CreateToolTip(tactics,support['attributes'][list(support['attributes'].keys())[0]][list(support['attributes'][list(support['attributes'].keys())[0]].keys())[4]]['tooltip'])

    # grids
    mainStrLabel.grid(row=0, column=0, columnspan=3)
    meleFight.grid(row=1, column=0)
    meleFightAtt.grid(row=1, column=1)
    meleFightButt.grid(row=1, column=2)
    shoot.grid(row=2, column=0)
    shootAtt.grid(row=2, column=1)
    shootButt.grid(row=2, column=2)
    strongHits.grid(row=3, column=0)
    strongHitsAtt.grid(row=3, column=1)
    strongHitsButt.grid(row=3, column=2)
    warBusiness.grid(row=4, column=0)
    warBusinessAtt.grid(row=4, column=1)
    warBusinessButt.grid(row=4, column=2)
    tactics.grid(row=5, column=0)
    tacticsAtt.grid(row=5, column=1)
    tacticsButt.grid(row=5, column=2)

    # agi
    # config
    frameAgi.rowconfigure(0, pad=3)
    frameAgi.rowconfigure(1, pad=3)
    frameAgi.rowconfigure(2, pad=3)
    frameAgi.rowconfigure(3, pad=3)
    frameAgi.rowconfigure(4, pad=3)
    frameAgi.rowconfigure(5, pad=3)
    frameAgi.rowconfigure(6, pad=3)
    frameAgi.columnconfigure(0, pad=3)
    frameAgi.columnconfigure(1, pad=3)
    frameAgi.columnconfigure(2, pad=3)
    frameAgi.grid(row=0, column=1)



    # labeles
    mainAgiLabel = Label(frameAgi, text=list(support['attributes'].keys())[1])
    attack = Label(frameAgi, text='{0}:'.format(list(support['attributes'][list(support['attributes'].keys())[1]].keys())[0]))
    attackAtt = Label(frameAgi, text='{0}'.format(attackAttInt))
    attackButt = Button(frameAgi, command=lambda: add_att(5,attackAtt), text='+')
    evasion = Label(frameAgi, text='{0}:'.format(list(support['attributes'][list(support['attributes'].keys())[1]].keys())[1]))
    evasionAtt = Label(frameAgi, text='{0}'.format(evasionAttInt))
    evasionButt = Button(frameAgi, command=lambda: add_att(6,evasionAtt), text='+')
    haste = Label(frameAgi, text='{0}:'.format(list(support['attributes'][list(support['attributes'].keys())[1]].keys())[2]))
    hasteAtt = Label(frameAgi, text='{0}'.format(hasteAttInt))
    hasteButt = Button(frameAgi, command=lambda: add_att(7,hasteAtt), text='+')
    coldBlood = Label(frameAgi, text='{0}:'.format(list(support['attributes'][list(support['attributes'].keys())[1]].keys())[3]))
    coldBloodAtt= Label(frameAgi, text='{0}'.format(coldBloodAttInt))
    coldBloodButt = Button(frameAgi, command=lambda: add_att(8,coldBloodAtt), text='+')
    thiefArt = Label(frameAgi, text='{0}:'.format(list(support['attributes'][list(support['attributes'].keys())[1]].keys())[4]))
    thiefArtAtt= Label(frameAgi, text='{0}'.format(thiefArtAttInt))
    thiefArtButt = Button(frameAgi, command=lambda: add_att(9,thiefArtAtt), text='+')

    # tooltips
    CreateToolTip(attack,support['attributes'][list(support['attributes'].keys())[1]][list(support['attributes'][list(support['attributes'].keys())[1]].keys())[0]]['tooltip'])
    CreateToolTip(evasion,support['attributes'][list(support['attributes'].keys())[1]][list(support['attributes'][list(support['attributes'].keys())[1]].keys())[1]]['tooltip'])
    CreateToolTip(haste,support['attributes'][list(support['attributes'].keys())[1]][list(support['attributes'][list(support['attributes'].keys())[1]].keys())[2]]['tooltip'])
    CreateToolTip(coldBlood,support['attributes'][list(support['attributes'].keys())[1]][list(support['attributes'][list(support['attributes'].keys())[1]].keys())[3]]['tooltip'])
    CreateToolTip(thiefArt,support['attributes'][list(support['attributes'].keys())[1]][list(support['attributes'][list(support['attributes'].keys())[1]].keys())[4]]['tooltip'])

    # grids
    mainAgiLabel.grid(row=0, column=0, columnspan=3)
    attack.grid(row=1, column=0)
    attackAtt.grid(row=1, column=1)
    attackButt.grid(row=1, column=2)
    evasion.grid(row=2, column=0)
    evasionAtt.grid(row=2, column=1)
    evasionButt.grid(row=2, column=2)
    haste.grid(row=3, column=0)
    hasteAtt.grid(row=3, column=1)
    hasteButt.grid(row=3, column=2)
    coldBlood.grid(row=4, column=0)
    coldBloodAtt.grid(row=4, column=1)
    coldBloodButt.grid(row=4, column=2)
    thiefArt.grid(row=5, column=0)
    thiefArtAtt.grid(row=5, column=1)
    thiefArtButt.grid(row=5, column=2)

    # int
    # config
    frameInt.rowconfigure(0, pad=3)
    frameInt.rowconfigure(1, pad=3)
    frameInt.rowconfigure(2, pad=3)
    frameInt.rowconfigure(3, pad=3)
    frameInt.rowconfigure(4, pad=3)
    frameInt.rowconfigure(5, pad=3)
    frameInt.rowconfigure(6, pad=3)
    frameInt.columnconfigure(0, pad=3)
    frameInt.columnconfigure(1, pad=3)
    frameInt.columnconfigure(2, pad=3)
    frameInt.grid(row=0, column=2)



    # labeles
    mainIntLabel = Label(frameInt, text=list(support['attributes'].keys())[2])
    mana = Label(frameInt, text='{0}:'.format(list(support['attributes'][list(support['attributes'].keys())[2]].keys())[0]))
    manaAtt = Label(frameInt, text='{0}'.format(manaAttInt))
    manaButt = Button(frameInt, command=lambda: add_att(10,manaAtt), text='+')
    firstAid = Label(frameInt, text='{0}:'.format(list(support['attributes'][list(support['attributes'].keys())[2]].keys())[1]))
    firstAidAtt = Label(frameInt, text='{0}'.format(firstAidAttInt))
    firstAidButt = Button(frameInt, command=lambda: add_att(11,firstAidAtt), text='+')
    magicCircle = Label(frameInt, text='{0}:'.format(list(support['attributes'][list(support['attributes'].keys())[2]].keys())[2]))
    magicCircleAtt = Label(frameInt, text='{0}'.format(magicCircleAttInt))
    magicCircleButt = Button(frameInt, command=lambda: add_att(12,magicCircleAtt), text='+')
    magicPower = Label(frameInt, text='{0}:'.format(list(support['attributes'][list(support['attributes'].keys())[2]].keys())[3]))
    magicPowerAtt= Label(frameInt, text='{0}'.format(magicPowerAttInt))
    magicPowerButt = Button(frameInt, command=lambda: add_att(13,magicPowerAtt), text='+')
    learning = Label(frameInt, text='{0}:'.format(list(support['attributes'][list(support['attributes'].keys())[2]].keys())[4]))
    learningAtt= Label(frameInt, text='{0}'.format(learningAttInt))
    learningButt = Button(frameInt, command=lambda: add_att(14,learningAtt), text='+')

    # tooltips
    CreateToolTip(mana,support['attributes'][list(support['attributes'].keys())[2]][list(support['attributes'][list(support['attributes'].keys())[2]].keys())[0]]['tooltip'])
    CreateToolTip(firstAid,support['attributes'][list(support['attributes'].keys())[2]][list(support['attributes'][list(support['attributes'].keys())[2]].keys())[1]]['tooltip'])
    CreateToolTip(magicCircle,support['attributes'][list(support['attributes'].keys())[2]][list(support['attributes'][list(support['attributes'].keys())[2]].keys())[2]]['tooltip'])
    CreateToolTip(magicPower,support['attributes'][list(support['attributes'].keys())[2]][list(support['attributes'][list(support['attributes'].keys())[2]].keys())[3]]['tooltip'])
    CreateToolTip(learning,support['attributes'][list(support['attributes'].keys())[2]][list(support['attributes'][list(support['attributes'].keys())[2]].keys())[4]]['tooltip'])

    # grids
    mainIntLabel.grid(row=0, column=0, columnspan=3)
    mana.grid(row=1, column=0)
    manaAtt.grid(row=1, column=1)
    manaButt.grid(row=1, column=2)
    firstAid.grid(row=2, column=0)
    firstAidAtt.grid(row=2, column=1)
    firstAidButt.grid(row=2, column=2)
    magicCircle.grid(row=3, column=0)
    magicCircleAtt.grid(row=3, column=1)
    magicCircleButt.grid(row=3, column=2)
    magicPower.grid(row=4, column=0)
    magicPowerAtt.grid(row=4, column=1)
    magicPowerButt.grid(row=4, column=2)
    learning.grid(row=5, column=0)
    learningAtt.grid(row=5, column=1)
    learningButt.grid(row=5, column=2)

    # body
    # config
    frameBody.rowconfigure(0, pad=3)
    frameBody.rowconfigure(1, pad=3)
    frameBody.rowconfigure(2, pad=3)
    frameBody.rowconfigure(3, pad=3)
    frameBody.rowconfigure(4, pad=3)
    frameBody.rowconfigure(5, pad=3)
    frameBody.rowconfigure(6, pad=3)
    frameBody.columnconfigure(0, pad=3)
    frameBody.columnconfigure(1, pad=3)
    frameBody.columnconfigure(2, pad=3)
    frameBody.grid(row=0, column=3)



    # labeles
    mainBodyLabel = Label(frameBody, text=list(support['attributes'].keys())[3])
    health = Label(frameBody, text='{0}:'.format(list(support['attributes'][list(support['attributes'].keys())[3]].keys())[0]))
    healthAtt = Label(frameBody, text='{0}'.format(healthAttInt))
    healthButt = Button(frameBody, command=lambda: add_att(15,healthAtt), text='+')
    energy = Label(frameBody, text='{0}:'.format(list(support['attributes'][list(support['attributes'].keys())[3]].keys())[1]))
    energyAtt = Label(frameBody, text='{0}'.format(energyAttInt))
    energyButt = Button(frameBody, command=lambda: add_att(16,energyAtt), text='+')
    resist = Label(frameBody, text='{0}:'.format(list(support['attributes'][list(support['attributes'].keys())[3]].keys())[2]))
    resistAtt = Label(frameBody, text='{0}'.format(resistAttInt))
    resistButt = Button(frameBody, command=lambda: add_att(17,resistAtt), text='+')
    secondBreath = Label(frameBody, text='{0}:'.format(list(support['attributes'][list(support['attributes'].keys())[3]].keys())[3]))
    secondBreathAtt= Label(frameBody, text='{0}'.format(secondBreathAttInt))
    secondBreathButt = Button(frameBody, command=lambda: add_att(18,secondBreathAtt), text='+')
    steelBody = Label(frameBody, text='{0}:'.format(list(support['attributes'][list(support['attributes'].keys())[3]].keys())[4]))
    steelBodyAtt= Label(frameBody, text='{0}'.format(steelBodyAttInt))
    steelBodyButt = Button(frameBody, command=lambda: add_att(19,steelBodyAtt), text='+')

    # tooltips
    CreateToolTip(health,support['attributes'][list(support['attributes'].keys())[3]][list(support['attributes'][list(support['attributes'].keys())[3]].keys())[0]]['tooltip'])
    CreateToolTip(energy,support['attributes'][list(support['attributes'].keys())[3]][list(support['attributes'][list(support['attributes'].keys())[3]].keys())[1]]['tooltip'])
    CreateToolTip(resist,support['attributes'][list(support['attributes'].keys())[3]][list(support['attributes'][list(support['attributes'].keys())[3]].keys())[2]]['tooltip'])
    CreateToolTip(secondBreath,support['attributes'][list(support['attributes'].keys())[3]][list(support['attributes'][list(support['attributes'].keys())[3]].keys())[3]]['tooltip'])
    CreateToolTip(steelBody,support['attributes'][list(support['attributes'].keys())[3]][list(support['attributes'][list(support['attributes'].keys())[3]].keys())[4]]['tooltip'])

    # grids
    mainBodyLabel.grid(row=0, column=0, columnspan=3)
    health.grid(row=1, column=0)
    healthAtt.grid(row=1, column=1)
    healthButt.grid(row=1, column=2)
    energy.grid(row=2, column=0)
    energyAtt.grid(row=2, column=1)
    energyButt.grid(row=2, column=2)
    resist.grid(row=3, column=0)
    resistAtt.grid(row=3, column=1)
    resistButt.grid(row=3, column=2)
    secondBreath.grid(row=4, column=0)
    secondBreathAtt.grid(row=4, column=1)
    secondBreathButt.grid(row=4, column=2)
    steelBody.grid(row=5, column=0)
    steelBodyAtt.grid(row=5, column=1)
    steelBodyButt.grid(row=5, column=2)

def create_magic_window():
    global spell11ProgressLabelInt,spell12ProgressLabelInt,spell21ProgressLabelInt,spell22ProgressLabelInt,spell31ProgressLabelInt,spell32ProgressLabelInt,spell41ProgressLabelInt,spell42ProgressLabelInt,spell51ProgressLabelInt,spell52ProgressLabelInt,spell11LVLInt,spell12LVLInt,spell21LVLInt,spell22LVLInt,spell31LVLInt,spell32LVLInt,spell41LVLInt,spell42LVLInt,spell51LVLInt,spell52LVLInt,magicCircleAttLabel,spell211ProgressLabelInt,spell212ProgressLabelInt,spell221ProgressLabelInt,spell222ProgressLabelInt,spell231ProgressLabelInt,spell232ProgressLabelInt,spell241ProgressLabelInt,spell242ProgressLabelInt,spell251ProgressLabelInt,spell252ProgressLabelInt,spell211LVLInt,spell212LVLInt,spell221LVLInt,spell222LVLInt,spell231LVLInt,spell232LVLInt,spell241LVLInt,spell242LVLInt,spell251LVLInt,spell252LVLInt,magicCircleAttLabel2,firstSchMag,secondSchMag

    def change_lines_in_magic_window(event):
        global firstSchMag
        firstSchMag = firstMagicSchool.get()
        spell11.config(text = list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[0]].keys())[0])
        CreateToolTip(spell11,'{0}\n{1}'.format(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[0]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[0]].keys())[0]]['tooltip'],support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[0]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[0]].keys())[0]]['level']))
        spell12.config(text = list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[0]].keys())[1])
        CreateToolTip(spell12,'{0}\n{1}'.format(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[0]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[0]].keys())[1]]['tooltip'],support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[0]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[0]].keys())[1]]['level']))
        spell21.config(text = list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[1]].keys())[0])
        CreateToolTip(spell21,'{0}\n{1}'.format(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[1]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[1]].keys())[0]]['tooltip'],support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[1]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[1]].keys())[0]]['level']))
        spell22.config(text = list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[1]].keys())[1])
        CreateToolTip(spell22,'{0}\n{1}'.format(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[1]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[1]].keys())[1]]['tooltip'],support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[1]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[1]].keys())[1]]['level']))
        spell31.config(text = list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[2]].keys())[0])
        CreateToolTip(spell31,'{0}\n{1}'.format(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[2]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[2]].keys())[0]]['tooltip'],support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[2]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[2]].keys())[0]]['level']))
        spell32.config(text = list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[2]].keys())[1])
        CreateToolTip(spell32,'{0}\n{1}'.format(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[2]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[2]].keys())[1]]['tooltip'],support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[2]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[2]].keys())[1]]['level']))
        spell41.config(text = list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[3]].keys())[0])
        CreateToolTip(spell41,'{0}\n{1}'.format(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[3]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[3]].keys())[0]]['tooltip'],support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[3]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[3]].keys())[0]]['level']))
        spell42.config(text = list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[3]].keys())[1])
        CreateToolTip(spell42,'{0}\n{1}'.format(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[3]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[3]].keys())[1]]['tooltip'],support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[3]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[3]].keys())[1]]['level']))
        spell51.config(text = list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[4]].keys())[0])
        CreateToolTip(spell51,'{0}\n{1}'.format(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[4]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[4]].keys())[0]]['tooltip'],support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[4]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[4]].keys())[0]]['level']))
        spell52.config(text = list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[4]].keys())[1])
        CreateToolTip(spell52,'{0}\n{1}'.format(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[4]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[4]].keys())[1]]['tooltip'],support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[4]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[4]].keys())[1]]['level']))

    def change_lines_in_magic_window2(event):
        global secondSchMag
        secondSchMag = secondMagicSchool.get()
        spell211.config(text = list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[0]].keys())[0])
        CreateToolTip(spell211,'{0}\n{1}'.format(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[0]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[0]].keys())[0]]['tooltip'],support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[0]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[0]].keys())[0]]['level']))
        spell212.config(text = list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[0]].keys())[1])
        CreateToolTip(spell212,'{0}\n{1}'.format(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[0]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[0]].keys())[1]]['tooltip'],support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[0]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[0]].keys())[1]]['level']))
        spell221.config(text = list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[1]].keys())[0])
        CreateToolTip(spell221,'{0}\n{1}'.format(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[1]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[1]].keys())[0]]['tooltip'],support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[1]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[1]].keys())[0]]['level']))
        spell222.config(text = list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[1]].keys())[1])
        CreateToolTip(spell222,'{0}\n{1}'.format(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[1]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[1]].keys())[1]]['tooltip'],support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[1]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[1]].keys())[1]]['level']))
        spell231.config(text = list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[2]].keys())[0])
        CreateToolTip(spell231,'{0}\n{1}'.format(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[2]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[2]].keys())[0]]['tooltip'],support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[2]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[2]].keys())[0]]['level']))
        spell232.config(text = list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[2]].keys())[1])
        CreateToolTip(spell232,'{0}\n{1}'.format(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[2]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[2]].keys())[1]]['tooltip'],support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[2]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[2]].keys())[1]]['level']))
        spell241.config(text = list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[3]].keys())[0])
        CreateToolTip(spell241,'{0}\n{1}'.format(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[3]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[3]].keys())[0]]['tooltip'],support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[3]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[3]].keys())[0]]['level']))
        spell242.config(text = list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[3]].keys())[1])
        CreateToolTip(spell242,'{0}\n{1}'.format(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[3]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[3]].keys())[1]]['tooltip'],support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[3]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[3]].keys())[1]]['level']))
        spell251.config(text = list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[4]].keys())[0])
        CreateToolTip(spell251,'{0}\n{1}'.format(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[4]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[4]].keys())[0]]['tooltip'],support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[4]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[4]].keys())[0]]['level']))
        spell252.config(text = list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[4]].keys())[1])
        CreateToolTip(spell252,'{0}\n{1}'.format(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[4]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[4]].keys())[1]]['tooltip'],support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[4]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[4]].keys())[1]]['level']))

    def add_spell_exp(num):
        global spell11ProgressLabelInt,spell12ProgressLabelInt,spell21ProgressLabelInt,spell22ProgressLabelInt,spell31ProgressLabelInt,spell32ProgressLabelInt,spell41ProgressLabelInt,spell42ProgressLabelInt,spell51ProgressLabelInt,spell52ProgressLabelInt,spell11LVLInt,spell12LVLInt,spell21LVLInt,spell22LVLInt,spell31LVLInt,spell32LVLInt,spell41LVLInt,spell42LVLInt,spell51LVLInt,spell52LVLInt,spell211ProgressLabelInt,spell212ProgressLabelInt,spell221ProgressLabelInt,spell222ProgressLabelInt,spell231ProgressLabelInt,spell232ProgressLabelInt,spell241ProgressLabelInt,spell242ProgressLabelInt,spell251ProgressLabelInt,spell252ProgressLabelInt,spell211LVLInt,spell212LVLInt,spell221LVLInt,spell222LVLInt,spell231LVLInt,spell232LVLInt,spell241LVLInt,spell242LVLInt,spell251LVLInt,spell252LVLInt

        if num == 0:
            if magicCircleAttInt == 1:
                spell11ProgressLabelInt += 1
                if 6 > math.floor(spell11ProgressLabelInt/10 + 1) > spell11LVLInt:
                    spell11LVLInt = math.floor(spell11ProgressLabelInt/10 + 1)
                    spell11LVLLabel.config(text='{0}'.format(spell11LVLInt))
                spell11ProgressLabel.config(text='{0}'.format(spell11ProgressLabelInt))
        elif num == 1:
            if magicCircleAttInt == 1:
                spell12ProgressLabelInt += 1
                if 6 > math.floor(spell12ProgressLabelInt/10 + 1) > spell12LVLInt:
                    spell12LVLInt = math.floor(spell12ProgressLabelInt/10 + 1)
                    spell12LVLLabel.config(text='{0}'.format(spell12LVLInt))
                spell12ProgressLabel.config(text='{0}'.format(spell12ProgressLabelInt))
        elif num == 2:
            if magicCircleAttInt == 2:
                spell21ProgressLabelInt += 1
                if 6 > math.floor(spell21ProgressLabelInt/10 + 1) > spell21LVLInt:
                    spell21LVLInt = math.floor(spell21ProgressLabelInt/10 + 1)
                    spell21LVLLabel.config(text='{0}'.format(spell21LVLInt))
                spell21ProgressLabel.config(text='{0}'.format(spell21ProgressLabelInt))
        elif num == 3:
            if magicCircleAttInt == 2:
                spell22ProgressLabelInt += 1
                if 6 > math.floor(spell22ProgressLabelInt/10 + 1) > spell22LVLInt:
                    spell22LVLInt = math.floor(spell22ProgressLabelInt/10 + 1)
                    spell22LVLLabel.config(text='{0}'.format(spell22LVLInt))
                spell22ProgressLabel.config(text='{0}'.format(spell22ProgressLabelInt))
        elif num == 4:
            if magicCircleAttInt == 3:
                spell31ProgressLabelInt += 1
                if 6 > math.floor(spell31ProgressLabelInt/10 + 1) > spell31LVLInt:
                    spell31LVLInt = math.floor(spell31ProgressLabelInt/10 + 1)
                    spell31LVLLabel.config(text='{0}'.format(spell31LVLInt))
                spell31ProgressLabel.config(text='{0}'.format(spell31ProgressLabelInt))
        elif num == 5:
            if magicCircleAttInt == 3:
                spell32ProgressLabelInt += 1
                if 6 > math.floor(spell32ProgressLabelInt/10 + 1) > spell32LVLInt:
                    spell32LVLInt = math.floor(spell32ProgressLabelInt/10 + 1)
                    spell32LVLLabel.config(text='{0}'.format(spell32LVLInt))
                spell32ProgressLabel.config(text='{0}'.format(spell32ProgressLabelInt))
        elif num == 6:
            if magicCircleAttInt == 4:
                spell41ProgressLabelInt += 1
                if 6 > math.floor(spell41ProgressLabelInt/10 + 1) > spell41LVLInt:
                    spell41LVLInt = math.floor(spell41ProgressLabelInt/10 + 1)
                    spell41LVLLabel.config(text='{0}'.format(spell41LVLInt))
                spell41ProgressLabel.config(text='{0}'.format(spell41ProgressLabelInt))
        elif num == 7:
            if magicCircleAttInt == 4:
                spell42ProgressLabelInt += 1
                if 6 > math.floor(spell42ProgressLabelInt/10 + 1) > spell42LVLInt:
                    spell42LVLInt = math.floor(spell42ProgressLabelInt/10 + 1)
                    spell42LVLLabel.config(text='{0}'.format(spell42LVLInt))
                spell42ProgressLabel.config(text='{0}'.format(spell42ProgressLabelInt))
        elif num == 8:
            if magicCircleAttInt == 5:
                spell51ProgressLabelInt += 1
                if 6 > math.floor(spell51ProgressLabelInt/10 + 1) > spell51LVLInt:
                    spell51LVLInt = math.floor(spell51ProgressLabelInt/10 + 1)
                    spell51LVLLabel.config(text='{0}'.format(spell51LVLInt))
                spell51ProgressLabel.config(text='{0}'.format(spell51ProgressLabelInt))
        elif num == 9:
            if magicCircleAttInt == 5:
                spell52ProgressLabelInt += 1
                if 6 > math.floor(spell52ProgressLabelInt/10 + 1) > spell52LVLInt:
                    spell52LVLInt = math.floor(spell52ProgressLabelInt/10 + 1)
                    spell52LVLLabel.config(text='{0}'.format(spell52LVLInt))
                spell52ProgressLabel.config(text='{0}'.format(spell52ProgressLabelInt))
        elif num == 10:
            if magicCircleAttInt == 1:
                spell211ProgressLabelInt += 1
                if 6 > math.floor(spell211ProgressLabelInt/10 + 1) > spell211LVLInt:
                    spell211LVLInt = math.floor(spell211ProgressLabelInt/10 + 1)
                    spell211LVLLabel.config(text='{0}'.format(spell211LVLInt))
                spell211ProgressLabel.config(text='{0}'.format(spell211ProgressLabelInt))
        elif num == 11:
            if magicCircleAttInt == 1:
                spell212ProgressLabelInt += 1
                if 6 > math.floor(spell212ProgressLabelInt/10 + 1) > spell212LVLInt:
                    spell212LVLInt = math.floor(spell212ProgressLabelInt/10 + 1)
                    spell212LVLLabel.config(text='{0}'.format(spell212LVLInt))
                spell212ProgressLabel.config(text='{0}'.format(spell212ProgressLabelInt))
        elif num == 12:
            if magicCircleAttInt == 2:
                spell221ProgressLabelInt += 1
                if 6 > math.floor(spell221ProgressLabelInt/10 + 1) > spell221LVLInt:
                    spell221LVLInt = math.floor(spell221ProgressLabelInt/10 + 1)
                    spell221LVLLabel.config(text='{0}'.format(spell221LVLInt))
                spell221ProgressLabel.config(text='{0}'.format(spell221ProgressLabelInt))
        elif num == 13:
            if magicCircleAttInt == 2:
                spell222ProgressLabelInt += 1
                if 6 > math.floor(spell222ProgressLabelInt/10 + 1) > spell222LVLInt:
                    spell222LVLInt = math.floor(spell222ProgressLabelInt/10 + 1)
                    spell222LVLLabel.config(text='{0}'.format(spell222LVLInt))
                spell222ProgressLabel.config(text='{0}'.format(spell222ProgressLabelInt))
        elif num == 14:
            if magicCircleAttInt == 3:
                spell231ProgressLabelInt += 1
                if 6 > math.floor(spell231ProgressLabelInt/10 + 1) > spell231LVLInt:
                    spell231LVLInt = math.floor(spell231ProgressLabelInt/10 + 1)
                    spell231LVLLabel.config(text='{0}'.format(spell231LVLInt))
                spell231ProgressLabel.config(text='{0}'.format(spell231ProgressLabelInt))
        elif num == 15:
            if magicCircleAttInt == 3:
                spell232ProgressLabelInt += 1
                if 6 > math.floor(spell232ProgressLabelInt/10 + 1) > spell232LVLInt:
                    spell232LVLInt = math.floor(spell232ProgressLabelInt/10 + 1)
                    spell232LVLLabel.config(text='{0}'.format(spell232LVLInt))
                spell232ProgressLabel.config(text='{0}'.format(spell232ProgressLabelInt))
        elif num == 16:
            if magicCircleAttInt == 4:
                spell241ProgressLabelInt += 1
                if 6 > math.floor(spell241ProgressLabelInt/10 + 1) > spell241LVLInt:
                    spell241LVLInt = math.floor(spell241ProgressLabelInt/10 + 1)
                    spell241LVLLabel.config(text='{0}'.format(spell241LVLInt))
                spell241ProgressLabel.config(text='{0}'.format(spell241ProgressLabelInt))
        elif num == 17:
            if magicCircleAttInt == 4:
                spell242ProgressLabelInt += 1
                if 6 > math.floor(spell242ProgressLabelInt/10 + 1) > spell242LVLInt:
                    spell242LVLInt = math.floor(spell242ProgressLabelInt/10 + 1)
                    spell242LVLLabel.config(text='{0}'.format(spell242LVLInt))
                spell242ProgressLabel.config(text='{0}'.format(spell242ProgressLabelInt))
        elif num == 18:
            if magicCircleAttInt == 5:
                spell251ProgressLabelInt += 1
                if 6 > math.floor(spell251ProgressLabelInt/10 + 1) > spell251LVLInt:
                    spell251LVLInt = math.floor(spell251ProgressLabelInt/10 + 1)
                    spell251LVLLabel.config(text='{0}'.format(spell251LVLInt))
                spell251ProgressLabel.config(text='{0}'.format(spell251ProgressLabelInt))
        elif num == 19:
            if magicCircleAttInt == 5:
                spell252ProgressLabelInt += 1
                if 6 > math.floor(spell252ProgressLabelInt/10 + 1) > spell252LVLInt:
                    spell252LVLInt = math.floor(spell252ProgressLabelInt/10 + 1)
                    spell252LVLLabel.config(text='{0}'.format(spell252LVLInt))
                spell252ProgressLabel.config(text='{0}'.format(spell252ProgressLabelInt))

    ChoMag = Toplevel(window)
    ChoMag.title('Школы магии')
    ChoMag.resizable(width=False, height=False)
    ChoMag.rowconfigure(0, pad=3)
    ChoMag.rowconfigure(1, pad=3)
    ChoMag.rowconfigure(2, pad=3)
    ChoMag.rowconfigure(3, pad=3)
    ChoMag.rowconfigure(4, pad=3)
    ChoMag.columnconfigure(0, pad=3)
    ChoMag.columnconfigure(1, pad=3)
    ChoMag.columnconfigure(2, pad=3)
    ChoMag.columnconfigure(3, pad=3)

    frameFirstMagic=Frame(ChoMag, relief=RAISED, borderwidth=1)
    frameFirstMagic.rowconfigure(0, pad=3)
    frameFirstMagic.rowconfigure(1, pad=3)
    frameFirstMagic.rowconfigure(2, pad=3)
    frameFirstMagic.rowconfigure(3, pad=3)
    frameFirstMagic.rowconfigure(4, pad=3)
    frameFirstMagic.rowconfigure(5, pad=3)
    frameFirstMagic.rowconfigure(6, pad=3)
    frameFirstMagic.rowconfigure(7, pad=3)
    frameFirstMagic.rowconfigure(8, pad=3)
    frameFirstMagic.rowconfigure(9, pad=3)
    frameFirstMagic.rowconfigure(10, pad=3)
    frameFirstMagic.rowconfigure(11, pad=3)
    frameFirstMagic.columnconfigure(0, pad=3)
    frameFirstMagic.columnconfigure(1, pad=3)
    frameFirstMagic.columnconfigure(2, pad=3)
    frameFirstMagic.columnconfigure(3, pad=3)
    frameFirstMagic.columnconfigure(4, pad=3)
    frameFirstMagic.columnconfigure(5, pad=3)
    frameFirstMagic.grid(row=0, column=0)

    firstMagicSchool = ttk.Combobox(frameFirstMagic, values = allMagicSchool)
    firstMagicSchool.set(firstSchMag)
    firstMagicSchool.bind("<<ComboboxSelected>>", change_lines_in_magic_window)
    magicCircleLabel = Label(frameFirstMagic, text='Круг магии:')
    magicCircleAttLabel = Label(frameFirstMagic, text='{0}'.format(magicCircleAttInt))
    spellLabel = Label(frameFirstMagic, text='Заклинания')
    spellProgressLabel = Label(frameFirstMagic, text='Прогресс')
    spellLVLLebel = Label(frameFirstMagic, text='Уровень')

    firstMagicSchool.grid(row=0, column=0, columnspan=6)
    magicCircleLabel.grid(row=1, column=0)
    magicCircleAttLabel.grid(row=1, column=1)
    spellLabel.grid(row=1, column=2)
    spellProgressLabel.grid(row=1, column=3, columnspan=2)
    spellLVLLebel.grid(row=1, column=5)

    Label(frameFirstMagic, text=list(support['magic'][firstMagicSchool.get()].keys())[0]).grid(row=2, column=0, sticky=W, columnspan=2)
    Label(frameFirstMagic, text=list(support['magic'][firstMagicSchool.get()].keys())[0]).grid(row=3, column=0, sticky=W, columnspan=2)
    Label(frameFirstMagic, text=list(support['magic'][firstMagicSchool.get()].keys())[1]).grid(row=4, column=0, sticky=W, columnspan=2)
    Label(frameFirstMagic, text=list(support['magic'][firstMagicSchool.get()].keys())[1]).grid(row=5, column=0, sticky=W, columnspan=2)
    Label(frameFirstMagic, text=list(support['magic'][firstMagicSchool.get()].keys())[2]).grid(row=6, column=0, sticky=W, columnspan=2)
    Label(frameFirstMagic, text=list(support['magic'][firstMagicSchool.get()].keys())[2]).grid(row=7, column=0, sticky=W, columnspan=2)
    Label(frameFirstMagic, text=list(support['magic'][firstMagicSchool.get()].keys())[3]).grid(row=8, column=0, sticky=W, columnspan=2)
    Label(frameFirstMagic, text=list(support['magic'][firstMagicSchool.get()].keys())[3]).grid(row=9, column=0, sticky=W, columnspan=2)
    Label(frameFirstMagic, text=list(support['magic'][firstMagicSchool.get()].keys())[4]).grid(row=10, column=0, sticky=W, columnspan=2)
    Label(frameFirstMagic, text=list(support['magic'][firstMagicSchool.get()].keys())[4]).grid(row=11, column=0, sticky=W, columnspan=2)

    spell11 = Label(frameFirstMagic, text = list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[0]].keys())[0])
    CreateToolTip(spell11,'{0}\n{1}'.format(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[0]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[0]].keys())[0]]['tooltip'],support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[0]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[0]].keys())[0]]['level']))
    spell12 = Label(frameFirstMagic, text = list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[0]].keys())[1])
    CreateToolTip(spell12,'{0}\n{1}'.format(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[0]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[0]].keys())[1]]['tooltip'],support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[0]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[0]].keys())[1]]['level']))
    spell21 = Label(frameFirstMagic, text = list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[1]].keys())[0])
    CreateToolTip(spell21,'{0}\n{1}'.format(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[1]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[1]].keys())[0]]['tooltip'],support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[1]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[1]].keys())[0]]['level']))
    spell22 = Label(frameFirstMagic, text = list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[1]].keys())[1])
    CreateToolTip(spell22,'{0}\n{1}'.format(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[1]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[1]].keys())[1]]['tooltip'],support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[1]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[1]].keys())[1]]['level']))
    spell31 = Label(frameFirstMagic, text = list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[2]].keys())[0])
    CreateToolTip(spell31,'{0}\n{1}'.format(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[2]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[2]].keys())[0]]['tooltip'],support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[2]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[2]].keys())[0]]['level']))
    spell32 = Label(frameFirstMagic, text = list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[2]].keys())[1])
    CreateToolTip(spell32,'{0}\n{1}'.format(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[2]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[2]].keys())[1]]['tooltip'],support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[2]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[2]].keys())[1]]['level']))
    spell41 = Label(frameFirstMagic, text = list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[3]].keys())[0])
    CreateToolTip(spell41,'{0}\n{1}'.format(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[3]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[3]].keys())[0]]['tooltip'],support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[3]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[3]].keys())[0]]['level']))
    spell42 = Label(frameFirstMagic, text = list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[3]].keys())[1])
    CreateToolTip(spell42,'{0}\n{1}'.format(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[3]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[3]].keys())[1]]['tooltip'],support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[3]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[3]].keys())[1]]['level']))
    spell51 = Label(frameFirstMagic, text = list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[4]].keys())[0])
    CreateToolTip(spell51,'{0}\n{1}'.format(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[4]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[4]].keys())[0]]['tooltip'],support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[4]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[4]].keys())[0]]['level']))
    spell52 = Label(frameFirstMagic, text = list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[4]].keys())[1])
    CreateToolTip(spell52,'{0}\n{1}'.format(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[4]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[4]].keys())[1]]['tooltip'],support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[4]][list(support['magic'][firstMagicSchool.get()][list(support['magic'][firstMagicSchool.get()].keys())[4]].keys())[1]]['level']))

    spell11.grid(row=2, column=2)
    spell12.grid(row=3, column=2)
    spell21.grid(row=4, column=2)
    spell22.grid(row=5, column=2)
    spell31.grid(row=6, column=2)
    spell32.grid(row=7, column=2)
    spell41.grid(row=8, column=2)
    spell42.grid(row=9, column=2)
    spell51.grid(row=10, column=2)
    spell52.grid(row=11, column=2)

    spell11ProgressLabel = Label(frameFirstMagic, text = '{0}'.format(spell11ProgressLabelInt))
    spell12ProgressLabel = Label(frameFirstMagic, text = '{0}'.format(spell12ProgressLabelInt))
    spell21ProgressLabel = Label(frameFirstMagic, text = '{0}'.format(spell21ProgressLabelInt))
    spell22ProgressLabel = Label(frameFirstMagic, text = '{0}'.format(spell22ProgressLabelInt))
    spell31ProgressLabel = Label(frameFirstMagic, text = '{0}'.format(spell31ProgressLabelInt))
    spell32ProgressLabel = Label(frameFirstMagic, text = '{0}'.format(spell32ProgressLabelInt))
    spell41ProgressLabel = Label(frameFirstMagic, text = '{0}'.format(spell41ProgressLabelInt))
    spell42ProgressLabel = Label(frameFirstMagic, text = '{0}'.format(spell42ProgressLabelInt))
    spell51ProgressLabel = Label(frameFirstMagic, text = '{0}'.format(spell51ProgressLabelInt))
    spell52ProgressLabel = Label(frameFirstMagic, text = '{0}'.format(spell52ProgressLabelInt))

    spell11ProgressLabel.grid(row=2, column=3)
    spell12ProgressLabel.grid(row=3, column=3)
    spell21ProgressLabel.grid(row=4, column=3)
    spell22ProgressLabel.grid(row=5, column=3)
    spell31ProgressLabel.grid(row=6, column=3)
    spell32ProgressLabel.grid(row=7, column=3)
    spell41ProgressLabel.grid(row=8, column=3)
    spell42ProgressLabel.grid(row=9, column=3)
    spell51ProgressLabel.grid(row=10, column=3)
    spell52ProgressLabel.grid(row=11, column=3)

    spell11ProgressButt = Button(frameFirstMagic, command=lambda: add_spell_exp(0), text='+')
    spell12ProgressButt = Button(frameFirstMagic, command=lambda: add_spell_exp(1), text='+')
    spell21ProgressButt = Button(frameFirstMagic, command=lambda: add_spell_exp(2), text='+')
    spell22ProgressButt = Button(frameFirstMagic, command=lambda: add_spell_exp(3), text='+')
    spell31ProgressButt = Button(frameFirstMagic, command=lambda: add_spell_exp(4), text='+')
    spell32ProgressButt = Button(frameFirstMagic, command=lambda: add_spell_exp(5), text='+')
    spell41ProgressButt = Button(frameFirstMagic, command=lambda: add_spell_exp(6), text='+')
    spell42ProgressButt = Button(frameFirstMagic, command=lambda: add_spell_exp(7), text='+')
    spell51ProgressButt = Button(frameFirstMagic, command=lambda: add_spell_exp(8), text='+')
    spell52ProgressButt = Button(frameFirstMagic, command=lambda: add_spell_exp(9), text='+')

    spell11ProgressButt.grid(row=2, column=4)
    spell12ProgressButt.grid(row=3, column=4)
    spell21ProgressButt.grid(row=4, column=4)
    spell22ProgressButt.grid(row=5, column=4)
    spell31ProgressButt.grid(row=6, column=4)
    spell32ProgressButt.grid(row=7, column=4)
    spell41ProgressButt.grid(row=8, column=4)
    spell42ProgressButt.grid(row=9, column=4)
    spell51ProgressButt.grid(row=10, column=4)
    spell52ProgressButt.grid(row=11, column=4)

    spell11LVLLabel = Label(frameFirstMagic, text = '{0}'.format(spell11LVLInt))
    spell12LVLLabel = Label(frameFirstMagic, text = '{0}'.format(spell12LVLInt))
    spell21LVLLabel = Label(frameFirstMagic, text = '{0}'.format(spell21LVLInt))
    spell22LVLLabel = Label(frameFirstMagic, text = '{0}'.format(spell22LVLInt))
    spell31LVLLabel = Label(frameFirstMagic, text = '{0}'.format(spell31LVLInt))
    spell32LVLLabel = Label(frameFirstMagic, text = '{0}'.format(spell32LVLInt))
    spell41LVLLabel = Label(frameFirstMagic, text = '{0}'.format(spell41LVLInt))
    spell42LVLLabel = Label(frameFirstMagic, text = '{0}'.format(spell42LVLInt))
    spell51LVLLabel = Label(frameFirstMagic, text = '{0}'.format(spell51LVLInt))
    spell52LVLLabel = Label(frameFirstMagic, text = '{0}'.format(spell52LVLInt))

    spell11LVLLabel.grid(row=2, column=5)
    spell12LVLLabel.grid(row=3, column=5)
    spell21LVLLabel.grid(row=4, column=5)
    spell22LVLLabel.grid(row=5, column=5)
    spell31LVLLabel.grid(row=6, column=5)
    spell32LVLLabel.grid(row=7, column=5)
    spell41LVLLabel.grid(row=8, column=5)
    spell42LVLLabel.grid(row=9, column=5)
    spell51LVLLabel.grid(row=10, column=5)
    spell52LVLLabel.grid(row=11, column=5)

    frameSecondMagic=Frame(ChoMag, relief=RAISED, borderwidth=1)
    frameSecondMagic.rowconfigure(0, pad=3)
    frameSecondMagic.rowconfigure(1, pad=3)
    frameSecondMagic.rowconfigure(2, pad=3)
    frameSecondMagic.rowconfigure(3, pad=3)
    frameSecondMagic.rowconfigure(4, pad=3)
    frameSecondMagic.rowconfigure(5, pad=3)
    frameSecondMagic.rowconfigure(6, pad=3)
    frameSecondMagic.rowconfigure(7, pad=3)
    frameSecondMagic.rowconfigure(8, pad=3)
    frameSecondMagic.rowconfigure(9, pad=3)
    frameSecondMagic.rowconfigure(10, pad=3)
    frameSecondMagic.rowconfigure(11, pad=3)
    frameSecondMagic.columnconfigure(0, pad=3)
    frameSecondMagic.columnconfigure(1, pad=3)
    frameSecondMagic.columnconfigure(2, pad=3)
    frameSecondMagic.columnconfigure(3, pad=3)
    frameSecondMagic.columnconfigure(4, pad=3)
    frameSecondMagic.columnconfigure(5, pad=3)
    frameSecondMagic.grid(row=0, column=1)

    secondMagicSchool = ttk.Combobox(frameSecondMagic, values = allMagicSchool)
    secondMagicSchool.set(secondSchMag)
    secondMagicSchool.bind("<<ComboboxSelected>>", change_lines_in_magic_window2)
    magicCircleLabel = Label(frameSecondMagic, text='Круг магии:')
    magicCircleAttLabel2 = Label(frameSecondMagic, text='{0}'.format(magicCircleAttInt))
    spellLabel = Label(frameSecondMagic, text='Заклинания')
    spellProgressLabel = Label(frameSecondMagic, text='Прогресс')
    spellLVLLebel = Label(frameSecondMagic, text='Уровень')

    secondMagicSchool.grid(row=0, column=0, columnspan=6)
    magicCircleLabel.grid(row=1, column=0)
    magicCircleAttLabel2.grid(row=1, column=1)
    spellLabel.grid(row=1, column=2)
    spellProgressLabel.grid(row=1, column=3, columnspan=2)
    spellLVLLebel.grid(row=1, column=5)

    Label(frameSecondMagic, text=list(support['magic'][secondMagicSchool.get()].keys())[0]).grid(row=2, column=0, sticky=W, columnspan=2)
    Label(frameSecondMagic, text=list(support['magic'][secondMagicSchool.get()].keys())[0]).grid(row=3, column=0, sticky=W, columnspan=2)
    Label(frameSecondMagic, text=list(support['magic'][secondMagicSchool.get()].keys())[1]).grid(row=4, column=0, sticky=W, columnspan=2)
    Label(frameSecondMagic, text=list(support['magic'][secondMagicSchool.get()].keys())[1]).grid(row=5, column=0, sticky=W, columnspan=2)
    Label(frameSecondMagic, text=list(support['magic'][secondMagicSchool.get()].keys())[2]).grid(row=6, column=0, sticky=W, columnspan=2)
    Label(frameSecondMagic, text=list(support['magic'][secondMagicSchool.get()].keys())[2]).grid(row=7, column=0, sticky=W, columnspan=2)
    Label(frameSecondMagic, text=list(support['magic'][secondMagicSchool.get()].keys())[3]).grid(row=8, column=0, sticky=W, columnspan=2)
    Label(frameSecondMagic, text=list(support['magic'][secondMagicSchool.get()].keys())[3]).grid(row=9, column=0, sticky=W, columnspan=2)
    Label(frameSecondMagic, text=list(support['magic'][secondMagicSchool.get()].keys())[4]).grid(row=10, column=0, sticky=W, columnspan=2)
    Label(frameSecondMagic, text=list(support['magic'][secondMagicSchool.get()].keys())[4]).grid(row=11, column=0, sticky=W, columnspan=2)

    spell211 = Label(frameSecondMagic, text = list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[0]].keys())[0])
    CreateToolTip(spell211,'{0}\n{1}'.format(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[0]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[0]].keys())[0]]['tooltip'],support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[0]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[0]].keys())[0]]['level']))
    spell212 = Label(frameSecondMagic, text = list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[0]].keys())[1])
    CreateToolTip(spell212,'{0}\n{1}'.format(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[0]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[0]].keys())[1]]['tooltip'],support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[0]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[0]].keys())[1]]['level']))
    spell221 = Label(frameSecondMagic, text = list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[1]].keys())[0])
    CreateToolTip(spell221,'{0}\n{1}'.format(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[1]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[1]].keys())[0]]['tooltip'],support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[1]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[1]].keys())[0]]['level']))
    spell222 = Label(frameSecondMagic, text = list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[1]].keys())[1])
    CreateToolTip(spell222,'{0}\n{1}'.format(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[1]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[1]].keys())[1]]['tooltip'],support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[1]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[1]].keys())[1]]['level']))
    spell231 = Label(frameSecondMagic, text = list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[2]].keys())[0])
    CreateToolTip(spell231,'{0}\n{1}'.format(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[2]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[2]].keys())[0]]['tooltip'],support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[2]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[2]].keys())[0]]['level']))
    spell232 = Label(frameSecondMagic, text = list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[2]].keys())[1])
    CreateToolTip(spell232,'{0}\n{1}'.format(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[2]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[2]].keys())[1]]['tooltip'],support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[2]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[2]].keys())[1]]['level']))
    spell241 = Label(frameSecondMagic, text = list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[3]].keys())[0])
    CreateToolTip(spell241,'{0}\n{1}'.format(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[3]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[3]].keys())[0]]['tooltip'],support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[3]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[3]].keys())[0]]['level']))
    spell242 = Label(frameSecondMagic, text = list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[3]].keys())[1])
    CreateToolTip(spell242,'{0}\n{1}'.format(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[3]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[3]].keys())[1]]['tooltip'],support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[3]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[3]].keys())[1]]['level']))
    spell251 = Label(frameSecondMagic, text = list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[4]].keys())[0])
    CreateToolTip(spell251,'{0}\n{1}'.format(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[4]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[4]].keys())[0]]['tooltip'],support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[4]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[4]].keys())[0]]['level']))
    spell252 = Label(frameSecondMagic, text = list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[4]].keys())[1])
    CreateToolTip(spell252,'{0}\n{1}'.format(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[4]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[4]].keys())[1]]['tooltip'],support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[4]][list(support['magic'][secondMagicSchool.get()][list(support['magic'][secondMagicSchool.get()].keys())[4]].keys())[1]]['level']))

    spell211.grid(row=2, column=2)
    spell212.grid(row=3, column=2)
    spell221.grid(row=4, column=2)
    spell222.grid(row=5, column=2)
    spell231.grid(row=6, column=2)
    spell232.grid(row=7, column=2)
    spell241.grid(row=8, column=2)
    spell242.grid(row=9, column=2)
    spell251.grid(row=10, column=2)
    spell252.grid(row=11, column=2)

    spell211ProgressLabel = Label(frameSecondMagic, text = '{0}'.format(spell211ProgressLabelInt))
    spell212ProgressLabel = Label(frameSecondMagic, text = '{0}'.format(spell212ProgressLabelInt))
    spell221ProgressLabel = Label(frameSecondMagic, text = '{0}'.format(spell221ProgressLabelInt))
    spell222ProgressLabel = Label(frameSecondMagic, text = '{0}'.format(spell222ProgressLabelInt))
    spell231ProgressLabel = Label(frameSecondMagic, text = '{0}'.format(spell231ProgressLabelInt))
    spell232ProgressLabel = Label(frameSecondMagic, text = '{0}'.format(spell232ProgressLabelInt))
    spell241ProgressLabel = Label(frameSecondMagic, text = '{0}'.format(spell241ProgressLabelInt))
    spell242ProgressLabel = Label(frameSecondMagic, text = '{0}'.format(spell242ProgressLabelInt))
    spell251ProgressLabel = Label(frameSecondMagic, text = '{0}'.format(spell251ProgressLabelInt))
    spell252ProgressLabel = Label(frameSecondMagic, text = '{0}'.format(spell252ProgressLabelInt))

    spell211ProgressLabel.grid(row=2, column=3)
    spell212ProgressLabel.grid(row=3, column=3)
    spell221ProgressLabel.grid(row=4, column=3)
    spell222ProgressLabel.grid(row=5, column=3)
    spell231ProgressLabel.grid(row=6, column=3)
    spell232ProgressLabel.grid(row=7, column=3)
    spell241ProgressLabel.grid(row=8, column=3)
    spell242ProgressLabel.grid(row=9, column=3)
    spell251ProgressLabel.grid(row=10, column=3)
    spell252ProgressLabel.grid(row=11, column=3)

    spell211ProgressButt = Button(frameSecondMagic, command=lambda: add_spell_exp(10), text='+')
    spell212ProgressButt = Button(frameSecondMagic, command=lambda: add_spell_exp(11), text='+')
    spell221ProgressButt = Button(frameSecondMagic, command=lambda: add_spell_exp(12), text='+')
    spell222ProgressButt = Button(frameSecondMagic, command=lambda: add_spell_exp(13), text='+')
    spell231ProgressButt = Button(frameSecondMagic, command=lambda: add_spell_exp(14), text='+')
    spell232ProgressButt = Button(frameSecondMagic, command=lambda: add_spell_exp(15), text='+')
    spell241ProgressButt = Button(frameSecondMagic, command=lambda: add_spell_exp(16), text='+')
    spell242ProgressButt = Button(frameSecondMagic, command=lambda: add_spell_exp(17), text='+')
    spell251ProgressButt = Button(frameSecondMagic, command=lambda: add_spell_exp(18), text='+')
    spell252ProgressButt = Button(frameSecondMagic, command=lambda: add_spell_exp(19), text='+')

    spell211ProgressButt.grid(row=2, column=4)
    spell212ProgressButt.grid(row=3, column=4)
    spell221ProgressButt.grid(row=4, column=4)
    spell222ProgressButt.grid(row=5, column=4)
    spell231ProgressButt.grid(row=6, column=4)
    spell232ProgressButt.grid(row=7, column=4)
    spell241ProgressButt.grid(row=8, column=4)
    spell242ProgressButt.grid(row=9, column=4)
    spell251ProgressButt.grid(row=10, column=4)
    spell252ProgressButt.grid(row=11, column=4)

    spell211LVLLabel = Label(frameSecondMagic, text = '{0}'.format(spell211LVLInt))
    spell212LVLLabel = Label(frameSecondMagic, text = '{0}'.format(spell212LVLInt))
    spell221LVLLabel = Label(frameSecondMagic, text = '{0}'.format(spell221LVLInt))
    spell222LVLLabel = Label(frameSecondMagic, text = '{0}'.format(spell222LVLInt))
    spell231LVLLabel = Label(frameSecondMagic, text = '{0}'.format(spell231LVLInt))
    spell232LVLLabel = Label(frameSecondMagic, text = '{0}'.format(spell232LVLInt))
    spell241LVLLabel = Label(frameSecondMagic, text = '{0}'.format(spell241LVLInt))
    spell242LVLLabel = Label(frameSecondMagic, text = '{0}'.format(spell242LVLInt))
    spell251LVLLabel = Label(frameSecondMagic, text = '{0}'.format(spell251LVLInt))
    spell252LVLLabel = Label(frameSecondMagic, text = '{0}'.format(spell252LVLInt))

    spell211LVLLabel.grid(row=2, column=5)
    spell212LVLLabel.grid(row=3, column=5)
    spell221LVLLabel.grid(row=4, column=5)
    spell222LVLLabel.grid(row=5, column=5)
    spell231LVLLabel.grid(row=6, column=5)
    spell232LVLLabel.grid(row=7, column=5)
    spell241LVLLabel.grid(row=8, column=5)
    spell242LVLLabel.grid(row=9, column=5)
    spell251LVLLabel.grid(row=10, column=5)
    spell252LVLLabel.grid(row=11, column=5)

def create_race_window():
    ChoRace = Toplevel(window)
    ChoRace.title('Раса персонажа')
    ChoRace.resizable(width=False, height=False)
    ChoRace.columnconfigure(0, pad=3)
    i = 0
    buttons = [create_radio(ChoRace,c) for c in OPTIONS]
    for button in buttons:
        ChoRace.rowconfigure(i, pad=3)
        button.grid(row = i, column = 0, sticky=W)
        i += 1

def create_radio(ChoRace,option):
    text = value = option
    return Radiobutton(ChoRace, text=text, value=value,
                      command=change_race,
                      variable=raceVar)

def change_race():
    global allStr,allAgi,allInt,allBody,lvlNow,allAtt,expNow,learningAttInt,shootAttInt,language,lastRace
    raceLabel2.config(text = raceVar.get())
    if raceVar.get() == 'Человек' and lastRace != 'Человек':
        learningAttInt += 1
    elif lastRace == 'Человек':
        learningAttInt -= 1
    if raceVar.get() == 'Лесной Эльф' and lastRace != 'Лесной Эльф':
        shootAttInt += 1
    elif lastRace == 'Лесной Эльф':
        shootAttInt -= 1
    allStr = int(support['race'][raceVar.get()]['att']['str'])
    allAgi = int(support['race'][raceVar.get()]['att']['agi'])
    allInt = int(support['race'][raceVar.get()]['att']['int'])
    allBody = int(support['race'][raceVar.get()]['att']['body'])
    lvlNow = int(support['race'][raceVar.get()]['startLVL'])
    expNow = lvl_exp(lvlNow)
    allAtt = allStr+allAgi+allInt+allBody
    availableAttNumb.config(text='{0}'.format(allAtt))
    levelLabel2.config(text='{0}'.format(lvlNow))
    expNowAttLabel.config(text='{0}'.format(expNow))
    language = ''
    for lang in support['race'][raceVar.get()]['language']:
        if language:
            language = '{0},{1}'.format(language,lang)
        else:
            language = lang
    lastRace = raceVar.get()
    CreateToolTip(raceLabel2,support['race'][raceVar.get()]['tooltip'])

def add_att(num,widget):
    global allAtt, meleFightAttInt,shootAttInt,strongHitsAttInt,warBusinessAttInt,tacticsAttInt,attackAttInt,evasionAttInt,hasteAttInt,coldBloodAttInt,firstAidAttInt,manaAttInt,thiefArtAttInt,magicCircleAttInt,magicPowerAttInt,learningAttInt,healthAttInt,energyAttInt,resistAttInt,secondBreathAttInt,steelBodyAttInt,magicCircleAttLabel,magicCircleAttLabel2
    if allAtt > 0:
        if num == 0:
            meleFightAttInt += 1
            widget.config(text='{0}'.format(meleFightAttInt))
        elif num == 1:
            shootAttInt += 1
            widget.config(text='{0}'.format(shootAttInt))
        elif num == 2:
            strongHitsAttInt += 1
            widget.config(text='{0}'.format(strongHitsAttInt))
        elif num == 3:
            warBusinessAttInt += 1
            widget.config(text='{0}'.format(warBusinessAttInt))
        elif num == 4:
            tacticsAttInt += 1
            widget.config(text='{0}'.format(tacticsAttInt))
        elif num == 5:
            attackAttInt += 1
            widget.config(text='{0}'.format(attackAttInt))
        elif num == 6:
            evasionAttInt += 1
            widget.config(text='{0}'.format(evasionAttInt))
        elif num == 7:
            hasteAttInt += 1
            widget.config(text='{0}'.format(hasteAttInt))
        elif num == 8:
            coldBloodAttInt += 1
            widget.config(text='{0}'.format(coldBloodAttInt))
        elif num == 9:
            thiefArtAttInt += 1
            widget.config(text='{0}'.format(thiefArtAttInt))
        elif num == 10:
            manaAttInt += 1
            widget.config(text='{0}'.format(manaAttInt))
        elif num == 11:
            firstAidAttInt += 1
            widget.config(text='{0}'.format(firstAidAttInt))
        elif num == 12:
            magicCircleAttInt += 1
            if magicCircleAttInt == 1:
                spell11LVLInt = 1
                spell12LVLInt = 1
            elif magicCircleAttInt == 2:
                spell21LVLInt = 1
                spell22LVLInt = 1
            elif magicCircleAttInt == 3:
                spell31LVLInt = 1
                spell32LVLInt = 1
            elif magicCircleAttInt == 4:
                spell41LVLInt = 1
                spell42LVLInt = 1
            elif magicCircleAttInt == 5:
                spell51LVLInt = 1
                spell52LVLInt = 1
            widget.config(text='{0}'.format(magicCircleAttInt))
            try:
                if magicCircleAttLabel:
                    magicCircleAttLabel.config(text='{0}'.format(magicCircleAttInt))
                    magicCircleAttLabel2.config(text='{0}'.format(magicCircleAttInt))
            except:
                print("magic window don't open")
        elif num == 13:
            magicPowerAttInt += 1
            widget.config(text='{0}'.format(magicPowerAttInt))
        elif num == 14:
            learningAttInt += 1
            widget.config(text='{0}'.format(learningAttInt))
        elif num == 15:
            healthAttInt += 1
            widget.config(text='{0}'.format(healthAttInt))
        elif num == 16:
            energyAttInt += 1
            widget.config(text='{0}'.format(energyAttInt))
        elif num == 17:
            resistAttInt += 1
            widget.config(text='{0}'.format(resistAttInt))
        elif num == 18:
            secondBreathAttInt += 1
            widget.config(text='{0}'.format(secondBreathAttInt))
        elif num == 19:
            steelBodyAttInt += 1
            widget.config(text='{0}'.format(steelBodyAttInt))

        allAtt -= 1
        availableAttNumb.config(text='{0}'.format(allAtt))

# all vars
lvlNow = 1
expNow = 0
allAtt = 12
OPTIONS = list(support['race'].keys())
allMagicSchool = list(support['magic'].keys())
list_lvl = list_lvlExp()
language = 'Общий'
firstSchMag = allMagicSchool[0]
secondSchMag = allMagicSchool[0]

# Variables str
allStr = 0
meleFightAttInt = 0
shootAttInt = 0
strongHitsAttInt = 0
warBusinessAttInt = 0
tacticsAttInt = 0
# Variables agi
allAgi = 0
attackAttInt = 0
evasionAttInt = 0
hasteAttInt = 0
coldBloodAttInt = 0
thiefArtAttInt = 0
# Variables int
allInt = 0
manaAttInt = 0
firstAidAttInt = 0
magicCircleAttInt = 0
magicPowerAttInt = 0
learningAttInt = 1
# Variables body
allBody = 0
healthAttInt = 0
energyAttInt = 0
resistAttInt = 0
secondBreathAttInt = 0
steelBodyAttInt = 0

spell11ProgressLabelInt = 0
spell12ProgressLabelInt = 0
spell21ProgressLabelInt = 0
spell22ProgressLabelInt = 0
spell31ProgressLabelInt = 0
spell32ProgressLabelInt = 0
spell41ProgressLabelInt = 0
spell42ProgressLabelInt = 0
spell51ProgressLabelInt = 0
spell52ProgressLabelInt = 0

spell211ProgressLabelInt = 0
spell212ProgressLabelInt = 0
spell221ProgressLabelInt = 0
spell222ProgressLabelInt = 0
spell231ProgressLabelInt = 0
spell232ProgressLabelInt = 0
spell241ProgressLabelInt = 0
spell242ProgressLabelInt = 0
spell251ProgressLabelInt = 0
spell252ProgressLabelInt = 0

spell11LVLInt = 0
spell12LVLInt = 0
spell21LVLInt = 0
spell22LVLInt = 0
spell31LVLInt = 0
spell32LVLInt = 0
spell41LVLInt = 0
spell42LVLInt = 0
spell51LVLInt = 0
spell52LVLInt = 0

spell211LVLInt = 0
spell212LVLInt = 0
spell221LVLInt = 0
spell222LVLInt = 0
spell231LVLInt = 0
spell232LVLInt = 0
spell241LVLInt = 0
spell242LVLInt = 0
spell251LVLInt = 0
spell252LVLInt = 0

window = Tk() #sozdanie okna
window.title('Лист персонажа.') #Присвоение окну тайтла
window.resizable(width=False, height=False) #Запрет на изменение размеров окна
window.rowconfigure(0, pad=3)
window.rowconfigure(1, pad=3)
window.columnconfigure(0, pad=3)
window.columnconfigure(1, pad=3)

raceVar = StringVar()
raceVar.set(OPTIONS[0]) # default value
lastRace = raceVar.get()

#race,name,lvl
frame2=Frame(window, relief=RAISED, borderwidth=1)
frame2.rowconfigure(0, pad=3)
frame2.rowconfigure(1, pad=3)
frame2.rowconfigure(2, pad=3)
frame2.rowconfigure(3, pad=3)
frame2.rowconfigure(4, pad=3)
frame2.rowconfigure(5, pad=3)
frame2.rowconfigure(6, pad=3)
frame2.columnconfigure(0, pad=3)
frame2.columnconfigure(1, pad=3)
frame2.columnconfigure(2, pad=3)
frame2.grid(row=0, column=0)
# frame2.grid_propagate(0) #Запрет изменения размеров фрейма


persLable = Label(frame2, text='Персонаж:')
loginLabel = Label(frame2, text='Имя*:')
login = Entry(frame2)
levelLabel = Label(frame2, text='Уровень:')
levelLabel2 = Label(frame2, text='{0}'.format(lvlNow))
raceLabel = Label(frame2, text='Раса:')
raceLabel2 = Label(frame2, text='{0}'.format(raceVar.get()))
# raceOpt = ttk.Combobox(frame2, values = OPTIONS)
raceADD = Button(frame2, command=create_race_window, text='Выбрать расу')
lanLabel = Label(frame2, text='Языки:')
lanAttLabel = Label(frame2, text='Языки:')

CreateToolTip(raceLabel2,support['race'][OPTIONS[0]]['tooltip'])

persLable.grid(row=0, column=0, columnspan=3)
loginLabel.grid(row=1, column=0)
login.grid(row=1, column=1, columnspan=2)
levelLabel.grid(row=2, column=0)
levelLabel2.grid(row=2, column=1, columnspan=2)
raceLabel.grid(row=3, column=0)
raceLabel2.grid(row=3, column=1)
raceADD.grid(row=3,column=2)
# raceOpt.grid(row=3,column=2)

# raceOpt.bind("<<ComboboxSelected>>", change_race)

# frame3 attributes
frame3=Frame(window, relief=RAISED, borderwidth=1)
frame3.rowconfigure(0, pad=3)
frame3.rowconfigure(1, pad=3)
frame3.rowconfigure(2, pad=3)
frame3.rowconfigure(3, pad=3)
frame3.rowconfigure(4, pad=3)
frame3.rowconfigure(5, pad=3)
frame3.rowconfigure(6, pad=3)
frame3.columnconfigure(0, pad=3)
frame3.columnconfigure(1, pad=3)
frame3.columnconfigure(2, pad=3)
frame3.grid(row=0, column=1)

availableAtt = Label(frame3, text='Доступные очки характеристик:')
availableAttNumb = Label(frame3, text='{0}'.format(allAtt))
changeAtt = Button(frame3, command=create_attribute_window, text='Окно характеристик')
expNowLabel = Label(frame3, text='Текущее количество опыта:')
expNowAttLabel = Label(frame3, text='{0}'.format(expNow))
addExpLabel = Label(frame3, text='Добавить опыт:')
addExp = Entry(frame3)
addExpButt = Button(frame3, command=new_exp, text='Прокачаться!')


availableAtt.grid(row=0, column=0, columnspan=2)
availableAttNumb.grid(row=0, column=2)
changeAtt.grid(row=1, column=0, columnspan=3)
expNowLabel.grid(row=2, column=0, columnspan=2)
expNowAttLabel.grid(row=2, column=2)
addExpLabel.grid(row=3, column=0)
addExp.grid(row=3, column=1, columnspan=2)
addExpButt.grid(row=4, column=0, columnspan=3)

frame4=Frame(window, relief=RAISED, borderwidth=1)
frame4.rowconfigure(0, pad=3)
frame4.rowconfigure(1, pad=3)
frame4.rowconfigure(2, pad=3)
frame4.rowconfigure(3, pad=3)
frame4.rowconfigure(4, pad=3)
frame4.rowconfigure(5, pad=3)
frame4.rowconfigure(6, pad=3)
frame4.columnconfigure(0, pad=3)
frame4.columnconfigure(1, pad=3)
frame4.grid(row=1, column=0)

magicButt = Button(frame2, command=create_magic_window, text='Магия')
activeAbilButt = Button(frame2, command=create_attribute_window, text='Активные умения')

# magicButt.grid(row=0, column=0)
# activeAbilButt.grid(row=0, column=1)

magicButt.grid(row=4, column=0)
activeAbilButt.grid(row=4, column=1, columnspan=2)

window.mainloop()
