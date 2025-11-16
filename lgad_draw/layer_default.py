from phidl import LayerSet

layerset = LayerSet()
layerset.add_layer(name='AKEY',  gds_layer=1,  gds_datatype=0, color='goldenrod')
layerset.add_layer(name='JTE',   gds_layer=2,  gds_datatype=0, color='pink')
layerset.add_layer(name='GAIN',  gds_layer=3,  gds_datatype=0, color='blue')
layerset.add_layer(name='NPLUS', gds_layer=4,  gds_datatype=0, color='red')
layerset.add_layer(name='PSTOP', gds_layer=5,  gds_datatype=0, color='lightblue')
layerset.add_layer(name='ILD',   gds_layer=6,  gds_datatype=0, color='green')
layerset.add_layer(name='METAL', gds_layer=7,  gds_datatype=0, color='gray')
layerset.add_layer(name='OXIDE', gds_layer=8,  gds_datatype=0, color='lightgreen')
layerset.add_layer(name='WAFER', gds_layer=80, gds_datatype=0, color='black')
layerset.add_layer(name='AUX',   gds_layer=81, gds_datatype=0, color='white')

