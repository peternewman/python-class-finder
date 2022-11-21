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
    cls = getattr(module, symbol)
    if not inspect.isclass(cls):
      continue
    base_classes = [
        Tests.Base,
        Tests.Subclass1,
        Tests.Subclass2
    ]

    if cls in base_classes:
      continue
    if issubclass(cls, Tests.Base):
      classes.append(cls)
  return classes
