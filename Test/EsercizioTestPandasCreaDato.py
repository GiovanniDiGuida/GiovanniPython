import pandas as pd
import numpy as nd


filiali=["Filiale Napoli","Filiale Milano","Filiale Roma","Filiale Palermo"]
vendite=[10,20,30,40,50,60,70,80]
dati={"Data": ["5 Giugno","6 Giugno","7 Giugno","8 Giugno","9 Giugno"],
      "Filiali":nd.random.choice(filiali,size=5),
      "Vendite":nd.random.choice(vendite,size=5)}

trasformato=pd.DataFrame(dati)
print(trasformato)
trasformato.to_csv("TestNegozio.csv")