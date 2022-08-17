from itertools import count
import json
import csv
from scipy import stats
import numpy as np

if __name__=="__main__":
    """Read in CSV file that contains all pairs from the appropriateness studies, and calculate barnards test for each system combination."""
    results = "results/app_speech_full.csv"
    output = "results/app_speech_full_statistics.csv"
    l_results = []
    with open(results, 'r') as f:
        rs = f.readlines()
        for r in rs:
            r = r.strip('\n').split(',')
            l_results.append(r)
    counts = {}
    for l in l_results:
        code = l[0][:3]
        if code not in counts:
            counts[code] = {"normal": 0, "mismatched" : 0, "ties" : 0}
        if "mismatched" in l[0] and not "mismatched" in l[1]:
            if "True" in l[2] and not "True" in l[3]:
                counts[code]['mismatched'] += 1
            elif not "True" in l[2] and "True" in l[3]:
                counts[code]['normal'] += 1
            elif not "True" in l[2] and not "True" in l[3]:
                counts[code]['ties'] += 1
        elif not "mismatched" in l[0] and "mismatched" in l[1]:
            if "True" in l[3] and not "True" in l[2]:
                counts[code]['mismatched'] += 1
            elif not "True" in l[3] and "True" in l[2]:
                counts[code]['normal'] += 1
            elif not "True" in l[3] and not "True" in l[2]:
                counts[code]['ties'] += 1
    #count ties 50/50 to normal and mismatched
    for key in counts.keys():
        if int(counts[key]['ties'])%2 == 1:
            tie_1 = (int(counts[key]['ties'])/2) - 0.5
            tie_2 = (int(counts[key]['ties'])/2) + 0.5
            counts[key]['normal'] += int(tie_1)
            counts[key]['mismatched'] += int(tie_2)
        else:
            counts[key]['normal'] += int(int(counts[key]['ties'])/2)
            counts[key]['mismatched'] += int(int(counts[key]['ties'])/2)
        counts[key]['ties'] = 0
    visited = []
    print("Contingency table is 2x2, normal on 1st row, mismatched on 2nd. Ties are equally distributed over both situations.")
    with open(output, 'w') as f:
        f.write("condition_id_1,condition_id_2,wald_statistic,p_value\n")
        for key in counts.keys():
            contingency_table = np.zeros((2,2))
            for another_key in counts.keys():
                if key == another_key:
                    continue
                comb1 = another_key + "_" + key
                comb2 = key + "_" + another_key
                if comb1 in visited or comb2 in visited:
                    continue
                visited.append(comb1)
                visited.append(comb2)
                contingency_table[0][0] = counts[key]['normal']
                contingency_table[1][0] = counts[key]['mismatched']
                contingency_table[0][1] = counts[another_key]['normal']
                contingency_table[1][1] = counts[another_key]['mismatched']
                res = stats.barnard_exact(contingency_table, pooled=True, n=128) 
                f.write("{},{},{},{}\n".format(key, another_key, res.statistic, res.pvalue))
                print("{},{},{},{}".format(key, another_key, res.statistic, res.pvalue))
                #print("System 1: {} System 2: {} Wald-statistic: {} P-value: {}".format(key, another_key, res.statistic, res.pvalue))