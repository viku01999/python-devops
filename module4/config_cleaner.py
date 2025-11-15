configs = [
    " user = root ",
    " port = 8080 ",
    " environment = production "
]


cleaned = [line.strip().replace(" ", "") for line in configs]


for c in cleaned:
    print(c)