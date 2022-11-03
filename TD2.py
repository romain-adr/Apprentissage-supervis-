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

#config = [0, 0, 0, 0]
config = list(configs[0])

# testons la cellule "a" aka "cellule 0" :
p1 = list(p[0])
cellule=0

#print(cellule)
print("-------config-----")
print(config)

for cellule in range(4):
    a = []
    somme = 0
    print("-----Cellule-----")
    print(cellule)
    print("-----List--------")
    print(list(configs[cellule]))
    for i in range(4):
        print("------config[i]----")
        print(config[i])
        print("------p[cellule][i]----")
        print(p[cellule][i])
        # somme de p + conf
        somme += p[cellule][i]+config[i]
        #activation de la somme 1>0 sinon 0
        config[cellule] = f_activation(somme)
        #ajouter dans list a=[]
        a.append(config[cellule])
    print("-----Sortie------")
    print(a)