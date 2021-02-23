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
    global expNow,lvlNow,allAtt,repLvl,repExp
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
    if addRep.get():
        repExp = repExp + int(addRep.get())
        repExpNowAttLabel.config(text='{0}'.format(repExp))
        if math.floor(repExp/10) > repLvl:
            repLvl = math.floor(repExp/10)
            repLabel2.config(text='{0}'.format(repLvl))
        addRep.delete(0, 'end')

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
    global spell11ProgressLabelInt,spell12ProgressLabelInt,spell21ProgressLabelInt,spell22ProgressLabelInt,spell31ProgressLabelInt,spell32ProgressLabelInt,spell41ProgressLabelInt,spell42ProgressLabelInt,spell51ProgressLabelInt,spell52ProgressLabelInt,spell11LVLInt,spell12LVLInt,spell21LVLInt,spell22LVLInt,spell31LVLInt,spell32LVLInt,spell41LVLInt,spell42LVLInt,spell51LVLInt,spell52LVLInt,magicCircleAttLabel,spell211ProgressLabelInt,spell212ProgressLabelInt,spell221ProgressLabelInt,spell222ProgressLabelInt,spell231ProgressLabelInt,spell232ProgressLabelInt,spell241ProgressLabelInt,spell242ProgressLabelInt,spell251ProgressLabelInt,spell252ProgressLabelInt,spell211LVLInt,spell212LVLInt,spell221LVLInt,spell222LVLInt,spell231LVLInt,spell232LVLInt,spell241LVLInt,spell242LVLInt,spell251LVLInt,spell252LVLInt,magicCircleAttLabel2,firstSchMag,secondSchMag,spell211LVLLabel,spell212LVLLabel,spell221LVLLabel,spell222LVLLabel,spell231LVLLabel,spell232LVLLabel,spell241LVLLabel,spell242LVLLabel,spell251LVLLabel,spell252LVLLabel,spell11LVLLabel,spell12LVLLabel,spell21LVLLabel,spell22LVLLabel,spell31LVLLabel,spell32LVLLabel,spell41LVLLabel,spell42LVLLabel,spell51LVLLabel,spell52LVLLabel

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
            if magicCircleAttInt > 0:
                spell11ProgressLabelInt += 1
                if 6 > math.floor(spell11ProgressLabelInt/10 + 1) > spell11LVLInt:
                    spell11LVLInt = math.floor(spell11ProgressLabelInt/10 + 1)
                    spell11LVLLabel.config(text='{0}'.format(spell11LVLInt))
                spell11ProgressLabel.config(text='{0}'.format(spell11ProgressLabelInt))
        elif num == 1:
            if magicCircleAttInt > 0:
                spell12ProgressLabelInt += 1
                if 6 > math.floor(spell12ProgressLabelInt/10 + 1) > spell12LVLInt:
                    spell12LVLInt = math.floor(spell12ProgressLabelInt/10 + 1)
                    spell12LVLLabel.config(text='{0}'.format(spell12LVLInt))
                spell12ProgressLabel.config(text='{0}'.format(spell12ProgressLabelInt))
        elif num == 2:
            if magicCircleAttInt > 1:
                spell21ProgressLabelInt += 1
                if 6 > math.floor(spell21ProgressLabelInt/10 + 1) > spell21LVLInt:
                    spell21LVLInt = math.floor(spell21ProgressLabelInt/10 + 1)
                    spell21LVLLabel.config(text='{0}'.format(spell21LVLInt))
                spell21ProgressLabel.config(text='{0}'.format(spell21ProgressLabelInt))
        elif num == 3:
            if magicCircleAttInt > 1:
                spell22ProgressLabelInt += 1
                if 6 > math.floor(spell22ProgressLabelInt/10 + 1) > spell22LVLInt:
                    spell22LVLInt = math.floor(spell22ProgressLabelInt/10 + 1)
                    spell22LVLLabel.config(text='{0}'.format(spell22LVLInt))
                spell22ProgressLabel.config(text='{0}'.format(spell22ProgressLabelInt))
        elif num == 4:
            if magicCircleAttInt > 2:
                spell31ProgressLabelInt += 1
                if 6 > math.floor(spell31ProgressLabelInt/10 + 1) > spell31LVLInt:
                    spell31LVLInt = math.floor(spell31ProgressLabelInt/10 + 1)
                    spell31LVLLabel.config(text='{0}'.format(spell31LVLInt))
                spell31ProgressLabel.config(text='{0}'.format(spell31ProgressLabelInt))
        elif num == 5:
            if magicCircleAttInt > 2:
                spell32ProgressLabelInt += 1
                if 6 > math.floor(spell32ProgressLabelInt/10 + 1) > spell32LVLInt:
                    spell32LVLInt = math.floor(spell32ProgressLabelInt/10 + 1)
                    spell32LVLLabel.config(text='{0}'.format(spell32LVLInt))
                spell32ProgressLabel.config(text='{0}'.format(spell32ProgressLabelInt))
        elif num == 6:
            if magicCircleAttInt > 3:
                spell41ProgressLabelInt += 1
                if 5 > math.floor(spell41ProgressLabelInt/10 + 1) > spell41LVLInt:
                    spell41LVLInt = math.floor(spell41ProgressLabelInt/10 + 1)
                    spell41LVLLabel.config(text='{0}'.format(spell41LVLInt))
                spell41ProgressLabel.config(text='{0}'.format(spell41ProgressLabelInt))
        elif num == 7:
            if magicCircleAttInt > 3:
                spell42ProgressLabelInt += 1
                if 5 > math.floor(spell42ProgressLabelInt/10 + 1) > spell42LVLInt:
                    spell42LVLInt = math.floor(spell42ProgressLabelInt/10 + 1)
                    spell42LVLLabel.config(text='{0}'.format(spell42LVLInt))
                spell42ProgressLabel.config(text='{0}'.format(spell42ProgressLabelInt))
        elif num == 8:
            if magicCircleAttInt > 4:
                spell51ProgressLabelInt += 1
                if 4 > math.floor(spell51ProgressLabelInt/10 + 1) > spell51LVLInt:
                    spell51LVLInt = math.floor(spell51ProgressLabelInt/10 + 1)
                    spell51LVLLabel.config(text='{0}'.format(spell51LVLInt))
                spell51ProgressLabel.config(text='{0}'.format(spell51ProgressLabelInt))
        elif num == 9:
            if magicCircleAttInt > 4:
                spell52ProgressLabelInt += 1
                if 4 > math.floor(spell52ProgressLabelInt/10 + 1) > spell52LVLInt:
                    spell52LVLInt = math.floor(spell52ProgressLabelInt/10 + 1)
                    spell52LVLLabel.config(text='{0}'.format(spell52LVLInt))
                spell52ProgressLabel.config(text='{0}'.format(spell52ProgressLabelInt))
        elif num == 10:
            if magicCircleAttInt > 0:
                spell211ProgressLabelInt += 1
                if 6 > math.floor(spell211ProgressLabelInt/10 + 1) > spell211LVLInt:
                    spell211LVLInt = math.floor(spell211ProgressLabelInt/10 + 1)
                    spell211LVLLabel.config(text='{0}'.format(spell211LVLInt))
                spell211ProgressLabel.config(text='{0}'.format(spell211ProgressLabelInt))
        elif num == 11:
            if magicCircleAttInt > 0:
                spell212ProgressLabelInt += 1
                if 6 > math.floor(spell212ProgressLabelInt/10 + 1) > spell212LVLInt:
                    spell212LVLInt = math.floor(spell212ProgressLabelInt/10 + 1)
                    spell212LVLLabel.config(text='{0}'.format(spell212LVLInt))
                spell212ProgressLabel.config(text='{0}'.format(spell212ProgressLabelInt))
        elif num == 12:
            if magicCircleAttInt > 1:
                spell221ProgressLabelInt += 1
                if 6 > math.floor(spell221ProgressLabelInt/10 + 1) > spell221LVLInt:
                    spell221LVLInt = math.floor(spell221ProgressLabelInt/10 + 1)
                    spell221LVLLabel.config(text='{0}'.format(spell221LVLInt))
                spell221ProgressLabel.config(text='{0}'.format(spell221ProgressLabelInt))
        elif num == 13:
            if magicCircleAttInt > 1:
                spell222ProgressLabelInt += 1
                if 6 > math.floor(spell222ProgressLabelInt/10 + 1) > spell222LVLInt:
                    spell222LVLInt = math.floor(spell222ProgressLabelInt/10 + 1)
                    spell222LVLLabel.config(text='{0}'.format(spell222LVLInt))
                spell222ProgressLabel.config(text='{0}'.format(spell222ProgressLabelInt))
        elif num == 14:
            if magicCircleAttInt > 2:
                spell231ProgressLabelInt += 1
                if 6 > math.floor(spell231ProgressLabelInt/10 + 1) > spell231LVLInt:
                    spell231LVLInt = math.floor(spell231ProgressLabelInt/10 + 1)
                    spell231LVLLabel.config(text='{0}'.format(spell231LVLInt))
                spell231ProgressLabel.config(text='{0}'.format(spell231ProgressLabelInt))
        elif num == 15:
            if magicCircleAttInt > 2:
                spell232ProgressLabelInt += 1
                if 6 > math.floor(spell232ProgressLabelInt/10 + 1) > spell232LVLInt:
                    spell232LVLInt = math.floor(spell232ProgressLabelInt/10 + 1)
                    spell232LVLLabel.config(text='{0}'.format(spell232LVLInt))
                spell232ProgressLabel.config(text='{0}'.format(spell232ProgressLabelInt))
        elif num == 16:
            if magicCircleAttInt > 3:
                spell241ProgressLabelInt += 1
                if 5 > math.floor(spell241ProgressLabelInt/10 + 1) > spell241LVLInt:
                    spell241LVLInt = math.floor(spell241ProgressLabelInt/10 + 1)
                    spell241LVLLabel.config(text='{0}'.format(spell241LVLInt))
                spell241ProgressLabel.config(text='{0}'.format(spell241ProgressLabelInt))
        elif num == 17:
            if magicCircleAttInt > 3:
                spell242ProgressLabelInt += 1
                if 5 > math.floor(spell242ProgressLabelInt/10 + 1) > spell242LVLInt:
                    spell242LVLInt = math.floor(spell242ProgressLabelInt/10 + 1)
                    spell242LVLLabel.config(text='{0}'.format(spell242LVLInt))
                spell242ProgressLabel.config(text='{0}'.format(spell242ProgressLabelInt))
        elif num == 18:
            if magicCircleAttInt > 4:
                spell251ProgressLabelInt += 1
                if 4 > math.floor(spell251ProgressLabelInt/10 + 1) > spell251LVLInt:
                    spell251LVLInt = math.floor(spell251ProgressLabelInt/10 + 1)
                    spell251LVLLabel.config(text='{0}'.format(spell251LVLInt))
                spell251ProgressLabel.config(text='{0}'.format(spell251ProgressLabelInt))
        elif num == 19:
            if magicCircleAttInt > 4:
                spell252ProgressLabelInt += 1
                if 4 > math.floor(spell252ProgressLabelInt/10 + 1) > spell252LVLInt:
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
    global allStr,allAgi,allInt,allBody,lvlNow,allAtt,expNow,learningAttInt,shootAttInt,language,lastRace,lanAttLabel
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
    lanAttLabel.config(text=language)
    lastRace = raceVar.get()
    CreateToolTip(raceLabel2,support['race'][raceVar.get()]['tooltip'])

def add_att(num,widget):
    global allAtt, meleFightAttInt,shootAttInt,strongHitsAttInt,warBusinessAttInt,tacticsAttInt,attackAttInt,evasionAttInt,hasteAttInt,coldBloodAttInt,firstAidAttInt,manaAttInt,thiefArtAttInt,magicCircleAttInt,magicPowerAttInt,learningAttInt,healthAttInt,energyAttInt,resistAttInt,secondBreathAttInt,steelBodyAttInt,magicCircleAttLabel,magicCircleAttLabel2,spell211LVLLabel,spell212LVLLabel,spell221LVLLabel,spell222LVLLabel,spell231LVLLabel,spell232LVLLabel,spell241LVLLabel,spell242LVLLabel,spell251LVLLabel,spell252LVLLabel,spell11LVLLabel,spell12LVLLabel,spell21LVLLabel,spell22LVLLabel,spell31LVLLabel,spell32LVLLabel,spell41LVLLabel,spell42LVLLabel,spell51LVLLabel,spell52LVLLabel,staticEnergy,staticRegenEnergy,staticHaste,staticAttack,staticDMG,staticHP,staticRegenHP,staticEvade,staticDMG,staticMP,staticRegenMP,staticDirectMagicDMG,staticPeriodicMagicDMG,totalEnergy,totalRegenEnergy,totalHaste,totalAttack,totalDMG,totalHP,totalRegenHP,totalEvade,totalDMG,totalMP,totalRegenMP,totalDirectMagicDMG,totalPeriodicMagicDMG,totalSpellPenetration,staticSpellPenetration,staticEnergyLabel,staticDMGLabel,staticAttackLabel,staticDMGLabel,staticEvadeLabel,staticHasteLabel,staticMPLabel,staticRegenMPLabel,staticDirectMagicDMGLabel,staticSpellPenetrationLabel,staticHPLabel,staticRegenHPLabel,staticPeriodicMagicDMG,staticPeriodicMagicDMGLabel,totalEnergy,totalRegenEnergy,totalHaste,totalAttack,totalDMG,totalARP,totalHP,totalRegenHP,totalEvade,totalArmor,totalMgicArmor,totalMP,totalRegenMP,totalSpellPenetration,totalDirectMagicDMG,totalPeriodicMagicDMG,totalAttackLabel,totalDMGLabel,totalEvadeLabel,totalHasteLabel,totalMPLabel,totalRegenMPLabel,totalDirectMagicDMGLabel,totalSpellPenetrationLabel,totalPeriodicMagicDMGLabel,totalHPLabel,totalRegenHPLabel,staticHit,totalHit,staticHitLabel,totalHitLabel


    if allAtt > 0:
        if num == 0:
            if meleFightAttInt < 5:
                meleFightAttInt += 1
                staticAttackMin = int(staticAttack.split('-')[0])
                staticAttackMid = int(staticAttack.split('-')[1])
                staticAttackMax = int(staticAttack.split('-')[2])
                staticAttackMin += 1
                staticAttackMid += 1
                staticAttackMax += 1
                staticAttack = '{0}-{1}-{2}'.format(staticAttackMin,staticAttackMid,staticAttackMax)
                allAtt -= 1
                totalAttack = '{0}-{1}-{2}'.format(int(staticAttack.split('-')[0])-int(changeAttack.split('-')[0]),int(staticAttack.split('-')[1])-int(changeAttack.split('-')[1]),int(staticAttack.split('-')[2])-int(changeAttack.split('-')[2]))
                widget.config(text='{0}'.format(meleFightAttInt))
                staticAttackLabel.config(text = '{0}'.format(staticAttack))
                totalAttackLabel.config(text = '{0}'.format(totalAttack))
        elif num == 1:
            if shootAttInt < 5:
                shootAttInt += 1
                staticDMGMin = int(staticDMG.split('-')[0])
                staticDMGMid = int(staticDMG.split('-')[1])
                staticDMGMax = int(staticDMG.split('-')[2])
                staticDMGMin += 1
                staticDMGMid += 1
                staticDMGMax += 1
                staticDMG = '{0}-{1}-{2}'.format(staticDMGMin,staticDMGMid,staticDMGMax)
                allAtt -= 1
                totalDMG = '{0}-{1}-{2}'.format(int(staticDMG.split('-')[0])-int(changeDMG.split('-')[0]),int(staticDMG.split('-')[1])-int(changeDMG.split('-')[1]),int(staticDMG.split('-')[2])-int(changeDMG.split('-')[2]))
                widget.config(text='{0}'.format(shootAttInt))
                staticDMGLabel.config(text = '{0}'.format(staticDMG))
                totalDMGLabel.config(text = '{0}'.format(totalDMG))
        elif num == 2:
            if strongHitsAttInt < 5:
                strongHitsAttInt += 1
                allAtt -= 1
                widget.config(text='{0}'.format(strongHitsAttInt))
        elif num == 3:
            if warBusinessAttInt < 5:
                warBusinessAttInt += 1
                allAtt -= 1
                widget.config(text='{0}'.format(warBusinessAttInt))
        elif num == 4:
            if tacticsAttInt < 5:
                tacticsAttInt += 1
                allAtt -= 1
                widget.config(text='{0}'.format(tacticsAttInt))
        elif num == 5:
            if attackAttInt < 5:
                attackAttInt += 1
                staticHit += 1
                allAtt -= 1
                totalHit = staticHit + changeHit
                widget.config(text='{0}'.format(attackAttInt))
                staticHitLabel.config(text = '{0}'.format(staticHit))
                totalHitLabel.config(text = '{0}'.format(totalHit))
        elif num == 6:
            if evasionAttInt < 5:
                evasionAttInt += 1
                staticEvade += 1
                allAtt -= 1
                totalEvade = staticEvade + changeEvade
                widget.config(text='{0}'.format(evasionAttInt))
                staticEvadeLabel.config(text = '{0}'.format(staticEvade))
                totalEvadeLabel.config(text = '{0}'.format(totalEvade))
        elif num == 7:
            if hasteAttInt < 5:
                hasteAttInt += 1
                staticHaste += 1
                allAtt -= 1
                totalHaste = staticHaste + changeHaste
                widget.config(text='{0}'.format(hasteAttInt))
                staticHasteLabel.config(text = '{0}'.format(staticHaste))
                totalHasteLabel.config(text = '{0}'.format(totalHaste))
        elif num == 8:
            if coldBloodAttInt < 5:
                coldBloodAttInt += 1
                allAtt -= 1
                widget.config(text='{0}'.format(coldBloodAttInt))
        elif num == 9:
            if thiefArtAttInt < 5:
                thiefArtAttInt += 1
                allAtt -= 1
                widget.config(text='{0}'.format(thiefArtAttInt))
        elif num == 10:
            if manaAttInt < 5:
                manaAttInt += 1
                staticMP += 2
                staticRegenMP += 1
                allAtt -= 1
                totalMP = staticMP + changeMP
                totalRegenMP = staticRegenMP + changeRegenMP
                widget.config(text='{0}'.format(manaAttInt))
                staticMPLabel.config(text = '{0}'.format(staticMP))
                staticRegenMPLabel.config(text = '{0}'.format(staticRegenMP))
                totalMPLabel.config(text = '{0}'.format(totalMP))
                totalRegenMPLabel.config(text = '{0}'.format(totalRegenMP))
        elif num == 11:
            if firstAidAttInt < 5:
                firstAidAttInt += 1
                allAtt -= 1
                widget.config(text='{0}'.format(firstAidAttInt))
        elif num == 12:
            if magicCircleAttInt < 5:
                magicCircleAttInt += 1
                allAtt -= 1
                if magicCircleAttInt == 1:
                    spell11LVLInt = 1
                    spell12LVLInt = 1
                    spell211LVLInt = 1
                    spell212LVLInt = 1
                    spell11LVLLabel.config(text = '{0}'.format(spell11LVLInt))
                    spell12LVLLabel.config(text = '{0}'.format(spell12LVLInt))
                    spell211LVLLabel.config(text = '{0}'.format(spell211LVLInt))
                    spell212LVLLabel.config(text = '{0}'.format(spell212LVLInt))
                elif magicCircleAttInt == 2:
                    spell21LVLInt = 1
                    spell22LVLInt = 1
                    spell221LVLInt = 1
                    spell222LVLInt = 1
                    spell21LVLLabel.config(text = '{0}'.format(spell21LVLInt))
                    spell22LVLLabel.config(text = '{0}'.format(spell22LVLInt))
                    spell221LVLLabel.config(text = '{0}'.format(spell221LVLInt))
                    spell222LVLLabel.config(text = '{0}'.format(spell222LVLInt))
                elif magicCircleAttInt == 3:
                    spell31LVLInt = 1
                    spell32LVLInt = 1
                    spell231LVLInt = 1
                    spell232LVLInt = 1
                    spell31LVLLabel.config(text = '{0}'.format(spell31LVLInt))
                    spell32LVLLabel.config(text = '{0}'.format(spell32LVLInt))
                    spell231LVLLabel.config(text = '{0}'.format(spell231LVLInt))
                    spell232LVLLabel.config(text = '{0}'.format(spell232LVLInt))
                elif magicCircleAttInt == 4:
                    spell41LVLInt = 1
                    spell42LVLInt = 1
                    spell241LVLInt = 1
                    spell242LVLInt = 1
                    spell41LVLLabel.config(text = '{0}'.format(spell41LVLInt))
                    spell42LVLLabel.config(text = '{0}'.format(spell42LVLInt))
                    spell241LVLLabel.config(text = '{0}'.format(spell241LVLInt))
                    spell242LVLLabel.config(text = '{0}'.format(spell242LVLInt))
                elif magicCircleAttInt == 5:
                    spell51LVLInt = 1
                    spell52LVLInt = 1
                    spell251LVLInt = 1
                    spell252LVLInt = 1
                    spell251LVLLabel.config(text = '{0}'.format(spell51LVLInt))
                    spell252LVLLabel.config(text = '{0}'.format(spell52LVLInt))
                    spell251LVLLabel.config(text = '{0}'.format(spell251LVLInt))
                    spell252LVLLabel.config(text = '{0}'.format(spell252LVLInt))

                widget.config(text='{0}'.format(magicCircleAttInt))
                try:
                    if magicCircleAttLabel:
                        magicCircleAttLabel.config(text='{0}'.format(magicCircleAttInt))
                        magicCircleAttLabel2.config(text='{0}'.format(magicCircleAttInt))
                except:
                    print("magic window don't open")
        elif num == 13:
            if magicPowerAttInt < 5:
                magicPowerAttInt += 1
                staticDirectMagicDMG += 1
                staticSpellPenetration += 1
                staticPeriodicMagicDMG += 1
                allAtt -= 1
                totalDirectMagicDMG = staticDirectMagicDMG + changeDirectMagicDMG
                totalSpellPenetration = staticSpellPenetration + changeSpellPenetration
                totalPeriodicMagicDMG = staticPeriodicMagicDMG + changePeriodicMagicDMG
                widget.config(text='{0}'.format(magicPowerAttInt))
                staticDirectMagicDMGLabel.config(text='{0}'.format(staticDirectMagicDMG))
                staticSpellPenetrationLabel.config(text='{0}'.format(staticSpellPenetration))
                staticPeriodicMagicDMGLabel.config(text='{0}'.format(staticPeriodicMagicDMG))
                totalDirectMagicDMGLabel.config(text='{0}'.format(totalDirectMagicDMG))
                totalSpellPenetrationLabel.config(text='{0}'.format(totalSpellPenetration))
                totalPeriodicMagicDMGLabel.config(text='{0}'.format(totalPeriodicMagicDMG))
        elif num == 14:
            if learningAttInt < 5:
                learningAttInt += 1
                allAtt -= 1
                widget.config(text='{0}'.format(learningAttInt))
        elif num == 15:
            if healthAttInt < 5:
                healthAttInt += 1
                staticHP += 2
                staticRegenHP += 1
                allAtt -= 1
                totalHP = staticHP + changeHP
                totalRegenHP = staticRegenHP + changeRegenHP
                widget.config(text='{0}'.format(healthAttInt))
                staticHPLabel.config(text='{0}'.format(staticHP))
                staticRegenHPLabel.config(text='{0}'.format(staticRegenHP))
                totalHPLabel.config(text='{0}'.format(totalHP))
                totalRegenHPLabel.config(text='{0}'.format(totalRegenHP))
        elif num == 16:
            if energyAttInt < 5:
                energyAttInt += 1
                staticEnergy += 1
                allAtt -= 1
                totalEnergy = staticEnergy + changeEnergy
                widget.config(text='{0}'.format(energyAttInt))
                staticEnergyLabel.config(text='{0}'.format(staticEnergy))
                totalEnergyLabel.config(text='{0}'.format(totalEnergy))
        elif num == 17:
            if resistAttInt < 5:
                resistAttInt += 1
                allAtt -= 1
                widget.config(text='{0}'.format(resistAttInt))
        elif num == 18:
            if secondBreathAttInt < 5:
                secondBreathAttInt += 1
                allAtt -= 1
                widget.config(text='{0}'.format(secondBreathAttInt))
        elif num == 19:
            if steelBodyAttInt < 5:
                steelBodyAttInt += 1
                allAtt -= 1
                widget.config(text='{0}'.format(steelBodyAttInt))

        availableAttNumb.config(text='{0}'.format(allAtt))

