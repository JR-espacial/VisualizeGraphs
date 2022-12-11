import turtle as t
import time


CIRSZ=30


def getCenter():
    return [t.xcor(), t.ycor()+CIRSZ]


def drawLine(src,dst,w = None):
    t.pu()
    t.goto(centers[src])
    t.seth(t.towards(centers[dst][0],centers[dst][1]))
    t.fd(CIRSZ)
    t.pd()
    t.goto(centers[dst])

    #code for labeling weight
    if w:
        pass


#TODO
#function for decideng on the node coordinates so that ther are visualy separeted
def createNodes(graph):
    #get the node with most connections and count them
    pass



centers ={ 0: [0,30], 1: [100,200] }

t.mode("standard")
t.circle(CIRSZ)


drawLine(0,1)






t.exitonclick()
