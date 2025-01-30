#calcule PI=3.14
#dans un cerle de rayons =1, et 360°
#perimetre variable    P=2*pi*r
#avec un variastion poligomme, à interier du celce

#i =iterateur
#pi =P/2r
#AngleTriangle=360/iterateur(i)
#op =longeur de position
#hipotenus =r =1
# op=  (sin(  (angleTriangle)/2)*1)*2

#FORMULE GLOBALE
#          op*i
#   Pi =---------
#           1*2

#           i*( ((sin( ((360/i)/2))*1)*2 )
# pi  = --------------------------------
#                   2

import math
def PI(i):
    hipo =1
    angle =math.radians(  360/i /2)   #encoorde angle en radians
    op =hipo* math.sin(angle )*2      #langleur de oppsser du retangle isosle
    return op*i/2                    #perimetrte sur diametre  2*rayon


for i in range(1,100):
    print('ITERASTION ; ',i,' Pi : ',  PI(i))

