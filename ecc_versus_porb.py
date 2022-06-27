

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.ticker
%matplotlib inline
from matplotlib.ticker import FormatStrFormatter

#abrindo o arquivo
df = pd.read_excel('Pasta1.xlsx', sheet_name='dados')

#criando a figura
fig, ax = plt.subplots(figsize=(11,7))


#plotando o gráfico
ax.scatter(df['orbital_period'],df['eccentricity'],s=100,edgecolor='k',color='blue',label='Estrelas tipo M \n Temperatura: \n <3500K')


#limites dos eixos
ax.set_xlim(-1300000, 20000000)
#ax.set_ylim(0, 1000)

#marcadores nos eixos
#ax.tick_params(which='both', width=1, direction='in',labelsize=16)
#ax.tick_params(which='major', length=10)
#ax.tick_params(which='minor', length=5)

#Título e rótulos
ax.set_title('Eccentricity versus Porb ',fontsize=20)
ax.set_xlabel('Porb', fontsize=15)
ax.set_ylabel('Eccentricity', fontsize=15)


#legenda
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.8, box.height])

# Put a legend to the right of the current axis
lgnd = ax.legend(loc='center left', bbox_to_anchor=(1, 0.7),borderaxespad=1,prop={'size':14})

#plt.legend()


plt.savefig("Eccentricity_versus_Porb_rafa_zoom2.jpg",dpi=300)


plt.show()