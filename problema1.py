
def minimo(x,a):
    for i in range(len(a)):
        if a[i] == x:
            if i != (len(a)-1) and i != 0:
               #  print(i, 'I DENTRO')
                j=i-a[i]
               # print(j, 'actual')
                while a[j] <= x and  j != i and j >=0 and j <= i+a[i]:
                    a[j]=-1
                    j+=1
                    if(j==i):
                        j+=1
    return a 


def funcionarRegadera(x,a):
    global c3,c2,c1,c0
    for i in range(len(a)):
        #PARA REGADERA DISTANCIA 3
        if a[i] == x:
            if i == len(a)-1: #si se encuentra en la ultima pos
                '''
                temp[i-3]=1  
                temp[i-2]=1
                temp[i-1]=1
                temp[i-0]=1  '''
                for j in range(a[i]+1):
                    temp[i-j]=1
            elif i == 0: #al inicio
                '''
                temp[i]=1
                temp[i+a[i]]=1  
                '''
                for j in range (a[i]+1):
                    temp[i+j]=1    
            else:  #en cualquier parte
                for j in range(a[i]+1):
                    if (i-j) >=0: #hasta que no sobreexceda el min 
                        temp[i-j]=1
                temp[i]=1  #actual pos
                for j in range (a[i]+1):
                    if (i+j) < len(a): #hasta que no sobreexceda el max
                        temp[i+j]=1
            if x == 0:
                c0+=1
            elif x == 1:
                c1+=1
            elif x == 2:
                c2+=1
            elif x == 3:
                c3+=1
            



if __name__ == '__main__':
    
    c0=c1=c2=c3=0
    #ARREGLO
    a1 = [0,2,2,2,0,0,0,1,2,1,1,0,0,0]# reemplazable (ej: array 3)
    #inicializando temp ,   0 : no regado, 1 : regado
    temp = [0]*(len(a1))
    #mi función minimo convierte en -1 las regaderas q estan a los extremos, para que no se enciendan
    minimo(3,a1)
    minimo(2,a1)
    minimo(1,a1)
    minimo(0,a1)
    '''for i in range(len(a1)):
        print(a1[i]) '''
    print("separador")
    #mi función funcionarRegadera establece a 1 (regado) a mi array temp
    funcionarRegadera(3,a1)
    funcionarRegadera(2,a1)
    funcionarRegadera(1,a1)
    funcionarRegadera(0,a1)
    '''for i in range(len(temp)):
        print(temp[i]) #si todos imprimen 1, toda la parcela está regada
    '''
    print(c1+c2+c3+c0 , 'regaderas totales')


