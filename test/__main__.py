# -*- coding: utf-8 -*-

import sys
import unittest

sys.path.append('../debian_interfaces_parser')

loader = unittest.TestLoader()
test_suite = loader.discover('test')
test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(test_suite)