def create_active_skill_window():

    global skillProgressInt1,skillProgressInt2,skillProgressInt3,skillProgressInt4,skillProgressInt5,skillProgressInt6,skillProgressInt7,skillProgressInt8,skillProgressInt9,skillProgressInt10,skillLevelInt1,skillLevelInt2,skillLevelInt3,skillLevelInt4,skillLevelInt5,skillLevelInt6,skillLevelInt7,skillLevelInt8,skillLevelInt9,skillLevelInt10,skillLevelLabel1,skillLevelLabel2,skillLevelLabel3,skillLevelLabel4,skillLevelLabel5,skillLevelLabel6,skillLevelLabel7,skillLevelLabel8,skillLevelLabel9,skillLevelLabel10,skillProgressLabel1,skillProgressLabel2,skillProgressLabel3,skillProgressLabel4,skillProgressLabel5,skillProgressLabel6,skillProgressLabel7,skillProgressLabel8,skillProgressLabel9,skillProgressLabel10

    ChoAct = Toplevel(window)
    ChoAct.title('Личные умения')
    ChoAct.resizable(width=False, height=False)
    ChoAct.rowconfigure(0, pad=3)
    ChoAct.rowconfigure(1, pad=3)
    ChoAct.rowconfigure(2, pad=3)
    ChoAct.rowconfigure(3, pad=3)
    ChoAct.rowconfigure(4, pad=3)
    ChoAct.columnconfigure(0, pad=3)
    ChoAct.columnconfigure(1, pad=3)
    ChoAct.columnconfigure(2, pad=3)
    ChoAct.columnconfigure(3, pad=3)

    def add_skill_exp(num):

        global skillProgressInt1,skillProgressInt2,skillProgressInt3,skillProgressInt4,skillProgressInt5,skillProgressInt6,skillProgressInt7,skillProgressInt8,skillProgressInt9,skillProgressInt10,skillLevelInt1,skillLevelInt2,skillLevelInt3,skillLevelInt4,skillLevelInt5,skillLevelInt6,skillLevelInt7,skillLevelInt8,skillLevelInt9,skillLevelInt10,skillLevelLabel1,skillLevelLabel2,skillLevelLabel3,skillLevelLabel4,skillLevelLabel5,skillLevelLabel6,skillLevelLabel7,skillLevelLabel8,skillLevelLabel9,skillLevelLabel10,skillProgressLabel1,skillProgressLabel2,skillProgressLabel3,skillProgressLabel4,skillProgressLabel5,skillProgressLabel6,skillProgressLabel7,skillProgressLabel8,skillProgressLabel9,skillProgressLabel10

        if num == 0:
            skillProgressInt1 += 1
            skillProgressLabel1.config(text='{0}'.format(skillProgressInt1))
            if 6 > math.floor(skillProgressInt1/10 + 1) > skillLevelInt1:
                skillLevelInt1 = math.floor(skillProgressInt1/10 + 1)
                skillLevelLabel1.config(text='{0}'.format(skillLevelInt1))
        elif num == 1:
            skillProgressInt2 += 1
            skillProgressLabel2.config(text='{0}'.format(skillProgressInt2))
            if 6 > math.floor(skillProgressInt2/10 + 1) > skillLevelInt2:
                skillLevelInt2 = math.floor(skillProgressInt2/10 + 1)
                skillLevelLabel2.config(text='{0}'.format(skillLevelInt2))
        elif num == 2:
            skillProgressInt3 += 1
            skillProgressLabel3.config(text='{0}'.format(skillProgressInt3))
            if 6 > math.floor(skillProgressInt3/10 + 1) > skillLevelInt3:
                skillLevelInt3 = math.floor(skillProgressInt3/10 + 1)
                skillLevelLabel3.config(text='{0}'.format(skillLevelInt3))
        elif num == 3:
            skillProgressInt4 += 1
            skillProgressLabel4.config(text='{0}'.format(skillProgressInt4))
            if 6 > math.floor(skillProgressInt4/10 + 1) > skillLevelInt4:
                skillLevelInt4 = math.floor(skillProgressInt4/10 + 1)
                skillLevelLabel4.config(text='{0}'.format(skillLevelInt4))
        elif num == 4:
            skillProgressInt5 += 1
            skillProgressLabel5.config(text='{0}'.format(skillProgressInt5))
            if 6 > math.floor(skillProgressInt5/10 + 1) > skillLevelInt5:
                skillLevelInt5 = math.floor(skillProgressInt5/10 + 1)
                skillLevelLabel5.config(text='{0}'.format(skillLevelInt5))
        elif num == 5:
            skillProgressInt6 += 1
            skillProgressLabel6.config(text='{0}'.format(skillProgressInt6))
            if 6 > math.floor(skillProgressInt6/10 + 1) > skillLevelInt6:
                skillLevelInt6 = math.floor(skillProgressInt6/10 + 1)
                skillLevelLabel6.config(text='{0}'.format(skillLevelInt6))
        elif num == 6:
            skillProgressInt7 += 1
            skillProgressLabel7.config(text='{0}'.format(skillProgressInt7))
            if 6 > math.floor(skillProgressInt7/10 + 1) > skillLevelInt7:
                skillLevelInt7 = math.floor(skillProgressInt7/10 + 1)
                skillLevelLabel7.config(text='{0}'.format(skillLevelInt7))
        elif num == 7:
            skillProgressInt8 += 1
            skillProgressLabel8.config(text='{0}'.format(skillProgressInt8))
            if 6 > math.floor(skillProgressInt8/10 + 1) > skillLevelInt8:
                skillLevelInt8 = math.floor(skillProgressInt8/10 + 1)
                skillLevelLabel8.config(text='{0}'.format(skillLevelInt8))
        elif num == 8:
            skillProgressInt9 += 1
            skillProgressLabel9.config(text='{0}'.format(skillProgressInt9))
            if 6 > math.floor(skillProgressInt9/10 + 1) > skillLevelInt9:
                skillLevelInt9 = math.floor(skillProgressInt9/10 + 1)
                skillLevelLabel9.config(text='{0}'.format(skillLevelInt9))
        elif num == 9:
            skillProgressInt10 += 1
            skillProgressLabel10.config(text='{0}'.format(skillProgressInt10))
            if 6 > math.floor(skillProgressInt10/10 + 1) > skillLevelInt10:
                skillLevelInt10 = math.floor(skillProgressInt10/10 + 1)
                skillLevelLabel10.config(text='{0}'.format(skillLevelInt10))

    skillLabel1 = Label(ChoAct, text=list(support['activeSkill'].keys())[0])
    skillLabel2 = Label(ChoAct, text=list(support['activeSkill'].keys())[1])
    skillLabel3 = Label(ChoAct, text=list(support['activeSkill'].keys())[2])
    skillLabel4 = Label(ChoAct, text=list(support['activeSkill'].keys())[3])
    skillLabel5 = Label(ChoAct, text=list(support['activeSkill'].keys())[4])
    skillLabel6 = Label(ChoAct, text=list(support['activeSkill'].keys())[5])
    skillLabel7 = Label(ChoAct, text=list(support['activeSkill'].keys())[6])
    skillLabel8 = Label(ChoAct, text=list(support['activeSkill'].keys())[7])
    skillLabel9 = Label(ChoAct, text=list(support['activeSkill'].keys())[8])
    skillLabel10 = Label(ChoAct, text=list(support['activeSkill'].keys())[9])

    CreateToolTip(skillLabel1,support['activeSkill'][list(support['activeSkill'].keys())[0]])
    CreateToolTip(skillLabel2,support['activeSkill'][list(support['activeSkill'].keys())[1]])
    CreateToolTip(skillLabel3,support['activeSkill'][list(support['activeSkill'].keys())[2]])
    CreateToolTip(skillLabel4,support['activeSkill'][list(support['activeSkill'].keys())[3]])
    CreateToolTip(skillLabel5,support['activeSkill'][list(support['activeSkill'].keys())[4]])
    CreateToolTip(skillLabel6,support['activeSkill'][list(support['activeSkill'].keys())[5]])
    CreateToolTip(skillLabel7,support['activeSkill'][list(support['activeSkill'].keys())[6]])
    CreateToolTip(skillLabel8,support['activeSkill'][list(support['activeSkill'].keys())[7]])
    CreateToolTip(skillLabel9,support['activeSkill'][list(support['activeSkill'].keys())[8]])
    CreateToolTip(skillLabel10,support['activeSkill'][list(support['activeSkill'].keys())[9]])

    skillLabel1.grid(row=0, column=0, sticky=W)
    skillLabel2.grid(row=1, column=0, sticky=W)
    skillLabel3.grid(row=2, column=0, sticky=W)
    skillLabel4.grid(row=3, column=0, sticky=W)
    skillLabel5.grid(row=4, column=0, sticky=W)
    skillLabel6.grid(row=5, column=0, sticky=W)
    skillLabel7.grid(row=6, column=0, sticky=W)
    skillLabel8.grid(row=7, column=0, sticky=W)
    skillLabel9.grid(row=8, column=0, sticky=W)
    skillLabel10.grid(row=9, column=0, sticky=W)

    skillProgressLabel1 = Label(ChoAct, text='{0}'.format(skillProgressInt1))
    skillProgressLabel2 = Label(ChoAct, text='{0}'.format(skillProgressInt2))
    skillProgressLabel3 = Label(ChoAct, text='{0}'.format(skillProgressInt3))
    skillProgressLabel4 = Label(ChoAct, text='{0}'.format(skillProgressInt4))
    skillProgressLabel5 = Label(ChoAct, text='{0}'.format(skillProgressInt5))
    skillProgressLabel6 = Label(ChoAct, text='{0}'.format(skillProgressInt6))
    skillProgressLabel7 = Label(ChoAct, text='{0}'.format(skillProgressInt7))
    skillProgressLabel8 = Label(ChoAct, text='{0}'.format(skillProgressInt8))
    skillProgressLabel9 = Label(ChoAct, text='{0}'.format(skillProgressInt9))
    skillProgressLabel10 = Label(ChoAct, text='{0}'.format(skillProgressInt10))

    skillProgressLabel1.grid(row=0, column=1)
    skillProgressLabel2.grid(row=1, column=1)
    skillProgressLabel3.grid(row=2, column=1)
    skillProgressLabel4.grid(row=3, column=1)
    skillProgressLabel5.grid(row=4, column=1)
    skillProgressLabel6.grid(row=5, column=1)
    skillProgressLabel7.grid(row=6, column=1)
    skillProgressLabel8.grid(row=7, column=1)
    skillProgressLabel9.grid(row=8, column=1)
    skillProgressLabel10.grid(row=9, column=1)

    skillButt1 = Button(ChoAct, text='+', command=lambda: add_skill_exp(0))
    skillButt2 = Button(ChoAct, text='+', command=lambda: add_skill_exp(1))
    skillButt3 = Button(ChoAct, text='+', command=lambda: add_skill_exp(2))
    skillButt4 = Button(ChoAct, text='+', command=lambda: add_skill_exp(3))
    skillButt5 = Button(ChoAct, text='+', command=lambda: add_skill_exp(4))
    skillButt6 = Button(ChoAct, text='+', command=lambda: add_skill_exp(5))
    skillButt7 = Button(ChoAct, text='+', command=lambda: add_skill_exp(6))
    skillButt8 = Button(ChoAct, text='+', command=lambda: add_skill_exp(7))
    skillButt9 = Button(ChoAct, text='+', command=lambda: add_skill_exp(8))
    skillButt10 = Button(ChoAct, text='+', command=lambda: add_skill_exp(9))

    skillButt1.grid(row=0, column=2)
    skillButt2.grid(row=1, column=2)
    skillButt3.grid(row=2, column=2)
    skillButt4.grid(row=3, column=2)
    skillButt5.grid(row=4, column=2)
    skillButt6.grid(row=5, column=2)
    skillButt7.grid(row=6, column=2)
    skillButt8.grid(row=7, column=2)
    skillButt9.grid(row=8, column=2)
    skillButt10.grid(row=9, column=2)

    skillLevelLabel1 = Label(ChoAct, text='{0}'.format(skillLevelInt1))
    skillLevelLabel2 = Label(ChoAct, text='{0}'.format(skillLevelInt2))
    skillLevelLabel3 = Label(ChoAct, text='{0}'.format(skillLevelInt3))
    skillLevelLabel4 = Label(ChoAct, text='{0}'.format(skillLevelInt4))
    skillLevelLabel5 = Label(ChoAct, text='{0}'.format(skillLevelInt5))
    skillLevelLabel6 = Label(ChoAct, text='{0}'.format(skillLevelInt6))
    skillLevelLabel7 = Label(ChoAct, text='{0}'.format(skillLevelInt7))
    skillLevelLabel8 = Label(ChoAct, text='{0}'.format(skillLevelInt8))
    skillLevelLabel9 = Label(ChoAct, text='{0}'.format(skillLevelInt9))
    skillLevelLabel10 = Label(ChoAct, text='{0}'.format(skillLevelInt10))

    skillLevelLabel1.grid(row=0, column=3)
    skillLevelLabel2.grid(row=1, column=3)
    skillLevelLabel3.grid(row=2, column=3)
    skillLevelLabel4.grid(row=3, column=3)
    skillLevelLabel5.grid(row=4, column=3)
    skillLevelLabel6.grid(row=5, column=3)
    skillLevelLabel7.grid(row=6, column=3)
    skillLevelLabel8.grid(row=7, column=3)
    skillLevelLabel9.grid(row=8, column=3)
    skillLevelLabel10.grid(row=9, column=3)

