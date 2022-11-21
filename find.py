#!/usr/bin/env python
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# find.py
# Copyright (C) 2022 Peter Newman

from __future__ import print_function
#import Tests
import pkg1.pkg2.Tests
import TestRunner
import sys

def main():
  #test_classes = TestRunner.GetTestClasses(Tests)
  #test_classes = TestRunner.GetTestClasses(pkg1.Tests)
  test_classes = TestRunner.GetTestClasses(pkg1.pkg2.Tests)
  if len(test_classes) <= 0:
    print('Failed to find any tests to run')
    sys.exit(2)
  print("="*80)
  for test_name in sorted(c.__name__ for c in test_classes):
    print(test_name)
  sys.exit(0)

if __name__ == '__main__':
  main()
