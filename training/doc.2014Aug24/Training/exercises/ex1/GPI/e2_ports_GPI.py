# Author: Nick Zwart
# Date: 2013oct18

# Exercise 2:
#   Make the port labeled 'in-data' require a 2-D float (64bit) array only.
#   Set the output port to only post 1D arrays (modify the algorithm
#   accordingly).
#
#	Hint: Type-attributes can also be found in the Node Developer's Guide.
#       Multi-dimensional arrays can be flattened to 1D see
#       http://www.numpy.org/.  Don't forget to import numpy.  Use a Shapes
#       and Statistics node for testing.

import gpi


class ExternalNode(gpi.NodeAPI):

    """This is an example node that shows how ports are instantiated,
    configured and set.
    """

    def initUI(self):
        '''This is where UI elements such as widgets and ports are declared.
        '''

        # Ports
        #   InPorts have an 'obligation' attribute that determines whether or
        #       or not they require data in order for the node to execute.  By
        #       default it is set to 'REQUIRED'.
        #
        #   set the:    <name>,      <type>,     <attributes>
        self.addInPort('in-data', 'NPYarray', obligation=gpi.OPTIONAL)  # E2: modify
        self.addOutPort('out-data', 'NPYarray')  # E2: modify

    def compute(self):
        '''This is where the main algorithm should be implemented.
        '''

        # get data from the port
        data = self.getData('in-data')

        # if the port is 'OPTIONAL', then check to see
        # if data exists before trying to use it.
        if data is not None:

            # do something with the data
            out = data * 2.0

            # E2: flatten the data before passing to out-port

            # set the output port
            self.setData('out-data', out)

        # Play with this clause.  If 'None' is not set, then the second time
        # the node is run, the port will change to a yellow color indicating
        # that the data have not changed, no downstream event will be
        # triggered.
        else:
            # don't trigger a downstream event
            #   -the port will turn red indicating no data present
            self.setData('out-data', None)  # E2: modify and observe

        return 0  # success