def create_inventory_window():
    global allAtt, meleFightAttInt,shootAttInt,strongHitsAttInt,warBusinessAttInt,tacticsAttInt,attackAttInt,evasionAttInt,hasteAttInt,coldBloodAttInt,firstAidAttInt,manaAttInt,thiefArtAttInt,magicCircleAttInt,magicPowerAttInt,learningAttInt,healthAttInt,energyAttInt,resistAttInt,secondBreathAttInt,steelBodyAttInt,magicCircleAttLabel,magicCircleAttLabel2,spell211LVLLabel,spell212LVLLabel,spell221LVLLabel,spell222LVLLabel,spell231LVLLabel,spell232LVLLabel,spell241LVLLabel,spell242LVLLabel,spell251LVLLabel,spell252LVLLabel,spell11LVLLabel,spell12LVLLabel,spell21LVLLabel,spell22LVLLabel,spell31LVLLabel,spell32LVLLabel,spell41LVLLabel,spell42LVLLabel,spell51LVLLabel,spell52LVLLabel,staticEnergy,staticRegenEnergy,staticHaste,staticAttack,staticDMG,staticHP,staticRegenHP,staticEvade,staticDMG,staticMP,staticRegenMP,staticDirectMagicDMG,staticPeriodicMagicDMG,totalEnergy,totalRegenEnergy,totalHaste,totalAttack,totalDMG,totalHP,totalRegenHP,totalEvade,totalDMG,totalMP,totalRegenMP,totalDirectMagicDMG,totalPeriodicMagicDMG,totalSpellPenetration,staticSpellPenetration,staticEnergyLabel,staticDMGLabel,staticAttackLabel,staticDMGLabel,staticEvadeLabel,staticHasteLabel,staticMPLabel,staticRegenMPLabel,staticDirectMagicDMGLabel,staticSpellPenetrationLabel,staticHPLabel,staticRegenHPLabel,staticPeriodicMagicDMG,staticPeriodicMagicDMGLabel,totalEnergy,totalRegenEnergy,totalHaste,totalAttack,totalDMG,totalARP,totalHP,totalRegenHP,totalEvade,totalArmor,totalMgicArmor,totalMP,totalRegenMP,totalSpellPenetration,totalDirectMagicDMG,totalPeriodicMagicDMG,totalAttackLabel,totalDMGLabel,totalEvadeLabel,totalHasteLabel,totalMPLabel,totalRegenMPLabel,totalDirectMagicDMGLabel,totalSpellPenetrationLabel,totalPeriodicMagicDMGLabel,totalHPLabel,totalRegenHPLabel,staticHit,totalHit,staticHitLabel,totalHitLabel,rightHandEnergy,rightHandRegenEnergy,rightHandHaste,rightHandHit,rightHandAttack,rightHandMinAttack,rightHandMidAttack,rightHandMaxAttack,rightHandMinDMG,rightHandMidDMG,rightHandMaxDMG,rightHandDMG,rightHandARP,rightHandHP,rightHandRegenHP,rightHandEvade,rightHandArmor,rightHandMgicArmor,rightHandMP,rightHandRegenMP,rightHandSpellPenetration,rightHandDirectMagicDMG,rightHandPeriodicMagicDMG,rightHandCharmEnergy,rightHandCharmRegenEnergy,rightHandCharmHaste,rightHandCharmHit,rightHandCharmAttack,rightHandCharmMinAttack,rightHandCharmMidAttack,rightHandCharmMaxAttack,rightHandCharmMinDMG,rightHandCharmMidDMG,rightHandCharmMaxDMG,rightHandCharmDMG,rightHandCharmARP,rightHandCharmHP,rightHandCharmRegenHP,rightHandCharmEvade,rightHandCharmArmor,rightHandCharmMgicArmor,rightHandCharmMP,rightHandCharmRegenMP,rightHandCharmSpellPenetration,rightHandCharmDirectMagicDMG,rightHandCharmPeriodicMagicDMG,leftHandEnergy,leftHandRegenEnergy,leftHandHaste,leftHandHit,leftHandAttack,leftHandMinAttack,leftHandMidAttack,leftHandMaxAttack,leftHandMinDMG,leftHandMidDMG,leftHandMaxDMG,leftHandDMG,leftHandARP,leftHandHP,leftHandRegenHP,leftHandEvade,leftHandArmor,leftHandMgicArmor,leftHandMP,leftHandRegenMP,leftHandSpellPenetration,leftHandDirectMagicDMG,leftHandPeriodicMagicDMG,leftHandCharmEnergy,leftHandCharmRegenEnergy,leftHandCharmHaste,leftHandCharmHit,leftHandCharmAttack,leftHandCharmMinAttack,leftHandCharmMidAttack,leftHandCharmMaxAttack,leftHandCharmMinDMG,leftHandCharmMidDMG,leftHandCharmMaxDMG,leftHandCharmDMG,leftHandCharmARP,leftHandCharmHP,leftHandCharmRegenHP,leftHandCharmEvade,leftHandCharmArmor,leftHandCharmMgicArmor,leftHandCharmMP,leftHandCharmRegenMP,leftHandCharmSpellPenetration,leftHandCharmDirectMagicDMG,leftHandCharmPeriodicMagicDMG,ChestEnergy,ChestRegenEnergy,ChestHaste,ChestHit,ChestAttack,ChestMinAttack,ChestMidAttack,ChestMaxAttack,ChestMinDMG,ChestMidDMG,ChestMaxDMG,ChestDMG,ChestARP,ChestHP,ChestRegenHP,ChestEvade,ChestArmor,ChestMgicArmor,ChestMP,ChestRegenMP,ChestSpellPenetration,ChestDirectMagicDMG,ChestPeriodicMagicDMG,ChestCharmEnergy,ChestCharmRegenEnergy,ChestCharmHaste,ChestCharmHit,ChestCharmAttack,ChestCharmMinAttack,ChestCharmMidAttack,ChestCharmMaxAttack,ChestCharmMinDMG,ChestCharmMidDMG,ChestCharmMaxDMG,ChestCharmDMG,ChestCharmARP,ChestCharmHP,ChestCharmRegenHP,ChestCharmEvade,ChestCharmArmor,ChestCharmMgicArmor,ChestCharmMP,ChestCharmRegenMP,ChestCharmSpellPenetration,ChestCharmDirectMagicDMG,ChestCharmPeriodicMagicDMG,amuletEnergy,amuletRegenEnergy,amuletHaste,amuletHit,amuletAttack,amuletMinAttack,amuletMidAttack,amuletMaxAttack,amuletMinDMG,amuletMidDMG,amuletMaxDMG,amuletDMG,amuletARP,amuletHP,amuletRegenHP,amuletEvade,amuletArmor,amuletMgicArmor,amuletMP,amuletRegenMP,amuletSpellPenetration,amuletDirectMagicDMG,amuletPeriodicMagicDMG,amuletCharmEnergy,amuletCharmRegenEnergy,amuletCharmHaste,amuletCharmHit,amuletCharmAttack,amuletCharmMinAttack,amuletCharmMidAttack,amuletCharmMaxAttack,amuletCharmMinDMG,amuletCharmMidDMG,amuletCharmMaxDMG,amuletCharmDMG,amuletCharmARP,amuletCharmHP,amuletCharmRegenHP,amuletCharmEvade,amuletCharmArmor,amuletCharmMgicArmor,amuletCharmMP,amuletCharmRegenMP,amuletCharmSpellPenetration,amuletCharmDirectMagicDMG,amuletCharmPeriodicMagicDMG,ringEnergy,ringRegenEnergy,ringHaste,ringHit,ringAttack,ringMinAttack,ringMidAttack,ringMaxAttack,ringMinDMG,ringMidDMG,ringMaxDMG,ringDMG,ringARP,ringHP,ringRegenHP,ringEvade,ringArmor,ringMgicArmor,ringMP,ringRegenMP,ringSpellPenetration,ringDirectMagicDMG,ringPeriodicMagicDMG,ringCharmEnergy,ringCharmRegenEnergy,ringCharmHaste,ringCharmHit,ringCharmAttack,ringCharmMinAttack,ringCharmMidAttack,ringCharmMaxAttack,ringCharmMinDMG,ringCharmMidDMG,ringCharmMaxDMG,ringCharmDMG,ringCharmARP,ringCharmHP,ringCharmRegenHP,ringCharmEvade,ringCharmArmor,ringCharmMgicArmor,ringCharmMP,ringCharmRegenMP,ringCharmSpellPenetration,ringCharmDirectMagicDMG,ringCharmPeriodicMagicDMG,bookEnergy,bookRegenEnergy,bookHaste,bookHit,bookAttack,bookMinAttack,bookMidAttack,bookMaxAttack,bookMinDMG,bookMidDMG,bookMaxDMG,bookDMG,bookARP,bookHP,bookRegenHP,bookEvade,bookArmor,bookMgicArmor,bookMP,bookRegenMP,bookSpellPenetration,bookDirectMagicDMG,bookPeriodicMagicDMG,bookCharmEnergy,bookCharmRegenEnergy,bookCharmHaste,bookCharmHit,bookCharmAttack,bookCharmMinAttack,bookCharmMidAttack,bookCharmMaxAttack,bookCharmMinDMG,bookCharmMidDMG,bookCharmMaxDMG,bookCharmDMG,bookCharmARP,bookCharmHP,bookCharmRegenHP,bookCharmEvade,bookCharmArmor,bookCharmMgicArmor,bookCharmMP,bookCharmRegenMP,bookCharmSpellPenetration,bookCharmDirectMagicDMG,bookCharmPeriodicMagicDMG,staticArmor,staticMgicArmor,staticARP

    def add_att_inventory(event):
        global allAtt, meleFightAttInt,shootAttInt,strongHitsAttInt,warBusinessAttInt,tacticsAttInt,attackAttInt,evasionAttInt,hasteAttInt,coldBloodAttInt,firstAidAttInt,manaAttInt,thiefArtAttInt,magicCircleAttInt,magicPowerAttInt,learningAttInt,healthAttInt,energyAttInt,resistAttInt,secondBreathAttInt,steelBodyAttInt,magicCircleAttLabel,magicCircleAttLabel2,spell211LVLLabel,spell212LVLLabel,spell221LVLLabel,spell222LVLLabel,spell231LVLLabel,spell232LVLLabel,spell241LVLLabel,spell242LVLLabel,spell251LVLLabel,spell252LVLLabel,spell11LVLLabel,spell12LVLLabel,spell21LVLLabel,spell22LVLLabel,spell31LVLLabel,spell32LVLLabel,spell41LVLLabel,spell42LVLLabel,spell51LVLLabel,spell52LVLLabel,staticEnergy,staticRegenEnergy,staticHaste,staticAttack,staticDMG,staticHP,staticRegenHP,staticEvade,staticDMG,staticMP,staticRegenMP,staticDirectMagicDMG,staticPeriodicMagicDMG,totalEnergy,totalRegenEnergy,totalHaste,totalAttack,totalDMG,totalHP,totalRegenHP,totalEvade,totalDMG,totalMP,totalRegenMP,totalDirectMagicDMG,totalPeriodicMagicDMG,totalSpellPenetration,staticSpellPenetration,staticEnergyLabel,staticDMGLabel,staticAttackLabel,staticDMGLabel,staticEvadeLabel,staticHasteLabel,staticMPLabel,staticRegenMPLabel,staticDirectMagicDMGLabel,staticSpellPenetrationLabel,staticHPLabel,staticRegenHPLabel,staticPeriodicMagicDMG,staticPeriodicMagicDMGLabel,totalEnergy,totalRegenEnergy,totalHaste,totalAttack,totalDMG,totalARP,totalHP,totalRegenHP,totalEvade,totalArmor,totalMgicArmor,totalMP,totalRegenMP,totalSpellPenetration,totalDirectMagicDMG,totalPeriodicMagicDMG,totalAttackLabel,totalDMGLabel,totalEvadeLabel,totalHasteLabel,totalMPLabel,totalRegenMPLabel,totalDirectMagicDMGLabel,totalSpellPenetrationLabel,totalPeriodicMagicDMGLabel,totalHPLabel,totalRegenHPLabel,staticHit,totalHit,staticHitLabel,totalHitLabel,rightHandEnergy,rightHandRegenEnergy,rightHandHaste,rightHandHit,rightHandAttack,rightHandMinAttack,rightHandMidAttack,rightHandMaxAttack,rightHandMinDMG,rightHandMidDMG,rightHandMaxDMG,rightHandDMG,rightHandARP,rightHandHP,rightHandRegenHP,rightHandEvade,rightHandArmor,rightHandMgicArmor,rightHandMP,rightHandRegenMP,rightHandSpellPenetration,rightHandDirectMagicDMG,rightHandPeriodicMagicDMG,rightHandCharmEnergy,rightHandCharmRegenEnergy,rightHandCharmHaste,rightHandCharmHit,rightHandCharmAttack,rightHandCharmMinAttack,rightHandCharmMidAttack,rightHandCharmMaxAttack,rightHandCharmMinDMG,rightHandCharmMidDMG,rightHandCharmMaxDMG,rightHandCharmDMG,rightHandCharmARP,rightHandCharmHP,rightHandCharmRegenHP,rightHandCharmEvade,rightHandCharmArmor,rightHandCharmMgicArmor,rightHandCharmMP,rightHandCharmRegenMP,rightHandCharmSpellPenetration,rightHandCharmDirectMagicDMG,rightHandCharmPeriodicMagicDMG,leftHandEnergy,leftHandRegenEnergy,leftHandHaste,leftHandHit,leftHandAttack,leftHandMinAttack,leftHandMidAttack,leftHandMaxAttack,leftHandMinDMG,leftHandMidDMG,leftHandMaxDMG,leftHandDMG,leftHandARP,leftHandHP,leftHandRegenHP,leftHandEvade,leftHandArmor,leftHandMgicArmor,leftHandMP,leftHandRegenMP,leftHandSpellPenetration,leftHandDirectMagicDMG,leftHandPeriodicMagicDMG,leftHandCharmEnergy,leftHandCharmRegenEnergy,leftHandCharmHaste,leftHandCharmHit,leftHandCharmAttack,leftHandCharmMinAttack,leftHandCharmMidAttack,leftHandCharmMaxAttack,leftHandCharmMinDMG,leftHandCharmMidDMG,leftHandCharmMaxDMG,leftHandCharmDMG,leftHandCharmARP,leftHandCharmHP,leftHandCharmRegenHP,leftHandCharmEvade,leftHandCharmArmor,leftHandCharmMgicArmor,leftHandCharmMP,leftHandCharmRegenMP,leftHandCharmSpellPenetration,leftHandCharmDirectMagicDMG,leftHandCharmPeriodicMagicDMG,ChestEnergy,ChestRegenEnergy,ChestHaste,ChestHit,ChestAttack,ChestMinAttack,ChestMidAttack,ChestMaxAttack,ChestMinDMG,ChestMidDMG,ChestMaxDMG,ChestDMG,ChestARP,ChestHP,ChestRegenHP,ChestEvade,ChestArmor,ChestMgicArmor,ChestMP,ChestRegenMP,ChestSpellPenetration,ChestDirectMagicDMG,ChestPeriodicMagicDMG,ChestCharmEnergy,ChestCharmRegenEnergy,ChestCharmHaste,ChestCharmHit,ChestCharmAttack,ChestCharmMinAttack,ChestCharmMidAttack,ChestCharmMaxAttack,ChestCharmMinDMG,ChestCharmMidDMG,ChestCharmMaxDMG,ChestCharmDMG,ChestCharmARP,ChestCharmHP,ChestCharmRegenHP,ChestCharmEvade,ChestCharmArmor,ChestCharmMgicArmor,ChestCharmMP,ChestCharmRegenMP,ChestCharmSpellPenetration,ChestCharmDirectMagicDMG,ChestCharmPeriodicMagicDMG,amuletEnergy,amuletRegenEnergy,amuletHaste,amuletHit,amuletAttack,amuletMinAttack,amuletMidAttack,amuletMaxAttack,amuletMinDMG,amuletMidDMG,amuletMaxDMG,amuletDMG,amuletARP,amuletHP,amuletRegenHP,amuletEvade,amuletArmor,amuletMgicArmor,amuletMP,amuletRegenMP,amuletSpellPenetration,amuletDirectMagicDMG,amuletPeriodicMagicDMG,amuletCharmEnergy,amuletCharmRegenEnergy,amuletCharmHaste,amuletCharmHit,amuletCharmAttack,amuletCharmMinAttack,amuletCharmMidAttack,amuletCharmMaxAttack,amuletCharmMinDMG,amuletCharmMidDMG,amuletCharmMaxDMG,amuletCharmDMG,amuletCharmARP,amuletCharmHP,amuletCharmRegenHP,amuletCharmEvade,amuletCharmArmor,amuletCharmMgicArmor,amuletCharmMP,amuletCharmRegenMP,amuletCharmSpellPenetration,amuletCharmDirectMagicDMG,amuletCharmPeriodicMagicDMG,ringEnergy,ringRegenEnergy,ringHaste,ringHit,ringAttack,ringMinAttack,ringMidAttack,ringMaxAttack,ringMinDMG,ringMidDMG,ringMaxDMG,ringDMG,ringARP,ringHP,ringRegenHP,ringEvade,ringArmor,ringMgicArmor,ringMP,ringRegenMP,ringSpellPenetration,ringDirectMagicDMG,ringPeriodicMagicDMG,ringCharmEnergy,ringCharmRegenEnergy,ringCharmHaste,ringCharmHit,ringCharmAttack,ringCharmMinAttack,ringCharmMidAttack,ringCharmMaxAttack,ringCharmMinDMG,ringCharmMidDMG,ringCharmMaxDMG,ringCharmDMG,ringCharmARP,ringCharmHP,ringCharmRegenHP,ringCharmEvade,ringCharmArmor,ringCharmMgicArmor,ringCharmMP,ringCharmRegenMP,ringCharmSpellPenetration,ringCharmDirectMagicDMG,ringCharmPeriodicMagicDMG,bookEnergy,bookRegenEnergy,bookHaste,bookHit,bookAttack,bookMinAttack,bookMidAttack,bookMaxAttack,bookMinDMG,bookMidDMG,bookMaxDMG,bookDMG,bookARP,bookHP,bookRegenHP,bookEvade,bookArmor,bookMgicArmor,bookMP,bookRegenMP,bookSpellPenetration,bookDirectMagicDMG,bookPeriodicMagicDMG,bookCharmEnergy,bookCharmRegenEnergy,bookCharmHaste,bookCharmHit,bookCharmAttack,bookCharmMinAttack,bookCharmMidAttack,bookCharmMaxAttack,bookCharmMinDMG,bookCharmMidDMG,bookCharmMaxDMG,bookCharmDMG,bookCharmARP,bookCharmHP,bookCharmRegenHP,bookCharmEvade,bookCharmArmor,bookCharmMgicArmor,bookCharmMP,bookCharmRegenMP,bookCharmSpellPenetration,bookCharmDirectMagicDMG,bookCharmPeriodicMagicDMG,staticArmor,staticMgicArmor,staticARP

        rightHandEnergyNew = int(rightHandEnergyEntry.get())
        rightHandRegenEnergyNew = int(rightHandRegenEnergyEntry.get())
        rightHandHasteNew = int(rightHandHasteEntry.get())
        rightHandHitNew = int(rightHandHitEntry.get())
        # rightHandAttack = rightHandAttackEntry.get()
        rightHandMinAttackNew = int(rightHandAttackEntry.get().split('-')[0])
        rightHandMidAttackNew = int(rightHandAttackEntry.get().split('-')[1])
        rightHandMaxAttackNew = int(rightHandAttackEntry.get().split('-')[2])
        # rightHandDMG = rightHandDMGEntry.get()
        rightHandMinDMGNew = int(rightHandDMGEntry.get().split('-')[0])
        rightHandMidDMGNew = int(rightHandDMGEntry.get().split('-')[1])
        rightHandMaxDMGNew = int(rightHandDMGEntry.get().split('-')[2])
        rightHandARPNew = int(rightHandARPEntry.get())
        rightHandHPNew = int(rightHandHPEntry.get())
        rightHandRegenHPNew = int(rightHandRegenHPEntry.get())
        rightHandEvadeNew = int(rightHandEvadeEntry.get())
        rightHandArmorNew = int(rightHandArmorEntry.get())
        rightHandMgicArmorNew = int(rightHandMgicArmorEntry.get())
        rightHandMPNew = int(rightHandMPEntry.get())
        rightHandRegenMPNew = int(rightHandRegenMPEntry.get())
        rightHandSpellPenetrationNew = int(rightHandSpellPenetrationEntry.get())
        rightHandDirectMagicDMGNew = int(rightHandDirectMagicDMGEntry.get())
        rightHandPeriodicMagicDMGNew = int(rightHandPeriodicMagicDMGEntry.get())

        rightHandCharmEnergyNew = int(rightHandCharmEnergyEntry.get())
        rightHandCharmRegenEnergyNew = int(rightHandCharmRegenEnergyEntry.get())
        rightHandCharmHasteNew = int(rightHandCharmHasteEntry.get())
        rightHandCharmHitNew = int(rightHandCharmHitEntry.get())
        rightHandCharmMinAttackNew = int(rightHandCharmAttackEntry.get().split('-')[0])
        rightHandCharmMidAttackNew = int(rightHandCharmAttackEntry.get().split('-')[1])
        rightHandCharmMaxAttackNew = int(rightHandCharmAttackEntry.get().split('-')[2])
        rightHandCharmMinDMGNew = int(rightHandCharmDMGEntry.get().split('-')[0])
        rightHandCharmMidDMGNew = int(rightHandCharmDMGEntry.get().split('-')[1])
        rightHandCharmMaxDMGNew = int(rightHandCharmDMGEntry.get().split('-')[2])
        # rightHandCharmDMGNew = int(rightHandCharmDMGEntry.get())
        rightHandCharmARPNew = int(rightHandCharmARPEntry.get())
        rightHandCharmHPNew = int(rightHandCharmHPEntry.get())
        rightHandCharmRegenHPNew = int(rightHandCharmRegenHPEntry.get())
        rightHandCharmEvadeNew = int(rightHandCharmEvadeEntry.get())
        rightHandCharmArmorNew = int(rightHandCharmArmorEntry.get())
        rightHandCharmMgicArmorNew = int(rightHandCharmMgicArmorEntry.get())
        rightHandCharmMPNew = int(rightHandCharmMPEntry.get())
        rightHandCharmRegenMPNew = int(rightHandCharmRegenMPEntry.get())
        rightHandCharmSpellPenetrationNew = int(rightHandCharmSpellPenetrationEntry.get())
        rightHandCharmDirectMagicDMGNew = int(rightHandCharmDirectMagicDMGEntry.get())
        rightHandCharmPeriodicMagicDMGNew = int(rightHandCharmPeriodicMagicDMGEntry.get())

        leftHandEnergyNew = int(leftHandEnergyEntry.get())
        leftHandRegenEnergyNew = int(leftHandRegenEnergyEntry.get())
        leftHandHasteNew = int(leftHandHasteEntry.get())
        leftHandHitNew = int(leftHandHitEntry.get())
        # leftHandAttackNew = int(leftHandAttackEntry.get())
        leftHandMinAttackNew = int(leftHandAttackEntry.get().split('-')[0])
        leftHandMidAttackNew = int(leftHandAttackEntry.get().split('-')[1])
        leftHandMaxAttackNew = int(leftHandAttackEntry.get().split('-')[2])
        leftHandMinDMGNew = int(leftHandDMGEntry.get().split('-')[0])
        leftHandMidDMGNew = int(leftHandDMGEntry.get().split('-')[1])
        leftHandMaxDMGNew = int(leftHandDMGEntry.get().split('-')[2])
        # leftHandDMGNew = int(leftHandDMGEntry.get())
        leftHandARPNew = int(leftHandARPEntry.get())
        leftHandHPNew = int(leftHandHPEntry.get())
        leftHandRegenHPNew = int(leftHandRegenHPEntry.get())
        leftHandEvadeNew = int(leftHandEvadeEntry.get())
        leftHandArmorNew = int(leftHandArmorEntry.get())
        leftHandMgicArmorNew = int(leftHandMgicArmorEntry.get())
        leftHandMPNew = int(leftHandMPEntry.get())
        leftHandRegenMPNew = int(leftHandRegenMPEntry.get())
        leftHandSpellPenetrationNew = int(leftHandSpellPenetrationEntry.get())
        leftHandDirectMagicDMGNew = int(leftHandDirectMagicDMGEntry.get())
        leftHandPeriodicMagicDMGNew = int(leftHandPeriodicMagicDMGEntry.get())

        leftHandCharmEnergyNew = int(leftHandCharmEnergyEntry.get())
        leftHandCharmRegenEnergyNew = int(leftHandCharmRegenEnergyEntry.get())
        leftHandCharmHasteNew = int(leftHandCharmHasteEntry.get())
        leftHandCharmHitNew = int(leftHandCharmHitEntry.get())
        # leftHandCharmAttackNew = int(leftHandCharmAttackEntry.get())
        leftHandCharmMinAttackNew = int(leftHandCharmAttackEntry.get().split('-')[0])
        leftHandCharmMidAttackNew = int(leftHandCharmAttackEntry.get().split('-')[1])
        leftHandCharmMaxAttackNew = int(leftHandCharmAttackEntry.get().split('-')[2])
        leftHandCharmMinDMGNew = int(leftHandCharmDMGEntry.get().split('-')[0])
        leftHandCharmMidDMGNew = int(leftHandCharmDMGEntry.get().split('-')[1])
        leftHandCharmMaxDMGNew = int(leftHandCharmDMGEntry.get().split('-')[2])
        # leftHandCharmDMGNew = int(leftHandCharmDMGEntry.get())
        leftHandCharmARPNew = int(leftHandCharmARPEntry.get())
        leftHandCharmHPNew = int(leftHandCharmHPEntry.get())
        leftHandCharmRegenHPNew = int(leftHandCharmRegenHPEntry.get())
        leftHandCharmEvadeNew = int(leftHandCharmEvadeEntry.get())
        leftHandCharmArmorNew = int(leftHandCharmArmorEntry.get())
        leftHandCharmMgicArmorNew = int(leftHandCharmMgicArmorEntry.get())
        leftHandCharmMPNew = int(leftHandCharmMPEntry.get())
        leftHandCharmRegenMPNew = int(leftHandCharmRegenMPEntry.get())
        leftHandCharmSpellPenetrationNew = int(leftHandCharmSpellPenetrationEntry.get())
        leftHandCharmDirectMagicDMGNew = int(leftHandCharmDirectMagicDMGEntry.get())
        leftHandCharmPeriodicMagicDMGNew = int(leftHandCharmPeriodicMagicDMGEntry.get())

        ChestEnergyNew = int(ChestEnergyEntry.get())
        ChestRegenEnergyNew = int(ChestRegenEnergyEntry.get())
        ChestHasteNew = int(ChestHasteEntry.get())
        ChestHitNew = int(ChestHitEntry.get())
        # ChestAttackNew = int(ChestAttackEntry.get())
        ChestMinAttackNew = int(ChestAttackEntry.get().split('-')[0])
        ChestMidAttackNew = int(ChestAttackEntry.get().split('-')[1])
        ChestMaxAttackNew = int(ChestAttackEntry.get().split('-')[2])
        ChestMinDMGNew = int(ChestDMGEntry.get().split('-')[0])
        ChestMidDMGNew = int(ChestDMGEntry.get().split('-')[1])
        ChestMaxDMGNew = int(ChestDMGEntry.get().split('-')[2])
        # ChestDMGNew = int(ChestDMGEntry.get())
        ChestARPNew = int(ChestARPEntry.get())
        ChestHPNew = int(ChestHPEntry.get())
        ChestRegenHPNew = int(ChestRegenHPEntry.get())
        ChestEvadeNew = int(ChestEvadeEntry.get())
        ChestArmorNew = int(ChestArmorEntry.get())
        ChestMgicArmorNew = int(ChestMgicArmorEntry.get())
        ChestMPNew = int(ChestMPEntry.get())
        ChestRegenMPNew = int(ChestRegenMPEntry.get())
        ChestSpellPenetrationNew = int(ChestSpellPenetrationEntry.get())
        ChestDirectMagicDMGNew = int(ChestDirectMagicDMGEntry.get())
        ChestPeriodicMagicDMGNew = int(ChestPeriodicMagicDMGEntry.get())

        ChestCharmEnergyNew = int(ChestCharmEnergyEntry.get())
        ChestCharmRegenEnergyNew = int(ChestCharmRegenEnergyEntry.get())
        ChestCharmHasteNew = int(ChestCharmHasteEntry.get())
        ChestCharmHitNew = int(ChestCharmHitEntry.get())
        # ChestCharmAttackNew = int(ChestCharmAttackEntry.get())
        ChestCharmMinAttackNew = int(ChestCharmAttackEntry.get().split('-')[0])
        ChestCharmMidAttackNew = int(ChestCharmAttackEntry.get().split('-')[1])
        ChestCharmMaxAttackNew = int(ChestCharmAttackEntry.get().split('-')[2])
        ChestCharmMinDMGNew = int(ChestCharmDMGEntry.get().split('-')[0])
        ChestCharmMidDMGNew = int(ChestCharmDMGEntry.get().split('-')[1])
        ChestCharmMaxDMGNew = int(ChestCharmDMGEntry.get().split('-')[2])
        # ChestCharmDMGNew = int(ChestCharmDMGEntry.get())
        ChestCharmARPNew = int(ChestCharmARPEntry.get())
        ChestCharmHPNew = int(ChestCharmHPEntry.get())
        ChestCharmRegenHPNew = int(ChestCharmRegenHPEntry.get())
        ChestCharmEvadeNew = int(ChestCharmEvadeEntry.get())
        ChestCharmArmorNew = int(ChestCharmArmorEntry.get())
        ChestCharmMgicArmorNew = int(ChestCharmMgicArmorEntry.get())
        ChestCharmMPNew = int(ChestCharmMPEntry.get())
        ChestCharmRegenMPNew = int(ChestCharmRegenMPEntry.get())
        ChestCharmSpellPenetrationNew = int(ChestCharmSpellPenetrationEntry.get())
        ChestCharmDirectMagicDMGNew = int(ChestCharmDirectMagicDMGEntry.get())
        ChestCharmPeriodicMagicDMGNew = int(ChestCharmPeriodicMagicDMGEntry.get())

        amuletEnergyNew = int(amuletEnergyEntry.get())
        amuletRegenEnergyNew = int(amuletRegenEnergyEntry.get())
        amuletHasteNew = int(amuletHasteEntry.get())
        amuletHitNew = int(amuletHitEntry.get())
        # amuletAttackNew = int(amuletAttackEntry.get())
        amuletMinAttackNew = int(amuletAttackEntry.get().split('-')[0])
        amuletMidAttackNew = int(amuletAttackEntry.get().split('-')[1])
        amuletMaxAttackNew = int(amuletAttackEntry.get().split('-')[2])
        amuletMinDMGNew = int(amuletDMGEntry.get().split('-')[0])
        amuletMidDMGNew = int(amuletDMGEntry.get().split('-')[1])
        amuletMaxDMGNew = int(amuletDMGEntry.get().split('-')[2])
        # amuletDMGNew = int(amuletDMGEntry.get())
        amuletARPNew = int(amuletARPEntry.get())
        amuletHPNew = int(amuletHPEntry.get())
        amuletRegenHPNew = int(amuletRegenHPEntry.get())
        amuletEvadeNew = int(amuletEvadeEntry.get())
        amuletArmorNew = int(amuletArmorEntry.get())
        amuletMgicArmorNew = int(amuletMgicArmorEntry.get())
        amuletMPNew = int(amuletMPEntry.get())
        amuletRegenMPNew = int(amuletRegenMPEntry.get())
        amuletSpellPenetrationNew = int(amuletSpellPenetrationEntry.get())
        amuletDirectMagicDMGNew = int(amuletDirectMagicDMGEntry.get())
        amuletPeriodicMagicDMGNew = int(amuletPeriodicMagicDMGEntry.get())

        amuletCharmEnergyNew = int(amuletCharmEnergyEntry.get())
        amuletCharmRegenEnergyNew = int(amuletCharmRegenEnergyEntry.get())
        amuletCharmHasteNew = int(amuletCharmHasteEntry.get())
        amuletCharmHitNew = int(amuletCharmHitEntry.get())
        # amuletCharmAttackNew = int(amuletCharmAttackEntry.get())
        amuletCharmMinAttackNew = int(amuletCharmAttackEntry.get().split('-')[0])
        amuletCharmMidAttackNew = int(amuletCharmAttackEntry.get().split('-')[1])
        amuletCharmMaxAttackNew = int(amuletCharmAttackEntry.get().split('-')[2])
        amuletCharmMinDMGNew = int(amuletCharmDMGEntry.get().split('-')[0])
        amuletCharmMidDMGNew = int(amuletCharmDMGEntry.get().split('-')[1])
        amuletCharmMaxDMGNew = int(amuletCharmDMGEntry.get().split('-')[2])
        # amuletCharmDMGNew = int(amuletCharmDMGEntry.get())
        amuletCharmARPNew = int(amuletCharmARPEntry.get())
        amuletCharmHPNew = int(amuletCharmHPEntry.get())
        amuletCharmRegenHPNew = int(amuletCharmRegenHPEntry.get())
        amuletCharmEvadeNew = int(amuletCharmEvadeEntry.get())
        amuletCharmArmorNew = int(amuletCharmArmorEntry.get())
        amuletCharmMgicArmorNew = int(amuletCharmMgicArmorEntry.get())
        amuletCharmMPNew = int(amuletCharmMPEntry.get())
        amuletCharmRegenMPNew = int(amuletCharmRegenMPEntry.get())
        amuletCharmSpellPenetrationNew = int(amuletCharmSpellPenetrationEntry.get())
        amuletCharmDirectMagicDMGNew = int(amuletCharmDirectMagicDMGEntry.get())
        amuletCharmPeriodicMagicDMGNew = int(amuletCharmPeriodicMagicDMGEntry.get())

        ringEnergyNew = int(ringEnergyEntry.get())
        ringRegenEnergyNew = int(ringRegenEnergyEntry.get())
        ringHasteNew = int(ringHasteEntry.get())
        ringHitNew = int(ringHitEntry.get())
        # ringAttackNew = int(ringAttackEntry.get())
        ringMinAttackNew = int(ringAttackEntry.get().split('-')[0])
        ringMidAttackNew = int(ringAttackEntry.get().split('-')[1])
        ringMaxAttackNew = int(ringAttackEntry.get().split('-')[2])
        ringMinDMGNew = int(ringDMGEntry.get().split('-')[0])
        ringMidDMGNew = int(ringDMGEntry.get().split('-')[1])
        ringMaxDMGNew = int(ringDMGEntry.get().split('-')[2])
        # ringDMGNew = int(ringDMGEntry.get())
        ringARPNew = int(ringARPEntry.get())
        ringHPNew = int(ringHPEntry.get())
        ringRegenHPNew = int(ringRegenHPEntry.get())
        ringEvadeNew = int(ringEvadeEntry.get())
        ringArmorNew = int(ringArmorEntry.get())
        ringMgicArmorNew = int(ringMgicArmorEntry.get())
        ringMPNew = int(ringMPEntry.get())
        ringRegenMPNew = int(ringRegenMPEntry.get())
        ringSpellPenetrationNew = int(ringSpellPenetrationEntry.get())
        ringDirectMagicDMGNew = int(ringDirectMagicDMGEntry.get())
        ringPeriodicMagicDMGNew = int(ringPeriodicMagicDMGEntry.get())

        ringCharmEnergyNew = int(ringCharmEnergyEntry.get())
        ringCharmRegenEnergyNew = int(ringCharmRegenEnergyEntry.get())
        ringCharmHasteNew = int(ringCharmHasteEntry.get())
        ringCharmHitNew = int(ringCharmHitEntry.get())
        # ringCharmAttackNew = int(ringCharmAttackEntry.get())
        ringCharmMinAttackNew = int(ringCharmAttackEntry.get().split('-')[0])
        ringCharmMidAttackNew = int(ringCharmAttackEntry.get().split('-')[1])
        ringCharmMaxAttackNew = int(ringCharmAttackEntry.get().split('-')[2])
        ringCharmMinDMGNew = int(ringCharmDMGEntry.get().split('-')[0])
        ringCharmMidDMGNew = int(ringCharmDMGEntry.get().split('-')[1])
        ringCharmMaxDMGNew = int(ringCharmDMGEntry.get().split('-')[2])
        # ringCharmDMGNew = int(ringCharmDMGEntry.get())
        ringCharmARPNew = int(ringCharmARPEntry.get())
        ringCharmHPNew = int(ringCharmHPEntry.get())
        ringCharmRegenHPNew = int(ringCharmRegenHPEntry.get())
        ringCharmEvadeNew = int(ringCharmEvadeEntry.get())
        ringCharmArmorNew = int(ringCharmArmorEntry.get())
        ringCharmMgicArmorNew = int(ringCharmMgicArmorEntry.get())
        ringCharmMPNew = int(ringCharmMPEntry.get())
        ringCharmRegenMPNew = int(ringCharmRegenMPEntry.get())
        ringCharmSpellPenetrationNew = int(ringCharmSpellPenetrationEntry.get())
        ringCharmDirectMagicDMGNew = int(ringCharmDirectMagicDMGEntry.get())
        ringCharmPeriodicMagicDMGNew = int(ringCharmPeriodicMagicDMGEntry.get())

        bookEnergyNew = int(bookEnergyEntry.get())
        bookRegenEnergyNew = int(bookRegenEnergyEntry.get())
        bookHasteNew = int(bookHasteEntry.get())
        bookHitNew = int(bookHitEntry.get())
        # bookAttackNew = int(bookAttackEntry.get())
        bookMinAttackNew = int(bookAttackEntry.get().split('-')[0])
        bookMidAttackNew = int(bookAttackEntry.get().split('-')[1])
        bookMaxAttackNew = int(bookAttackEntry.get().split('-')[2])
        bookMinDMGNew = int(bookDMGEntry.get().split('-')[0])
        bookMidDMGNew = int(bookDMGEntry.get().split('-')[1])
        bookMaxDMGNew = int(bookDMGEntry.get().split('-')[2])
        # bookDMGNew = int(bookDMGEntry.get())
        bookARPNew = int(bookARPEntry.get())
        bookHPNew = int(bookHPEntry.get())
        bookRegenHPNew = int(bookRegenHPEntry.get())
        bookEvadeNew = int(bookEvadeEntry.get())
        bookArmorNew = int(bookArmorEntry.get())
        bookMgicArmorNew = int(bookMgicArmorEntry.get())
        bookMPNew = int(bookMPEntry.get())
        bookRegenMPNew = int(bookRegenMPEntry.get())
        bookSpellPenetrationNew = int(bookSpellPenetrationEntry.get())
        bookDirectMagicDMGNew = int(bookDirectMagicDMGEntry.get())
        bookPeriodicMagicDMGNew = int(bookPeriodicMagicDMGEntry.get())

        bookCharmEnergyNew = int(bookCharmEnergyEntry.get())
        bookCharmRegenEnergyNew = int(bookCharmRegenEnergyEntry.get())
        bookCharmHasteNew = int(bookCharmHasteEntry.get())
        bookCharmHitNew = int(bookCharmHitEntry.get())
        # bookCharmAttackNew = int(bookCharmAttackEntry.get())
        bookCharmMinAttackNew = int(bookCharmAttackEntry.get().split('-')[0])
        bookCharmMidAttackNew = int(bookCharmAttackEntry.get().split('-')[1])
        bookCharmMaxAttackNew = int(bookCharmAttackEntry.get().split('-')[2])
        bookCharmMinDMGNew = int(bookCharmDMGEntry.get().split('-')[0])
        bookCharmMidDMGNew = int(bookCharmDMGEntry.get().split('-')[1])
        bookCharmMaxDMGNew = int(bookCharmDMGEntry.get().split('-')[2])
        # bookCharmDMGNew = int(bookCharmDMGEntry.get())
        bookCharmARPNew = int(bookCharmARPEntry.get())
        bookCharmHPNew = int(bookCharmHPEntry.get())
        bookCharmRegenHPNew = int(bookCharmRegenHPEntry.get())
        bookCharmEvadeNew = int(bookCharmEvadeEntry.get())
        bookCharmArmorNew = int(bookCharmArmorEntry.get())
        bookCharmMgicArmorNew = int(bookCharmMgicArmorEntry.get())
        bookCharmMPNew = int(bookCharmMPEntry.get())
        bookCharmRegenMPNew = int(bookCharmRegenMPEntry.get())
        bookCharmSpellPenetrationNew = int(bookCharmSpellPenetrationEntry.get())
        bookCharmDirectMagicDMGNew = int(bookCharmDirectMagicDMGEntry.get())
        bookCharmPeriodicMagicDMGNew = int(bookCharmPeriodicMagicDMGEntry.get())

        staticEnergy += rightHandEnergyNew-rightHandEnergy+rightHandCharmEnergyNew-rightHandCharmEnergy+leftHandEnergyNew-leftHandEnergy+leftHandCharmEnergyNew-leftHandCharmEnergy+ChestEnergyNew-ChestEnergy+ChestCharmEnergyNew-ChestCharmEnergy+amuletEnergyNew-amuletEnergy+amuletCharmEnergyNew-amuletCharmEnergy+ringEnergyNew-ringEnergy+ringCharmEnergyNew-ringCharmEnergy+bookEnergyNew-bookEnergy+bookCharmEnergyNew-bookCharmEnergy

        staticRegenEnergy += rightHandRegenEnergyNew-rightHandRegenEnergy+rightHandCharmRegenEnergyNew-rightHandCharmRegenEnergy+leftHandRegenEnergyNew-leftHandRegenEnergy+leftHandCharmRegenEnergyNew-leftHandCharmRegenEnergy+ChestRegenEnergyNew-ChestRegenEnergy+ChestCharmRegenEnergyNew-ChestCharmRegenEnergy+amuletRegenEnergyNew-amuletRegenEnergy+amuletCharmRegenEnergyNew-amuletCharmRegenEnergy+ringRegenEnergyNew-ringRegenEnergy+ringCharmRegenEnergyNew-ringCharmRegenEnergy+bookRegenEnergyNew-bookRegenEnergy+bookCharmRegenEnergyNew-bookCharmRegenEnergy

        staticHaste += rightHandHasteNew-rightHandHaste+rightHandCharmHasteNew-rightHandCharmHaste+leftHandHasteNew-leftHandHaste+leftHandCharmHasteNew-leftHandCharmHaste+ChestHasteNew-ChestHaste+ChestCharmHasteNew-ChestCharmHaste+amuletHasteNew-amuletHaste+amuletCharmHasteNew-amuletCharmHaste+ringHasteNew-ringHaste+ringCharmHasteNew-ringCharmHaste+bookHasteNew-bookHaste+bookCharmHasteNew-bookCharmHaste

        staticHit += rightHandHitNew-rightHandHit+rightHandCharmHitNew-rightHandCharmHit+leftHandHitNew-leftHandHit+leftHandCharmHitNew-leftHandCharmHit+ChestHitNew-ChestHit+ChestCharmHitNew-ChestCharmHit+amuletHitNew-amuletHit+amuletCharmHitNew-amuletCharmHit+ringHitNew-ringHit+ringCharmHitNew-ringCharmHit+bookHitNew-bookHit+bookCharmHitNew-bookCharmHit

        staticARP += rightHandARPNew-rightHandARP+rightHandCharmARPNew-rightHandCharmARP+leftHandARPNew-leftHandARP+leftHandCharmARPNew-leftHandCharmARP+ChestARPNew-ChestARP+ChestCharmARPNew-ChestCharmARP+amuletARPNew-amuletARP+amuletCharmARPNew-amuletCharmARP+ringARPNew-ringARP+ringCharmARPNew-ringCharmARP+bookARPNew-bookARP+bookCharmARPNew-bookCharmARP

        staticHP += rightHandHPNew-rightHandHP+rightHandCharmHPNew-rightHandCharmHP+leftHandHPNew-leftHandHP+leftHandCharmHPNew-leftHandCharmHP+ChestHPNew-ChestHP+ChestCharmHPNew-ChestCharmHP+amuletHPNew-amuletHP+amuletCharmHPNew-amuletCharmHP+ringHPNew-ringHP+ringCharmHPNew-ringCharmHP+bookHPNew-bookHP+bookCharmHPNew-bookCharmHP

        staticRegenHP += rightHandRegenHPNew-rightHandRegenHP+rightHandCharmRegenHPNew-rightHandCharmRegenHP+leftHandRegenHPNew-leftHandRegenHP+leftHandCharmRegenHPNew-leftHandCharmRegenHP+ChestRegenHPNew-ChestRegenHP+ChestCharmRegenHPNew-ChestCharmRegenHP+amuletRegenHPNew-amuletRegenHP+amuletCharmRegenHPNew-amuletCharmRegenHP+ringRegenHPNew-ringRegenHP+ringCharmRegenHPNew-ringCharmRegenHP+bookRegenHPNew-bookRegenHP+bookCharmRegenHPNew-bookCharmRegenHP

        staticEvade += rightHandEvadeNew-rightHandEvade+rightHandCharmEvadeNew-rightHandCharmEvade+leftHandEvadeNew-leftHandEvade+leftHandCharmEvadeNew-leftHandCharmEvade+ChestEvadeNew-ChestEvade+ChestCharmEvadeNew-ChestCharmEvade+amuletEvadeNew-amuletEvade+amuletCharmEvadeNew-amuletCharmEvade+ringEvadeNew-ringEvade+ringCharmEvadeNew-ringCharmEvade+bookEvadeNew-bookEvade+bookCharmEvadeNew-bookCharmEvade

        staticArmor += rightHandArmorNew-rightHandArmor+rightHandCharmArmorNew-rightHandCharmArmor+leftHandArmorNew-leftHandArmor+leftHandCharmArmorNew-leftHandCharmArmor+ChestArmorNew-ChestArmor+ChestCharmArmorNew-ChestCharmArmor+amuletArmorNew-amuletArmor+amuletCharmArmorNew-amuletCharmArmor+ringArmorNew-ringArmor+ringCharmArmorNew-ringCharmArmor+bookArmorNew-bookArmor+bookCharmArmorNew-bookCharmArmor

        staticMgicArmor += rightHandMgicArmorNew-rightHandMgicArmor+rightHandCharmMgicArmorNew-rightHandCharmMgicArmor+leftHandMgicArmorNew-leftHandMgicArmor+leftHandCharmMgicArmorNew-leftHandCharmMgicArmor+ChestMgicArmorNew-ChestMgicArmor+ChestCharmMgicArmorNew-ChestCharmMgicArmor+amuletMgicArmorNew-amuletMgicArmor+amuletCharmMgicArmorNew-amuletCharmMgicArmor+ringMgicArmorNew-ringMgicArmor+ringCharmMgicArmorNew-ringCharmMgicArmor+bookMgicArmorNew-bookMgicArmor+bookCharmMgicArmorNew-bookCharmMgicArmor

        staticMP += rightHandMPNew-rightHandMP+rightHandCharmMPNew-rightHandCharmMP+leftHandMPNew-leftHandMP+leftHandCharmMPNew-leftHandCharmMP+ChestMPNew-ChestMP+ChestCharmMPNew-ChestCharmMP+amuletMPNew-amuletMP+amuletCharmMPNew-amuletCharmMP+ringMPNew-ringMP+ringCharmMPNew-ringCharmMP+bookMPNew-bookMP+bookCharmMPNew-bookCharmMP

        staticRegenMP += rightHandRegenMPNew-rightHandRegenMP+rightHandCharmRegenMPNew-rightHandCharmRegenMP+leftHandRegenMPNew-leftHandRegenMP+leftHandCharmRegenMPNew-leftHandCharmRegenMP+ChestRegenMPNew-ChestRegenMP+ChestCharmRegenMPNew-ChestCharmRegenMP+amuletRegenMPNew-amuletRegenMP+amuletCharmRegenMPNew-amuletCharmRegenMP+ringRegenMPNew-ringRegenMP+ringCharmRegenMPNew-ringCharmRegenMP+bookRegenMPNew-bookRegenMP+bookCharmRegenMPNew-bookCharmRegenMP

        staticSpellPenetration += rightHandSpellPenetrationNew-rightHandSpellPenetration+rightHandCharmSpellPenetrationNew-rightHandCharmSpellPenetration+leftHandSpellPenetrationNew-leftHandSpellPenetration+leftHandCharmSpellPenetrationNew-leftHandCharmSpellPenetration+ChestSpellPenetrationNew-ChestSpellPenetration+ChestCharmSpellPenetrationNew-ChestCharmSpellPenetration+amuletSpellPenetrationNew-amuletSpellPenetration+amuletCharmSpellPenetrationNew-amuletCharmSpellPenetration+ringSpellPenetrationNew-ringSpellPenetration+ringCharmSpellPenetrationNew-ringCharmSpellPenetration+bookSpellPenetrationNew-bookSpellPenetration+bookCharmSpellPenetrationNew-bookCharmSpellPenetration

        staticDirectMagicDMG += rightHandDirectMagicDMGNew-rightHandDirectMagicDMG+rightHandCharmDirectMagicDMGNew-rightHandCharmDirectMagicDMG+leftHandDirectMagicDMGNew-leftHandDirectMagicDMG+leftHandCharmDirectMagicDMGNew-leftHandCharmDirectMagicDMG+ChestDirectMagicDMGNew-ChestDirectMagicDMG+ChestCharmDirectMagicDMGNew-ChestCharmDirectMagicDMG+amuletDirectMagicDMGNew-amuletDirectMagicDMG+amuletCharmDirectMagicDMGNew-amuletCharmDirectMagicDMG+ringDirectMagicDMGNew-ringDirectMagicDMG+ringCharmDirectMagicDMGNew-ringCharmDirectMagicDMG+bookDirectMagicDMGNew-bookDirectMagicDMG+bookCharmDirectMagicDMGNew-bookCharmDirectMagicDMG

        staticPeriodicMagicDMG += rightHandPeriodicMagicDMGNew-rightHandPeriodicMagicDMG+rightHandCharmPeriodicMagicDMGNew-rightHandCharmPeriodicMagicDMG+leftHandPeriodicMagicDMGNew-leftHandPeriodicMagicDMG+leftHandCharmPeriodicMagicDMGNew-leftHandCharmPeriodicMagicDMG+ChestPeriodicMagicDMGNew-ChestPeriodicMagicDMG+ChestCharmPeriodicMagicDMGNew-ChestCharmPeriodicMagicDMG+amuletPeriodicMagicDMGNew-amuletPeriodicMagicDMG+amuletCharmPeriodicMagicDMGNew-amuletCharmPeriodicMagicDMG+ringPeriodicMagicDMGNew-ringPeriodicMagicDMG+ringCharmPeriodicMagicDMGNew-ringCharmPeriodicMagicDMG+bookPeriodicMagicDMGNew-bookPeriodicMagicDMG+bookCharmPeriodicMagicDMGNew-bookCharmPeriodicMagicDMG

        rightHandEnergy = rightHandEnergyNew
        rightHandRegenEnergy = rightHandRegenEnergyNew
        rightHandHaste = rightHandHasteNew
        rightHandHit = rightHandHitNew
        # rightHandAttack = rightHandAttackNew
        # rightHandMinAttack = rightHandMinAttackNew
        # rightHandMidAttack = rightHandMidAttackNew
        # rightHandMaxAttack = rightHandMaxAttackNew
        # rightHandMinDMG = rightHandMinDMGNew
        # rightHandMidDMG = rightHandMidDMGNew
        # rightHandMaxDMG = rightHandMaxDMGNew
        # rightHandDMG = rightHandDMGNew
        rightHandARP = rightHandARPNew
        rightHandHP = rightHandHPNew
        rightHandRegenHP = rightHandRegenHPNew
        rightHandEvade = rightHandEvadeNew
        rightHandArmor = rightHandArmorNew
        rightHandMgicArmor = rightHandMgicArmorNew
        rightHandMP = rightHandMPNew
        rightHandRegenMP = rightHandRegenMPNew
        rightHandSpellPenetration = rightHandSpellPenetrationNew
        rightHandDirectMagicDMG = rightHandDirectMagicDMGNew
        rightHandPeriodicMagicDMG = rightHandPeriodicMagicDMGNew

        rightHandCharmEnergy = rightHandCharmEnergyNew
        rightHandCharmRegenEnergy = rightHandCharmRegenEnergyNew
        rightHandCharmHaste = rightHandCharmHasteNew
        rightHandCharmHit = rightHandCharmHitNew
        # rightHandCharmAttack = rightHandCharmAttackNew
        # rightHandCharmMinAttack = rightHandCharmMinAttackNew
        # rightHandCharmMidAttack = rightHandCharmMidAttackNew
        # rightHandCharmMaxAttack = rightHandCharmMaxAttackNew
        # rightHandCharmMinDMG = rightHandCharmMinDMGNew
        # rightHandCharmMidDMG = rightHandCharmMidDMGNew
        # rightHandCharmMaxDMG = rightHandCharmMaxDMGNew
        # rightHandCharmDMG = rightHandCharmDMGNew
        rightHandCharmARP = rightHandCharmARPNew
        rightHandCharmHP = rightHandCharmHPNew
        rightHandCharmRegenHP = rightHandCharmRegenHPNew
        rightHandCharmEvade = rightHandCharmEvadeNew
        rightHandCharmArmor = rightHandCharmArmorNew
        rightHandCharmMgicArmor = rightHandCharmMgicArmorNew
        rightHandCharmMP = rightHandCharmMPNew
        rightHandCharmRegenMP = rightHandCharmRegenMPNew
        rightHandCharmSpellPenetration = rightHandCharmSpellPenetrationNew
        rightHandCharmDirectMagicDMG = rightHandCharmDirectMagicDMGNew
        rightHandCharmPeriodicMagicDMG = rightHandCharmPeriodicMagicDMGNew

        leftHandEnergy = leftHandEnergyNew
        leftHandRegenEnergy = leftHandRegenEnergyNew
        leftHandHaste = leftHandHasteNew
        leftHandHit = leftHandHitNew
        # leftHandAttack = leftHandAttackNew
        # leftHandMinAttack = leftHandMinAttackNew
        # leftHandMidAttack = leftHandMidAttackNew
        # leftHandMaxAttack = leftHandMaxAttackNew
        # leftHandMinDMG = leftHandMinDMGNew
        # leftHandMidDMG = leftHandMidDMGNew
        # leftHandMaxDMG = leftHandMaxDMGNew
        # leftHandDMG = leftHandDMGNew
        leftHandARP = leftHandARPNew
        leftHandHP = leftHandHPNew
        leftHandRegenHP = leftHandRegenHPNew
        leftHandEvade = leftHandEvadeNew
        leftHandArmor = leftHandArmorNew
        leftHandMgicArmor = leftHandMgicArmorNew
        leftHandMP = leftHandMPNew
        leftHandRegenMP = leftHandRegenMPNew
        leftHandSpellPenetration = leftHandSpellPenetrationNew
        leftHandDirectMagicDMG = leftHandDirectMagicDMGNew
        leftHandPeriodicMagicDMG = leftHandPeriodicMagicDMGNew

        leftHandCharmEnergy = leftHandCharmEnergyNew
        leftHandCharmRegenEnergy = leftHandCharmRegenEnergyNew
        leftHandCharmHaste = leftHandCharmHasteNew
        leftHandCharmHit = leftHandCharmHitNew
        # leftHandCharmAttack = leftHandCharmAttackNew
        # leftHandCharmMinAttack = leftHandCharmMinAttackNew
        # leftHandCharmMidAttack = leftHandCharmMidAttackNew
        # leftHandCharmMaxAttack = leftHandCharmMaxAttackNew
        # leftHandCharmMinDMG = leftHandCharmMinDMGNew
        # leftHandCharmMidDMG = leftHandCharmMidDMGNew
        # leftHandCharmMaxDMG = leftHandCharmMaxDMGNew
        # leftHandCharmDMG = leftHandCharmDMGNew
        leftHandCharmARP = leftHandCharmARPNew
        leftHandCharmHP = leftHandCharmHPNew
        leftHandCharmRegenHP = leftHandCharmRegenHPNew
        leftHandCharmEvade = leftHandCharmEvadeNew
        leftHandCharmArmor = leftHandCharmArmorNew
        leftHandCharmMgicArmor = leftHandCharmMgicArmorNew
        leftHandCharmMP = leftHandCharmMPNew
        leftHandCharmRegenMP = leftHandCharmRegenMPNew
        leftHandCharmSpellPenetration = leftHandCharmSpellPenetrationNew
        leftHandCharmDirectMagicDMG = leftHandCharmDirectMagicDMGNew
        leftHandCharmPeriodicMagicDMG = leftHandCharmPeriodicMagicDMGNew

        ChestEnergy = ChestEnergyNew
        ChestRegenEnergy = ChestRegenEnergyNew
        ChestHaste = ChestHasteNew
        ChestHit = ChestHitNew
        # ChestAttack = ChestAttackNew
        # ChestMinAttack = ChestMinAttackNew
        # ChestMidAttack = ChestMidAttackNew
        # ChestMaxAttack = ChestMaxAttackNew
        # ChestMinDMG = ChestMinDMGNew
        # ChestMidDMG = ChestMidDMGNew
        # ChestMaxDMG = ChestMaxDMGNew
        # ChestDMG = ChestDMGNew
        ChestARP = ChestARPNew
        ChestHP = ChestHPNew
        ChestRegenHP = ChestRegenHPNew
        ChestEvade = ChestEvadeNew
        ChestArmor = ChestArmorNew
        ChestMgicArmor = ChestMgicArmorNew
        ChestMP = ChestMPNew
        ChestRegenMP = ChestRegenMPNew
        ChestSpellPenetration = ChestSpellPenetrationNew
        ChestDirectMagicDMG = ChestDirectMagicDMGNew
        ChestPeriodicMagicDMG = ChestPeriodicMagicDMGNew

        ChestCharmEnergy = ChestCharmEnergyNew
        ChestCharmRegenEnergy = ChestCharmRegenEnergyNew
        ChestCharmHaste = ChestCharmHasteNew
        ChestCharmHit = ChestCharmHitNew
        # ChestCharmAttack = ChestCharmAttackNew
        # ChestCharmMinAttack = ChestCharmMinAttackNew
        # ChestCharmMidAttack = ChestCharmMidAttackNew
        # ChestCharmMaxAttack = ChestCharmMaxAttackNew
        # ChestCharmMinDMG = ChestCharmMinDMGNew
        # ChestCharmMidDMG = ChestCharmMidDMGNew
        # ChestCharmMaxDMG = ChestCharmMaxDMGNew
        # ChestCharmDMG = ChestCharmDMGNew
        ChestCharmARP = ChestCharmARPNew
        ChestCharmHP = ChestCharmHPNew
        ChestCharmRegenHP = ChestCharmRegenHPNew
        ChestCharmEvade = ChestCharmEvadeNew
        ChestCharmArmor = ChestCharmArmorNew
        ChestCharmMgicArmor = ChestCharmMgicArmorNew
        ChestCharmMP = ChestCharmMPNew
        ChestCharmRegenMP = ChestCharmRegenMPNew
        ChestCharmSpellPenetration = ChestCharmSpellPenetrationNew
        ChestCharmDirectMagicDMG = ChestCharmDirectMagicDMGNew
        ChestCharmPeriodicMagicDMG = ChestCharmPeriodicMagicDMGNew

        amuletEnergy = amuletEnergyNew
        amuletRegenEnergy = amuletRegenEnergyNew
        amuletHaste = amuletHasteNew
        amuletHit = amuletHitNew
        # amuletAttack = amuletAttackNew
        # amuletMinAttack = amuletMinAttackNew
        # amuletMidAttack = amuletMidAttackNew
        # amuletMaxAttack = amuletMaxAttackNew
        # amuletMinDMG = amuletMinDMGNew
        # amuletMidDMG = amuletMidDMGNew
        # amuletMaxDMG = amuletMaxDMGNew
        # amuletDMG = amuletDMGNew
        amuletARP = amuletARPNew
        amuletHP = amuletHPNew
        amuletRegenHP = amuletRegenHPNew
        amuletEvade = amuletEvadeNew
        amuletArmor = amuletArmorNew
        amuletMgicArmor = amuletMgicArmorNew
        amuletMP = amuletMPNew
        amuletRegenMP = amuletRegenMPNew
        amuletSpellPenetration = amuletSpellPenetrationNew
        amuletDirectMagicDMG = amuletDirectMagicDMGNew
        amuletPeriodicMagicDMG = amuletPeriodicMagicDMGNew

        amuletCharmEnergy = amuletCharmEnergyNew
        amuletCharmRegenEnergy = amuletCharmRegenEnergyNew
        amuletCharmHaste = amuletCharmHasteNew
        amuletCharmHit = amuletCharmHitNew
        # amuletCharmAttack = amuletCharmAttackNew
        # amuletCharmMinAttack = amuletCharmMinAttackNew
        # amuletCharmMidAttack = amuletCharmMidAttackNew
        # amuletCharmMaxAttack = amuletCharmMaxAttackNew
        # amuletCharmMinDMG = amuletCharmMinDMGNew
        # amuletCharmMidDMG = amuletCharmMidDMGNew
        # amuletCharmMaxDMG = amuletCharmMaxDMGNew
        # amuletCharmDMG = amuletCharmDMGNew
        amuletCharmARP = amuletCharmARPNew
        amuletCharmHP = amuletCharmHPNew
        amuletCharmRegenHP = amuletCharmRegenHPNew
        amuletCharmEvade = amuletCharmEvadeNew
        amuletCharmArmor = amuletCharmArmorNew
        amuletCharmMgicArmor = amuletCharmMgicArmorNew
        amuletCharmMP = amuletCharmMPNew
        amuletCharmRegenMP = amuletCharmRegenMPNew
        amuletCharmSpellPenetration = amuletCharmSpellPenetrationNew
        amuletCharmDirectMagicDMG = amuletCharmDirectMagicDMGNew
        amuletCharmPeriodicMagicDMG = amuletCharmPeriodicMagicDMGNew

        ringEnergy = ringEnergyNew
        ringRegenEnergy = ringRegenEnergyNew
        ringHaste = ringHasteNew
        ringHit = ringHitNew
        # ringAttack = ringAttackNew
        # ringMinAttack = ringMinAttackNew
        # ringMidAttack = ringMidAttackNew
        # ringMaxAttack = ringMaxAttackNew
        # ringMinDMG = ringMinDMGNew
        # ringMidDMG = ringMidDMGNew
        # ringMaxDMG = ringMaxDMGNew
        # ringDMG = ringDMGNew
        ringARP = ringARPNew
        ringHP = ringHPNew
        ringRegenHP = ringRegenHPNew
        ringEvade = ringEvadeNew
        ringArmor = ringArmorNew
        ringMgicArmor = ringMgicArmorNew
        ringMP = ringMPNew
        ringRegenMP = ringRegenMPNew
        ringSpellPenetration = ringSpellPenetrationNew
        ringDirectMagicDMG = ringDirectMagicDMGNew
        ringPeriodicMagicDMG = ringPeriodicMagicDMGNew

        ringCharmEnergy = ringCharmEnergyNew
        ringCharmRegenEnergy = ringCharmRegenEnergyNew
        ringCharmHaste = ringCharmHasteNew
        ringCharmHit = ringCharmHitNew
        # ringCharmAttack = ringCharmAttackNew
        # ringCharmMinAttack = ringCharmMinAttackNew
        # ringCharmMidAttack = ringCharmMidAttackNew
        # ringCharmMaxAttack = ringCharmMaxAttackNew
        # ringCharmMinDMG = ringCharmMinDMGNew
        # ringCharmMidDMG = ringCharmMidDMGNew
        # ringCharmMaxDMG = ringCharmMaxDMGNew
        # ringCharmDMG = ringCharmDMGNew
        ringCharmARP = ringCharmARPNew
        ringCharmHP = ringCharmHPNew
        ringCharmRegenHP = ringCharmRegenHPNew
        ringCharmEvade = ringCharmEvadeNew
        ringCharmArmor = ringCharmArmorNew
        ringCharmMgicArmor = ringCharmMgicArmorNew
        ringCharmMP = ringCharmMPNew
        ringCharmRegenMP = ringCharmRegenMPNew
        ringCharmSpellPenetration = ringCharmSpellPenetrationNew
        ringCharmDirectMagicDMG = ringCharmDirectMagicDMGNew
        ringCharmPeriodicMagicDMG = ringCharmPeriodicMagicDMGNew

        bookEnergy = bookEnergyNew
        bookRegenEnergy = bookRegenEnergyNew
        bookHaste = bookHasteNew
        bookHit = bookHitNew
        # bookAttack = bookAttackNew
        # bookMinAttack = bookMinAttackNew
        # bookMidAttack = bookMidAttackNew
        # bookMaxAttack = bookMaxAttackNew
        # bookMinDMG = bookMinDMGNew
        # bookMidDMG = bookMidDMGNew
        # bookMaxDMG = bookMaxDMGNew
        # bookDMG = bookDMGNew
        bookARP = bookARPNew
        bookHP = bookHPNew
        bookRegenHP = bookRegenHPNew
        bookEvade = bookEvadeNew
        bookArmor = bookArmorNew
        bookMgicArmor = bookMgicArmorNew
        bookMP = bookMPNew
        bookRegenMP = bookRegenMPNew
        bookSpellPenetration = bookSpellPenetrationNew
        bookDirectMagicDMG = bookDirectMagicDMGNew
        bookPeriodicMagicDMG = bookPeriodicMagicDMGNew

        bookCharmEnergy = bookCharmEnergyNew
        bookCharmRegenEnergy = bookCharmRegenEnergyNew
        bookCharmHaste = bookCharmHasteNew
        bookCharmHit = bookCharmHitNew
        # bookCharmAttack = bookCharmAttackNew
        # bookCharmMinAttack = bookCharmMinAttackNew
        # bookCharmMidAttack = bookCharmMidAttackNew
        # bookCharmMaxAttack = bookCharmMaxAttackNew
        # bookCharmMinDMG = bookCharmMinDMGNew
        # bookCharmMidDMG = bookCharmMidDMGNew
        # bookCharmMaxDMG = bookCharmMaxDMGNew
        # bookCharmDMG = bookCharmDMGNew
        bookCharmARP = bookCharmARPNew
        bookCharmHP = bookCharmHPNew
        bookCharmRegenHP = bookCharmRegenHPNew
        bookCharmEvade = bookCharmEvadeNew
        bookCharmArmor = bookCharmArmorNew
        bookCharmMgicArmor = bookCharmMgicArmorNew
        bookCharmMP = bookCharmMPNew
        bookCharmRegenMP = bookCharmRegenMPNew
        bookCharmSpellPenetration = bookCharmSpellPenetrationNew
        bookCharmDirectMagicDMG = bookCharmDirectMagicDMGNew
        bookCharmPeriodicMagicDMG = bookCharmPeriodicMagicDMGNew

        staticEnergyLabel.config(text = '{0}'.format(staticEnergy))
        staticRegenEnergyLabel.config(text = '{0}'.format(staticRegenEnergy))
        staticHasteLabel.config(text = '{0}'.format(staticHaste))
        staticHitLabel.config(text = '{0}'.format(staticHit))
        staticARPLabel.config(text = '{0}'.format(staticARP))
        staticHPLabel.config(text = '{0}'.format(staticHP))
        staticRegenHPLabel.config(text = '{0}'.format(staticRegenHP))
        staticEvadeLabel.config(text = '{0}'.format(staticEvade))
        staticArmorLabel.config(text = '{0}'.format(staticArmor))
        staticMgicArmorLabel.config(text = '{0}'.format(staticMgicArmor))
        staticMPLabel.config(text = '{0}'.format(staticMP))
        staticRegenMPLabel.config(text = '{0}'.format(staticRegenMP))
        staticSpellPenetrationLabel.config(text = '{0}'.format(staticSpellPenetration))
        staticDirectMagicDMGLabel.config(text = '{0}'.format(staticDirectMagicDMG))
        staticPeriodicMagicDMGLabel.config(text = '{0}'.format(staticPeriodicMagicDMG))

        sum_stats(1)

        staticAttackMin = int(staticAttack.split('-')[0])
        staticAttackMid = int(staticAttack.split('-')[1])
        staticAttackMax = int(staticAttack.split('-')[2])
        staticAttack = staticAttack = '{0}-{1}-{2}'.format(staticAttackMin+rightHandMinAttackNew-rightHandMinAttack,staticAttackMid+rightHandMidAttackNew-rightHandMidAttack,staticAttackMax+rightHandMaxAttackNew-rightHandMaxAttack)
        totalAttack = '{0}-{1}-{2}'.format(int(staticAttack.split('-')[0])-int(changeAttack.split('-')[0]),int(staticAttack.split('-')[1])-int(changeAttack.split('-')[1]),int(staticAttack.split('-')[2])-int(changeAttack.split('-')[2]))
        staticAttackLabel.config(text = '{0}'.format(staticAttack))
        totalAttackLabel.config(text = '{0}'.format(totalAttack))

        rightHandMinAttack = rightHandMinAttackNew
        rightHandMidAttack = rightHandMidAttackNew
        rightHandMaxAttack = rightHandMaxAttackNew

        staticDMGMin = int(staticDMG.split('-')[0])
        staticDMGMid = int(staticDMG.split('-')[1])
        staticDMGMax = int(staticDMG.split('-')[2])
        staticDMG = '{0}-{1}-{2}'.format(staticDMGMin+rightHandMinDMGNew-rightHandMinDMG,staticDMGMid+rightHandMidDMGNew-rightHandMidDMG,staticDMGMax+rightHandMaxDMGNew-rightHandMaxDMG)
        totalDMG = '{0}-{1}-{2}'.format(int(staticDMG.split('-')[0])-int(changeDMG.split('-')[0]),int(staticDMG.split('-')[1])-int(changeDMG.split('-')[1]),int(staticDMG.split('-')[2])-int(changeDMG.split('-')[2]))
        staticDMGLabel.config(text = '{0}'.format(staticDMG))
        totalDMGLabel.config(text = '{0}'.format(totalDMG))

        rightHandMinDMG = rightHandMinDMGNew
        rightHandMidDMG = rightHandMidDMGNew
        rightHandMaxDMG = rightHandMaxDMGNew

    ChoInv = Toplevel(window)
    ChoInv.title('Инвентарь')
    ChoInv.resizable(width=False, height=False)
    ChoInv.rowconfigure(0, pad=3)
    ChoInv.rowconfigure(1, pad=3)
    ChoInv.rowconfigure(2, pad=3)
    ChoInv.rowconfigure(3, pad=3)
    ChoInv.rowconfigure(4, pad=3)
    ChoInv.rowconfigure(5, pad=3)
    ChoInv.rowconfigure(6, pad=3)
    ChoInv.rowconfigure(7, pad=3)
    ChoInv.rowconfigure(8, pad=3)
    ChoInv.rowconfigure(9, pad=3)
    ChoInv.rowconfigure(10, pad=3)
    ChoInv.rowconfigure(11, pad=3)
    ChoInv.rowconfigure(12, pad=3)
    ChoInv.rowconfigure(13, pad=3)
    ChoInv.rowconfigure(14, pad=3)
    ChoInv.rowconfigure(15, pad=3)
    ChoInv.rowconfigure(16, pad=3)
    ChoInv.rowconfigure(17, pad=3)
    ChoInv.columnconfigure(0, pad=3)
    ChoInv.columnconfigure(1, pad=3)
    ChoInv.columnconfigure(2, pad=3)
    ChoInv.columnconfigure(3, pad=3)
    ChoInv.columnconfigure(4, pad=3)
    ChoInv.columnconfigure(5, pad=3)
    ChoInv.columnconfigure(6, pad=3)
    ChoInv.columnconfigure(7, pad=3)
    ChoInv.columnconfigure(8, pad=3)
    ChoInv.columnconfigure(9, pad=3)
    ChoInv.columnconfigure(10, pad=3)
    ChoInv.columnconfigure(11, pad=3)
    ChoInv.columnconfigure(12, pad=3)
    ChoInv.columnconfigure(13, pad=3)
    ChoInv.columnconfigure(14, pad=3)
    ChoInv.columnconfigure(15, pad=3)
    ChoInv.columnconfigure(16, pad=3)
    ChoInv.columnconfigure(17, pad=3)
    ChoInv.columnconfigure(18, pad=3)
    ChoInv.columnconfigure(19, pad=3)

    Label(ChoInv, text = 'Слот').grid(row=0, column=0)
    create_labels(ChoInv,1,parametrList,0)

    slotLabels = ['Правая рука',
                    'Чары',
                    'Левая рука',
                    'Чары',
                    'Броня',
                    'Чары',
                    'Амулет',
                    'Чары',
                    'Кольцо',
                    'Чары',
                    'Книга магии',
                    'Чары'
    ]

    create_labels(ChoInv,1,slotLabels,1)

    rightHandEnergyEntry = Entry(ChoInv,width=8)
    rightHandRegenEnergyEntry = Entry(ChoInv,width=8)
    rightHandHasteEntry = Entry(ChoInv,width=8)
    rightHandHitEntry = Entry(ChoInv,width=8)
    rightHandAttackEntry = Entry(ChoInv,width=8)
    rightHandDMGEntry = Entry(ChoInv,width=8)
    rightHandARPEntry = Entry(ChoInv,width=8)
    rightHandHPEntry = Entry(ChoInv,width=8)
    rightHandRegenHPEntry = Entry(ChoInv,width=8)
    rightHandEvadeEntry = Entry(ChoInv,width=8)
    rightHandArmorEntry = Entry(ChoInv,width=8)
    rightHandMgicArmorEntry = Entry(ChoInv,width=8)
    rightHandMPEntry = Entry(ChoInv,width=8)
    rightHandRegenMPEntry = Entry(ChoInv,width=8)
    rightHandSpellPenetrationEntry = Entry(ChoInv,width=8)
    rightHandDirectMagicDMGEntry = Entry(ChoInv,width=8)
    rightHandPeriodicMagicDMGEntry = Entry(ChoInv,width=8)

    rightHandEnergyEntry.insert(0,'{0}'.format(rightHandEnergy))
    rightHandRegenEnergyEntry.insert(0,'{0}'.format(rightHandRegenEnergy))
    rightHandHasteEntry.insert(0,'{0}'.format(rightHandHaste))
    rightHandHitEntry.insert(0,'{0}'.format(rightHandHit))
    rightHandAttackEntry.insert(0,'{0}-{1}-{2}'.format(rightHandMinAttack,rightHandMidAttack,rightHandMaxAttack))
    rightHandDMGEntry.insert(0,'{0}-{1}-{2}'.format(rightHandMinDMG,rightHandMidDMG,rightHandMaxDMG))
    rightHandARPEntry.insert(0,'{0}'.format(rightHandARP))
    rightHandHPEntry.insert(0,'{0}'.format(rightHandHP))
    rightHandRegenHPEntry.insert(0,'{0}'.format(rightHandRegenHP))
    rightHandEvadeEntry.insert(0,'{0}'.format(rightHandEvade))
    rightHandArmorEntry.insert(0,'{0}'.format(rightHandArmor))
    rightHandMgicArmorEntry.insert(0,'{0}'.format(rightHandMgicArmor))
    rightHandMPEntry.insert(0,'{0}'.format(rightHandMP))
    rightHandRegenMPEntry.insert(0,'{0}'.format(rightHandRegenMP))
    rightHandSpellPenetrationEntry.insert(0,'{0}'.format(rightHandSpellPenetration))
    rightHandDirectMagicDMGEntry.insert(0,'{0}'.format(rightHandDirectMagicDMG))
    rightHandPeriodicMagicDMGEntry.insert(0,'{0}'.format(rightHandPeriodicMagicDMG))

    rightHandAttackEntry.bind('<Return>', add_att_inventory)

    rightHandCharmEnergyEntry = Entry(ChoInv,width=8)
    rightHandCharmRegenEnergyEntry = Entry(ChoInv,width=8)
    rightHandCharmHasteEntry = Entry(ChoInv,width=8)
    rightHandCharmHitEntry = Entry(ChoInv,width=8)
    rightHandCharmAttackEntry = Entry(ChoInv,width=8)
    rightHandCharmDMGEntry = Entry(ChoInv,width=8)
    rightHandCharmARPEntry = Entry(ChoInv,width=8)
    rightHandCharmHPEntry = Entry(ChoInv,width=8)
    rightHandCharmRegenHPEntry = Entry(ChoInv,width=8)
    rightHandCharmEvadeEntry = Entry(ChoInv,width=8)
    rightHandCharmArmorEntry = Entry(ChoInv,width=8)
    rightHandCharmMgicArmorEntry = Entry(ChoInv,width=8)
    rightHandCharmMPEntry = Entry(ChoInv,width=8)
    rightHandCharmRegenMPEntry = Entry(ChoInv,width=8)
    rightHandCharmSpellPenetrationEntry = Entry(ChoInv,width=8)
    rightHandCharmDirectMagicDMGEntry = Entry(ChoInv,width=8)
    rightHandCharmPeriodicMagicDMGEntry = Entry(ChoInv,width=8)

    rightHandCharmEnergyEntry.insert(0,'{0}'.format(rightHandCharmEnergy))
    rightHandCharmRegenEnergyEntry.insert(0,'{0}'.format(rightHandCharmRegenEnergy))
    rightHandCharmHasteEntry.insert(0,'{0}'.format(rightHandCharmHaste))
    rightHandCharmHitEntry.insert(0,'{0}'.format(rightHandCharmHit))
    rightHandCharmAttackEntry.insert(0,'{0}-{1}-{2}'.format(rightHandCharmMinAttack,rightHandCharmMidAttack,rightHandCharmMaxAttack))
    rightHandCharmDMGEntry.insert(0,'{0}-{1}-{2}'.format(rightHandCharmMinDMG,rightHandCharmMidDMG,rightHandCharmMaxDMG))
    rightHandCharmARPEntry.insert(0,'{0}'.format(rightHandCharmARP))
    rightHandCharmHPEntry.insert(0,'{0}'.format(rightHandCharmHP))
    rightHandCharmRegenHPEntry.insert(0,'{0}'.format(rightHandCharmRegenHP))
    rightHandCharmEvadeEntry.insert(0,'{0}'.format(rightHandCharmEvade))
    rightHandCharmArmorEntry.insert(0,'{0}'.format(rightHandCharmArmor))
    rightHandCharmMgicArmorEntry.insert(0,'{0}'.format(rightHandCharmMgicArmor))
    rightHandCharmMPEntry.insert(0,'{0}'.format(rightHandCharmMP))
    rightHandCharmRegenMPEntry.insert(0,'{0}'.format(rightHandCharmRegenMP))
    rightHandCharmSpellPenetrationEntry.insert(0,'{0}'.format(rightHandCharmSpellPenetration))
    rightHandCharmDirectMagicDMGEntry.insert(0,'{0}'.format(rightHandCharmDirectMagicDMG))
    rightHandCharmPeriodicMagicDMGEntry.insert(0,'{0}'.format(rightHandCharmPeriodicMagicDMG))

    rightHandEnergyEntry.grid(row=1,column=1)
    rightHandRegenEnergyEntry.grid(row=1,column=2)
    rightHandHasteEntry.grid(row=1,column=3)
    rightHandHitEntry.grid(row=1,column=4)
    rightHandAttackEntry.grid(row=1,column=5)
    rightHandDMGEntry.grid(row=1,column=6)
    rightHandARPEntry.grid(row=1,column=7)
    rightHandHPEntry.grid(row=1,column=8)
    rightHandRegenHPEntry.grid(row=1,column=9)
    rightHandEvadeEntry.grid(row=1,column=10)
    rightHandArmorEntry.grid(row=1,column=11)
    rightHandMgicArmorEntry.grid(row=1,column=12)
    rightHandMPEntry.grid(row=1,column=13)
    rightHandRegenMPEntry.grid(row=1,column=14)
    rightHandSpellPenetrationEntry.grid(row=1,column=15)
    rightHandDirectMagicDMGEntry.grid(row=1,column=16)
    rightHandPeriodicMagicDMGEntry.grid(row=1,column=17)

    rightHandCharmEnergyEntry.grid(row=2,column=1)
    rightHandCharmRegenEnergyEntry.grid(row=2,column=2)
    rightHandCharmHasteEntry.grid(row=2,column=3)
    rightHandCharmHitEntry.grid(row=2,column=4)
    rightHandCharmAttackEntry.grid(row=2,column=5)
    rightHandCharmDMGEntry.grid(row=2,column=6)
    rightHandCharmARPEntry.grid(row=2,column=7)
    rightHandCharmHPEntry.grid(row=2,column=8)
    rightHandCharmRegenHPEntry.grid(row=2,column=9)
    rightHandCharmEvadeEntry.grid(row=2,column=10)
    rightHandCharmArmorEntry.grid(row=2,column=11)
    rightHandCharmMgicArmorEntry.grid(row=2,column=12)
    rightHandCharmMPEntry.grid(row=2,column=13)
    rightHandCharmRegenMPEntry.grid(row=2,column=14)
    rightHandCharmSpellPenetrationEntry.grid(row=2,column=15)
    rightHandCharmDirectMagicDMGEntry.grid(row=2,column=16)
    rightHandCharmPeriodicMagicDMGEntry.grid(row=2,column=17)

    leftHandEnergyEntry = Entry(ChoInv,width=8)
    leftHandRegenEnergyEntry = Entry(ChoInv,width=8)
    leftHandHasteEntry = Entry(ChoInv,width=8)
    leftHandHitEntry = Entry(ChoInv,width=8)
    leftHandAttackEntry = Entry(ChoInv,width=8)
    leftHandDMGEntry = Entry(ChoInv,width=8)
    leftHandARPEntry = Entry(ChoInv,width=8)
    leftHandHPEntry = Entry(ChoInv,width=8)
    leftHandRegenHPEntry = Entry(ChoInv,width=8)
    leftHandEvadeEntry = Entry(ChoInv,width=8)
    leftHandArmorEntry = Entry(ChoInv,width=8)
    leftHandMgicArmorEntry = Entry(ChoInv,width=8)
    leftHandMPEntry = Entry(ChoInv,width=8)
    leftHandRegenMPEntry = Entry(ChoInv,width=8)
    leftHandSpellPenetrationEntry = Entry(ChoInv,width=8)
    leftHandDirectMagicDMGEntry = Entry(ChoInv,width=8)
    leftHandPeriodicMagicDMGEntry = Entry(ChoInv,width=8)

    leftHandEnergyEntry.insert(0,'{0}'.format(leftHandEnergy))
    leftHandRegenEnergyEntry.insert(0,'{0}'.format(leftHandRegenEnergy))
    leftHandHasteEntry.insert(0,'{0}'.format(leftHandHaste))
    leftHandHitEntry.insert(0,'{0}'.format(leftHandHit))
    leftHandAttackEntry.insert(0,'{0}-{1}-{2}'.format(leftHandMinAttack,leftHandMidAttack,leftHandMaxAttack))
    leftHandDMGEntry.insert(0,'{0}-{1}-{2}'.format(leftHandMinDMG,leftHandMidDMG,leftHandMaxDMG))
    leftHandARPEntry.insert(0,'{0}'.format(leftHandARP))
    leftHandHPEntry.insert(0,'{0}'.format(leftHandHP))
    leftHandRegenHPEntry.insert(0,'{0}'.format(leftHandRegenHP))
    leftHandEvadeEntry.insert(0,'{0}'.format(leftHandEvade))
    leftHandArmorEntry.insert(0,'{0}'.format(leftHandArmor))
    leftHandMgicArmorEntry.insert(0,'{0}'.format(leftHandMgicArmor))
    leftHandMPEntry.insert(0,'{0}'.format(leftHandMP))
    leftHandRegenMPEntry.insert(0,'{0}'.format(leftHandRegenMP))
    leftHandSpellPenetrationEntry.insert(0,'{0}'.format(leftHandSpellPenetration))
    leftHandDirectMagicDMGEntry.insert(0,'{0}'.format(leftHandDirectMagicDMG))
    leftHandPeriodicMagicDMGEntry.insert(0,'{0}'.format(leftHandPeriodicMagicDMG))

    leftHandCharmEnergyEntry = Entry(ChoInv,width=8)
    leftHandCharmRegenEnergyEntry = Entry(ChoInv,width=8)
    leftHandCharmHasteEntry = Entry(ChoInv,width=8)
    leftHandCharmHitEntry = Entry(ChoInv,width=8)
    leftHandCharmAttackEntry = Entry(ChoInv,width=8)
    leftHandCharmDMGEntry = Entry(ChoInv,width=8)
    leftHandCharmARPEntry = Entry(ChoInv,width=8)
    leftHandCharmHPEntry = Entry(ChoInv,width=8)
    leftHandCharmRegenHPEntry = Entry(ChoInv,width=8)
    leftHandCharmEvadeEntry = Entry(ChoInv,width=8)
    leftHandCharmArmorEntry = Entry(ChoInv,width=8)
    leftHandCharmMgicArmorEntry = Entry(ChoInv,width=8)
    leftHandCharmMPEntry = Entry(ChoInv,width=8)
    leftHandCharmRegenMPEntry = Entry(ChoInv,width=8)
    leftHandCharmSpellPenetrationEntry = Entry(ChoInv,width=8)
    leftHandCharmDirectMagicDMGEntry = Entry(ChoInv,width=8)
    leftHandCharmPeriodicMagicDMGEntry = Entry(ChoInv,width=8)

    leftHandCharmEnergyEntry.insert(0,'{0}'.format(leftHandCharmEnergy))
    leftHandCharmRegenEnergyEntry.insert(0,'{0}'.format(leftHandCharmRegenEnergy))
    leftHandCharmHasteEntry.insert(0,'{0}'.format(leftHandCharmHaste))
    leftHandCharmHitEntry.insert(0,'{0}'.format(leftHandCharmHit))
    leftHandCharmAttackEntry.insert(0,'{0}-{1}-{2}'.format(leftHandCharmMinAttack,leftHandCharmMidAttack,leftHandCharmMaxAttack))
    leftHandCharmDMGEntry.insert(0,'{0}-{1}-{2}'.format(leftHandCharmMinDMG,leftHandCharmMidDMG,leftHandCharmMaxDMG))
    leftHandCharmARPEntry.insert(0,'{0}'.format(leftHandCharmARP))
    leftHandCharmHPEntry.insert(0,'{0}'.format(leftHandCharmHP))
    leftHandCharmRegenHPEntry.insert(0,'{0}'.format(leftHandCharmRegenHP))
    leftHandCharmEvadeEntry.insert(0,'{0}'.format(leftHandCharmEvade))
    leftHandCharmArmorEntry.insert(0,'{0}'.format(leftHandCharmArmor))
    leftHandCharmMgicArmorEntry.insert(0,'{0}'.format(leftHandCharmMgicArmor))
    leftHandCharmMPEntry.insert(0,'{0}'.format(leftHandCharmMP))
    leftHandCharmRegenMPEntry.insert(0,'{0}'.format(leftHandCharmRegenMP))
    leftHandCharmSpellPenetrationEntry.insert(0,'{0}'.format(leftHandCharmSpellPenetration))
    leftHandCharmDirectMagicDMGEntry.insert(0,'{0}'.format(leftHandCharmDirectMagicDMG))
    leftHandCharmPeriodicMagicDMGEntry.insert(0,'{0}'.format(leftHandCharmPeriodicMagicDMG))

    leftHandEnergyEntry.grid(row=3,column=1)
    leftHandRegenEnergyEntry.grid(row=3,column=2)
    leftHandHasteEntry.grid(row=3,column=3)
    leftHandHitEntry.grid(row=3,column=4)
    leftHandAttackEntry.grid(row=3,column=5)
    leftHandDMGEntry.grid(row=3,column=6)
    leftHandARPEntry.grid(row=3,column=7)
    leftHandHPEntry.grid(row=3,column=8)
    leftHandRegenHPEntry.grid(row=3,column=9)
    leftHandEvadeEntry.grid(row=3,column=10)
    leftHandArmorEntry.grid(row=3,column=11)
    leftHandMgicArmorEntry.grid(row=3,column=12)
    leftHandMPEntry.grid(row=3,column=13)
    leftHandRegenMPEntry.grid(row=3,column=14)
    leftHandSpellPenetrationEntry.grid(row=3,column=15)
    leftHandDirectMagicDMGEntry.grid(row=3,column=16)
    leftHandPeriodicMagicDMGEntry.grid(row=3,column=17)

    leftHandCharmEnergyEntry.grid(row=4,column=1)
    leftHandCharmRegenEnergyEntry.grid(row=4,column=2)
    leftHandCharmHasteEntry.grid(row=4,column=3)
    leftHandCharmHitEntry.grid(row=4,column=4)
    leftHandCharmAttackEntry.grid(row=4,column=5)
    leftHandCharmDMGEntry.grid(row=4,column=6)
    leftHandCharmARPEntry.grid(row=4,column=7)
    leftHandCharmHPEntry.grid(row=4,column=8)
    leftHandCharmRegenHPEntry.grid(row=4,column=9)
    leftHandCharmEvadeEntry.grid(row=4,column=10)
    leftHandCharmArmorEntry.grid(row=4,column=11)
    leftHandCharmMgicArmorEntry.grid(row=4,column=12)
    leftHandCharmMPEntry.grid(row=4,column=13)
    leftHandCharmRegenMPEntry.grid(row=4,column=14)
    leftHandCharmSpellPenetrationEntry.grid(row=4,column=15)
    leftHandCharmDirectMagicDMGEntry.grid(row=4,column=16)
    leftHandCharmPeriodicMagicDMGEntry.grid(row=4,column=17)

    ChestEnergyEntry = Entry(ChoInv,width=8)
    ChestRegenEnergyEntry = Entry(ChoInv,width=8)
    ChestHasteEntry = Entry(ChoInv,width=8)
    ChestHitEntry = Entry(ChoInv,width=8)
    ChestAttackEntry = Entry(ChoInv,width=8)
    ChestDMGEntry = Entry(ChoInv,width=8)
    ChestARPEntry = Entry(ChoInv,width=8)
    ChestHPEntry = Entry(ChoInv,width=8)
    ChestRegenHPEntry = Entry(ChoInv,width=8)
    ChestEvadeEntry = Entry(ChoInv,width=8)
    ChestArmorEntry = Entry(ChoInv,width=8)
    ChestMgicArmorEntry = Entry(ChoInv,width=8)
    ChestMPEntry = Entry(ChoInv,width=8)
    ChestRegenMPEntry = Entry(ChoInv,width=8)
    ChestSpellPenetrationEntry = Entry(ChoInv,width=8)
    ChestDirectMagicDMGEntry = Entry(ChoInv,width=8)
    ChestPeriodicMagicDMGEntry = Entry(ChoInv,width=8)

    ChestEnergyEntry.insert(0,'{0}'.format(ChestEnergy))
    ChestRegenEnergyEntry.insert(0,'{0}'.format(ChestRegenEnergy))
    ChestHasteEntry.insert(0,'{0}'.format(ChestHaste))
    ChestHitEntry.insert(0,'{0}'.format(ChestHit))
    ChestAttackEntry.insert(0,'{0}-{1}-{2}'.format(ChestMinAttack,ChestMidAttack,ChestMaxAttack))
    ChestDMGEntry.insert(0,'{0}-{1}-{2}'.format(ChestMinDMG,ChestMidDMG,ChestMaxDMG))
    ChestARPEntry.insert(0,'{0}'.format(ChestARP))
    ChestHPEntry.insert(0,'{0}'.format(ChestHP))
    ChestRegenHPEntry.insert(0,'{0}'.format(ChestRegenHP))
    ChestEvadeEntry.insert(0,'{0}'.format(ChestEvade))
    ChestArmorEntry.insert(0,'{0}'.format(ChestArmor))
    ChestMgicArmorEntry.insert(0,'{0}'.format(ChestMgicArmor))
    ChestMPEntry.insert(0,'{0}'.format(ChestMP))
    ChestRegenMPEntry.insert(0,'{0}'.format(ChestRegenMP))
    ChestSpellPenetrationEntry.insert(0,'{0}'.format(ChestSpellPenetration))
    ChestDirectMagicDMGEntry.insert(0,'{0}'.format(ChestDirectMagicDMG))
    ChestPeriodicMagicDMGEntry.insert(0,'{0}'.format(ChestPeriodicMagicDMG))

    ChestCharmEnergyEntry = Entry(ChoInv,width=8)
    ChestCharmRegenEnergyEntry = Entry(ChoInv,width=8)
    ChestCharmHasteEntry = Entry(ChoInv,width=8)
    ChestCharmHitEntry = Entry(ChoInv,width=8)
    ChestCharmAttackEntry = Entry(ChoInv,width=8)
    ChestCharmDMGEntry = Entry(ChoInv,width=8)
    ChestCharmARPEntry = Entry(ChoInv,width=8)
    ChestCharmHPEntry = Entry(ChoInv,width=8)
    ChestCharmRegenHPEntry = Entry(ChoInv,width=8)
    ChestCharmEvadeEntry = Entry(ChoInv,width=8)
    ChestCharmArmorEntry = Entry(ChoInv,width=8)
    ChestCharmMgicArmorEntry = Entry(ChoInv,width=8)
    ChestCharmMPEntry = Entry(ChoInv,width=8)
    ChestCharmRegenMPEntry = Entry(ChoInv,width=8)
    ChestCharmSpellPenetrationEntry = Entry(ChoInv,width=8)
    ChestCharmDirectMagicDMGEntry = Entry(ChoInv,width=8)
    ChestCharmPeriodicMagicDMGEntry = Entry(ChoInv,width=8)

    ChestCharmEnergyEntry.insert(0,'{0}'.format(ChestCharmEnergy))
    ChestCharmRegenEnergyEntry.insert(0,'{0}'.format(ChestCharmRegenEnergy))
    ChestCharmHasteEntry.insert(0,'{0}'.format(ChestCharmHaste))
    ChestCharmHitEntry.insert(0,'{0}'.format(ChestCharmHit))
    ChestCharmAttackEntry.insert(0,'{0}-{1}-{2}'.format(ChestCharmMinAttack,ChestCharmMidAttack,ChestCharmMaxAttack))
    ChestCharmDMGEntry.insert(0,'{0}-{1}-{2}'.format(ChestCharmMinDMG,ChestCharmMidDMG,ChestCharmMaxDMG))
    ChestCharmARPEntry.insert(0,'{0}'.format(ChestCharmARP))
    ChestCharmHPEntry.insert(0,'{0}'.format(ChestCharmHP))
    ChestCharmRegenHPEntry.insert(0,'{0}'.format(ChestCharmRegenHP))
    ChestCharmEvadeEntry.insert(0,'{0}'.format(ChestCharmEvade))
    ChestCharmArmorEntry.insert(0,'{0}'.format(ChestCharmArmor))
    ChestCharmMgicArmorEntry.insert(0,'{0}'.format(ChestCharmMgicArmor))
    ChestCharmMPEntry.insert(0,'{0}'.format(ChestCharmMP))
    ChestCharmRegenMPEntry.insert(0,'{0}'.format(ChestCharmRegenMP))
    ChestCharmSpellPenetrationEntry.insert(0,'{0}'.format(ChestCharmSpellPenetration))
    ChestCharmDirectMagicDMGEntry.insert(0,'{0}'.format(ChestCharmDirectMagicDMG))
    ChestCharmPeriodicMagicDMGEntry.insert(0,'{0}'.format(ChestCharmPeriodicMagicDMG))

    ChestEnergyEntry.grid(row=5,column=1)
    ChestRegenEnergyEntry.grid(row=5,column=2)
    ChestHasteEntry.grid(row=5,column=3)
    ChestHitEntry.grid(row=5,column=4)
    ChestAttackEntry.grid(row=5,column=5)
    ChestDMGEntry.grid(row=5,column=6)
    ChestARPEntry.grid(row=5,column=7)
    ChestHPEntry.grid(row=5,column=8)
    ChestRegenHPEntry.grid(row=5,column=9)
    ChestEvadeEntry.grid(row=5,column=10)
    ChestArmorEntry.grid(row=5,column=11)
    ChestMgicArmorEntry.grid(row=5,column=12)
    ChestMPEntry.grid(row=5,column=13)
    ChestRegenMPEntry.grid(row=5,column=14)
    ChestSpellPenetrationEntry.grid(row=5,column=15)
    ChestDirectMagicDMGEntry.grid(row=5,column=16)
    ChestPeriodicMagicDMGEntry.grid(row=5,column=17)

    ChestCharmEnergyEntry.grid(row=6,column=1)
    ChestCharmRegenEnergyEntry.grid(row=6,column=2)
    ChestCharmHasteEntry.grid(row=6,column=3)
    ChestCharmHitEntry.grid(row=6,column=4)
    ChestCharmAttackEntry.grid(row=6,column=5)
    ChestCharmDMGEntry.grid(row=6,column=6)
    ChestCharmARPEntry.grid(row=6,column=7)
    ChestCharmHPEntry.grid(row=6,column=8)
    ChestCharmRegenHPEntry.grid(row=6,column=9)
    ChestCharmEvadeEntry.grid(row=6,column=10)
    ChestCharmArmorEntry.grid(row=6,column=11)
    ChestCharmMgicArmorEntry.grid(row=6,column=12)
    ChestCharmMPEntry.grid(row=6,column=13)
    ChestCharmRegenMPEntry.grid(row=6,column=14)
    ChestCharmSpellPenetrationEntry.grid(row=6,column=15)
    ChestCharmDirectMagicDMGEntry.grid(row=6,column=16)
    ChestCharmPeriodicMagicDMGEntry.grid(row=6,column=17)

    amuletEnergyEntry = Entry(ChoInv,width=8)
    amuletRegenEnergyEntry = Entry(ChoInv,width=8)
    amuletHasteEntry = Entry(ChoInv,width=8)
    amuletHitEntry = Entry(ChoInv,width=8)
    amuletAttackEntry = Entry(ChoInv,width=8)
    amuletDMGEntry = Entry(ChoInv,width=8)
    amuletARPEntry = Entry(ChoInv,width=8)
    amuletHPEntry = Entry(ChoInv,width=8)
    amuletRegenHPEntry = Entry(ChoInv,width=8)
    amuletEvadeEntry = Entry(ChoInv,width=8)
    amuletArmorEntry = Entry(ChoInv,width=8)
    amuletMgicArmorEntry = Entry(ChoInv,width=8)
    amuletMPEntry = Entry(ChoInv,width=8)
    amuletRegenMPEntry = Entry(ChoInv,width=8)
    amuletSpellPenetrationEntry = Entry(ChoInv,width=8)
    amuletDirectMagicDMGEntry = Entry(ChoInv,width=8)
    amuletPeriodicMagicDMGEntry = Entry(ChoInv,width=8)

    amuletEnergyEntry.insert(0,'{0}'.format(amuletEnergy))
    amuletRegenEnergyEntry.insert(0,'{0}'.format(amuletRegenEnergy))
    amuletHasteEntry.insert(0,'{0}'.format(amuletHaste))
    amuletHitEntry.insert(0,'{0}'.format(amuletHit))
    amuletAttackEntry.insert(0,'{0}-{1}-{2}'.format(amuletMinAttack,amuletMidAttack,amuletMaxAttack))
    amuletDMGEntry.insert(0,'{0}-{1}-{2}'.format(amuletMinDMG,amuletMidDMG,amuletMaxDMG))
    amuletARPEntry.insert(0,'{0}'.format(amuletARP))
    amuletHPEntry.insert(0,'{0}'.format(amuletHP))
    amuletRegenHPEntry.insert(0,'{0}'.format(amuletRegenHP))
    amuletEvadeEntry.insert(0,'{0}'.format(amuletEvade))
    amuletArmorEntry.insert(0,'{0}'.format(amuletArmor))
    amuletMgicArmorEntry.insert(0,'{0}'.format(amuletMgicArmor))
    amuletMPEntry.insert(0,'{0}'.format(amuletMP))
    amuletRegenMPEntry.insert(0,'{0}'.format(amuletRegenMP))
    amuletSpellPenetrationEntry.insert(0,'{0}'.format(amuletSpellPenetration))
    amuletDirectMagicDMGEntry.insert(0,'{0}'.format(amuletDirectMagicDMG))
    amuletPeriodicMagicDMGEntry.insert(0,'{0}'.format(amuletPeriodicMagicDMG))

    amuletCharmEnergyEntry = Entry(ChoInv,width=8)
    amuletCharmRegenEnergyEntry = Entry(ChoInv,width=8)
    amuletCharmHasteEntry = Entry(ChoInv,width=8)
    amuletCharmHitEntry = Entry(ChoInv,width=8)
    amuletCharmAttackEntry = Entry(ChoInv,width=8)
    amuletCharmDMGEntry = Entry(ChoInv,width=8)
    amuletCharmARPEntry = Entry(ChoInv,width=8)
    amuletCharmHPEntry = Entry(ChoInv,width=8)
    amuletCharmRegenHPEntry = Entry(ChoInv,width=8)
    amuletCharmEvadeEntry = Entry(ChoInv,width=8)
    amuletCharmArmorEntry = Entry(ChoInv,width=8)
    amuletCharmMgicArmorEntry = Entry(ChoInv,width=8)
    amuletCharmMPEntry = Entry(ChoInv,width=8)
    amuletCharmRegenMPEntry = Entry(ChoInv,width=8)
    amuletCharmSpellPenetrationEntry = Entry(ChoInv,width=8)
    amuletCharmDirectMagicDMGEntry = Entry(ChoInv,width=8)
    amuletCharmPeriodicMagicDMGEntry = Entry(ChoInv,width=8)

    amuletCharmEnergyEntry.insert(0,'{0}'.format(amuletCharmEnergy))
    amuletCharmRegenEnergyEntry.insert(0,'{0}'.format(amuletCharmRegenEnergy))
    amuletCharmHasteEntry.insert(0,'{0}'.format(amuletCharmHaste))
    amuletCharmHitEntry.insert(0,'{0}'.format(amuletCharmHit))
    amuletCharmAttackEntry.insert(0,'{0}-{1}-{2}'.format(amuletCharmMinAttack,amuletCharmMidAttack,amuletCharmMaxAttack))
    amuletCharmDMGEntry.insert(0,'{0}-{1}-{2}'.format(amuletCharmMinDMG,amuletCharmMidDMG,amuletCharmMaxDMG))
    amuletCharmARPEntry.insert(0,'{0}'.format(amuletCharmARP))
    amuletCharmHPEntry.insert(0,'{0}'.format(amuletCharmHP))
    amuletCharmRegenHPEntry.insert(0,'{0}'.format(amuletCharmRegenHP))
    amuletCharmEvadeEntry.insert(0,'{0}'.format(amuletCharmEvade))
    amuletCharmArmorEntry.insert(0,'{0}'.format(amuletCharmArmor))
    amuletCharmMgicArmorEntry.insert(0,'{0}'.format(amuletCharmMgicArmor))
    amuletCharmMPEntry.insert(0,'{0}'.format(amuletCharmMP))
    amuletCharmRegenMPEntry.insert(0,'{0}'.format(amuletCharmRegenMP))
    amuletCharmSpellPenetrationEntry.insert(0,'{0}'.format(amuletCharmSpellPenetration))
    amuletCharmDirectMagicDMGEntry.insert(0,'{0}'.format(amuletCharmDirectMagicDMG))
    amuletCharmPeriodicMagicDMGEntry.insert(0,'{0}'.format(amuletCharmPeriodicMagicDMG))

    amuletEnergyEntry.grid(row=7,column=1)
    amuletRegenEnergyEntry.grid(row=7,column=2)
    amuletHasteEntry.grid(row=7,column=3)
    amuletHitEntry.grid(row=7,column=4)
    amuletAttackEntry.grid(row=7,column=5)
    amuletDMGEntry.grid(row=7,column=6)
    amuletARPEntry.grid(row=7,column=7)
    amuletHPEntry.grid(row=7,column=8)
    amuletRegenHPEntry.grid(row=7,column=9)
    amuletEvadeEntry.grid(row=7,column=10)
    amuletArmorEntry.grid(row=7,column=11)
    amuletMgicArmorEntry.grid(row=7,column=12)
    amuletMPEntry.grid(row=7,column=13)
    amuletRegenMPEntry.grid(row=7,column=14)
    amuletSpellPenetrationEntry.grid(row=7,column=15)
    amuletDirectMagicDMGEntry.grid(row=7,column=16)
    amuletPeriodicMagicDMGEntry.grid(row=7,column=17)

    amuletCharmEnergyEntry.grid(row=8,column=1)
    amuletCharmRegenEnergyEntry.grid(row=8,column=2)
    amuletCharmHasteEntry.grid(row=8,column=3)
    amuletCharmHitEntry.grid(row=8,column=4)
    amuletCharmAttackEntry.grid(row=8,column=5)
    amuletCharmDMGEntry.grid(row=8,column=6)
    amuletCharmARPEntry.grid(row=8,column=7)
    amuletCharmHPEntry.grid(row=8,column=8)
    amuletCharmRegenHPEntry.grid(row=8,column=9)
    amuletCharmEvadeEntry.grid(row=8,column=10)
    amuletCharmArmorEntry.grid(row=8,column=11)
    amuletCharmMgicArmorEntry.grid(row=8,column=12)
    amuletCharmMPEntry.grid(row=8,column=13)
    amuletCharmRegenMPEntry.grid(row=8,column=14)
    amuletCharmSpellPenetrationEntry.grid(row=8,column=15)
    amuletCharmDirectMagicDMGEntry.grid(row=8,column=16)
    amuletCharmPeriodicMagicDMGEntry.grid(row=8,column=17)

    ringEnergyEntry = Entry(ChoInv,width=8)
    ringRegenEnergyEntry = Entry(ChoInv,width=8)
    ringHasteEntry = Entry(ChoInv,width=8)
    ringHitEntry = Entry(ChoInv,width=8)
    ringAttackEntry = Entry(ChoInv,width=8)
    ringDMGEntry = Entry(ChoInv,width=8)
    ringARPEntry = Entry(ChoInv,width=8)
    ringHPEntry = Entry(ChoInv,width=8)
    ringRegenHPEntry = Entry(ChoInv,width=8)
    ringEvadeEntry = Entry(ChoInv,width=8)
    ringArmorEntry = Entry(ChoInv,width=8)
    ringMgicArmorEntry = Entry(ChoInv,width=8)
    ringMPEntry = Entry(ChoInv,width=8)
    ringRegenMPEntry = Entry(ChoInv,width=8)
    ringSpellPenetrationEntry = Entry(ChoInv,width=8)
    ringDirectMagicDMGEntry = Entry(ChoInv,width=8)
    ringPeriodicMagicDMGEntry = Entry(ChoInv,width=8)

    ringEnergyEntry.insert(0,'{0}'.format(ringEnergy))
    ringRegenEnergyEntry.insert(0,'{0}'.format(ringRegenEnergy))
    ringHasteEntry.insert(0,'{0}'.format(ringHaste))
    ringHitEntry.insert(0,'{0}'.format(ringHit))
    ringAttackEntry.insert(0,'{0}-{1}-{2}'.format(ringMinAttack,ringMidAttack,ringMaxAttack))
    ringDMGEntry.insert(0,'{0}-{1}-{2}'.format(ringMinDMG,ringMidDMG,ringMaxDMG))
    ringARPEntry.insert(0,'{0}'.format(ringARP))
    ringHPEntry.insert(0,'{0}'.format(ringHP))
    ringRegenHPEntry.insert(0,'{0}'.format(ringRegenHP))
    ringEvadeEntry.insert(0,'{0}'.format(ringEvade))
    ringArmorEntry.insert(0,'{0}'.format(ringArmor))
    ringMgicArmorEntry.insert(0,'{0}'.format(ringMgicArmor))
    ringMPEntry.insert(0,'{0}'.format(ringMP))
    ringRegenMPEntry.insert(0,'{0}'.format(ringRegenMP))
    ringSpellPenetrationEntry.insert(0,'{0}'.format(ringSpellPenetration))
    ringDirectMagicDMGEntry.insert(0,'{0}'.format(ringDirectMagicDMG))
    ringPeriodicMagicDMGEntry.insert(0,'{0}'.format(ringPeriodicMagicDMG))

    ringCharmEnergyEntry = Entry(ChoInv,width=8)
    ringCharmRegenEnergyEntry = Entry(ChoInv,width=8)
    ringCharmHasteEntry = Entry(ChoInv,width=8)
    ringCharmHitEntry = Entry(ChoInv,width=8)
    ringCharmAttackEntry = Entry(ChoInv,width=8)
    ringCharmDMGEntry = Entry(ChoInv,width=8)
    ringCharmARPEntry = Entry(ChoInv,width=8)
    ringCharmHPEntry = Entry(ChoInv,width=8)
    ringCharmRegenHPEntry = Entry(ChoInv,width=8)
    ringCharmEvadeEntry = Entry(ChoInv,width=8)
    ringCharmArmorEntry = Entry(ChoInv,width=8)
    ringCharmMgicArmorEntry = Entry(ChoInv,width=8)
    ringCharmMPEntry = Entry(ChoInv,width=8)
    ringCharmRegenMPEntry = Entry(ChoInv,width=8)
    ringCharmSpellPenetrationEntry = Entry(ChoInv,width=8)
    ringCharmDirectMagicDMGEntry = Entry(ChoInv,width=8)
    ringCharmPeriodicMagicDMGEntry = Entry(ChoInv,width=8)

    ringCharmEnergyEntry.insert(0,'{0}'.format(ringCharmEnergy))
    ringCharmRegenEnergyEntry.insert(0,'{0}'.format(ringCharmRegenEnergy))
    ringCharmHasteEntry.insert(0,'{0}'.format(ringCharmHaste))
    ringCharmHitEntry.insert(0,'{0}'.format(ringCharmHit))
    ringCharmAttackEntry.insert(0,'{0}-{1}-{2}'.format(ringCharmMinAttack,ringCharmMidAttack,ringCharmMaxAttack))
    ringCharmDMGEntry.insert(0,'{0}-{1}-{2}'.format(ringCharmMinDMG,ringCharmMidDMG,ringCharmMaxDMG))
    ringCharmARPEntry.insert(0,'{0}'.format(ringCharmARP))
    ringCharmHPEntry.insert(0,'{0}'.format(ringCharmHP))
    ringCharmRegenHPEntry.insert(0,'{0}'.format(ringCharmRegenHP))
    ringCharmEvadeEntry.insert(0,'{0}'.format(ringCharmEvade))
    ringCharmArmorEntry.insert(0,'{0}'.format(ringCharmArmor))
    ringCharmMgicArmorEntry.insert(0,'{0}'.format(ringCharmMgicArmor))
    ringCharmMPEntry.insert(0,'{0}'.format(ringCharmMP))
    ringCharmRegenMPEntry.insert(0,'{0}'.format(ringCharmRegenMP))
    ringCharmSpellPenetrationEntry.insert(0,'{0}'.format(ringCharmSpellPenetration))
    ringCharmDirectMagicDMGEntry.insert(0,'{0}'.format(ringCharmDirectMagicDMG))
    ringCharmPeriodicMagicDMGEntry.insert(0,'{0}'.format(ringCharmPeriodicMagicDMG))

    ringEnergyEntry.grid(row=9,column=1)
    ringRegenEnergyEntry.grid(row=9,column=2)
    ringHasteEntry.grid(row=9,column=3)
    ringHitEntry.grid(row=9,column=4)
    ringAttackEntry.grid(row=9,column=5)
    ringDMGEntry.grid(row=9,column=6)
    ringARPEntry.grid(row=9,column=7)
    ringHPEntry.grid(row=9,column=8)
    ringRegenHPEntry.grid(row=9,column=9)
    ringEvadeEntry.grid(row=9,column=10)
    ringArmorEntry.grid(row=9,column=11)
    ringMgicArmorEntry.grid(row=9,column=12)
    ringMPEntry.grid(row=9,column=13)
    ringRegenMPEntry.grid(row=9,column=14)
    ringSpellPenetrationEntry.grid(row=9,column=15)
    ringDirectMagicDMGEntry.grid(row=9,column=16)
    ringPeriodicMagicDMGEntry.grid(row=9,column=17)

    ringCharmEnergyEntry.grid(row=10,column=1)
    ringCharmRegenEnergyEntry.grid(row=10,column=2)
    ringCharmHasteEntry.grid(row=10,column=3)
    ringCharmHitEntry.grid(row=10,column=4)
    ringCharmAttackEntry.grid(row=10,column=5)
    ringCharmDMGEntry.grid(row=10,column=6)
    ringCharmARPEntry.grid(row=10,column=7)
    ringCharmHPEntry.grid(row=10,column=8)
    ringCharmRegenHPEntry.grid(row=10,column=9)
    ringCharmEvadeEntry.grid(row=10,column=10)
    ringCharmArmorEntry.grid(row=10,column=11)
    ringCharmMgicArmorEntry.grid(row=10,column=12)
    ringCharmMPEntry.grid(row=10,column=13)
    ringCharmRegenMPEntry.grid(row=10,column=14)
    ringCharmSpellPenetrationEntry.grid(row=10,column=15)
    ringCharmDirectMagicDMGEntry.grid(row=10,column=16)
    ringCharmPeriodicMagicDMGEntry.grid(row=10,column=17)

    bookEnergyEntry = Entry(ChoInv,width=8)
    bookRegenEnergyEntry = Entry(ChoInv,width=8)
    bookHasteEntry = Entry(ChoInv,width=8)
    bookHitEntry = Entry(ChoInv,width=8)
    bookAttackEntry = Entry(ChoInv,width=8)
    bookDMGEntry = Entry(ChoInv,width=8)
    bookARPEntry = Entry(ChoInv,width=8)
    bookHPEntry = Entry(ChoInv,width=8)
    bookRegenHPEntry = Entry(ChoInv,width=8)
    bookEvadeEntry = Entry(ChoInv,width=8)
    bookArmorEntry = Entry(ChoInv,width=8)
    bookMgicArmorEntry = Entry(ChoInv,width=8)
    bookMPEntry = Entry(ChoInv,width=8)
    bookRegenMPEntry = Entry(ChoInv,width=8)
    bookSpellPenetrationEntry = Entry(ChoInv,width=8)
    bookDirectMagicDMGEntry = Entry(ChoInv,width=8)
    bookPeriodicMagicDMGEntry = Entry(ChoInv,width=8)

    bookEnergyEntry.insert(0,'{0}'.format(bookEnergy))
    bookRegenEnergyEntry.insert(0,'{0}'.format(bookRegenEnergy))
    bookHasteEntry.insert(0,'{0}'.format(bookHaste))
    bookHitEntry.insert(0,'{0}'.format(bookHit))
    bookAttackEntry.insert(0,'{0}-{1}-{2}'.format(bookMinAttack,bookMidAttack,bookMaxAttack))
    bookDMGEntry.insert(0,'{0}-{1}-{2}'.format(bookMinDMG,bookMidDMG,bookMaxDMG))
    bookARPEntry.insert(0,'{0}'.format(bookARP))
    bookHPEntry.insert(0,'{0}'.format(bookHP))
    bookRegenHPEntry.insert(0,'{0}'.format(bookRegenHP))
    bookEvadeEntry.insert(0,'{0}'.format(bookEvade))
    bookArmorEntry.insert(0,'{0}'.format(bookArmor))
    bookMgicArmorEntry.insert(0,'{0}'.format(bookMgicArmor))
    bookMPEntry.insert(0,'{0}'.format(bookMP))
    bookRegenMPEntry.insert(0,'{0}'.format(bookRegenMP))
    bookSpellPenetrationEntry.insert(0,'{0}'.format(bookSpellPenetration))
    bookDirectMagicDMGEntry.insert(0,'{0}'.format(bookDirectMagicDMG))
    bookPeriodicMagicDMGEntry.insert(0,'{0}'.format(bookPeriodicMagicDMG))

    bookCharmEnergyEntry = Entry(ChoInv,width=8)
    bookCharmRegenEnergyEntry = Entry(ChoInv,width=8)
    bookCharmHasteEntry = Entry(ChoInv,width=8)
    bookCharmHitEntry = Entry(ChoInv,width=8)
    bookCharmAttackEntry = Entry(ChoInv,width=8)
    bookCharmDMGEntry = Entry(ChoInv,width=8)
    bookCharmARPEntry = Entry(ChoInv,width=8)
    bookCharmHPEntry = Entry(ChoInv,width=8)
    bookCharmRegenHPEntry = Entry(ChoInv,width=8)
    bookCharmEvadeEntry = Entry(ChoInv,width=8)
    bookCharmArmorEntry = Entry(ChoInv,width=8)
    bookCharmMgicArmorEntry = Entry(ChoInv,width=8)
    bookCharmMPEntry = Entry(ChoInv,width=8)
    bookCharmRegenMPEntry = Entry(ChoInv,width=8)
    bookCharmSpellPenetrationEntry = Entry(ChoInv,width=8)
    bookCharmDirectMagicDMGEntry = Entry(ChoInv,width=8)
    bookCharmPeriodicMagicDMGEntry = Entry(ChoInv,width=8)

    bookCharmEnergyEntry.insert(0,'{0}'.format(bookCharmEnergy))
    bookCharmRegenEnergyEntry.insert(0,'{0}'.format(bookCharmRegenEnergy))
    bookCharmHasteEntry.insert(0,'{0}'.format(bookCharmHaste))
    bookCharmHitEntry.insert(0,'{0}'.format(bookCharmHit))
    bookCharmAttackEntry.insert(0,'{0}-{1}-{2}'.format(bookCharmMinAttack,bookCharmMidAttack,bookCharmMaxAttack))
    bookCharmDMGEntry.insert(0,'{0}-{1}-{2}'.format(bookCharmMinDMG,bookCharmMidDMG,bookCharmMaxDMG))
    bookCharmARPEntry.insert(0,'{0}'.format(bookCharmARP))
    bookCharmHPEntry.insert(0,'{0}'.format(bookCharmHP))
    bookCharmRegenHPEntry.insert(0,'{0}'.format(bookCharmRegenHP))
    bookCharmEvadeEntry.insert(0,'{0}'.format(bookCharmEvade))
    bookCharmArmorEntry.insert(0,'{0}'.format(bookCharmArmor))
    bookCharmMgicArmorEntry.insert(0,'{0}'.format(bookCharmMgicArmor))
    bookCharmMPEntry.insert(0,'{0}'.format(bookCharmMP))
    bookCharmRegenMPEntry.insert(0,'{0}'.format(bookCharmRegenMP))
    bookCharmSpellPenetrationEntry.insert(0,'{0}'.format(bookCharmSpellPenetration))
    bookCharmDirectMagicDMGEntry.insert(0,'{0}'.format(bookCharmDirectMagicDMG))
    bookCharmPeriodicMagicDMGEntry.insert(0,'{0}'.format(bookCharmPeriodicMagicDMG))

    bookEnergyEntry.grid(row=11,column=1)
    bookRegenEnergyEntry.grid(row=11,column=2)
    bookHasteEntry.grid(row=11,column=3)
    bookHitEntry.grid(row=11,column=4)
    bookAttackEntry.grid(row=11,column=5)
    bookDMGEntry.grid(row=11,column=6)
    bookARPEntry.grid(row=11,column=7)
    bookHPEntry.grid(row=11,column=8)
    bookRegenHPEntry.grid(row=11,column=9)
    bookEvadeEntry.grid(row=11,column=10)
    bookArmorEntry.grid(row=11,column=11)
    bookMgicArmorEntry.grid(row=11,column=12)
    bookMPEntry.grid(row=11,column=13)
    bookRegenMPEntry.grid(row=11,column=14)
    bookSpellPenetrationEntry.grid(row=11,column=15)
    bookDirectMagicDMGEntry.grid(row=11,column=16)
    bookPeriodicMagicDMGEntry.grid(row=11,column=17)

    bookCharmEnergyEntry.grid(row=12,column=1)
    bookCharmRegenEnergyEntry.grid(row=12,column=2)
    bookCharmHasteEntry.grid(row=12,column=3)
    bookCharmHitEntry.grid(row=12,column=4)
    bookCharmAttackEntry.grid(row=12,column=5)
    bookCharmDMGEntry.grid(row=12,column=6)
    bookCharmARPEntry.grid(row=12,column=7)
    bookCharmHPEntry.grid(row=12,column=8)
    bookCharmRegenHPEntry.grid(row=12,column=9)
    bookCharmEvadeEntry.grid(row=12,column=10)
    bookCharmArmorEntry.grid(row=12,column=11)
    bookCharmMgicArmorEntry.grid(row=12,column=12)
    bookCharmMPEntry.grid(row=12,column=13)
    bookCharmRegenMPEntry.grid(row=12,column=14)
    bookCharmSpellPenetrationEntry.grid(row=12,column=15)
    bookCharmDirectMagicDMGEntry.grid(row=12,column=16)
    bookCharmPeriodicMagicDMGEntry.grid(row=12,column=17)

