import random




def montyHall(switch):
    '''
     Prend switch qui caractérise si le joueur change de porte 
     et retourne si le joueur à gagné 
    '''

    portes = ['Voiture','Chevre','Chevre'] #les 3 issus 
    random.shuffle(portes) #portes généré 

    nportes = [0, 1, 2]

    choose = random.choice(nportes) # le premier choix du joueur

    show = random.choice([x for x in nportes if x != choose and portes[x] == 'Chevre']) #porte enlevé

    if switch:
        choose = [x for x in nportes if x not in [choose, show]][0]   #changement de porte
    return portes[choose]=='Voiture'
    

def expmontyHall(n,switch):
    """
    Prend n le nombre de fois que la fonction @montyHall est appelé et switch si le joueur change de porte ou pas
    et retourne le quotien du nombre de victoire sur le nombre total de tentative
    """
    r = 0
    for _ in range(n):
        if montyHall(switch):
            r+=1
    return r/n



print(expmontyHall(100,False)) # quotien d'une expérience de 100 tentative sans changement
print(expmontyHall(100,True)) # quotien d'une expérience de 100 tentative avec changement