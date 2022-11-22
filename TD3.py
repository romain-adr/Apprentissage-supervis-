# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 10:46:48 2022

@author: raudureau
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

N = 5 # nombre de lignes (et de colonnes) d'une forme

N_cell = N*N

# états des cellules du réseau (booléens)
etats = [ False for _ in range(N_cell) ]

# seuils des cellules du réseau (réels)
seuils = [ 0.0 for _ in range(N_cell) ]

# poids des connexions du réseau (réels)
poids = [ [ 0.5 for _ in range(N_cell)] for _ in range(N_cell) ]

exemple_a_reconnaitre = [ [True,  False, True,  False, True],
                          [True,  True,  False, False, True],
                          [False, False, True,  False, True],
                          [True,  False, False, True,  True],
                          [True, False, False, False, True] ]

alphabet = \
[ [ [False, True,  True,  True,  False],  # { A }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  True],
     [True,  False, False, False, True],
     [True,  False, False, False, True] ],
   [ [True,  True,  True,  True,  False],  # { B }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False],
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False] ],
   [ [False, True,  True,  True,  True],   # { C }
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [False, True,  True,  True,  True] ],
   [ [True,  True,  True,  True,  False],  # { D }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False] ],
   [ [True,  True,  True,  True,  True],   # { E }
     [True,  False, False, False, False],
     [True,  True,  True,  False, False],
     [True,  False, False, False, False],
     [True,  True,  True,  True,  True] ],
   [ [True,  True,  True,  True,  True],   # { F }
     [True,  False, False, False, False],
     [True,  True,  True,  False, False],
     [True,  False, False, False, False],
     [True,  False, False, False, False] ],
   [ [True,  True,  True,  True,  True],   # { G }
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [True,  False, False, False, True],
     [True,  True,  True,  True,  True] ],
   [ [True,  False, False, False, True],   # { H }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  True],
     [True,  False, False, False, True],
     [True,  False, False, False, True] ],
   [ [False, False, True,  False, False],  # { I }
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False] ],
   [ [False, False, True,  True,  True],   # { J }
     [False, False, False, True,  False],
     [False, False, False, True,  False],
     [False, False, False, True,  False],
     [True,  True,  True,  True,  False] ],
   [ [True,  False, False, False, True],   # { K }
     [True,  False, False, True,  False],
     [True,  True,  True,  False, False],
     [True,  False, False, True,  False],
     [True,  False, False, False, True] ],
   [ [True,  False, False, False, False],  # { L }
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [True,  True,  True,  True,  True] ],
   [ [True,  True,  False, True,  True],   # { N }
     [True,  False, True,  False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True] ],
   [ [True,  False, False, False, True],   # { M }
     [True,  True,  False, False, True],
     [True,  False, True,  False, True],
     [True,  False, False, True,  True],
     [True,  False, False, False, True] ],
   [ [False, True,  True,  True,  False],  # { O }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [False, True,  True,  True,  False] ],
   [ [True,  True,  True,  True,  False],  # { P }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False],
     [True,  False, False, False, False],
     [True,  False, False, False, False] ],
   [ [True,  True,  True,  True,  True],   # { Q }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, True,  True],
     [True,  True,  True,  True,  True] ],
   [ [True,  True,  True,  True,  False],  # { R }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False],
     [True,  False, False, True,  False],
     [True,  False, False, False, True] ],
   [ [False, True,  True,  True,  True],   # { S }
     [True,  False, False, False, False],
     [False, True,  True,  True,  False],
     [False, False, False, False, True],
     [True,  True,  True,  True,  False] ],
   [ [True,  True,  True,  True,  True],   # { T }
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False] ],
   [ [True,  False, False, False, True],   # { U }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [False, True,  True,  True,  False] ],
   [ [True,  False, False, False, True],   # { V }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [False, True,  False, True,  False],
     [False, False, True,  False, False] ],
   [ [True,  False, False, False, True],   # { W }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, True,  False, True],
     [False, True,  False, True,  False] ],
   [ [True,  False, False, False, True],   # { X }
     [False, True,  False, True,  False],
     [False, False, True,  False, False],
     [False, True,  False, True,  False],
     [True,  False, False, False, True] ],
   [ [True,  False, False, False, True],   # { Y }
     [False, True,  False, True,  False],
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False] ],
   [ [True,  True,  True,  True,  True],   # { Z }
     [False, False, False, True,  False],
     [False, False, True,  False, False],
     [False, True,  False, False, False],
     [True,  True,  True,  True,  True] ] ]

lettre = list(alphabet[0])
box = chr(0x2588) + chr(0x2588)
for i in range(N):
  for j in range(N):
    if lettre[i][j]:
      print (box, end="")
    else :
      print ("  ", end="")
  print ("")
print ("")

#for i in range(25):
 #   poids[i][i] = 0
#boucle qui prends toutes les lettres + nb de modification de cell
f_activation = lambda x: 1 if x > 0 else 0

etats = []
lettre = alphabet[0]
for t in range(5):
    for v in range(5):
        etats.append(lettre[t][v])
print(etats)

for k in range(25):
    print(f"\cellue : {k}")
    cellule = k
    cell_act = 0

    for l in range(25):
        if(etats[l]):
            cell_act += 1
    print(f"Cellules activées {cell_act} ")

e = 0.1
t = seuils[cellule]
d = 0
test = True

while(test):
    test = True
    s = 0
    for i in range(len(etats)):
        if(etats[i]):
            s += poids[cellule][i]
    print(f"activation : somme - theta = {f_activation(s - t)}")
    print("")
    if (f_activation(s - t) == etats[cellule]):
        test = False
    else:
        if(s - t > 0):
            d = (s - t + e) / (1 + cell_act)
            print(d)
        else:
            d = (s - t - e ) / (1 + cell_act)
            print(d)
    poids[cellule] -= d
    seuils[cellule] += d

    for j in range(25):
        if(etats[i] and i != cellule):
            poids[cellule][i] = poids[cellule][i] - d






'''
if s-t negatif -e 
positif + e
poids[cellule] -= d
seuils[cellule] += d
'''

