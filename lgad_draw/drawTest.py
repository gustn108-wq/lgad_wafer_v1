import numpy as np
import pylab as plt

import phidl.geometry as pg
from phidl import Device
from phidl import quickplot as qp

import layer_default 

layerset = layer_default.layerset

def draw_X_test(doping_layer, doping_name, width=100, metal_layer=7, oxide_layer=8, ild_layer=6):
    D = Device('X_test')
    d_tilt  = Device('X_tilt')
    d_long  = Device('X_long')
    d_short = Device('X_short')
    d_left  = Device('X_left')

    # tilt
    tpad = pg.rectangle(size=(400, width), layer=doping_layer)
    tpad.center = (0, 0)
    d_tilt.add_ref(tpad)

    tline1 = pg.rectangle(size=(30, 220), layer=metal_layer)
    tline1.xmin = tpad.xmin
    tline1.ymax = tpad.ymax
    r_tline1 = d_tilt.add_ref(tline1)

    tline2 = pg.rectangle(size=(30, 180), layer=metal_layer)
    tline2.xmax = tpad.xmax
    tline2.ymax = tpad.ymax
    r_tline2 = d_tilt.add_ref(tline2)

    ild1 = pg.boolean(tpad, tline1, operation='and', layer=ild_layer)
    ild1 = pg.offset(ild1, distance = -5, layer=ild_layer)
    ild2 = pg.boolean(tpad, tline2, operation='and', layer=ild_layer)
    ild2 = pg.offset(ild2, distance = -5, layer=ild_layer)

    r_ild1 = d_tilt.add_ref(ild1)
    r_ild2 = d_tilt.add_ref(ild2)
    
    r_tilt = d_left.add_ref(d_tilt)
    r_tilt.rotate(-45)

    mrot = np.array([[np.cos(np.radians(-45)), -np.sin(np.radians(-45))], 
                     [np.sin(np.radians(-45)),  np.cos(np.radians(-45))]])

    tip1 = np.array((r_tline1.xmin, r_tline1.ymin))
    tip2 = np.array((r_tline2.xmin, r_tline2.ymin))
    tip1 = np.matmul(mrot, tip1)
    tip2 = np.matmul(mrot, tip2)

    # long
    lpad  = pg.rectangle(size=(90, 135), layer=metal_layer)
    lline = pg.rectangle(size=(40, 250), layer=metal_layer)

    r_lline = d_long.add_ref(lline)
    r_lpad  = d_long.add_ref(lpad)
    r_lline.xmin = tip1[0]
    r_lline.ymax = tip1[1]

    # short
    sep = tip1[1] - tip2[1]
    sline = pg.rectangle(size=(40, 250 - sep), layer=metal_layer)

    r_sline = d_long.add_ref(sline)
    r_spad  = d_long.add_ref(lpad)
    r_sline.xmin = tip2[0]
    r_sline.ymax = tip2[1]

    # adjust
    r_lpad.xmin = r_lline.xmin
    r_lpad.ymax = r_lline.ymin
    r_spad.xmin = r_sline.xmin
    r_spad.ymax = r_sline.ymin

    r_loxide = d_long.add_ref(pg.offset(r_lpad, distance=-3, layer=oxide_layer))
    r_soxide = d_long.add_ref(pg.offset(r_spad, distance=-3, layer=oxide_layer))
    
    # all
    r_long  = d_left.add_ref(d_long)
    r_short = d_left.add_ref(d_short)

    d_right = pg.copy(d_left)
    d_right.mirror(p1=(0, 0), p2 = (0, 1))

    d_text = pg.text(text=doping_name, size=80, layer=metal_layer)
    d_text1 = pg.text(text=f"L400 W{width}", size=60, layer=metal_layer)
    d_text.center = (0, 360)
    d_text1.center = (0, 260)

    D << d_left
    D << d_right
    D << d_text
    D << d_text1

    return D

def draw_I_test():
    D = Device('I_test')

def main():
    D = Device('xtest')
    D_Xnplus = draw_X_test(layerset['NPLUS'], 'NPLUS')
    D_Xgain  = draw_X_test(layerset['GAIN'], 'GAIN')
    D_Xjte   = draw_X_test(layerset['JTE'], 'JTE')
    D_Xpstop = draw_X_test(layerset['PSTOP'], 'PSTOP')

    r_Xnplus = D << D_Xnplus
    r_Xgain  = D << D_Xgain
    r_Xjte   = D << D_Xjte
    r_Xpstop = D << D_Xpstop

    separation = 650
    r_Xjte.center = (separation*0, 0)
    r_Xgain.center = (separation*1, 0)
    r_Xnplus.center = (separation*2, 0)
    r_Xpstop.center = (separation*3, 0)

    D_I = draw_I_test()

    D.write_gds('test_X.gds')

if __name__=="__main__":
    main()
