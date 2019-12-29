# Author: Nick Zwart
# Date: 2013oct18

# Exercise 3: SOLN
#   Compile and run the cpp node.  Observe how R2 arrays are created and
#       translated from numpy arrays.  Add another input and output array of
#       type 'int'.  Observe the output of cout() with R2 arrays (identify the
#       array type).

import gpi
import numpy as np


class ExternalNode(gpi.NodeAPI):
    """This example demonstrates the PyFI interface for arrays.
    """

    def initUI(self):
        # Widgets
        self.addWidget('PushButton', 'Compute')

    def compute(self):
        '''This is where the main algorithm should be implemented.
        '''

        # create an example data set
        data = np.ones((2,2), dtype=np.complex64) + 1.0
        data2 = np.ones((2,2), dtype=np.int32) + 2
            
        # import the C++ module
        import solutions.ex2.e3_module as e3

        # run one of the functions contained within the module
        out, out2 = e3.myFunc(data, data2)

        # display output on the console
        msg = 'Output: ' + str(out) + ', '
        msg += 'Output2: ' + str(out2)
        self.log.warn(msg)

        return 0  # success
