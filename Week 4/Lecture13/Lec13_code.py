#Lecture13
def gen_pos():
    i = 1
    while True:
        yield i
        i += 1

def test():
    x = yield from gen_pos()
    print("hi" + x)

e = test()
for i in range(10):
    print(next(e))