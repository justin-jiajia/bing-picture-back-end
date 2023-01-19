from json import loads, dumps

with open("conf.json") as f:
    j = loads(f.read())
    SAVE_JSON_PATH = j["SAVE_JSON_PATH"]

with open(SAVE_JSON_PATH, "r", encoding="UTF-8") as f:
    d = loads(f.read())
for i in range(0, len(d)):
    d[i]["long_description"] = d[i]["long_description"].replace(" ", "")
    if "阅读更多" in d[i]["long_description"]:
        d[i]["long_description"] = d[i]["long_description"][
            d[i]["long_description"].index("阅读更多") + 4:
        ]
        pass
    if (
        len(d[i]["long_description"]) % 2 == 0
        and d[i]["long_description"][0: int(len(d[i]["long_description"]) / 2)]
        == d[i]["long_description"][int(len(d[i]["long_description"]) / 2):]
    ):
        d[i]["long_description"] = d[i]["long_description"][
            : int(len(d[i]["long_description"]) / 2)
        ]
with open(SAVE_JSON_PATH, "w", encoding="UTF-8") as f:
    f.write(dumps(d))
