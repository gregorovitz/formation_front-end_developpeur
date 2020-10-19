import datetime
print("veuillez insérez le jour  ")
jour=int(input())
print ("veuillez insérez le mois ")
mois=int(input())
print("veuillez insérez l'anné en format 0000")
annee=int(input())
daysWeek=["dimanche","lundi","mardi","mecredi","jeudi","vendredi","samedi"]
if mois ==2:
    if annee %4 ==0 and annee % 100 == 0 and annee % 400 == 0 or(annee %4 ==0 and annee%100 !=0):

        if jour>0 and jour<29:
            IsDate=True
    else:
        if jour>0 and jour<28:
            IsDate=True
elif mois == 4 or mois== 6 or mois== 9 or mois== 11:
    if jour>0 and jour<30:
        IsDate = True
else:
    if jour>0 and jour<31:
        IsDate = True

if IsDate:

   if mois<3:
       dayWeek=(((23*mois)//9)+jour+4+annee+((annee-1)//4)-((annee-1)//100)+((annee-1)//400))%7
       print(daysWeek[dayWeek])
   else :
       dayWeek = (((23 * mois)// 9) + jour + 2 + annee + ((annee ) // 4) - ((annee) // 100) + (
                   (annee) // 400))%7
       print(daysWeek[dayWeek])

else:
    print("la date n'est pas corecte")




