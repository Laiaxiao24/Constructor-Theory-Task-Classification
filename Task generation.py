#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 13:16:58 2022

@author: laiaplanas
"""

#IMPORT ZONE

from math import comb
from math import factorial
from itertools import combinations
from itertools import product
from itertools import groupby
from itertools import permutations
import os.path
import json



def combi(i,o):
    """
    
    Generate tasks from inputs and outputs (attributes).
    
    Parameters
    ----------
    i : list
        inputs 
    o : list
        outputs

    Returns
    -------
    Task in format: [[in,out], [in,out]...]
    """
    
    perm = (list(tup) for tup in permutations(o, len(o)))
    tasks = []
    
    for n in range(factorial(len(o))):
        task_i = []
        outp = next(perm)
        for j in range(len(i)):
            task_i_p = []
            task_i_p.append(i[j]) #input
            task_i_p.append(outp[j]) #output
            task_i.append(task_i_p)
        tasks.append(task_i)
    return tasks 


all_t = []


#System dimension
dim = int(input("System dimension: "))

#directory

path = str(dim)
if not os.path.exists(path):
    os.mkdir(path)

save_path = path

#Attributes
d_single = int(dim ** (0.5))
s1 = []
for i in range(d_single):
    s1.append(i)
#print(s1)
s = list((list(tup) for tup in product(s1,s1)))
    
print("System attributes: ", s)

  
#example: system dimension - 4
#s = ['00','01','10','11']

#Number of reversible tasks
total = 0
for i in range(dim):
    total += (comb(dim,i+1)**2 * factorial(i+1))
print("Number of reversible tasks: ", total)

#Task generation
for k in range(dim):
    all_t_diagram = []
    r = []
    mini_l = list(list(tup) for tup in combinations(s, (k+1))) #crea els in/out per cada diagrama
    mini_task = (list(tup) for tup in product(mini_l, mini_l)) #estableix relacions in/out
    mini_l.clear()
    r.append(mini_task)
    pro = (comb(dim,k+1)**2)
    for j in range(pro):
        rela = next(r[0])
        all_t_diagram += combi(rela[0], rela[1])
        
    all_t += all_t_diagram
        
    #Save tasks: txt, json
    name = 'T (read)' + str(k+1)
    com_name = os.path.join(save_path, name + ".txt")   
    file = open(com_name, 'w')
    for n in all_t_diagram:
        file.write(str(n) + '\n')
    file.close()
    
    name2 = 'T' + str(k+1)
    com_name1 = os.path.join(save_path, name2)   
    with open(com_name1, 'w') as file:
        json.dump(all_t_diagram, file)
    file.close()
    
#print(all_t)

#SAVE TASKS IN SINGLE FILE

#txt file (readable)
name_of_file = 'Tasks (read)'+ str(dim)
com_name2 = os.path.join(save_path, name_of_file + ".txt")         
file1 = open(com_name2, 'w')
for i in all_t:
    file1.write(str(i) + '\n')
file1.close()


#json file (practical)
name_of_file3 = 'Tasks' + str(dim)
com_name3 = os.path.join(save_path, name_of_file3)         
with open(com_name3, 'w') as file2:
    json.dump(all_t, file2)
file2.close()



