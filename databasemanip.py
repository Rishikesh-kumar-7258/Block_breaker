from os import error
from typing import NoReturn


def exists_data(attr) :
    file = open("database.csv")
    lines = file.readlines()
    file.close()

    # if lines == "" : return False

    for line in lines:
        words = line.split(",")
        if (words[0] == attr) : 
            return True
    
    return False

def add_data(att, value) :
    file = open("database.csv", "a")

    if exists_data(att) : raise FileExistsError
    toAdd = att + "," + str(value) + "\n"
    file.write(toAdd)

    file.close()

def delete_data(attr) :

    if not exists_data(attr) : return False

    file = open("database.csv")
    lines = file.readlines()
    file.close()

    file = open("database.csv", "w")
    for line in lines:
        arr = line.split(",")
        if arr[0] != attr : file.write(line)
    file.close()

    return True

def change_data(attr, data) :
    if not exists_data(attr) : return False

    file = open("database.csv")
    lines = file.readlines()
    file.close()

    file = open("database.csv", "w")
    for line in lines:
        line = line.strip("\n")
        arr = line.split(",")
        if arr[0] == attr : file.write(attr+","+str(data)+"\n")
        else : file.write(line)
    file.close()

    return True

def get_data(attr):
    file = open("database.csv")
    lines = file.readlines()
    file.close()

    for line in lines:
        line = line.strip("\n")
        words = line.split(",")
        if (words[0] == attr) : 
            return int(words[1])
    
    raise NoReturn