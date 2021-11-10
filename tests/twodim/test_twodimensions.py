import numpy as np

from punting.twodim.twodimensions import to_flat_quinella, to_list, from_list, all_exacta_close, from_flat_quinella, to_flat_exacta, from_flat_exacta

def test_conversions():
    x = np.ndarray(shape=(5, 5))
    xl = to_list(x, diag_val=-1)
    xl1 = to_list(x, diag_val=-1)
    assert all_exacta_close(xl, xl1)
    q = to_flat_quinella(xl)
    print(len(q))


def test_inversion():
    x = np.ndarray(shape=(5, 5))
    xl = to_list(x)
    y = from_list(xl)
    assert all_exacta_close(x,y)


def test_from_exacta():
    x = np.ndarray(shape=(5, 5))
    q = to_flat_exacta(x)
    x1 = from_flat_exacta(q)
    q1 = to_flat_exacta(x1)
    x2 = from_flat_exacta(q1)
    assert all_exacta_close(x1,x2)


def test_from_quinella():
    x = np.ndarray(shape=(5, 5))
    q = to_flat_quinella(x)
    x1 = from_flat_quinella(q)
    q1 = to_flat_quinella(x1)
    x2 = from_flat_quinella(q1)
    assert all_exacta_close(x1,x2)






if __name__=='__main__':
    test_from_exacta()
    test_from_quinella()