from __future__ import print_function
from pprint import pprint
import inspect
#import pkg1.Tests
import ola.testing.rdm.Tests

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
#        Tests.Base,
#        Tests.Subclass1,
#        Tests.Subclass2
#        pkg1.Tests.Base,
#        pkg1.pkg2.Tests.Base,
        ola.testing.rdm.Tests.Base,
    ]

    if cls in base_classes:
      print("Class", cls, "in base classes, skipping")
      continue
    if issubclass(cls, ola.testing.rdm.Tests.Base):
      print("Class", cls, "IS a subclass of", ola.testing.rdm.Tests.Base)
      pprint(symbol)
      # Python 3 only
      #pprint(cls.__subclasses__())
      classes.append(cls)
    else:
      print("Class", cls, "is not a subclass of", ola.testing.rdm.Tests.Base)
  return classes
