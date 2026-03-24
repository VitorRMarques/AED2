import numpy as np
import pandas as pd
from scipy import stats

dados = [153, 154, 155, 156, 158, 160, 160, 161, 161, 161,
         162, 162, 163, 163, 164, 164, 165, 166, 167, 167, 
         168, 168, 169, 169, 170, 170, 170, 171, 171, 171, 
         172, 172, 173, 173,174 ,174 ,175 ,175 ,176 , 177,
         178 ,179 ,179 ,180 ,182 ,183 ,184 ,185 ,186 ,186,
         187 ,188 ,188 ,189 ,190 ,191 ,192 ,192 ,192 ,192,
         193 ,194 ,194 ,195 ,197 ,197 ,199 ,200 ,201 ,205
    ]

dados = np.array(dados)

media = np.mean(dados)
mediana = np.median(dados)
moda = stats.mode(dados, keepdims=True)

variancia_amostral = np.var(dados, ddof=1)
desvio_padrao = np.std(dados, ddof=1)
coef_variacao = (desvio_padrao / media) * 100

assimetria = stats.skew(dados)
curtose = stats.kurtosis(dados)

print("\nMEDIA:", round(media, 2))
print("\nMEDIANA:", mediana)
print("\nMODA:", moda.mode[0])

print("\nVARIANCIA AMOSTRAL:", round(variancia_amostral, 2))
print("\nDESVIO PADRAO:", round(desvio_padrao, 2))
print("\nCOEFICIENTE DE VARIACAO (%):", round(coef_variacao, 2))

print("\nASSIMETRIA:", round(assimetria, 3))
print("\nCURTOSE:",round(curtose, 3))

df = pd.DataFrame(dados, columns=['Altura'])
df.describe()
df["Altura"].mode()


