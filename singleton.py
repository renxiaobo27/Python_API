def singleton(class_):
  instances = {}
  def getinstance(*args, **kwargs):
    if class_ not in instances:
        instances[class_] = class_(*args, **kwargs)
    return instances[class_]
  return getinstance

@singleton
class A:

    def __init__(self):
        self.count = 0
    def inc(self):
        self.count +=1

class B:
    def __init__(self):
        print 'a'

        
a = A()
a.inc()
print a.count
print type(a)
b = A()
print a==b

g = B()
h=B()
print g==h
