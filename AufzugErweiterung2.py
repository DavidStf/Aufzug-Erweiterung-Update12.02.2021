class Aufzug():
   
    #Atributte
    def __init__(self,bezeichnung,maxKapazität,tiefsteEtage,aktuelleEtage,höchsteEtage,aktuelleAnzahlPersonen,Türauf,):
        self.bezeichnung= bezeichnung
        self.maxKapazität=maxKapazität
        self.tiefsteEtage=tiefsteEtage
        self.aktuelleEtage=aktuelleEtage
        self.höchsteEtage= höchsteEtage
        self.aktuelleAnzahlPersonen=aktuelleAnzahlPersonen
        self.Türauf=False

    #Methode
    def einsteigenPerson(self,person):
        self.Türauf = True
        print(":Die Tür geht auf:",self.Türauf)
        self.aktuelleAnzahlPersonen +=person
        print(self.aktuelleAnzahlPersonen,"Person(en) ist(sind) eingestiegen")
        
        if self.aktuelleAnzahlPersonen > self.maxKapazität:
            self.aktuelleAnzahlPersonen -=person
            print("Achtung max Kapazität erreicht!!")
        print("\n")
         

    def aussteigenPerson(self,person):
        self.Türauf = True
        print("Die Tür geht auf:",self.Türauf)
        self.aktuelleAnzahlPersonen -=person
        print("\n")
        if self.aktuelleAnzahlPersonen > 0:
            print("Es ist(sind) nur ",self.aktuelleAnzahlPersonen,"Person(en) im Aufzug")
        else:
            print("Es gibt niemandem mehr !")
            self.aktuelleAnzahlPersonen +=person
      
        

    def hochfahren(self,etage):
        self.aktuelleEtage +=etage
        if self.aktuelleEtage < self.höchsteEtage:
            print("hochfahren","Der Aufzug befinded sich in der ",self.aktuelleEtage,"Etage")
        else:
            print("Es gibt keine Etagen mehr !")
            self.aktuelleEtage -=etage
       

    def runterfahren(self,etage):
        self.aktuelleEtage -=etage
        if self.aktuelleEtage > self.tiefsteEtage:
            print("runterfahren","Der Aufzug befinded sich in der ",self.aktuelleEtage,"Etage")
        else:
            print("Es gibt keine Etagen mehr !")
            self.aktuelleEtage +=etage

    def info(self):
        print("Aufzug Info")
        print("Der Aufzug befinded sich in der ",self.aktuelleEtage,"Etage")
        print("Es ist(sind) nur ",self.aktuelleAnzahlPersonen,"Person(en) im Aufzug")
        
        print(self.aktuelleAnzahlPersonen,"Person(en) ist(sind) eingestiegen")
        
        print("Die Tür ist zu:",self.Türauf)
        #pass
    def anleitung(self):
        print("Es.. ladet.....")
        print("Wählen Sie ein der folgenden Optionen aus:")
        print("-------------------------------------------")
        print(":Für Hochfahren drücken Sie die (1).")
        print(":Für Runterfahren drücken Sie die (2)")
        print(":Für Einsteigen drücken Sie (3)")
        print(":Für Aussteigen drücken Sie (4)")
        print("-------------------------------------------")   


#Kommandos
#Reihenfolge: bezeichnung,maxKapazität,tiefsteEtage,aktuelleEtage,höchsteEtage,aktuelleAnzahlPersonen,Türauf,

aufzug= Aufzug("AufzugNebengebäude",7,4,0,6,0,False)
aufzug.anleitung()
print("\n")
aufzug.info()
Option= int(input("Wählen Sie eine Option aus: "))


if Option == 1:
  aufzug.hochfahren(1)
elif Option == 2:
  aufzug.runterfahren(1)
elif Option ==3:
  aufzug.einsteigenPerson(1)
elif Option == 4:
  aufzug.aussteigenPerson(1)

while True:
    print("\n")
    aufzug.info()
    print("\n")
    aufzug.anleitung()
    weitermachen = input("Wollen Sie noch eine Option auswählen j/n: ")
    print("\n")
    if weitermachen=="j":
        OptionR= int(input("Wählen Sie eine Option aus: "))
        if OptionR == 1:
          aufzug.hochfahren(1)
        elif OptionR ==2:
          aufzug.runterfahren(1)
        elif OptionR ==3:
          aufzug.einsteigenPerson(1)
        elif OptionR == 4:
          aufzug.aussteigenPerson(1)
        continue
    elif weitermachen=="n":
        break
    else:
        print("Bitte geben Sie entwieder  j/n")



  
