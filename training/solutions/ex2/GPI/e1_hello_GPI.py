# Author: Nick Zwart
# Date: 2013oct18

# Exercise 1: SOLN
#   Compile and run the cpp node.  In the terminal/console window type:
#       $ gpi_make e1_module
#   This will build the cpp code into a python module that can be imported.
#   Run the module once with the default message string, then change the
#   message, recompile, and run again to test the update of the newly compiled
#   module.

import gpi


class ExternalNode(gpi.NodeAPI):
    """This is an example node that shows how a C++ python-module is called 
    within a node.
    """

    def initUI(self):
        # Widgets
        self.addWidget('PushButton', 'Compute')

    def compute(self):
        '''This is where the main algorithm should be implemented.
        '''
            
        # import the C++ module
        import solutions.ex2.e1_module as e1

        # run one of the functions contained within
        e1.myFunc()

        return 0  # success
