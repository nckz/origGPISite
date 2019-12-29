# Author: Nick Zwart
# Date: 2013oct18

# Exercise 7:
#   Compile and run the cpp node.  Observe the code format for creating R2
#       algorithms that can be easily transported to the Recon Platform.
#       Pass dimensions to the kernel algorithm and generate an R2 array inside.
#
#   Guidelines:
#       1) Code all algorithm components in C++.  Anything done in python will
#           have to be converted when the node is ported to R2.
#       2) Pull all algorithm code into a separate .cpp file (different from
#           the PyMOD.cpp).  This file will be directly included in the R2 node.
#           This file is usually suffixed with '_kernel.cpp' for easy
#           identification.
#       3) All pure algorithm code should be clear of PyFI or Python function
#           calls.  Only R2 library calls are portable.

import gpi


class ExternalNode(gpi.NodeAPI):
    """This example demonstrates the PyFI error function for passing
    exceptions to python.
    """

    def initUI(self):
        # Widgets
        self.addWidget('DoubleSpinBox', 'input', decimals=3, singlestep=0.1, immediate=True)

    def compute(self):
        '''This is where the main algorithm should be implemented.
        '''
        val = self.getVal('input')
            
        # import the C++ module
        import exercises.ex2.e7_module as e7

        # call an R2 portable PyMOD
        out = e7.myFunc(val)

        # display output on the console
        msg = 'Output: ' + str(out)
        self.log.warn(msg)

        return 0  # success