def create_labels(frame,columnParam,list,sixParam):
    if sixParam == 0:
        for param in list:
            Label(frame, text = param).grid(row=0, column=columnParam)
            columnParam+=1
    elif sixParam == 1:
        for param in list:
            Label(frame, text = param).grid(row=columnParam, column=0)
            columnParam+=1

def sum_stats(event):
    global totalEnergy,staticEnergy,changeEnergy,totalRegenEnergy,changeRegenEnergy,changeRegenEnergy,totalHaste,staticHaste,changeHaste,totalHit,staticHit,changeHit,totalAttack,staticAttack,changeAttack,totalDMG,staticDMG,changeDMG,totalARP,staticARP,changeARP,totalHP,staticHP,changeHP,totalRegenHP,staticRegenHP,changeRegenHP,totalEvade,staticEvade,changeEvade,totalArmor,staticArmor,changeArmor,totalMgicArmor,staticMgicArmor,changeMgicArmor,totalMP,staticMP,changeMP,totalRegenMP,staticRegenMP,changeRegenMP,totalSpellPenetration,staticSpellPenetration,changeSpellPenetration,totalDirectMagicDMG,staticDirectMagicDMG,changeDirectMagicDMG,totalPeriodicMagicDMG,staticPeriodicMagicDMG,changePeriodicMagicDMG,totalEnergyLabel,totalRegenEnergyLabel,totalHasteLabel,totalHitLabel,totalAttackLabel,totalDMGLabel,totalARPLabel,totalHPLabel,totalRegenHPLabel,totalEvadeLabel,totalArmorLabel,totalMgicArmorLabel,totalMPLabel,totalRegenMPLabel,totalSpellPenetrationLabel,totalDirectMagicDMGLabel,totalPeriodicMagicDMGLabel,changeEnergyLabel,changeRegenEnergyLabel,changeHasteLabel,changeHitLabel,changeAttackLabel,changeDMGLabel,changeARPLabel,changeHPLabel,changeRegenHPLabel,changeEvadeLabel,changeArmorLabel,changeMgicArmorLabel,changeMPLabel,changeRegenMPLabel,changeSpellPenetrationLabel,changeDirectMagicDMGLabel,changePeriodicMagicDMGLabel,secondBreathAttInt

    if changeEnergyLabel.get():
        changeEnergy = int(changeEnergyLabel.get())
    if changeRegenEnergyLabel.get():
        changeRegenEnergy = int(changeRegenEnergyLabel.get())
    if changeHasteLabel.get():
        changeHaste = int(changeHasteLabel.get())
    if changeHitLabel.get():
        changeHit = int(changeHitLabel.get())
    if changeAttackLabel.get():
        changeAttack = changeAttackLabel.get()
        # changeAttackMin = int(changeAttack.split('-')[0])
        # changeAttackMid = int(changeAttack.split('-')[1])
        # changeAttackMax = int(changeAttack.split('-')[2])
    if changeDMGLabel.get():
        changeDMG = changeDMGLabel.get()
        # changeDMGMin = int(changeDMG.split('-')[0])
        # changeDMGMid = int(changeDMG.split('-')[1])
        # changeDMGMax = int(changeDMG.split('-')[2])
    if changeARPLabel.get():
        changeARP = int(changeARPLabel.get())
    if changeHPLabel.get():
        changeHP = int(changeHPLabel.get())
    if changeRegenHPLabel.get():
        changeRegenHP = int(changeRegenHPLabel.get())
    if changeEvadeLabel.get():
        changeEvade = int(changeEvadeLabel.get())
    if changeArmorLabel.get():
        changeArmor = int(changeArmorLabel.get())
    if changeMgicArmorLabel.get():
        changeMgicArmor = int(changeMgicArmorLabel.get())
    if changeMPLabel.get():
        changeMP = int(changeMPLabel.get())
    if changeRegenMPLabel.get():
        changeRegenMP = int(changeRegenMPLabel.get())
    if changeSpellPenetrationLabel.get():
        changeSpellPenetration = int(changeSpellPenetrationLabel.get())
    if changeDirectMagicDMGLabel.get():
        changeDirectMagicDMG = int(changeDirectMagicDMGLabel.get())
    if changePeriodicMagicDMGLabel.get():
        changePeriodicMagicDMG = int(changePeriodicMagicDMGLabel.get())

    totalEnergy = staticEnergy + changeEnergy
    if totalEnergy < 0:
        totalEnergy = 0
    totalRegenEnergy = changeRegenEnergy + changeRegenEnergy
    if totalRegenEnergy < 0:
        totalRegenEnergy = 0
    totalHaste = staticHaste + changeHaste
    if totalHaste < 0:
        totalHaste = 0
    totalHit = staticHit + changeHit
    if totalHit < 0:
        totalHit = 0
    totalAttackMin = int(staticAttack.split('-')[0])-int(changeAttack.split('-')[0])
    if totalAttackMin < 0:
        totalAttackMin = 0
    totalAttackMid = int(staticAttack.split('-')[1])-int(changeAttack.split('-')[1])
    if totalAttackMid < 0:
        totalAttackMid = 0
    totalAttackMax = int(staticAttack.split('-')[2])-int(changeAttack.split('-')[2])
    if totalAttackMax < 0:
        totalAttackMax = 0
    totalAttack = '{0}-{1}-{2}'.format(totalAttackMin,totalAttackMid,totalAttackMax)
    totalDMGMin = int(staticDMG.split('-')[0])-int(changeDMG.split('-')[0])
    if totalDMGMin < 0:
        totalDMGMin = 0
    totalDMGMid = int(staticDMG.split('-')[1])-int(changeDMG.split('-')[1])
    if totalDMGMid < 0:
        totalDMGMid = 0
    totalDMGMax = int(staticDMG.split('-')[2])-int(changeDMG.split('-')[2])
    if totalDMGMax < 0:
        totalDMGMax = 0
    totalDMG = '{0}-{1}-{2}'.format(totalDMGMin,totalDMGMid,totalDMGMax)
    totalARP = staticARP + changeARP
    if totalARP < 0:
        totalARP = 0
    totalHP = staticHP + changeHP
    # if totalHP < totalHP/2:
    #     totalHP += secondBreathAttInt*2
    if totalHP < 0:
        totalHP = 0
    totalRegenHP = staticRegenHP + changeRegenHP
    if totalRegenHP < 0:
        totalRegenHP = 0
    totalEvade = staticEvade + changeEvade
    if totalEvade < 0:
        totalEvade = 0
    totalArmor = staticArmor + changeArmor
    if totalArmor < 0:
        totalArmor = 0
    totalMgicArmor = staticMgicArmor + changeMgicArmor
    if totalMgicArmor < 0:
        totalMgicArmor = 0
    totalMP = staticMP + changeMP
    if totalMP < 0:
        totalMP = 0
    totalRegenMP = staticRegenMP + changeRegenMP
    if totalRegenMP < 0:
        totalRegenMP = 0
    totalSpellPenetration = staticSpellPenetration + changeSpellPenetration
    if totalSpellPenetration < 0:
        totalSpellPenetration = 0
    totalDirectMagicDMG = staticDirectMagicDMG + changeDirectMagicDMG
    if totalDirectMagicDMG < 0:
        totalDirectMagicDMG = 0
    totalPeriodicMagicDMG = staticPeriodicMagicDMG + changePeriodicMagicDMG
    if totalPeriodicMagicDMG < 0:
        totalPeriodicMagicDMG = 0

    totalEnergyLabel.config(text = '{0}'.format(totalEnergy))
    totalRegenEnergyLabel.config(text = '{0}'.format(totalRegenEnergy))
    totalHasteLabel.config(text = '{0}'.format(totalHaste))
    totalHitLabel.config(text = '{0}'.format(totalHit))
    totalAttackLabel.config(text = '{0}'.format(totalAttack))
    totalDMGLabel.config(text = '{0}'.format(totalDMG))
    totalARPLabel.config(text = '{0}'.format(totalARP))
    totalHPLabel.config(text = '{0}'.format(totalHP))
    totalRegenHPLabel.config(text = '{0}'.format(totalRegenHP))
    totalEvadeLabel.config(text = '{0}'.format(totalEvade))
    totalArmorLabel.config(text = '{0}'.format(totalArmor))
    totalMgicArmorLabel.config(text = '{0}'.format(totalMgicArmor))
    totalMPLabel.config(text = '{0}'.format(totalMP))
    totalRegenMPLabel.config(text = '{0}'.format(totalRegenMP))
    totalSpellPenetrationLabel.config(text = '{0}'.format(totalSpellPenetration))
    totalDirectMagicDMGLabel.config(text = '{0}'.format(totalDirectMagicDMG))
    totalPeriodicMagicDMGLabel.config(text = '{0}'.format(totalPeriodicMagicDMG))

