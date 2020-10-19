def affichage_list(l0):
    print(l0)


def fusion(l1, l2):
    result = []
    if not l1 or len(l1) == 0:
        return l2
    if not l2 or len(l2) == 0:
        return l1

    if l1[0] < l2[0]:
        result.append(l1[0])
        l1 = l1[1:]

    else:
        result.append(l2[0])
        l2 = l2[1:]
    list_fusion = fusion(l1, l2)
    result.extend(list_fusion)
    return result


def tri_fusion(tab):
    if len(tab) <= 1:
        return tab
    millieu = len(tab)//2
    return fusion(tri_fusion(tab[:millieu]), tri_fusion(tab[millieu:]))


list_base = [20, 3, 5, 21, 20, 12, 42, 30, 5, 9, 13, 18, 5]
affichage_list(list_base)
list_trier = tri_fusion(list_base)
affichage_list(list_trier)
