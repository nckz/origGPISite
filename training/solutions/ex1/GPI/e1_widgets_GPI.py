# Author: Nick Zwart
# Date: 2013oct18

# Exercise 1: SOLN
#   Add a PushButton widget that toggles the TextBox widget's
#   visibility attribute.
#
#   Hint: Reference other node-code that has the desired behavior
#       or the Node Developer's Guide for the attribute name.

import gpi


class ExternalNode(gpi.NodeAPI):
    """This is an example node that shows how widgets are instantiated,
    modified and queried.  This text shows up in the Mouse Menu under 
    the 'about' widget (double-click with the left mouse button).
    """

    def initUI(self):
        '''This is where UI elements such as widgets and ports are declared.
        '''
 
        # Widgets
        #   set the:    <type>,   <name>,   <default attribute>
        self.addWidget('TextBox', 'My Info', val='hello world!')
        self.addWidget('PushButton', 'Change Message', toggle=True)
        self.addWidget('PushButton', 'Text Visibility', toggle=True)

    def compute(self):
        '''This is where the main algorithm should be implemented.
        '''
            
        # get data from widgets
        #   -retrieves the 'val' attribute of the widget.
        pushed = self.getVal('Change Message')
        vis = self.getVal('Text Visibility')

        # one-shot pushbutton
        if pushed:

            # set widget data
            #   -the 'val' attribute is considered the main/central data of
            #    a widget.
            #   -setAttr() can set multiple attributes of a widget at the same
            #    time, just add more comma separated arguments.
            self.setAttr('My Info', val='goodbye world!')
        else:
            self.setAttr('My Info', val='hello world!')

        # toggle pushbutton
        if vis:
            self.setAttr('My Info', visible=True)
        else:
            self.setAttr('My Info', visible=False)

        return 0  # success