# all vars
lvlNow = 1
expNow = 0
repLvl = 0
repExp = 0
allAtt = 12
OPTIONS = list(support['race'].keys())
allMagicSchool = list(support['magic'].keys())
list_lvl = list_lvlExp()
language = 'Общий'
firstSchMag = allMagicSchool[0]
secondSchMag = allMagicSchool[0]

# status att
staticEnergy = 1
staticRegenEnergy = 0
staticHaste = 0
staticHit = 0
staticAttack = '0-0-0'
staticDMG = '0-0-0'
staticARP = 0
staticHP = 5
staticRegenHP = 0
staticEvade = 0
staticArmor = 0
staticMgicArmor = 0
staticMP = 1
staticRegenMP = 0
staticSpellPenetration = 0
staticDirectMagicDMG = 0
staticPeriodicMagicDMG = 0

changeEnergy = 0
changeRegenEnergy = 0
changeHaste = 0
changeHit = 0
changeAttack = staticAttack
changeDMG = staticDMG
changeARP = 0
changeHP = 0
changeRegenHP = 0
changeEvade = 0
changeArmor = 0
changeMgicArmor = 0
changeMP = 0
changeRegenMP = 0
changeSpellPenetration = 0
changeDirectMagicDMG = 0
changePeriodicMagicDMG = 0

