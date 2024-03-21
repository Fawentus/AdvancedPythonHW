import numpy as np
from hw_3.matrix import Matrix


def custom_print(name, matrix, sep="\n"):
    print(name, ":", sep, matrix, "\n", sep="")


a = Matrix(list(np.random.randint(0, 10, (10, 10))), False)
b = Matrix(list(np.random.randint(0, 10, (10, 10))), False)

custom_print("A", a)
custom_print("B", b)
custom_print("A+B", a+b)
custom_print("A*B", a*b)
custom_print("A@B", a@b)

while True:
    a = Matrix(list(np.random.randint(0, 10, (10, 10))))
    b = Matrix(list(np.random.randint(0, 10, (10, 10))))
    c = Matrix(list(np.random.randint(0, 10, (10, 10))), False)

    ab = a@b
    cb = c@b

    if hash(a) == hash(c) and a != c and ab != cb:
        custom_print("A", a)
        custom_print("Hash A", hash(a), sep=" ")

        custom_print("B", b)
        custom_print("Hash B", hash(b), sep=" ")

        custom_print("C", c)
        custom_print("Hash C", hash(c), sep=" ")

        custom_print("D", b)
        custom_print("Hash D", hash(b), sep=" ")

        custom_print("A@B", ab)
        custom_print("C@D", cb)
        custom_print("Hash A@B", hash(ab), sep=" ")
        custom_print("Hash C@D", hash(cb), sep=" ")

        break
