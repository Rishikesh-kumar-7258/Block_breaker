import os
from os import path

def Add_new_data(name, play_time, score):
    file = open("stats.csv", 'a+')
    new_data = name + ',' + str(play_time) + "," + str(score) + '\n'
    i = 0
    while (i < len(name) and name[i] == ' ') : i += 1
    if (i == len(name)) : return
    file.write(new_data)
    file.close()

def get_highScore():
    if not path.exists("stats.csv") : 
        file1 = open("stats.csv", 'w')
        file1.write("player_name,play_time,scores\n")

    file1 = open("stats.csv")
    scores = []
    i = 0
    for row in file1:
        if i == 0 :
            i+=1
            continue
        row = row.split(',')
        scores.append(int(row[2][:-1]))
        i += 1
    if (len(scores) == 0) : return 0
    return max(scores)
    file1.close()