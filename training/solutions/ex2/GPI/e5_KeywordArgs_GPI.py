# Author: Nick Zwart
# Date: 2013oct18

# Exercise 5: SOLN
#   Compile and run the cpp node.  Force the default keyword argument to be
#       used.  Add an R2 array as a keyword argument.
#
#   Hint: Output args are always positional.  Positional args are always placed
#       before keyword args.  A default keyword argument for an array needs to
#       be an array.

import gpi


class ExternalNode(gpi.NodeAPI):
    """This is an example node that shows how a C++ python-module is called 
    within a node when it requires both positional and keyword arguments.
    """

    def initUI(self):
        # Widgets
        self.addWidget('PushButton', 'Compute')

    def compute(self):
        '''This is where the main algorithm should be implemented.
        '''
            
        # import the C++ module
        import solutions.ex2.e5_module as e5

        # The keyword argument 'myKwArg' has the same name in the C++ code.
        # Not including 'myKwArg' in the list of args forces the default to be
        # used.
        out = e5.myFunc(1.0)

        # display output on the console
        msg = 'Output: ' + str(out)
        self.log.warn(msg)

        return 0  # success
