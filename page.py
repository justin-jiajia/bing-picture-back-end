from json import loads, dumps


def page():
    with open('conf.json') as f:
        j = loads(f.read())
        SAVE_JSON_PATH = j['SAVE_JSON_PATH']
    with open(SAVE_JSON_PATH.replace('*', ''), 'r', encoding='UTF-8') as f:
        zd = loads(f.read())
    zd.reverse()
    page = len(zd)//10
    for i in range(1, page+1):
        with open(SAVE_JSON_PATH.replace('*', str(i)), 'w', encoding='UTF-8') as f:
            t = zd[(i-1)*10:i*10]
            f.write(dumps(t))
    if len(zd) % 10:
        with open(SAVE_JSON_PATH.replace('*', str(page+1)), 'w', encoding='UTF-8') as f:
            t = zd[page*10:]
            f.write(dumps(t))
    with open(SAVE_JSON_PATH.replace('*', '0'), 'w', encoding='UTF-8') as f:
        f.write(dumps({'many': len(zd)}))


if __name__ == "__main__":
    page()
