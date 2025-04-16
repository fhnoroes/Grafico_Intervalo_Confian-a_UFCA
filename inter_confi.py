from scipy.stats import norm
import math
from numpy import mean, random, array
import matplotlib.pyplot as plt


dados = [[],[]]
pop = []
media = 45
desvio = 20
tam = 10
z = 0


#cria amostras começando com n = 10 e aumentando de 2 em 2 até 1000
while tam<=1000:
    pop = random.normal(loc=media, scale=desvio, size=tam)
    dados[0].append(mean(pop))
    dados[1].append(tam)
    tam+=2

int_confia = []
#gerando intervalo de confiança e armazenando em int_confia = []
for i in range(len(dados[0])):
    alfa = 0.01
    while alfa<=1:
        z= norm.ppf(1-alfa/2)
        alfa+=0.01
        aux = []
        aux.append(dados[0][i] - (z/2)*(desvio/(math.sqrt(dados[1][i]))))
        aux.append(dados[0][i] + (z/2)*(desvio/(math.sqrt(dados[1][i]))))
        int_confia.append(aux)

aux2 =[]
graf = []
cont = 0.01
#verificando se o valor da minha média está dentro do intervalo, quando isso acontece marco como 1, quando não marco como 0
for e in int_confia:
    if e[0]>media or e[1]<media:
        aux2.append(0)
        cont+=0.01
    else:
        aux2.append(1)
        cont+=0.01
    if cont>1:
        graf.append(aux2)
        aux2 = []
        cont = 0.01


dados = array(graf)
#gerando gráfico com os dados obtidos da matriz graf
plt.imshow(dados,cmap='binary',interpolation ='nearest')
plt.axis('on')
plt.gca().invert_yaxis()
plt.xlabel('alfa [0.01 - 1]')
plt.ylabel('N [10 - 1000]')



plt.yticks(ticks=[], labels=[])
plt.xticks(ticks=[], labels=[])

plt.show()





