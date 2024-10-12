from random import uniform
import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 


N = int(input("Digite la cantidad de dardos a tirar: "))
i = 0
a = 0
listax = list()
listay = list()
listanx = list()
listany = list()
fig, ax = plt.subplots()
ax.add_patch(plt.Circle((0,0),1,fill=False,color='black'))
plt.gca().set_aspect('equal')

while i<N:
  x = uniform(-1,1)
  y = uniform(-1,1)
  h = math.sqrt((x*x)+(y*y))
  if h<=1:
    listax.append(x)
    listay.append(y)
    a += 1
  else:
    listanx.append(x)
    listany.append(y)
  i += 1
pi = round(((4*a)/N),5)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Dardos lanzados: {}".format(N))
plt.scatter(listay,listax,5,color="green",label="Acertado")
plt.scatter(listany,listanx,5,color="red",label="No Acertado")
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
imprimir = 'π ≈ ' + str(pi)
plt.text(1.25,0.5,imprimir,fontsize=15)
plt.show()
  