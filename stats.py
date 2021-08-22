import pandas as pd

data = pd.read_csv("stats.csv")

def Add_new_data(name, play_time, score):
    new_data = {
    "player_name": name,
    "play_time" : play_time,
    "scores" : score,
    }
    df = pd.DataFrame(new_data, index=[len(data)])
    df.to_csv("stats.csv", mode='a', header=False, index=False)