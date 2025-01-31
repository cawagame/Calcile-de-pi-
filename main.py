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

def circleCos():
    for i in range(1,100):
        print('ITERASTION ; ',i,' Pi : ',  PI(i))

''''----------------------------------------------------------------------------------------
   https://fr.wikihow.com/calculer-Pi
   methode utuliser  la formule de Nilakantha. 
   Pi =3+4/(2*3*4)-4/(4*5*6)+4/(6*7*8)......
   
   
'''
listPi =[]   #save toutes les dominateur
def denominateurSomme(n:int)->int:
    out=n
    a=[n]
    for i in range(1+n,n+3):
        a.append(i)
        out =out*i

    listPi.append(out)
def alternePlusMois():
    pi:str='3.'
    for ind, ele in enumerate(listPi) :
        strele=str(ele)
        if ind%2:
            pi=pi+'-4/'+strele
        else:
            pi =pi+'+4/'+strele
    return eval( pi)

def Nilakantha():
    for i in range(2,1520,2):
        denominateurSomme(i)
        print ('methode Nilakamtha ',i,'  pi  :', alternePlusMois())


print ('-'*20)
print ('-'*20)
print('-- '+'Calculer de PI')
print ('-'*20)
print('[1]  methode de base avec cercle et cos')
print('[2]  methode de Nilakatha serie')
ch =input('choix methode ? ')
if ch =='2':Nilakantha()
elif ch=='1':circleCos()