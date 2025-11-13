import sys
import json

import pylab as plt
import lgad_draw as lg

def draw_reticle():
    if len(sys.argv) > 1:
        jsonname = sys.argv[1]
    else:
        jsonname = './reticle_template.json'
        print (f'[INFO] Using json file : {jsonname}', file=sys.stderr)

    with open(jsonname, "r", encoding="utf-8") as f:
        jdata = json.load(f)

    reticle_name = jdata['RETICLENAME']

    reticle = lg.DrawReticle(reticle_name)
    
    d_reticle = reticle.Draw_from_json(jsonname)

    d_reticle.write_gds(f'{reticle_name}.gds') 
    lg.qp(d_reticle)
    plt.show()


if __name__=="__main__":
    draw_reticle()
