# Author: Nick Zwart
# Date: 2013oct18

# Exercise 2: SOLN
#   Compile and run the cpp node.  Add a 'long' type positional input argument.
#   Add another output argument.
#
#   Hint: Output args are always positional.

import gpi


class ExternalNode(gpi.NodeAPI):
    """This is an example node that shows how a C++ python-module is called 
    within a node when it requires positional arguments.
    """

    def initUI(self):
        # Widgets
        self.addWidget('PushButton', 'Compute')

    def compute(self):
        '''This is where the main algorithm should be implemented.
        '''
            
        # import the C++ module
        import solutions.ex2.e2_module as e2

        # run one of the functions contained within the module
        out, out2 = e2.myFunc(1.0, 2)

        # display output on the console
        msg = 'Output: ' + str(out) + ', '
        msg += 'Output2: ' + str(out2)
        self.log.warn(msg)

        return 0  # success
