def cheksiz_tub_sonlar():
    n = 1
    while True:
        yield n
        n = n + 1

generator = cheksiz_tub_sonlar()
for _ in range(10):
    print(next(generator))
