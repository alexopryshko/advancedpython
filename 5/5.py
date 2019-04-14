def gen_fn():
    result = yield 1
    print('result of yield: {}'.format(result))
    result2 = yield 2
    print('result of 2nd yield: {}'.format(result2))
    return 'done'

def non_gen_fn():
    pass

generator_bit = 1 << 5
print(bin(gen_fn.__code__.co_flags))
print(bin(non_gen_fn.__code__.co_flags))

print(bool(gen_fn.__code__.co_flags & generator_bit))
print(bool(non_gen_fn.__code__.co_flags & generator_bit))


gen = gen_fn()
print('total', len(gen.gi_code.co_code))
gen.gi_frame.f_lasti  # (-1) - последняя инструкция

gen.send(None)
for i in range(10):
    print('send', gen.send(i * 100))


gen.gi_frame.f_lasti  # (2)
