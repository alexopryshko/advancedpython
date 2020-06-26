def gen_fn():
    result = yield 'abc'
    print('result of yield: {}'.format(result))
    result2 = yield 'def'
    print('result of 2nd yield: {}'.format(result2))
    return 'done'


print('first yield:', gen.send(None))
for i in range(10):
    print('send', gen.send(i * 100))


gen.gi_frame.f_lasti  # (2)
