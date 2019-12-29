# Author: Nick Zwart
# Date: 2013oct18

# Exercise 8:
#   Compile and run the cpp node.  Observe the threaded code and runtime output.
#   Run the threaded C-function as a single thread without the POSIX interface
#   (i.e. without calling create_threads1()).   

import gpi
import numpy as np


class ExternalNode(gpi.NodeAPI):
    """This example demonstrates the simplified POSIX thread interface.
    """

    def initUI(self):
        # Widgets
        self.addWidget('PushButton', 'Compute')

    def compute(self):
        '''This is where the main algorithm should be implemented.
        '''
            
        # import the C++ module
        import solutions.ex2.e8_module as e8

        # make an input array
        in1 = np.array(range(0,4), dtype=np.float32)

        # call a threaded function
        e8.myFunc(in1)

        return 0  # success
