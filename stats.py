import pandas as pd

data = pd.read_csv("stats.csv")

def Add_new_data(name, play_time, score):
    new_data = {
    "player_name": name,
    "play_time" : play_time,
    "scores" : score,
    }
    i = 0
    while (i < len(name) and name[i] == ' ') : i+= 1
    if (i == len(name)) : return
    df = pd.DataFrame(new_data, index=[len(data)])
    df.to_csv("stats.csv", mode='a', header=False, index=False)

def get_highScore():
    highScore = max(data["scores"]) or 0
    return highScore