totalEnergy = staticEnergy
totalRegenEnergy = staticRegenEnergy
totalHaste = staticHaste
totalHit = staticHit
totalAttack = staticAttack
totalDMG = staticDMG
totalARP = staticARP
totalHP = staticHP
totalRegenHP = staticRegenHP
totalEvade = staticEvade
totalArmor = staticArmor
totalMgicArmor = staticMgicArmor
totalMP = staticMP
totalRegenMP = staticRegenMP
totalSpellPenetration = staticSpellPenetration
totalDirectMagicDMG = staticDirectMagicDMG
totalPeriodicMagicDMG = staticPeriodicMagicDMG

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

skillProgressInt1 = 0
skillProgressInt2 = 0
skillProgressInt3 = 0
skillProgressInt4 = 0
skillProgressInt5 = 0
skillProgressInt6 = 0
skillProgressInt7 = 0
skillProgressInt8 = 0
skillProgressInt9 = 0
skillProgressInt10 = 0

skillLevelInt1 = 0
skillLevelInt2 = 0
skillLevelInt3 = 0
skillLevelInt4 = 0
skillLevelInt5 = 0
skillLevelInt6 = 0
skillLevelInt7 = 0
skillLevelInt8 = 0
skillLevelInt9 = 0
skillLevelInt10 = 0

