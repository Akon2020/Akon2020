from tkinter import *
from tkinter import ttk
from math import *

fenetre=Tk()
fenetre.geometry("320x375")
fenetre.title("Calculatrice")
Result=StringVar()
Result.set("Bienvenu")

calc=StringVar()
calc.set(0)

LongueurB="6"
HauteurB="1"

fenetre["bg"]="#f0f0f0"
Fonts="Cambria, 10"

Resultat=Entry(fenetre,textvariable=Result, bg="ivory")
Sol=Listbox(fenetre, justify=CENTER, font="Arial 12 italic")
Calcul=Entry(fenetre,textvariable=calc, bg="ivory")

Vlist=["grades", "dégrés", "radians"]

def Change() :
	pass

Combo=ttk.Combobox(fenetre, values=Vlist)
Combo1=ttk.Combobox(fenetre, values=Vlist)
Vers=Label(fenetre, text="vers")

Deg=StringVar()
Deg.set("0")

Vers2=Label(fenetre, textvariable=Deg)


Combo.place(x=18, y=170, width="80")
Combo1.place(x=130, y=170, width="80")
Vers.place(x=100, y=170)
Vers2.place(x=215, y=170)
Combo.current(0)
Combo1.current(0)

convert1="dégrés"
convert3="dégrés"

def convert(event):
	global convert1
	global convert3
	convert1=event.widget.get()

	if convert1=="dégrés" and convert3=="radians" :
		Deg.set((pi/180)*int(Expression))

	if convert1=="dégrés" and convert3=="grades" :
		Deg.set((10/9)*int(Expression))

	if convert1=="radians" and convert3=="dégrés" :
		Deg.set((180/pi)*int(Expression))
	if convert1=="radians" and convert3=="grades":
		Deg.set((200/pi)*int(Expression))
	if convert1=="grades" and convert3=="radians":
		Deg.set((pi/200)*int(Expression))
	if convert1=="grades" and convert3=="dégrés":
		Deg.set((9/10)*int(Expression))

def convert2(event):
	global convert1
	global convert3
	convert3=event.widget.get()

	if convert1=="dégrés" and convert3=="radians" :
		Deg.set((pi/180)*int(Expression))

	if convert1=="dégrés" and convert3=="grades" :
		Deg.set((10/9)*int(Expression))

	if convert1=="radians" and convert3=="dégrés" :
		Deg.set((180/pi)*int(Expression))
	if convert1=="radians" and convert3=="grades":
		Deg.set((200/pi)*int(Expression))
	if convert1=="grades" and convert3=="radians":
		Deg.set((pi/200)*int(Expression))
	if convert1=="grades" and convert3=="dégrés":
		Deg.set((9/10)*int(Expression))
		

Combo.bind("<<ComboboxSelected>>", convert)
Combo1.bind("<<ComboboxSelected>>", convert2)


#Le comboBox



Expression=""

#ListOne=tK.Combobox(fenetre, values=Vlist)





#---------Boutons -------------#

#--------Commandes boutons-------

def calcul():
	Resultat=0


def oneForAll(operat):

	global Expression

	if operat=="racine":
		try:
			if "." in Expression:
				traitement=sqrt(float(calc.get()))
				Sol.insert(0,("√({})=({})".format(Expression,traitement)))
				Expression=str(traitement)
				calc.set(Expression)

			else:
				traitement=sqrt(int(calc.get()))
				Sol.insert(0,("√({})=({})".format(Expression,traitement)))
				Expression=str(traitement)
				calc.set(Expression)
		except :
			pass

	if operat=="carre":
		try:
			if "." in Expression:
				traitement=pow(float(calc.get()),2)
				Sol.insert(0,("({})^2=({})".format(Expression,traitement)))
				Expression=str(traitement)
				calc.set(Expression)

			else:
				traitement=pow(int(calc.get()),2)
				Sol.insert(0,("({})^2=({})".format(Expression,traitement)))
				Expression=str(traitement)
				calc.set(Expression)
		except :
			pass

	if operat=="Pither":
		try:
			if "." in Expression:
				traitement=pi*(float(calc.get()))
				Sol.insert(0,("π({})=({})".format(Expression, traitement)))
				Expression=str(traitement)
				calc.set(Expression)

			else:
				traitement=pi*(int(calc.get()))
				Sol.insert(0,("π({})=({})".format(Expression, traitement)))
				Expression=str(traitement)
				calc.set(Expression)
		except :
			pass

	if operat=="facto":
		try:
			traitement=factorial(int(calc.get()))
			Sol.insert(0,("({})!=({})".format(Expression, traitement)))
			Expression=str(traitement)
			calc.set(Expression)
		except :
			pass
			
	if operat=="Pourcent":
		try:
			if "." in Expression:
				traitement=(float(calc.get()))/100
			else:
				traitement=(int(calc.get()))/100
			Sol.insert(0,("Pourc({})=({})".format(Expression,traitement)))
			Expression=str(traitement)
			calc.set(Expression)
		except :
			pass

