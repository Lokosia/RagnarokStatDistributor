# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 15:10:04 2020

@author: lokos
"""
#stat distributor
from tabulate import tabulate

fin_str = 110
fin_agi = 50
fin_vit = 50
fin_int = 1
fin_dex = 50
fin_luk = 1

stats = [fin_str, fin_agi, fin_vit, fin_int, fin_dex, fin_luk]

fin_table = []
for s in range(len(stats)):
    stat_table = []
    
    if s == 0:
        sn = 'STR'
    if s == 1:
        sn = 'AGI'
    if s == 2:
        sn = 'VIT'
    if s == 3:
        sn = 'INT'
    if s == 4:
        sn = 'DEX'
    if s == 5:
        sn = 'LUK'
    
    stat_weight = 0
    
    if s == 4:
        tempstat = stats[s]/5
    else:
        tempstat = stats[s]/10
    
    #adding first set of stats
    if int(tempstat) > 0:
        stat_table.append(int(tempstat))
    else:
        stat_table.append(stats[s])
    
    saved_progression = tempstat
    if stats[s] != 1:
        while tempstat < stats[s]:
            tempstat += saved_progression
            
            if not tempstat > stats[s]:
                if tempstat < 1:
                    stat_table.append(stats[s])
                    continue
                
                if tempstat < stats[s]:
                    if tempstat + saved_progression > stats[s]:
                        stat_table.append(stats[s])
                    else:
                        stat_table.append(int(tempstat))
                else:
                    stat_table.append(stats[s])
    
    stat_table.insert(0, sn)
    fin_table.append(stat_table)

print(tabulate(fin_table, ['', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], tablefmt="github"))

