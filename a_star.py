
from graph import *
import numpy as np

# Read graph data and coordinates data (to be implemented)

###########################################
########## A* implementation ##############
###########################################
graph=('data/USA-road-d.NY.gr')
coord=('data/USA-road-d.NY.co')
a= readGraph(graph)
b= readCoordinates(coord)
W= np.zeros(len(b))
H= np.zeros(len(b))

    

# Priority queue definition
class PriorityQueue:
    def __init__(self, f):
        self.elements = []
        self.f = f

    def empty(self):
        return len(self.elements) == 0

    def included(self, item):
        return item in self.elements

    def put(self, item):
        self.elements.append(item)

    def get(self):
        e_min = min(self.elements, key=lambda e:self.f[e])
        self.elements.pop(self.elements.index(e_min))
        return e_min


def angles2centimeters(la, lo):
    """
    :param la: latitude
    :param lo: longitude
    :return: new orthogonal grid centered around NYC
    """
    
    radius = 6300 * 1e4  # cm. While 6369.053*1e4 is more realistic, this could fail the heuristic
    la_mean = 40794234.  # 1e-6 degree
    lo_mean = -74016939.  # 1e-6 degree
    
    h = radius * np.radians((la - la_mean) / 1e6)
    w = radius * np.cos(np.radians(la / 1e6)) * np.radians((lo - lo_mean) / 1e6)
    
    return h, w


def h(pos1,pos2):
    """
    Heuristic function (to be implemented)
    convert coordinates from degree to cm (def angle2cm)
    """
    return abs(point.point[0] - point2.point[0]) + abs(point.point[1]-point2.point[0])
    return 0


# A* algorithm (to be implemented)
def a_star_search(graph,start,goal):
    """
    :param graph:
    :param start:
    :param goal:
    :return: The path and total length
    """
    return [],0



for x in  range(len(b)):
    lo,la=b[x]
    H[x],W[x]= angles2centimeters(la,lo)
    