def Ajout(Exp):
	calc.set(Exp)
	calcul()

def soluion(bouton):

	global Expression
	
	if bouton=="0" :
	
		if len(calc.get())==0 :
			pass
		else :
			Expression+="0"
			Ajout(Expression)
	
	if bouton=="." :
		Expression+="."
		Ajout(Expression)
	if bouton=="1" :
		Expression+="1"
		Ajout(Expression)

	if bouton=="2" :
		Expression+="2"
		Ajout(Expression)

	if bouton=="3" :
		Expression+="3"
		Ajout(Expression)

	if bouton=="4" :
		Expression+="4"
		Ajout(Expression)

	if bouton=="5" :
		Expression+="5"
		Ajout(Expression)

	if bouton=="6" :
		Expression+="6"
		Ajout(Expression)

	if bouton=="7" :
		Expression+="7"
		Ajout(Expression)

	if bouton=="(" :
		Expression+="("
		Ajout(Expression)

	if bouton=="**" :
		Expression+="**"
		Ajout(Expression)

	if bouton==")" :
		Expression+=")"
		Ajout(Expression)

	if bouton=="8" :
		Expression+="8"
		Ajout(Expression)

	if bouton=="9" :
		Expression+="9"
		Ajout(Expression)

	if bouton=="-" :
		Expression+="-"
		Ajout(Expression)

	if bouton=="+" :
		Expression+="+"
		Ajout(Expression)

	if bouton=="*" :
		Expression+="*"
		Ajout(Expression)

	if bouton=="/" :
		Expression+="/"
		Ajout(Expression)

	if bouton=="%" :
		Expression+="%"
		Ajout(Expression)

def egale():
	global Expression
	try:
		calc.set(eval(str(Expression)))
		Sol.insert(0,Expression+"="+calc.get())
		Expression=calc.get()
	except:
		pass

	#----------------------------------------------

def supprimer():

	global Expression

	Expression=""
	Ajout(Expression)


def Effacer():
	supprimer()
def ParaOuv():
	soluion("(")
def ParaFer():
	soluion(")")
def modulo():
	soluion("%")
def Phi():
	oneForAll("Pither")


def sept():
	soluion("7")
def huit():
	soluion("8")
def neuf():
	soluion("9")
def Div():
	soluion("/")
def Rac():
	oneForAll("racine")
def quatre():
	soluion("4")
def cinq():
	soluion("5")
def six():
	soluion("6")
def mulpti():
	soluion("*")
def exposant():
	oneForAll("carre")

def Un():
	soluion("1")
def deux():
	soluion("2")
def trois():
	soluion("3")
def moins():
	soluion("-")
def Fact():
	oneForAll("facto")


def Zero():
	soluion("0")
def Point():
	soluion(".")
def Modul():
	oneForAll("Pourcent")
def Plus():
	soluion("+")
def Equal():
	egale()
#---------------


BtnEff=Button(fenetre,text="Eff",width=LongueurB, height=HauteurB, font=Fonts, command=Effacer)
BtnOuVP=Button(fenetre,text="(",width=LongueurB, height=HauteurB, font=Fonts, command=ParaOuv)
BtnFermP=Button(fenetre,text=")",width=LongueurB, height=HauteurB, font=Fonts, command=ParaFer)
BtnMod=Button(fenetre,text="Mod",width=LongueurB, height=HauteurB, font=Fonts, command=modulo)
BtnPi=Button(fenetre,text="Pi",width=LongueurB, height=HauteurB, font=Fonts, command=Phi)


