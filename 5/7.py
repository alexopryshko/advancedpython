def gen_fn():
    result = yield 1
    print('result of yield: {}'.format(result))
    result2 = yield 2
    print('result of 2nd yield: {}'.format(result2))
    return 'done'


def f():
    res = yield from gen_fn()
    print('res', res)


gen = f()

for el in gen:
    print(el)

# gen.gi_frame.f_lasti  # demo