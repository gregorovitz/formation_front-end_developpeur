print('bonjour')
i=0
ma_list=[]
for i in range (9):
    print ('encodé un nombre')
    nbr=int(input())
    ma_list.append(nbr)
print (ma_list)
list_trier=[]
while (len(ma_list)!=0):
    y = 0
    for x in range(len(ma_list)):

        if (ma_list[x]< ma_list[y]):
            y=x
    list_trier.append(ma_list[y])
    ma_list.remove(ma_list[y])
print('voici votre liste de chiffre trier en ordre croissant',list_trier)