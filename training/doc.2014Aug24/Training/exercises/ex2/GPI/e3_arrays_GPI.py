# Author: Nick Zwart
# Date: 2013oct18

# Exercise 3:
#   Compile and run the cpp node.  Observe how R2 arrays are created and
#       translated from numpy arrays.  Add another input and output array of
#       type 'int'.  Observe the output of coutv() with R2 arrays (identify the
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
            
        # import the C++ module
        import exercises.ex2.e3_module as e3

        # run one of the functions contained within the module
        out = e3.myFunc(data)

        # display output on the console
        msg = 'Output: ' + str(out)
        self.log.warn(msg)

        return 0  # success
