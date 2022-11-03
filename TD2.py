p = [[0, -1, 1, 1],
    [-1, 0, 1, -1],
    [1, 1, 0, 1],
    [1, -1, 1, 0]]

configs = [[0,0,0,0], [0,0,0,1], [0,0,1,0], [0,0,1,1],
           [0,1,0,0], [0,1,0,1], [0,1,1,0], [0,1,1,1],
           [1,0,0,0], [1,0,0,1], [1,0,1,0], [1,0,1,1],
           [1,1,0,0], [1,1,0,1], [1,1,1,0], [1,1,1,1]]

f_activation = lambda x: 1 if x > 0 else 0

# on part de la config "0" :

#config = [0, 0, 0, 0]
config = list(configs[0])

# testons la cellule "a" aka "cellule 0" :
p1 = list(p[0])
cellule=0

#print(cellule)
#print(p1)

for cellule in range(4):
    a = []
    somme = 0
    print(cellule)
    print(list(configs[cellule]))
    for i in range(4):
        somme += p[cellule][i]+config[i]
        config[cellule] = f_activation(somme)
        #print(config[cellule])
        a.append(config[cellule])
        
    print(a)