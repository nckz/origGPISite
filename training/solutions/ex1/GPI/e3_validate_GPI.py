# Author: Nick Zwart
# Date: 2013oct18

# Exercise 3: SOLN
#   Using a Shapes node as the upstream input, execute the three different
#   return codes via the choice widget on an active canvas.  Practice returning
#   the node to an idle state after a warning or error code.  Make the error
#   messages more informative so that the user doesn't have to look through the
#   code to resolve the runtime requirements.
#
#	Hint: A new event can reactivate a node in 'Warning' mode.  Copy/Paste can
#       reactivate a node in 'Error' mode (the canvas will have to be
#       un-paused).  Set the Shapes node to the appropriate output value range
#       (i.e. Pass Value: <=1, Stop Value: >=0).

import gpi


class ExternalNode(gpi.NodeAPI):
    """This example shows how the validate function can be used.
    """

    def initUI(self):
        '''This is where UI elements such as widgets and ports are declared.
        '''
        # Widgets
        self.addWidget('ExclusivePushButtons', 'Return Code',
                       buttons=['Success', 'Warning', 'Error'],
                       val=0)
        self.codes = [0, 1, -1]  # 0:success, 1:warning, -1:error
 
        # Ports
        self.addInPort('in-data', 'NPYarray')
        self.addOutPort('out-data', 'NPYarray')


    def validate(self):
        '''This function runs before compute().  Here, widgets (bounds, limits,
        etc...) can be modified to ensure they are correctly validated before
        the widget values are used in compute().
        '''

        # check some requirement of the data that is not enforcible by the ports
        data = self.getData('in-data')
        if data.min() <= -0.1:
            self.log.warn('The input data cannot be <= -0.1!  Aborting.')
            return 1  # warning

        # check user specified return code
        ret = self.getVal('Return Code')

        # translate user's choice to the correct code and return
        return self.codes[ret]
        

    def compute(self):
        '''This is where the main algorithm should be implemented.
        '''

        # get data from the port
        data = self.getData('in-data')

        # algorithm code
        out = data * 2.0

        # Check that the algorithm didn't fail in some specific way.  In this
        # case we have an arbitrary threshold.
        if out.max() >= 2.1:
            self.log.warn('The results equal or exceed a value of 2.1.')
            return 1  # warning

        self.setData('out-data', out)

        return 0  # success
