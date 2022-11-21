from __future__ import print_function
from pprint import pprint
import inspect
import Tests

def GetTestClasses(module):
  """Return a list of test classes from a module.

  Args:
    module: The module to search for test classes.

  Returns:
    A list of test classes.
  """
  classes = []
  for symbol in dir(module):
    print("Looking at symbol", symbol)
    cls = getattr(module, symbol)
    clsstr = str(cls)
    print("Got attr:", clsstr[:80])
    if not inspect.isclass(cls):
      print("Not a class:")
      continue
    base_classes = [
        Tests.Base,
#        Tests.Subclass1,
#        Tests.Subclass2
    ]

    if cls in base_classes:
      print("Class", cls, "in base classes, skipping")
      continue
    if issubclass(cls, Tests.Base):
      print("Class", cls, "IS a subclass of",Tests.Base)
      pprint(symbol)
      # Python 3 only
      #pprint(cls.__subclasses__())
      classes.append(cls)
  return classes
