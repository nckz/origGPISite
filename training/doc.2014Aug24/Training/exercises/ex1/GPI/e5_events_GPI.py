# Author: Nick Zwart
# Date: 2013oct18

# Exercise 5:
#   Observe different events by connecting and interacting with the node
#   interface.  Add another interactive widget to observe different widget
#   events (by name).  Add another inport to see different port events.

import gpi


class ExternalNode(gpi.NodeAPI):
    """This example shows how to determine the type of event that triggered a
    node's exectution.
    """

    def initUI(self):
        '''This is where UI elements such as widgets and ports are declared.
        '''
        # Widgets
        self.addWidget('TextBox', 'Event')
        self.addWidget('PushButton', 'Compute')

        # Ports
        self.addInPort('in-data', 'NPYarray', obligation=gpi.OPTIONAL)

    def compute(self):
        '''This is where the main algorithm should be implemented.
        '''

        # get the events and post them to a text box in the UI
        msg  = 'Main getter: ' + str(self.getEvents()) + '\n'
        msg += '    Port event: ' + str(self.portEvents()) + '\n'
        msg += '    Wdg event: ' + str(self.widgetEvents())

        self.setAttr('Event', val=msg)

        return 0  # success
