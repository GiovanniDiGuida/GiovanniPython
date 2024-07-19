import matplotlib.pyplot as plt
import seaborn as sns

categories = ['Giorno 1', 'Giorno2', 'Giorno3', 'Giorno4', 'Giorno5',"Giorno6","Giorno7"]
values = [10, 8, 10, 7, -30,50,50]
colori=["blue","blue","blue","blue","red","yellow","yellow"]

plt.figure()
plt.bar(categories, values, color=colori)
sns.set_theme(style="whitegrid")
plt.title('Energia settimanale')
plt.xlabel('Giorni')
plt.ylabel('Valori')
plt.show()