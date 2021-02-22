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
    global allAtt, meleFightAttInt,shootAttInt,strongHitsAttInt,warBusinessAttInt,tacticsAttInt,attackAttInt,evasionAttInt,hasteAttInt,coldBloodAttInt,firstAidAttInt,manaAttInt,thiefArtAttInt,magicCircleAttInt,magicPowerAttInt,learningAttInt,healthAttInt,energyAttInt,resistAttInt,secondBreathAttInt,steelBodyAttInt,magicCircleAttLabel,magicCircleAttLabel2,spell211LVLLabel,spell212LVLLabel,spell221LVLLabel,spell222LVLLabel,spell231LVLLabel,spell232LVLLabel,spell241LVLLabel,spell242LVLLabel,spell251LVLLabel,spell252LVLLabel,spell11LVLLabel,spell12LVLLabel,spell21LVLLabel,spell22LVLLabel,spell31LVLLabel,spell32LVLLabel,spell41LVLLabel,spell42LVLLabel,spell51LVLLabel,spell52LVLLabel,staticEnergy,staticRegenEnergy,staticHaste,staticAttack,staticDMG,staticHP,staticRegenHP,staticEvade,staticDMG,staticMP,staticRegenMP,staticDirectMagicDMG,staticPeriodicMagicDMG,totalEnergy,totalRegenEnergy,totalHaste,totalAttack,totalDMG,totalHP,totalRegenHP,totalEvade,totalDMG,totalMP,totalRegenMP,totalDirectMagicDMG,totalPeriodicMagicDMG,totalSpellPenetration,staticSpellPenetration,staticEnergyLabel,staticDMGLabel,staticAttackLabel,staticDMGLabel,staticEvadeLabel,staticHasteLabel,staticMPLabel,staticRegenMPLabel,staticDirectMagicDMGLabel,staticSpellPenetrationLabel,staticHPLabel,staticRegenHPLabel,staticPeriodicMagicDMG,staticPeriodicMagicDMGLabel,totalEnergy,totalRegenEnergy,totalHaste,totalAttack,totalDMG,totalARP,totalHP,totalRegenHP,totalEvade,totalArmor,totalMgicArmor,totalMP,totalRegenMP,totalSpellPenetration,totalDirectMagicDMG,totalPeriodicMagicDMG,totalAttackLabel,totalDMGLabel,totalEvadeLabel,totalHasteLabel,totalMPLabel,totalRegenMPLabel,totalDirectMagicDMGLabel,totalSpellPenetrationLabel,totalPeriodicMagicDMGLabel,totalHPLabel,totalRegenHPLabel


    if allAtt > 0:
        if num == 0:
            if meleFightAttInt < 5:
                meleFightAttInt += 1
                staticAttack += 1
                allAtt -= 1
                totalAttack = staticAttack + changeAttack
                widget.config(text='{0}'.format(meleFightAttInt))
                staticAttackLabel.config(text = '{0}'.format(staticAttack))
                totalAttackLabel.config(text = '{0}'.format(totalAttack))
        elif num == 1:
            if shootAttInt < 5:
                shootAttInt += 1
                staticDMG += 1
                allAtt -= 1
                totalDMG = staticDMG + changeDMG
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
                staticAttack += 1
                staticDMG += 1
                allAtt -= 1
                totalAttack = staticAttack + changeAttack
                totalDMG = staticDMG + changeDMG
                widget.config(text='{0}'.format(attackAttInt))
                staticAttackLabel.config(text = '{0}'.format(staticAttack))
                staticDMGLabel.config(text = '{0}'.format(staticDMG))
                totalAttackLabel.config(text = '{0}'.format(totalAttack))
                totalDMGLabel.config(text = '{0}'.format(totalDMG))
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
    ChoInv = Toplevel(window)
    ChoInv.title('Школы магии')
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

    Label(ChoInv, text = 'Слот').grid(row=0, column=0)
    create_labels(ChoInv,1,parametrList)

