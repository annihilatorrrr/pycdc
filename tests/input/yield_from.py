def gen10():
    yield from range(10)

def gen20():
    yield from range(10, 20)

def generator():
    yield from gen10()
    yield from gen20()
