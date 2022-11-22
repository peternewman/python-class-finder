#!/usr/bin/env python

class Base:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)

class Subclass1(Base):
 pass

class SubSubclass1(Subclass1):
 pass

class Subclass2(Base):
 pass

class SubSubclass2(Subclass2):
 pass

def main():
  x = Base("Base")
  x.printname()

  a1 = Subclass1("Sub1")
  a1.printname()

  b1 = SubSubclass1("SubSub1")
  b1.printname()

  a2 = Subclass1("Sub2")
  a2.printname()

  b2 = SubSubclass1("SubSub2")
  b2.printname()

if __name__ == '__main__':
  main()
