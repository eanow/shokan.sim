#!/usr/bin/python3
#coordinate system is an cube/axial coordinate system, with the constraint
#that x+y+z=0
#east is +x, -y
#west is -x, +y
#NW is -z, +y
#SE is +z,-y
#NE is +x, -z
#SW is -x, +z
#when using axial, we refer to q,r,s and s becomes implicit (due to x+y+z=0)
#q=x, r=z

#map is stored as a dictionary, with the hex coordinate (axial) as the dictionary key
class RegionMap:
    def __init__(self):
        self._mapdata=dict()

    def add_hex(self,hex):
        hexkey=hex.get_axial()
        self._mapdata[hexkey]=hex
        
