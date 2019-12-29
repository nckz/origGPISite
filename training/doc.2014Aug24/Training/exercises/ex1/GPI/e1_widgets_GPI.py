# Author: Nick Zwart
# Date: 2013oct18

# Exercise 1:
#   Add a PushButton widget that toggles the TextBox widget's
#   visibility attribute.
#
#	Hint: Reference other node-code that has the desired behavior or the
#       Node Developer's Guide for the attribute name.  Use the 'gpi_make'
#       script to check your python code (in a terminal window): 
#           $ gpi_make e1_widgets_GPI.py

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
        self.addWidget('PushButton', 'Change Message')

        # E1: Your first line of code will go here...
        #   Add a new push-button widget.

    def compute(self):
        '''This is where the main algorithm should be implemented.
        '''

        # get data from widgets
        #   -retrieves the 'val' attribute of the widget.
        pushed = self.getVal('Change Message')

        # E1: Your second line of code will go here...
        #   Get the 'val' of your new push-button widget.

        # one-shot pushbutton
        if pushed:

            # set widget data
            #   -the 'val' attribute is considered the main/central data of
            #    a widget.
            #   -setAttr() can set multiple attributes of a widget at the same
            #    time, just add more comma separated arguments.
            self.setAttr('My Info', val='goodbye world!')

        # E1: Write an 'if' case based on the new push-button value.
        #   Set the visibility attribute of 'My Info' using setAttr().

        return 0  # success
