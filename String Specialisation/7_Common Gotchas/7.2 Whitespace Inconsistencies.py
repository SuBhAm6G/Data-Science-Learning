with open("data.csv", encoding="utf-8") as f:
    for line in f:
        line=line.strip()
        if line:
            fields=[field.strip() for field in line.split(',')]
            print(*fields)