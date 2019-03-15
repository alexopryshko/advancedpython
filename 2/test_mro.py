class A:
    pass


class B:
    pass


class C(A, B):
    pass


print(C.__mro__)

#   object
#    /  \
#   A   B
#   \  /
#    C
#
# L[C] = [C] + merge(L[A], L[B], [A, B])
# L[A] = [A] + merge(L[object], [object])
# L[B] = [B] + merge(L[object], [object])
#
# L[object] = [object]
# merge(L[object], [object]) = merge([object], [object]) = [object]
# L[A] = [A] + [object] = [A, object]
# L[B] = [B] + [object] = [B, object]
#
# L[C] = [C] + merge([A, object], [B, object], [A, B])
# Находим "A" в "head" 3го массива => добавляем его в итоговый список
# линеаризации. После этого класс A нужно удалить изо всех списков в объединении
#
# L[C] = [C, A] + merge([object], [B, object], [B])
# Находим "object" в "tail" 2го массива => означает, что класс
# object является предком класса B => возьмем 0 элемент из 2го списка
# Находим "B" в "head" 3го массива => добавляем его в итоговый список
# линеаризации. После этого класс B нужно удалить изо всех списков в объединении
#
# L[C] = [C, A, B] + merge([object], [object], []) = [C, A, B, object]


class A:
    pass


class B(A):
    pass


class C(B, A):
    pass


print(C.__mro__)

#  object
#    |
#    A
#   /|
#  B |
#   \|
#    C
#
# L[C] = [C] + merge(L[B], L[A], [B, A])
# L[B] = [B] + merge(L[A], [A])
# L[A] = [A] + merge(L[object], [object]) = [A, object]
#
# L[B] = [B] + merge([A, object], [A]) = [B, A] + merge([object]) =
# = [B, A, object]
#
# L[C] = [C] + merge([B, A, object], [A, object], [B, A]) =
# = [C, B] + merge([A, object], [A, object], [A]) =
# = [C, B, A, object]


class A:
    pass


class B(A):
    pass


class C(A, B):
    pass


print(C.__mro__)

# object
#   |
#   A
#   | \
#   |  B
#   | /
#   C
#
# L[C] = [C] + merge(L[A], L[B], [A, B])
# L[C] = [C] + merge([A, object], [B, A, object], [A, B])
# merge не может быть завершено тк A находится внутри "tail" L[B], а
# B находится внутри "tail" [A, B] => TypeError

