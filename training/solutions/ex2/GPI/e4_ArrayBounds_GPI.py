# Author: Nick Zwart
# Date: 2013oct18

# Exercise 4: SOLN
#   Compile and run the cpp node.  Observe how R2 arrays are created and
#       translated from numpy arrays.  Add an two more outputs to the PyMOD
#       that generate arrays using the R2 ArrayBounds object and one that
#       generates an ArrayBounds object from another R2 array.

import gpi
import numpy as np


class ExternalNode(gpi.NodeAPI):
    """This example shows other ways of generating R2 arrays in C++.
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
        import solutions.ex2.e4_module as e4

        # run one of the functions contained within the module
        out, out3, out4, out2 = e4.myFunc(data)

        # display output on the console
        msg = 'Output: ' + str(out) + ', \n'
        msg += 'Output2: ' + str(out2) + ', \n'
        msg += 'Output3: ' + str(out3) + ', \n'
        msg += 'Output4: ' + str(out4)
        self.log.warn(msg)

        return 0  # success
