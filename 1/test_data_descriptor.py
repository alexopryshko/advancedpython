# data descriptor


class DataDescriptor:
    def __get__(self, obj, cls):
        print("access from {0} class {1}".format(obj, cls))

    def __set__(self, obj, val):
        print("set {0} for {1}".format(val, obj))

    def __delete__(self, obj):
        print("delete from {0}".format(obj))


class SomeData:
    data = DataDescriptor()


# 1 методы дескриптора
d = SomeData()
SomeData.data  # вот тут будет вызван __get__ с obj None
d.data
d.data = 1
del d.data

# 2 особенность data descriptor
d.__dict__['data'] = 1
d.data

# 3 Если изменить значение атрибута с дескриптором через класс,
#   никаких методов дескриптора вызвано не будет
SomeData.data = 1
print(SomeData.data)
del SomeData.data
print(SomeData.data)
