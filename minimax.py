import random

def minimax(dizi):
    for i in range(len(dizi)-1,0,-1):
        if(i%2 != 0):
            for j in range(int(len(dizi[i])/5)):
                splitdizi=dizi[i][j*5:j*5+5]
                dizi[i-1].append(min(splitdizi))

        else:
            for j in range(int(len(dizi[i])/5)):
                splitdizi=dizi[i][j*5:j*5+5]
                dizi[i-1].append(max(splitdizi)) 

    return max(dizi[0])    


yapraklar=[]
    
for i in range(625):
    yapraklar.append(random.randint(1,1000))

minmaxskorlar=[[],[],[],yapraklar]
print("Oyun Skoru: ",minimax(minmaxskorlar))

seçim1=minmaxskorlar[0].index(max(minmaxskorlar[0]))

seçim2=minmaxskorlar[1][seçim1*5:seçim1*5+5].index(min(minmaxskorlar[1][seçim1*5:seçim1*5+5]))
index2=seçim1*5+seçim2

seçim3=minmaxskorlar[2][index2*5:index2*5+5].index(max(minmaxskorlar[2][index2*5:index2*5+5]))
index3=index2*5+seçim3

seçim4=minmaxskorlar[3][index3*5:index3*5+5].index(min(minmaxskorlar[3][index3*5:index3*5+5]))

print("1. katman: ",minmaxskorlar[0])
print("-----------------------------")
print("2. katman: ")
for i in range(len(minmaxskorlar[1])):
    if((i)%5==0):
        print(" ",int(i/5)+1,": ",end="")
    print(minmaxskorlar[1][i],end=", ")
print("")    
    
print("-----------------------------")
print("3. katman ")
for i in range(len(minmaxskorlar[2])):
    if((i)%5==0):
        print(" ",int(i/5)+1,": ",end="")
    print(minmaxskorlar[2][i],end=", ")
print("")  
print("-----------------------------")
print("4. katman ")
for i in range(len(minmaxskorlar[3])):
    if((i)%5==0):
        print(" ",int(i/5)+1,": ",end="")
    print(minmaxskorlar[3][i],end=", ")
print("")  
print("-----------------------------")

print("1.seçim(bilgisayar): ",seçim1+1)
print("2.seçim(oyuncu): ",seçim2+1)
print("3.seçim(bilgisayar): ",seçim3+1)
print("4.seçim(oyuncu): ",seçim4+1)