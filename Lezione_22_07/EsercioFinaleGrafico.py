import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#giorni=np.linspace(1, 365,365)
giorni= pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
media=2000
deviazione=500
min_visitatori=media-2*deviazione
max_visitatori=media+2*deviazione
visitatori=np.random.randint(min_visitatori,max_visitatori,size=365)
aumento=np.linspace(0.5,182.5 ,365)

#dati={}

trasformarto=pd.DataFrame({'Visitatori':visitatori+aumento}, index=giorni)
#print(trasformarto)

media_mensile= trasformarto.resample('M').mean()
media_mensile=media_mensile["Visitatori"]
#print(media_mensile)

deviazione_mensile= trasformarto.resample('M').std()
deviazione_mensile=deviazione_mensile["Visitatori"]


mediaSet= trasformarto.rolling(window=7).std()
print(mediaSet)

"""sns.barplot(x=giorni, y=visitatori, data=trasformarto)
plt.title('Grafico Parco Acquatico')
plt.xlabel('Giorni')
plt.ylabel('Visitatori')
plt.show()"""

sns.lineplot(x=giorni, y=visitatori, data=trasformarto)
plt.title('Grafico Parco Acquatico')
plt.xlabel('Giorni')
plt.ylabel('Visitatori')
plt.show()

sns.lineplot(x=[1,2,3,4,5,6,7,8,9,10,11,12], y=media_mensile)
plt.title('Grafico Parco Acquatico')
plt.xlabel('Mesi')
plt.ylabel('Media-Visitatori')
plt.show()


mediaSet= trasformarto.rolling(window=7).std()
print(mediaSet)

sns.lineplot(x=giorni, y=mediaSet)
plt.title('Grafico Parco Acquatico')
plt.xlabel('Settimana')
plt.ylabel('Media Settimanale')
plt.show()
