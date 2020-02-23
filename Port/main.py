class Mathcalc:
    def __init__(self):
        pass
    def calc (self,value):
        a = value['a']
        b = value['b']
        add = a + b
        sub = a - b
        div = a / b
        mul = a * b
        return {'input':value,'output':{'addition':add, 'subtraction':sub, 'division':div, 'multiplication':mul}}
