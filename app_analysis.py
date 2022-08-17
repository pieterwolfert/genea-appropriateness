from itertools import count
import json
import csv

def getStimuli(participants):
    responses = []
    for p in participants:
        for s in p['trials']:
            if s['id'] == "training":
                continue
            if "attn" in s['responses'][0]['stimulus'] or "attn" in s['responses'][1]['stimulus']:
                continue
            if s['responses'][0]['score'] == 99 and s['responses'][0]['score'] == 99:
                continue
            responses.append(s['responses'])
    return responses



if __name__=="__main__":
    """
    Goes from JSON to CSV format with item1, item2, value1, value2
    """
    results = "results/responses_app_speech_full.json"
    write_to = "results/app_speech_full.csv"
    with open(results, 'r') as f:
        rs = json.load(f)
    responses = getStimuli(rs)
    count_mismatch_true = 0
    count_mismatch_false = 0
    count_normal_true = 0
    count_normal_false = 0
    both_false = 0
    for r in responses:
        if "mismatched" in r[0]['stimulus'] and not "mismatched" in r[1]['stimulus']:
            if r[0]['score'] and not r[1]['score']:
                count_mismatch_true += 1
            elif not r[0]['score'] and r[1]['score']:
                count_normal_true += 1
            elif not r[0]['score'] and not r[1]['score']:
                both_false += 1
        elif "mismatched" in r[1]['stimulus'] and not "mismatched" in r[0]['stimulus']:
            if r[1]['score'] and not r[0]['score']:
                count_mismatch_true += 1
            elif not r[1]['score'] and r[0]['score']:
                count_normal_true += 1
            elif not r[1]['score'] and not r[0]['score']:
                both_false += 1
            
    print(count_mismatch_true, count_normal_true)
    f = open(write_to, 'w')
    writer = csv.writer(f)
    for r in responses:
        rep = [r[0]['stimulus'], r[1]['stimulus'], r[0]['score'], r[1]['score']]
        writer.writerow(rep)
        