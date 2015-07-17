#!/usr/bin/env python
#
#   Copyright 2014 Jonas Berg
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

"""

.. moduleauthor:: Jonas Berg <pyhys@users.sourceforge.net>

test_all_simulated: Run all the unit tests (without any hardware)

This Python file was changed (committed) at $Date: 2014-03-23 18:38:52 +0100 (Sun, 23 Mar 2014) $, 
which was $Revision: 179 $.

"""

__author__  = "Jonas Berg"
__email__   = "pyhys@users.sourceforge.net"
__license__ = "Apache License, Version 2.0"

__revision__  = "$Rev: 179 $"
__date__      = "$Date: 2014-03-23 18:38:52 +0100 (Sun, 23 Mar 2014) $"

import unittest

import test_minimalmodbus
import test_eurotherm3500
import test_omegacn7500

if __name__ == '__main__':
   
    suite = unittest.TestLoader().loadTestsFromModule( test_minimalmodbus )
    suite.addTest( unittest.TestLoader().loadTestsFromModule(test_eurotherm3500) )
    suite.addTest( unittest.TestLoader().loadTestsFromModule(test_omegacn7500) )

    unittest.TextTestRunner(verbosity=0).run(suite)

