import json

def add_image(id):
    with open("dat.json", "r") as read_file:
        dat = json.load(read_file)
    dat
    with open("dat.json", "w") as write_file:
        json.dump(dat, write_file)