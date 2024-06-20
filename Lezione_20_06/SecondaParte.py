condizione= True
x=int(input("Scrivi Numero Intero Positivo"))
while condizione:
 for i in range(x,-1,-1):
   print (i) 
 if x==0:
  condizione= False
 else:
  print("Ciclo Finito")
 break