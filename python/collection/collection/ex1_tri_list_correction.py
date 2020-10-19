# Exo1 - Créer un script Python qui permet à un utilisateur de créer une collection de 10 nombres
# V1 => Trie durant la création du tableau
numbers = []
NB_NUMBER = 10

print("Veuillez saisir 10 nombres : ")
count = NB_NUMBER
while count > 0:
    value = int(input("> "))

    # Recherche la position
    position = len(numbers)
    if len(numbers) == 0 or numbers[0] > value:
        position = 0
    elif numbers[len(numbers) - 1] > value:
        posMin = 0
        posMax = len(numbers) - 1
        find = False

        while posMin < posMax and not find:
            target = (posMin + posMax) // 2 + 1
            if numbers[target] > value:
                posMax = target - 1
            elif numbers[target] < value:
                posMin = target + 1
            else:
                find = True

        position = target if value < numbers[target] else target + 1

    numbers.insert(position, value)

    count -= 1

print("Affichage des nombres : ")
for nb in numbers:
    print(nb, end=' > ')












# Une année est bissextile si :
# Elle divisible par 4 et n'est pas divisible par 100
# Ou si elle est divisiable par 400


