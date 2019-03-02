# non data descriptor


class NonDataDescriptor:
    def __get__(self, obj, cls):
        print("access from {0} class {1}".format(obj, cls))


class SomeData:
    data = NonDataDescriptor()


# 1 методы дескриптора
d = SomeData()
SomeData.data  # вот тут будет вызван __get__ с obj None
d.data

# 2 особенность non data descriptor
d.data = 1
print(d.data)
