a = 2


def changeA():
    a = 3


changeA()
print(a)


def changeglobalA():
    global a
    a = 3


changeglobalA()
print(a)