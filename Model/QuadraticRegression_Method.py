import math
import test

#import sympy as sym
#import numpy as np

class LinealRegression():
    def __init__(self):
        self.valuestable = []
        self.xi = None
        self.yi = None
        self.ymean=None
        self.xisqr = None
        self.xicube = None
        self.xifourth = None
        self.xiyi = None
        self.xi2yi = None
        self.SR = None
        self.ST = None
        self.R=None
        self.Fx=""
        #self.flag = 1.00


    def iterate(self,tablex, tabley):
        #self.valuestable = table

        lenghtx = len(tablex)
        lenghty = len(tabley)

        for i in lenghtx:
            self.xi=tablex[i]

        for i in lenghty:
            self.yi=tabley[i]

        for i in lenghtx:
            self.xisqr=tablex[i]**2

        for i in lenghtx:
            self.xicube=tablex[i]**3

        for i in lenghtx:
            self.xi=tablex[i]**4

        for i in lenghtx:
            self.xiyi=tablex[i]*tabley[i]

        for i in lenghtx:
            self.xi2yi=(tablex[i]**2)*tabley[i]

        self.ymean=self.yi/lenghty

        gaussjordantable=[[lenghty,self.xi,self.xisqr,self.yi],
                          [self.xi,self.xisqr,self.xicube,self.xiyi],
                          [self.xisqr,self.xicube,self.xifourth,self.xi2yi]]

        self.valuestable=test.gauss_jordan(gaussjordantable)

        self.calculateSTSR(tablex,tabley)
        self.Fx=str(self.valuestable[0])+"+"+str(self.valuestable[1])+"x+"+str(self.valuestable[2])+"x^2"
        return self.R, self.Fx

    def calculateSTSR(self,tablex,tabley):
        #self.Fx.subs(sym.Symbol('x'), x)

        lenghtG= len(tablex)

        for i in lenghtG:
            self.SR=tabley[i]-self.valuestable[0]-self.valuestable[1]*tablex[i]-self.valuestable[2]*(tablex[i]**2)


        for i in lenghtG:
            self.ST=(tabley[i]-self.ymean)**2

        self.R=math.sqrt((self.ST-self.SR)/self.SR)
