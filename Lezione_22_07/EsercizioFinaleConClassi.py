import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

giorni= pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
media=2000
deviazione=500
min_visitatori=media-2*deviazione
max_visitatori=media+2*deviazione
visitatori=np.random.randint(min_visitatori,max_visitatori,size=365)
aumento=np.linspace(0.5,182.5 ,365)

class Parco:
    

    
    def __init__(self,visitatori,aumento,giorni):
    
        self.visitatori=visitatori
        self.aumento=aumento
        self.giorni=giorni
        self.nuovo= self.visitatori+self.aumento
        
        
    def trasformato(self):
        self.trasformarto=pd.DataFrame({'Visitatori':self.nuovo}, index=self.giorni)
    
    def media_mese(self):
        self.media_mensile= self.trasformarto.resample('M').mean()
        self.media_mensile=self.media_mensile["Visitatori"]
    
    def deviazione(self):
        self.deviazione_mensile= self.trasformarto.resample('M').std()
        self.deviazione_mensile=self.deviazione_mensile["Visitatori"]
    
    def grafico_barre(self):
        sns.barplot(x=self.trasformarto.index, y=self.visitatori["Visitatori"])
        plt.title('Grafico Parco Acquatico')
        plt.xlabel('Giorni')
        plt.ylabel('Visitatori')
        plt.show()
    
    def grafico_linee(self):
        sns.lineplot(x=self.trasformarto.index, y=self.visitatori["Visitatori"])
        plt.title('Grafico Parco Acquatico')
        plt.xlabel('Giorni')
        plt.ylabel('Visitatori')
        plt.show()
    
    def media_mensilee(self):
        sns.lineplot(x=[1,2,3,4,5,6,7,8,9,10,11,12], y=self.media_mensile)
        plt.title('Grafico Parco Acquatico')
        plt.xlabel('Mesi')
        plt.ylabel('Media-Visitatori')
        plt.show()
    
    def media_settimanale(self):
        mediaSet= self.trasformarto.rolling(window=7).std()
        print(mediaSet)

        sns.lineplot(x=giorni, y=mediaSet)
        plt.title('Grafico Parco Acquatico')
        plt.xlabel('Settimana')
        plt.ylabel('Media Settimanale')
        plt.show()

parco=Parco(giorni,visitatori,aumento)
parco.trasformato()
parco.media_mese()
parco.grafico_linee()
parco.media_mensilee()