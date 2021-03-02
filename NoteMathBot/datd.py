import json

def add_image(id):
    with open("dat.json", "r") as read_file:
        dat = json.load(read_file)
    dat[str(id)] = [str(id)+'.jpg']
    with open("dat.json", "w") as write_file:
        json.dump(dat, write_file)

def add_text(id, text):
    with open("dat.json", "r") as read_file:
        dat = json.load(read_file)

    t = text.split('&')
    print(text)
    print(t)
    bil= t[2].split()
    dat[str(id)].append(t[0]) #первый текст
    dat[str(id)].append(t[1]) #второй текст
    dat[str(id)].append(bil) #использованные материалы
    dat[str(id)].append(t[3]) #имя теоремы
    with open("dat.json", "w") as write_file:
        json.dump(dat, write_file)

def get(id):
    with open("dat.json", "r") as read_file:
        dat = json.load(read_file)
    otv = ''

    for i in dat[id][3]:
        ia = int(i)
        with open("dat.json", "r") as read_file:
            v = json.load(read_file)

        #print(v[i])
        otv += ("{0}: /{1}, ".format(v[i][4],i))
    dat[str(id)].append(otv)
    return dat[str(id)]