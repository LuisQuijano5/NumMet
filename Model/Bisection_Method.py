import numpy as np
import matplotlib.pyplot as plt
import sympy
from sympy import Symbol
from PySide6 import QtWidgets, QtCore
import sys
import sympy as sym

from View.BiseccionView import MainWindow
#with open('styleSheet.css', 'r') as f:
   # stylesheet = f.read()
#with open(stylesheet_path, 'r') as f:
 #   stylesheet = f.read()

class Bisection_Method():
    def __init__(self):
        self.expression = sym.parse_expr("(x**4)-(2*x**3)-(12*x**2)+(16*x)-(40)")#MainWindow.__init__().edit_ecuacion)
        self.a=4.2#MainWindow.__init__().edit_a
        self.Fa=None
        self.b=4.4#MainWindow.__init__().edit_b
        self.Fb=None
        self.Xr=None
        self.Xrminus1=None
        self.FXr=None
        self.aprovederror=0.01#MainWindow.__init__().edit_error
        self.calculatederror=100
        self.flag=1

    def evaluateExpression(self,x):
        return self.expression.subs(sym.Symbol('x'), x)

    def iteration(self):
        ##print(self.a)
        while( self.calculatederror>self.aprovederror):
            #print(self.a)
            self.Fa=self.evaluateExpression(self.a)
            self.Fb=self.evaluateExpression(self.b)

            self.Xr=(self.a+self.b)/2
            self.FXr=self.evaluateExpression(self.Xr)
            if(self.Xrminus1!=None):
                self.calculatederror=(abs((self.Xr-self.Xrminus1)/self.Xr))*100
            else:self.calculatederror=100

            self.Xrminus1 = self.Xr
            self.flag = self.FXr * self.Fa
            #print("a1="+str(self.a))
            #here we save the a and b values in the table (before the next change)
            if(self.flag>0):self.a=self.Xr
            else:self.b=self.Xr
            #here we save the rest of the variables on the table (the loop starts again)

            #print("b="+str(self.b))
            #print("a=" + str(self.a))
            #print("fa=" + str(self.Fa))
            #print("fb=" + str(self.Fb))
            #print("fxr=" + str(self.FXr))
            #print("flag=" + str(self.flag))

#test=Bisection_Method()
#test.iteration()