# inventory
rightHandEnergy = 0
rightHandRegenEnergy = 0
rightHandHaste = 0
rightHandHit = 0
rightHandAttack = 0
rightHandMinAttack = 0
rightHandMidAttack = 0
rightHandMaxAttack = 0
rightHandMinDMG = 0
rightHandMidDMG = 0
rightHandMaxDMG = 0
rightHandDMG = 0
rightHandARP = 0
rightHandHP = 0
rightHandRegenHP = 0
rightHandEvade = 0
rightHandArmor = 0
rightHandMgicArmor = 0
rightHandMP = 0
rightHandRegenMP = 0
rightHandSpellPenetration = 0
rightHandDirectMagicDMG = 0
rightHandPeriodicMagicDMG = 0

rightHandCharmEnergy = 0
rightHandCharmRegenEnergy = 0
rightHandCharmHaste = 0
rightHandCharmHit = 0
rightHandCharmAttack = 0
rightHandCharmMinAttack = 0
rightHandCharmMidAttack = 0
rightHandCharmMaxAttack = 0
rightHandCharmMinDMG = 0
rightHandCharmMidDMG = 0
rightHandCharmMaxDMG = 0
rightHandCharmDMG = 0
rightHandCharmARP = 0
rightHandCharmHP = 0
rightHandCharmRegenHP = 0
rightHandCharmEvade = 0
rightHandCharmArmor = 0
rightHandCharmMgicArmor = 0
rightHandCharmMP = 0
rightHandCharmRegenMP = 0
rightHandCharmSpellPenetration = 0
rightHandCharmDirectMagicDMG = 0
rightHandCharmPeriodicMagicDMG = 0

