'''
class Test:
    def __init__(self):
        self.x = 10

t = Test()
print(t.x)
'''

class Test:
    def __init__(self):
        self.__x = 10 # Python changes this to format _Test__x
        self._y = 20 # protected attribute

t = Test()
#print(t.__x) # does not work

print(t._Test__x) # works, but not recommended