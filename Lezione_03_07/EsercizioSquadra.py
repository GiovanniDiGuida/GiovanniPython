class Membro_Squadra:
    
    def __init__(self,nome,età):

        self.nome=nome
        self.età=età

    def lavora(caratteristiche):

        print("Le sue caratteristiche sono: "+ caratteristiche)

class Giocatore(Membro_Squadra):

    def __init__(self, nome, età, ruolo, numero_maglia):
        super().__init__(nome, età)

        self.ruolo=ruolo
        self.numero_maglia=numero_maglia
    
    def gioca_partita(self,come_gioca):
        print("il giocatore: "+ self.nome +"gioca la partita: "+come_gioca)
    
    def __str__(self):
        return f"nome: {self.nome}, età: {self.età}, ruolo: {self.ruolo}, numero maglia: {self.numero_maglia}"

class Allenatore(Membro_Squadra):

    def __init__(self, nome, età, ruolo, anni_esperienza):
        super().__init__(nome, età)

        self.ruolo=ruolo
        self.anni_esperienza=anni_esperienza
    
    def dirige_allenamento(self):
        print("L'allenatore"+ self.nome + "dirige l'allenamento in modo severo")
    
    def __str__(self):
        return f"nome: {self.nome}, età: {self.età}, ruolo: {self.ruolo}, anni esperienza: {self.anni_esperienza}"

class Assistente(Membro_Squadra):

    def __init__(self, nome, età, ruolo, specializzazione):
        super().__init__(nome, età)
        self.ruolo=ruolo
        self.specializzazione=specializzazione
    
    def supporto(self,come_supporta):
        print("L'assistente" + self.nome+"supporta i membri della squadra"+come_supporta)

giocatore1= Giocatore("Giovanni","20","attaccante","10")
print(giocatore1)
Membro_Squadra.lavora("alto 1.80 per 70kg")
Giocatore.gioca_partita("in modo aggressivo")

allenatore=Allenatore("Biagio","40","allenatore","20")
print(allenatore)
Membro_Squadra.lavora("altro 1.70 per 65kg")
Allenatore.dirige_allenamento

assistente=Assistente("Luigi","30","assistente","fisioterapista")
print(assistente)
Membro_Squadra.lavora("alto 1.85 per 75kg")
Assistente.supporto("aiutando")