leftHandEnergy = 0
leftHandRegenEnergy = 0
leftHandHaste = 0
leftHandHit = 0
leftHandAttack = 0
leftHandMinAttack = 0
leftHandMidAttack = 0
leftHandMaxAttack = 0
leftHandMinDMG = 0
leftHandMidDMG = 0
leftHandMaxDMG = 0
leftHandDMG = 0
leftHandARP = 0
leftHandHP = 0
leftHandRegenHP = 0
leftHandEvade = 0
leftHandArmor = 0
leftHandMgicArmor = 0
leftHandMP = 0
leftHandRegenMP = 0
leftHandSpellPenetration = 0
leftHandDirectMagicDMG = 0
leftHandPeriodicMagicDMG = 0

leftHandCharmEnergy = 0
leftHandCharmRegenEnergy = 0
leftHandCharmHaste = 0
leftHandCharmHit = 0
leftHandCharmAttack = 0
leftHandCharmMinAttack = 0
leftHandCharmMidAttack = 0
leftHandCharmMaxAttack = 0
leftHandCharmMinDMG = 0
leftHandCharmMidDMG = 0
leftHandCharmMaxDMG = 0
leftHandCharmDMG = 0
leftHandCharmARP = 0
leftHandCharmHP = 0
leftHandCharmRegenHP = 0
leftHandCharmEvade = 0
leftHandCharmArmor = 0
leftHandCharmMgicArmor = 0
leftHandCharmMP = 0
leftHandCharmRegenMP = 0
leftHandCharmSpellPenetration = 0
leftHandCharmDirectMagicDMG = 0
leftHandCharmPeriodicMagicDMG = 0

ChestEnergy = 0
ChestRegenEnergy = 0
ChestHaste = 0
ChestHit = 0
ChestAttack = 0
ChestMinAttack = 0
ChestMidAttack = 0
ChestMaxAttack = 0
ChestMinDMG = 0
ChestMidDMG = 0
ChestMaxDMG = 0
ChestDMG = 0
ChestARP = 0
ChestHP = 0
ChestRegenHP = 0
ChestEvade = 0
ChestArmor = 0
ChestMgicArmor = 0
ChestMP = 0
ChestRegenMP = 0
ChestSpellPenetration = 0
ChestDirectMagicDMG = 0
ChestPeriodicMagicDMG = 0

ChestCharmEnergy = 0
ChestCharmRegenEnergy = 0
ChestCharmHaste = 0
ChestCharmHit = 0
ChestCharmAttack = 0
ChestCharmMinAttack = 0
ChestCharmMidAttack = 0
ChestCharmMaxAttack = 0
ChestCharmMinDMG = 0
ChestCharmMidDMG = 0
ChestCharmMaxDMG = 0
ChestCharmDMG = 0
ChestCharmARP = 0
ChestCharmHP = 0
ChestCharmRegenHP = 0
ChestCharmEvade = 0
ChestCharmArmor = 0
ChestCharmMgicArmor = 0
ChestCharmMP = 0
ChestCharmRegenMP = 0
ChestCharmSpellPenetration = 0
ChestCharmDirectMagicDMG = 0
ChestCharmPeriodicMagicDMG = 0

amuletEnergy = 0
amuletRegenEnergy = 0
amuletHaste = 0
amuletHit = 0
amuletAttack = 0
amuletMinAttack = 0
amuletMidAttack = 0
amuletMaxAttack = 0
amuletMinDMG = 0
amuletMidDMG = 0
amuletMaxDMG = 0
amuletDMG = 0
amuletARP = 0
amuletHP = 0
amuletRegenHP = 0
amuletEvade = 0
amuletArmor = 0
amuletMgicArmor = 0
amuletMP = 0
amuletRegenMP = 0
amuletSpellPenetration = 0
amuletDirectMagicDMG = 0
amuletPeriodicMagicDMG = 0

amuletCharmEnergy = 0
amuletCharmRegenEnergy = 0
amuletCharmHaste = 0
amuletCharmHit = 0
amuletCharmAttack = 0
amuletCharmMinAttack = 0
amuletCharmMidAttack = 0
amuletCharmMaxAttack = 0
amuletCharmMinDMG = 0
amuletCharmMidDMG = 0
amuletCharmMaxDMG = 0
amuletCharmDMG = 0
amuletCharmARP = 0
amuletCharmHP = 0
amuletCharmRegenHP = 0
amuletCharmEvade = 0
amuletCharmArmor = 0
amuletCharmMgicArmor = 0
amuletCharmMP = 0
amuletCharmRegenMP = 0
amuletCharmSpellPenetration = 0
amuletCharmDirectMagicDMG = 0
amuletCharmPeriodicMagicDMG = 0

ringEnergy = 0
ringRegenEnergy = 0
ringHaste = 0
ringHit = 0
ringAttack = 0
ringMinAttack = 0
ringMidAttack = 0
ringMaxAttack = 0
ringMinDMG = 0
ringMidDMG = 0
ringMaxDMG = 0
ringDMG = 0
ringARP = 0
ringHP = 0
ringRegenHP = 0
ringEvade = 0
ringArmor = 0
ringMgicArmor = 0
ringMP = 0
ringRegenMP = 0
ringSpellPenetration = 0
ringDirectMagicDMG = 0
ringPeriodicMagicDMG = 0

ringCharmEnergy = 0
ringCharmRegenEnergy = 0
ringCharmHaste = 0
ringCharmHit = 0
ringCharmAttack = 0
ringCharmMinAttack = 0
ringCharmMidAttack = 0
ringCharmMaxAttack = 0
ringCharmMinDMG = 0
ringCharmMidDMG = 0
ringCharmMaxDMG = 0
ringCharmDMG = 0
ringCharmARP = 0
ringCharmHP = 0
ringCharmRegenHP = 0
ringCharmEvade = 0
ringCharmArmor = 0
ringCharmMgicArmor = 0
ringCharmMP = 0
ringCharmRegenMP = 0
ringCharmSpellPenetration = 0
ringCharmDirectMagicDMG = 0
ringCharmPeriodicMagicDMG = 0

bookEnergy = 0
bookRegenEnergy = 0
bookHaste = 0
bookHit = 0
bookAttack = 0
bookMinAttack = 0
bookMidAttack = 0
bookMaxAttack = 0
bookMinDMG = 0
bookMidDMG = 0
bookMaxDMG = 0
bookDMG = 0
bookARP = 0
bookHP = 0
bookRegenHP = 0
bookEvade = 0
bookArmor = 0
bookMgicArmor = 0
bookMP = 0
bookRegenMP = 0
bookSpellPenetration = 0
bookDirectMagicDMG = 0
bookPeriodicMagicDMG = 0

bookCharmEnergy = 0
bookCharmRegenEnergy = 0
bookCharmHaste = 0
bookCharmHit = 0
bookCharmAttack = 0
bookCharmMinAttack = 0
bookCharmMidAttack = 0
bookCharmMaxAttack = 0
bookCharmMinDMG = 0
bookCharmMidDMG = 0
bookCharmMaxDMG = 0
bookCharmDMG = 0
bookCharmARP = 0
bookCharmHP = 0
bookCharmRegenHP = 0
bookCharmEvade = 0
bookCharmArmor = 0
bookCharmMgicArmor = 0
bookCharmMP = 0
bookCharmRegenMP = 0
bookCharmSpellPenetration = 0
bookCharmDirectMagicDMG = 0
bookCharmPeriodicMagicDMG = 0



window = Tk() #sozdanie okna
window.title('Лист персонажа.') #Присвоение окну тайтла
window.resizable(width=False, height=False) #Запрет на изменение размеров окна
window.rowconfigure(0, pad=3)
window.rowconfigure(1, pad=3)
window.columnconfigure(0, pad=3)
window.columnconfigure(1, pad=3)
window.columnconfigure(2, pad=3)

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
repLabel = Label(frame2, text='Уровень репутации:')
repLabel2 = Label(frame2, text='{0}'.format(repLvl))
raceLabel = Label(frame2, text='Раса:')
raceLabel2 = Label(frame2, text='{0}'.format(raceVar.get()))
raceADD = Button(frame2, command=create_race_window, text='Выбрать расу')
magicButt = Button(frame2, command=create_magic_window, text='Магия')
activeAbilButt = Button(frame2, command=create_active_skill_window, text='Активные умения')
passiveAbilButt = Button(frame2, command=create_active_skill_window, text='Пассивки')
lanLabel = Label(frame2, text='Языки:')
lanAttLabel = Label(frame2, text=language)

CreateToolTip(raceLabel2,support['race'][OPTIONS[0]]['tooltip'])

persLable.grid(row=0, column=0, columnspan=3)
loginLabel.grid(row=1, column=0)
login.grid(row=1, column=1, columnspan=2)
levelLabel.grid(row=2, column=0)
levelLabel2.grid(row=2, column=1, columnspan=2)
repLabel.grid(row=3, column=0)
repLabel2.grid(row=3, column=1, columnspan=2)
lanLabel.grid(row=4, column=0)
lanAttLabel.grid(row=4, column=1, columnspan=2)
raceLabel.grid(row=5, column=0)
raceLabel2.grid(row=5, column=1)
raceADD.grid(row=5,column=2)
activeAbilButt.grid(row=6, column=0)
magicButt.grid(row=6, column=1)
passiveAbilButt.grid(row=6, column=2)
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
repExpNowLabel = Label(frame3, text='Текущее количество репутации:')
repExpNowAttLabel = Label(frame3, text='{0}'.format(repExp))
addExpLabel = Label(frame3, text='Добавить опыт:')
addExp = Entry(frame3)
addRepLabel = Label(frame3, text='Добавить репу:')
addRep = Entry(frame3)
addExpButt = Button(frame3, command=new_exp, text='Прокачаться!')


availableAtt.grid(row=0, column=0, columnspan=2)
availableAttNumb.grid(row=0, column=2)
changeAtt.grid(row=1, column=0, columnspan=3)
expNowLabel.grid(row=2, column=0, columnspan=2)
expNowAttLabel.grid(row=2, column=2)
repExpNowLabel.grid(row=3, column=0, columnspan=2)
repExpNowAttLabel.grid(row=3, column=2)
addExpLabel.grid(row=4, column=0)
addExp.grid(row=4, column=1, columnspan=2)
addRepLabel.grid(row=5, column=0)
addRep.grid(row=5, column=1, columnspan=2)
addExpButt.grid(row=6, column=0, columnspan=3)

# stats
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
frame4.columnconfigure(2, pad=3)
frame4.columnconfigure(3, pad=3)
frame4.columnconfigure(4, pad=3)
frame4.columnconfigure(5, pad=3)
frame4.columnconfigure(6, pad=3)
frame4.columnconfigure(7, pad=3)
frame4.columnconfigure(8, pad=3)
frame4.columnconfigure(9, pad=3)
frame4.columnconfigure(10, pad=3)
frame4.columnconfigure(11, pad=3)
frame4.columnconfigure(12, pad=3)
frame4.columnconfigure(13, pad=3)
frame4.columnconfigure(14, pad=3)
frame4.columnconfigure(15, pad=3)
frame4.columnconfigure(16, pad=3)
frame4.columnconfigure(17, pad=3)
frame4.grid(row=1, column=0, columnspan=3)

parametrList = ['Энергия',
                'Регенерация\nЭнергии',
                'Скорость',
                'Меткость',
                'Урон\nближний',
                'Урон\nдальний',
                'АРП',
                'ХП',
                'Регенерация\nХП',
                'Уклонение',
                'Броня',
                'Броня от\nмагии',
                'МП',
                'Регенерация\nМП',
                'Магическое\nпроникновение',
                'Прямой\nмаг.урон',
                'Период\nмаг.урон']

# columnParam = 0
# for param in parametrList:
#     Label(frame4, text = param).grid(row=0, column=columnParam)
#     columnParam+=1
Label(frame4, text = 'Параметр').grid(row=0, column=0)
create_labels(frame4,1,parametrList,0)
Label(frame4, text = 'Статус').grid(row=1, column=0)
Label(frame4, text = 'Изменения').grid(row=2, column=0)
Label(frame4, text = 'Текущий итог').grid(row=3, column=0)

staticEnergyLabel = Label(frame4, text = '{0}'.format(staticEnergy))
staticRegenEnergyLabel = Label(frame4, text = '{0}'.format(staticRegenEnergy))
staticHasteLabel = Label(frame4, text = '{0}'.format(staticHaste))
staticHitLabel = Label(frame4, text = '{0}'.format(staticHit))
staticAttackLabel = Label(frame4, text = '{0}'.format(staticAttack))
staticDMGLabel = Label(frame4, text = '{0}'.format(staticDMG))
staticARPLabel = Label(frame4, text = '{0}'.format(staticARP))
staticHPLabel = Label(frame4, text = '{0}'.format(staticHP))
staticRegenHPLabel = Label(frame4, text = '{0}'.format(staticRegenHP))
staticEvadeLabel = Label(frame4, text = '{0}'.format(staticEvade))
staticArmorLabel = Label(frame4, text = '{0}'.format(staticArmor))
staticMgicArmorLabel = Label(frame4, text = '{0}'.format(staticMgicArmor))
staticMPLabel = Label(frame4, text = '{0}'.format(staticMP))
staticRegenMPLabel = Label(frame4, text = '{0}'.format(staticRegenMP))
staticSpellPenetrationLabel = Label(frame4, text = '{0}'.format(staticSpellPenetration))
staticDirectMagicDMGLabel = Label(frame4, text = '{0}'.format(staticDirectMagicDMG))
staticPeriodicMagicDMGLabel = Label(frame4, text = '{0}'.format(staticPeriodicMagicDMG))

staticEnergyLabel.grid(row=1, column=1)
staticRegenEnergyLabel.grid(row=1, column=2)
staticHasteLabel.grid(row=1, column=3)
staticHitLabel.grid(row=1, column=4)
staticAttackLabel.grid(row=1, column=5)
staticDMGLabel.grid(row=1, column=6)
staticARPLabel.grid(row=1, column=7)
staticHPLabel.grid(row=1, column=8)
staticRegenHPLabel.grid(row=1, column=9)
staticEvadeLabel.grid(row=1, column=10)
staticArmorLabel.grid(row=1, column=11)
staticMgicArmorLabel.grid(row=1, column=12)
staticMPLabel.grid(row=1, column=13)
staticRegenMPLabel.grid(row=1, column=14)
staticSpellPenetrationLabel.grid(row=1, column=15)
staticDirectMagicDMGLabel.grid(row=1, column=16)
staticPeriodicMagicDMGLabel.grid(row=1, column=17)

changeEnergyLabel = Entry(frame4,width=8)
changeRegenEnergyLabel = Entry(frame4,width=8)
changeHasteLabel = Entry(frame4,width=8)
changeHitLabel = Entry(frame4,width=8)
changeAttackLabel = Entry(frame4,width=8)
changeDMGLabel = Entry(frame4,width=8)
changeARPLabel = Entry(frame4,width=8)
changeHPLabel = Entry(frame4,width=8)
changeRegenHPLabel = Entry(frame4,width=8)
changeEvadeLabel = Entry(frame4,width=8)
changeArmorLabel = Entry(frame4,width=8)
changeMgicArmorLabel = Entry(frame4,width=8)
changeMPLabel = Entry(frame4,width=8)
changeRegenMPLabel = Entry(frame4,width=8)
changeSpellPenetrationLabel = Entry(frame4,width=8)
changeDirectMagicDMGLabel = Entry(frame4,width=8)
changePeriodicMagicDMGLabel = Entry(frame4,width=8)

changeEnergyLabel.bind('<Return>', sum_stats)
changeRegenEnergyLabel.bind('<Return>', sum_stats)
changeHasteLabel.bind('<Return>', sum_stats)
changeHitLabel.bind('<Return>', sum_stats)
changeAttackLabel.bind('<Return>', sum_stats)
changeDMGLabel.bind('<Return>', sum_stats)
changeARPLabel.bind('<Return>', sum_stats)
changeHPLabel.bind('<Return>', sum_stats)
changeRegenHPLabel.bind('<Return>', sum_stats)
changeEvadeLabel.bind('<Return>', sum_stats)
changeArmorLabel.bind('<Return>', sum_stats)
changeMgicArmorLabel.bind('<Return>', sum_stats)
changeMPLabel.bind('<Return>', sum_stats)
changeRegenMPLabel.bind('<Return>', sum_stats)
changeSpellPenetrationLabel.bind('<Return>', sum_stats)
changeDirectMagicDMGLabel.bind('<Return>', sum_stats)
changePeriodicMagicDMGLabel.bind('<Return>', sum_stats)

changeEnergyLabel.grid(row=2, column=1)
changeRegenEnergyLabel.grid(row=2, column=2)
changeHasteLabel.grid(row=2, column=3)
changeHitLabel.grid(row=2, column=4)
changeAttackLabel.grid(row=2, column=5)
changeDMGLabel.grid(row=2, column=6)
changeARPLabel.grid(row=2, column=7)
changeHPLabel.grid(row=2, column=8)
changeRegenHPLabel.grid(row=2, column=9)
changeEvadeLabel.grid(row=2, column=10)
changeArmorLabel.grid(row=2, column=11)
changeMgicArmorLabel.grid(row=2, column=12)
changeMPLabel.grid(row=2, column=13)
changeRegenMPLabel.grid(row=2, column=14)
changeSpellPenetrationLabel.grid(row=2, column=15)
changeDirectMagicDMGLabel.grid(row=2, column=16)
changePeriodicMagicDMGLabel.grid(row=2, column=17)

totalEnergyLabel = Label(frame4, text = '{0}'.format(totalEnergy))
totalRegenEnergyLabel = Label(frame4, text = '{0}'.format(totalRegenEnergy))
totalHasteLabel = Label(frame4, text = '{0}'.format(totalHaste))
totalHitLabel = Label(frame4, text = '{0}'.format(totalHit))
totalAttackLabel = Label(frame4, text = '{0}'.format(totalAttack))
totalDMGLabel = Label(frame4, text = '{0}'.format(totalDMG))
totalARPLabel = Label(frame4, text = '{0}'.format(totalARP))
totalHPLabel = Label(frame4, text = '{0}'.format(totalHP))
totalRegenHPLabel = Label(frame4, text = '{0}'.format(totalRegenHP))
totalEvadeLabel = Label(frame4, text = '{0}'.format(totalEvade))
totalArmorLabel = Label(frame4, text = '{0}'.format(totalArmor))
totalMgicArmorLabel = Label(frame4, text = '{0}'.format(totalMgicArmor))
totalMPLabel = Label(frame4, text = '{0}'.format(totalMP))
totalRegenMPLabel = Label(frame4, text = '{0}'.format(totalRegenMP))
totalSpellPenetrationLabel = Label(frame4, text = '{0}'.format(totalSpellPenetration))
totalDirectMagicDMGLabel = Label(frame4, text = '{0}'.format(totalDirectMagicDMG))
totalPeriodicMagicDMGLabel = Label(frame4, text = '{0}'.format(totalPeriodicMagicDMG))

totalEnergyLabel.grid(row=3, column=1)
totalRegenEnergyLabel.grid(row=3, column=2)
totalHasteLabel.grid(row=3, column=3)
totalHitLabel.grid(row=3, column=4)
totalAttackLabel.grid(row=3, column=5)
totalDMGLabel.grid(row=3, column=6)
totalARPLabel.grid(row=3, column=7)
totalHPLabel.grid(row=3, column=8)
totalRegenHPLabel.grid(row=3, column=9)
totalEvadeLabel.grid(row=3, column=10)
totalArmorLabel.grid(row=3, column=11)
totalMgicArmorLabel.grid(row=3, column=12)
totalMPLabel.grid(row=3, column=13)
totalRegenMPLabel.grid(row=3, column=14)
totalSpellPenetrationLabel.grid(row=3, column=15)
totalDirectMagicDMGLabel.grid(row=3, column=16)
totalPeriodicMagicDMGLabel.grid(row=3, column=17)

frame5=Frame(window, relief=RAISED, borderwidth=1)
frame5.rowconfigure(0, pad=3)
frame5.columnconfigure(0, pad=3)
frame5.grid(row=0, column=2)

Button(frame5, command=create_inventory_window, text='Инвентарь').grid(row=0, column=0)

window.mainloop()