def create_labels(frame,columnParam,list):
    for param in list:
        Label(frame, text = param).grid(row=0, column=columnParam)
        columnParam+=1


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
staticAttack = 0
staticDMG = 0
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
changeAttack = 0
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
create_labels(frame4,1,parametrList)
Label(frame4, text = 'Статус').grid(row=1, column=0)
Label(frame4, text = 'Изменения').grid(row=2, column=0)
Label(frame4, text = 'Текущий итог').grid(row=3, column=0)

staticEnergyLabel = Label(frame4, text = '{0}'.format(staticEnergy))
staticRegenEnergyLabel = Label(frame4, text = '{0}'.format(staticRegenEnergy))
staticHasteLabel = Label(frame4, text = '{0}'.format(staticHaste))
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
staticAttackLabel.grid(row=1, column=4)
staticDMGLabel.grid(row=1, column=5)
staticARPLabel.grid(row=1, column=6)
staticHPLabel.grid(row=1, column=7)
staticRegenHPLabel.grid(row=1, column=8)
staticEvadeLabel.grid(row=1, column=9)
staticArmorLabel.grid(row=1, column=10)
staticMgicArmorLabel.grid(row=1, column=11)
staticMPLabel.grid(row=1, column=12)
staticRegenMPLabel.grid(row=1, column=13)
staticSpellPenetrationLabel.grid(row=1, column=14)
staticDirectMagicDMGLabel.grid(row=1, column=15)
staticPeriodicMagicDMGLabel.grid(row=1, column=16)

changeEnergyLabel = Entry(frame4,width=8)
changeRegenEnergyLabel = Entry(frame4,width=8)
changeHasteLabel = Entry(frame4,width=8)
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

# ADLogin.bind('<Return>', clickReturn)

changeEnergyLabel.grid(row=2, column=1)
changeRegenEnergyLabel.grid(row=2, column=2)
changeHasteLabel.grid(row=2, column=3)
changeAttackLabel.grid(row=2, column=4)
changeDMGLabel.grid(row=2, column=5)
changeARPLabel.grid(row=2, column=6)
changeHPLabel.grid(row=2, column=7)
changeRegenHPLabel.grid(row=2, column=8)
changeEvadeLabel.grid(row=2, column=9)
changeArmorLabel.grid(row=2, column=10)
changeMgicArmorLabel.grid(row=2, column=11)
changeMPLabel.grid(row=2, column=12)
changeRegenMPLabel.grid(row=2, column=13)
changeSpellPenetrationLabel.grid(row=2, column=14)
changeDirectMagicDMGLabel.grid(row=2, column=15)
changePeriodicMagicDMGLabel.grid(row=2, column=16)

totalEnergyLabel = Label(frame4, text = '{0}'.format(totalEnergy))
totalRegenEnergyLabel = Label(frame4, text = '{0}'.format(totalRegenEnergy))
totalHasteLabel = Label(frame4, text = '{0}'.format(totalHaste))
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
totalAttackLabel.grid(row=3, column=4)
totalDMGLabel.grid(row=3, column=5)
totalARPLabel.grid(row=3, column=6)
totalHPLabel.grid(row=3, column=7)
totalRegenHPLabel.grid(row=3, column=8)
totalEvadeLabel.grid(row=3, column=9)
totalArmorLabel.grid(row=3, column=10)
totalMgicArmorLabel.grid(row=3, column=11)
totalMPLabel.grid(row=3, column=12)
totalRegenMPLabel.grid(row=3, column=13)
totalSpellPenetrationLabel.grid(row=3, column=14)
totalDirectMagicDMGLabel.grid(row=3, column=15)
totalPeriodicMagicDMGLabel.grid(row=3, column=16)

frame5=Frame(window, relief=RAISED, borderwidth=1)
frame5.rowconfigure(0, pad=3)
frame5.columnconfigure(0, pad=3)
frame5.grid(row=0, column=2)

Button(frame5, command=create_inventory_window, text='Инвентарь').grid(row=0, column=0)

window.mainloop()
