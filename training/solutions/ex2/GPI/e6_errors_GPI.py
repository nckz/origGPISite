# Author: Nick Zwart
# Date: 2013oct18

# Exercise 6: SOLN
#   Compile and run the cpp node.  Capture the python exception and log the message.
#
#   Hint:
#       -Python Exceptions
#           http://docs.python.org/2/tutorial/errors.html#handling-exceptions
#       -Check the traceback in the terminal/console to find the exception-type

import gpi


class ExternalNode(gpi.NodeAPI):
    """This example demonstrates the PyFI error function for passing
    exceptions to python.
    """

    def initUI(self):
        # Widgets
        self.addWidget('PushButton', 'Compute')

    def compute(self):
        '''This is where the main algorithm should be implemented.
        '''
            
        # import the C++ module
        import solutions.ex2.e6_module as e6

        # Cause a python exception from C++.
        try:
            e6.myFunc()
        except RuntimeError:
            self.log.warn('Caught exception from PyMOD e6')

        return 0  # success
