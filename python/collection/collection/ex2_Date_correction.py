def get_month(month):
    day_in_month = 31
    if month == 2:
        is_bissextile = (annee % 400 == 0) or (annee % 4 == 0 and annee % 100 != 0)
        day_in_month = 29 if is_bissextile else 28
    elif month in [4, 6, 9, 11]:
        day_in_month = 30
        # IsDate= 1 <= mois <= 12 and jour >= 1 and jour <= dayInMonth
    return day_in_month


def get_day_of_week(day, month, year):
    c = (14 - month) // 12
    # c=1 if month<=2 else 0
    a = year - c
    m = month + (12 * c) - 2
    j = (day + a + a // 4 - a // 100 + a // 400 + (31 * m) // 12) % 7
    return j


def print_date(j):
    day_of_week = daysWeek[j]
    # msg="Le"+str(jour) +"/"+str(mois)+ "/"+str(annee) +" est un " +day_of_week
    # msg = "Le %s/%s/%s est un %s"% (jour,mois,annee,day_of_week)
    # msg="Le {}/{}/{} est un {}".format(jour,mois,annee,day_of_week)
    msg = "Le {d}/{m}/{y} est un {dw}".format(d=jour, m=mois, y=annee, dw=day_of_week)
    print(msg)


print("veuillez insérez le jour")
jour = int(input())
print("veuillez insérez le mois ")
mois = int(input())
print("veuillez insérez l'anné en format 0000")
annee = int(input())
daysWeek = ["dimanche", "lundi", "mardi", "mecredi", "jeudi", "vendredi", "samedi"]

dayInMonth = get_month(mois)

IsDate = 1 <= mois <= 12 and 1 <= jour <= dayInMonth

if IsDate:
    day_week = get_day_of_week(jour, mois, annee)
    print_date(day_week)
else:
    print("la date n'est pas corecte")
