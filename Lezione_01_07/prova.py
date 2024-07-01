cond= True
x="admin"
y=12345
utente=()

while cond:
     if utente==x and psw==y:
            cond= False
            print("Benvenuto, hai effettuato il login")
     else:
            print("Nome utente o password sbagliati")