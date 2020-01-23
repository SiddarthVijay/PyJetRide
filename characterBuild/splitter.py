with open("./dragon.txt") as f:
    l = []
    while True:
        c = f.read(1)
        if not c:
            print("End of file")
            break
        print("Read a character:" + c)
        l.append(c.rstrip())
    print(l)
    print()
