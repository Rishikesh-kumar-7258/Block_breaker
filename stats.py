import pandas as pd

data = pd.read_csv("stats.csv")

def Add_new_data(name, play_time, score):
    new_data = {
    "player_name": name,
    "play_time" : play_time,
    "scores" : score,
    "High_score" : 0
    }
    i = 0
    for names in data["player_name"]:
        if names == name:
            data["High_score"][i] = max(score, data["High_score"][i])
            s = data["scores"][i].split(':')
            s.append(score)
            s = map(lambda x : str(x), s)
            print(s)
            data["scores"][i] = ':'.join(s)
            data.to_csv("stats.csv", index=False)
            print("It already exists")
            return
        i+= 1
    df = pd.DataFrame(new_data, index=[len(data)])
    df.to_csv("stats.csv", mode='a', header=False, index=False)