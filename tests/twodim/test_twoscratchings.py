from punting.twodim.twoscratching import scratch_quinella, unscratch_quinella
from punting.twodim.twodimensions import all_exacta_close



def test_scratch_quinella():
    x = [[-1,2,3,-1],
         [2,-1,2,-1],
         [3,2,-1,-1],
         [-1,-1,-1,-1]]
    ndx = [0,1,2]
    x1 = scratch_quinella(q=x, ndx=ndx)
    x2 = unscratch_quinella(q=x1,ndx=ndx,n=4)
    assert all_exacta_close(x,x2)


if __name__=='__main__':
   test_scratch_quinella()