NomeUtente=input("ID:")
Password=input("Pass:")
ColorePreferito="verde"
IDreale="Giovanni"
PasswordReale="12345"
if NomeUtente==IDreale and Password==PasswordReale:
    print("Benvenuto")
    print("Inserisci nuova Password:")
    ColorePref=input("ColorePrefer:")
    if ColorePref==ColorePreferito:
        NuovaPassword=input("NuovaPass:")
        NuovaPassword==Password
        print("Password cambiata")
    else:
        print("colore sbagliato")
        

    
else:
    print("Credenziali Errate")

