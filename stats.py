def Add_new_data(name, play_time, score):
    file = open("C:\\Users\\Rishikesh Kumar\\Dropbox\\My PC (LAPTOP-KP31EEKV)\\Desktop\\Games\\Ball_breaker\\stats.csv", 'a+')
    new_data = name + ',' + str(play_time) + "," + str(score)
    i = 0
    while (i < len(name) and name[i] == ' ') : i += 1
    if (i == len(name)) : return
    file.write(new_data)
    file.close()

def get_highScore():
    file1 = open("C:\\Users\\Rishikesh Kumar\\Dropbox\\My PC (LAPTOP-KP31EEKV)\\Desktop\\Games\\Ball_breaker\\stats.csv")
    scores = []
    i = 0
    for row in file1:
        if i == 0 :
            i+=1
            continue
        row = row.split(',')
        scores.append(int(row[2][:-1]))
        i += 1
    return max(scores)
    file1.close()