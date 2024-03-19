#from .Equation_Solver import Function
import sympy as sym

#from View.BiseccionView import MainWindow


class Bisection_Method():
    def __init__(self):
        #self.function = Function()
        self.expression = None
        self.a=None#float()
        self.Fa=None
        self.b=None#float()
        self.Fb=None
        self.Xr=None
        self.Xrminus1=None
        self.FXr=None
        self.aprovederror=None#window edit error
        self.calculatederror=100.00
        self.flag=1.00

    def evaluateExpression(self,x):
        return self.expression.subs(sym.Symbol('x'), x)

    def iteration(self,expression,error,a,b):
        results = []
        error_message = None
        self.expression = sym.sympify(expression)
        self.a =float(a)
        self.b =float(b)
        self.aprovederror = float(error)
        while( self.calculatederror>self.aprovederror and self.flag!=0.00):
            try:
                #print(self.a)
                    #a and b evaluate
                self.Fa=self.evaluateExpression(self.a)
                self.Fb=self.evaluateExpression(self.b)
                    #calculating xr and evaluate
                self.Xr=(self.a+self.b)/2
                self.FXr=self.evaluateExpression(self.Xr)
                #error frame calculus
                if(self.Xrminus1!=None):
                    self.calculatederror=(abs((self.Xr-self.Xrminus1)/self.Xr))*100
                else:self.calculatederror=100

                self.Xrminus1 = self.Xr
                self.flag = self.FXr * self.Fa
                #print("a1="+str(self.a))
                #here we save the a and b values in the table (before the next change)
                results.append((self.a,self.b,self.Fa,self.Fb,self.Xr,self.FXr,self.calculatederror))
                #xi_minus_1, xi, f_xi_minus_1, f_xi, xi_plus_1, error
                    #a and b changes depending on flag value
                if(self.flag>0):self.a=self.Xr
                else:self.b=self.Xr

            except ValueError as e:
                error_message = str(e)

            print("b=" + str(self.b))
            print("a=" + str(self.a))
            print("fa=" + str(self.Fa))
            print("fb=" + str(self.Fb))
            print("xr=" + str(self.Xr))
            print("fxr=" + str(self.FXr))
            print("flag=" + str(self.flag))

            #here we save the rest of the variables on the table (the loop starts again)
            return results, error_message



#some tests
#test=Bisection_Method()
#test.iteration()
