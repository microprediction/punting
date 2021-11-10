import numpy as np
from punting.onedim.onescratching import scratch_win, unscratch_win
from punting.twodim.twoscratching import scratch_quinella, unscratch_quinella
from punting.twodim.twodimensions import all_exacta_close


def test_win():
    x = np.array([-1,2,3,-1,-1,3,-1,-1])
    x_starters, ndx, n = scratch_win(x)
    x1 = unscratch_win(x=x_starters, ndx=ndx, n=n, scr=-1)
    assert np.allclose(x,x1,atol=1e-6)


def test_win_list():
    x = [-1,2,3,-1,-1,3,-1,-1]
    x_starters, ndx, n = scratch_win(x)
    x1 = unscratch_win(x=x_starters, ndx=ndx, n=n, scr=-1)
    assert np.allclose(x,x1,atol=1e-6)




if __name__=='__main__':
   test_win()