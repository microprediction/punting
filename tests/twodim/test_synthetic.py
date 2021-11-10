from punting.twodim.twosynthetic import random_harville_market


def test_synthetic():
    n = 7
    m = random_harville_market(n=n, scr=-1)


if __name__=='__main__':
    test_synthetic()