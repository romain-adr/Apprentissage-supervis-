p = [[0, -1, 1, 1],
    [-1, 0, 1, -1],
    [1, 1, 0, 1],
    [1, -1, 1, 0]]

configs = [[0,0,0,0], [0,0,0,1], [0,0,1,0], [0,0,1,1],
           [0,1,0,0], [0,1,0,1], [0,1,1,0], [0,1,1,1],
           [1,0,0,0], [1,0,0,1], [1,0,1,0], [1,0,1,1],
           [1,1,0,0], [1,1,0,1], [1,1,1,0], [1,1,1,1]]


#fonction d'activation seuil
f_activation = lambda x: 1 if x > 0 else 0

# on part de la config "0" :


for c in range(16):

        #config = [0, 0, 0, 0]
        config = list(configs[c])

        # testons la cellule "a" aka "cellule 0" :
        p1 = list(p[0])
        cellule=0

        #print(cellule)
        print(config, end="")

#faire une boucle jusqu'a etat stable:
        for toto in range(4):

             a = []
             
             for cellule in range(4):
                
                somme = 0
                for i in range(4):
                    somme += p[cellule][i]*config[i]
                #activation de la somme 1>0 sinon 0
                config[cellule] = f_activation(somme)
                a.append(config[cellule])
             print(" -> ", a, end="")
        print()