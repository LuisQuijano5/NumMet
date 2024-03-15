import numpy as np
import matplotlib.pyplot as plt
import sympy
from sympy import Symbol
from PySide6 import QtWidgets, QtCore
import sys
import sympy as sym
from View.BiseccionView import MainWindow
with open('styleSheet.css', 'r') as f:
    stylesheet = f.read()

class Bisection_Method():
    def __init__(self):
        self.expression = sym.parse_expr(MainWindow.__init__().edit_ecuacion)
        self.a=MainWindow.__init__().edit_a
        self.Fa=None
        self.b=MainWindow.__init__().edit_b
        self.Fb=None
        self.Xr=None
        self.Xrminus1=None
        self.FXr=None
        self.aprovederror=MainWindow.__init__().edit_error
        self.calculatederror=None
        self.flag=None

    def evaluateExpression(self,x):
        return self.expression.subs(sym.Symbol('x'), x)

    def iteration(self):
        while(self.flag!=0 & self.calculatederror>self.aprovederror):
            self.Fa=self.evaluateExpression(self.a)
            self.Fb=self.evaluateExpression(self.b)

            self.Xr=(self.a+self.b)/2
            self.FXr=self.evaluateExpression(self.Xr)
            if(self.Xrminus1!=None):
                self.calculatederror=(abs((self.Xr-self.Xrminus1)/self.Xr))*100
            else:
                self.calculatederror=100

            self.Xrminus1 = self.Xr
            self.flag = self.FXr * self.Fa
            if(self.flag>0):self.a=self.Xr
            else:self.b=self.Xr
