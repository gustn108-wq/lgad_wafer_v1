
from phidl import geometry as pg

import pylab as plt

import lgad_draw as lg

def align_key(fname):   
    d_alignkey = pg.import_gds(fname, cellname='toplevel')
    d_alignkey.center = (0, 0)
    d_alignkey.write_gds('akey1')

    return d_alignkey

if __name__=="__main__":
    d = align_key('./akey.gds')
    lg.qp(d)
    plt.show()