Btn7=Button(fenetre,text="7",width=LongueurB, height=HauteurB, font=Fonts, command=sept)
Btn8=Button(fenetre,text="8",width=LongueurB, height=HauteurB, font=Fonts, command=huit)
Btn9=Button(fenetre,text="9",width=LongueurB, height=HauteurB, font=Fonts, command=neuf)
BtnDiv=Button(fenetre,text="/",width=LongueurB, height=HauteurB, font=Fonts, command=Div)
BtnRac=Button(fenetre,text="rac",width=LongueurB, height=HauteurB, font=Fonts, command=Rac)

Btn4=Button(fenetre,text="4",width=LongueurB, height=HauteurB, font=Fonts, command=quatre)
Btn5=Button(fenetre,text="5",width=LongueurB, height=HauteurB, font=Fonts, command=cinq)
Btn6=Button(fenetre,text="6",width=LongueurB, height=HauteurB, font=Fonts, command=six)
BtnMul=Button(fenetre,text="*",width=LongueurB, height=HauteurB, font=Fonts, command=mulpti)
BtnExp=Button(fenetre,text="x^2",width=LongueurB, height=HauteurB, font=Fonts, command=exposant)

BtnUn=Button(fenetre,text="1",width=LongueurB, height=HauteurB, font=Fonts, command=Un)
BtnDeux=Button(fenetre,text="2",width=LongueurB, height=HauteurB, font=Fonts, command=deux)
BtnTrois=Button(fenetre,text="3",width=LongueurB, height=HauteurB, font=Fonts, command=trois)
BtnMoins=Button(fenetre,text="-",width=LongueurB, height=HauteurB, font=Fonts, command=moins)
BtnFactoriel=Button(fenetre,text="x!",width=LongueurB, height=HauteurB, font=Fonts, command=Fact)

BtnZero=Button(fenetre,text="0",width=LongueurB, height=HauteurB, font=Fonts, command=Zero)
BtnPoint=Button(fenetre,text=".",width=LongueurB, height=HauteurB, font=Fonts, command=Point)
BtnMo=Button(fenetre,text="%",width=LongueurB, height=HauteurB, font=Fonts, command=Modul)
BtnPlus=Button(fenetre,text="+",width=LongueurB, height=HauteurB, font=Fonts, command=Plus)
BtnEqual=Button(fenetre,text="=",width=LongueurB, height=HauteurB, font=Fonts, command=Equal)
#--------Sockage des boutons ------------

#ListOne.place(x=18, y=180, width="50")
Ligne1=200

BtnEff.place(x=10,y=Ligne1)
BtnOuVP.place(x=70,y=Ligne1)
BtnFermP.place(x=130,y=Ligne1)
BtnMod.place(x=190,y=Ligne1)
BtnPi.place(x=250,y=Ligne1)

Ligne1=230

Btn7.place(x=10,y=Ligne1)
Btn8.place(x=70,y=Ligne1)
Btn9.place(x=130,y=Ligne1)
BtnDiv.place(x=190,y=Ligne1)
BtnRac.place(x=250,y=Ligne1)

Ligne1=260

Btn4.place(x=10,y=Ligne1)
Btn5.place(x=70,y=Ligne1)
Btn6.place(x=130,y=Ligne1)
BtnMul.place(x=190,y=Ligne1)
BtnExp.place(x=250,y=Ligne1)

Ligne1=290

BtnUn.place(x=10,y=Ligne1)
BtnDeux.place(x=70,y=Ligne1)
BtnTrois.place(x=130,y=Ligne1)
BtnMoins.place(x=190,y=Ligne1)
BtnFactoriel.place(x=250,y=Ligne1)

Ligne1=320

BtnZero.place(x=10,y=Ligne1)
BtnPoint.place(x=70,y=Ligne1)
BtnMo.place(x=130,y=Ligne1)
BtnPlus.place(x=190,y=Ligne1)
BtnEqual.place(x=250,y=Ligne1)



Sol.place(x=10, y=0, height="130", width="298")
Calcul.place(x=18, y=140, height=25, width="280")

fenetre.mainloop()