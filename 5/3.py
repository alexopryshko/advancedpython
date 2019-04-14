def foo():
    bar()

def bar():
    pass

import dis
dis.dis(foo)



