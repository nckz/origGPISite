# Author: Nick Zwart
# Date: 2013oct18

# Exercise 6:
#   Using the gpi library/node directory structure, create a new pure-python
#   module.  Move the contents of the compute() algorithm to the module and
#   call the algorithm as a function from that module.
#
#   Hint: Use the Statistics node to check your work.

import gpi


class ExternalNode(gpi.NodeAPI):
    """This example shows how to determine the type of event that triggered a
    node's exectution.
    """

    def initUI(self):
        '''This is where UI elements such as widgets and ports are declared.
        '''
        # Widgets
        self.addWidget('DoubleSpinBox', 'Scale', immediate=True)

        # Ports
        self.addOutPort('out', 'NPYarray')

    def compute(self):
        '''This is where the main algorithm should be implemented.
        '''
        import numpy as np
        # import exercises.ex1.e6_module  # E6: Hint

        # E6: Identify which lines of code (below) should go into an
        #       external kernel python-module '.py' file.

        # get user input
        scale = self.getVal('Scale')

        # generate a dataset
        out = np.ones((2,2))

        # perform the algorithm
        out *= scale

        self.setData('out', out)

        return 0  # success
