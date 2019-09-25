#!/usr/bin/python3
OUTDOOR_HEX_SIZE=1
DEBUG=True

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

class MapHex:
    #class representing the 'hex' entity that comprises a map. Knows its own
    #coordinate, and information about terrain and points of interest.
    def __init__(self,x,y,z):
        self._x=x
        self._y=y
        self._z=z
        self._road='trackless'
        self._terrain='none'

    def get_axial(self):
        return str(self._x)+'|'+str(self._z)

    def set_terrain(self,terrain_type):
        self._terrain=terrain_type
        #valid values include
        #desert
        #forest
        #hills
        #jungle
        #moor
        #mountains
        #plains
        #swamp
        #tundra
        #water

    def set_road(self,road_quality):
        self._road=road_quality
        #valid values include
        #highway
        #road
        #trail
        #trackless

    def move_cost(self):
        #returns the cost (normalized to hex scale) of moving into this hex.
        #this information is informed by the tables from CRB overland movement
        #section, table 7-8

        #certain simplifying assumptions are made.
        #Movement costs are determined by the destination hex terrain.
        if self._road=='highway':
            if self._terrain=='mountains':
                return float(4.0/3.0)
            else:
                return float(1.0)
        elif self._road=='road' or self._road=='trail':
            if self._terrain == 'desert':
                return float(2.0)
            elif self._terrain in ['hills','jungle','mountains','swamp','tundra']:
                return float(4.0/3.0)
            elif self._terrain in ['forest','moor','plains']:
                return float(1.0)
            else:
                if DEBUG:
                    print("unexpected road/terrain combination for hex "+str(self._x)+" "+str(self._y)+" "+str(self._z))
                return float(1.0)
        elif self._road=='trackless':
            if self._terrain in ['desert','forest','hills','mountains','swamp']:
                return float(2.0)
            elif self._terrain in ['jungle']:
                return float(4.0)
            elif self._terrain in ['moor','plains','tundra']:
                return float(4.0/3.0)
            elif self._terrain == 'water':
                return float(1.0)
            else:
                if DEBUG:
                    print("unexpected road/terrain combination for hex"+str(self._x)+" "+str(self._y)+" "+str(self._z))
                return float(1.0)
        else:
            if DEBUG:
                print("unexpected road/terrain combination for hex"+str(self._x)+" "+str(self._y)+" "+str(self._z))
            return float(1.0)
