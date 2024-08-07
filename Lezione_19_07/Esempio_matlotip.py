import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['figure.figsize'] = [10, 6]  
# Imposta la dimensione predefinita delle figure

plt.rcParams['figure.dpi'] = 100          
# Imposta la risoluzione delle figure in DPI

plt.rcParams['figure.facecolor'] = 'white'  # Colore di sfondo della figura

sns.set_theme()  # Applica il tema di default di Seaborn

sns.set_theme(style="whitegrid")