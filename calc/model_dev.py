x = 0
y = 0

def init(a, b): #отвечает за инициализацию
    global x #без этого метод не будет видеть х и y что указаны выше
    global y
    x = a
    y = b

def do_dev():
    return x/y