numero1= int(input("Scrivi i gradi"))
numero2= int(input("Umidità in %"))
tempo1= "bello"
tempo2= "brutto"
tempo3= "nuvoloso"
warning1= "attenzione"
warning2= "tuoni"
warning3= "zanzare"
if (numero1 > 25 and numero2 > 90 and tempo1 and tempo3 or tempo2 ):
    print ("si può uscire ma", warning1, warning3.upper()  )
elif (numero1 < 25 and numero2 > 90 and tempo2 or tempo3):
    print ("non si può uscire e", warning1.upper(), warning2.upper())
elif (numero1 > 25 and numero2 <90 and tempo1 ):
    print ("andiamo tutti al mare")
elif (numero1 < 25 and numero2 < 90  and tempo1):
    print("si può uscire")
else:
    print("fine del mondo")
