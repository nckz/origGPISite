# Author: Nick Zwart
# Date: 2013oct18

# Exercise 4:
#   Test each log message against the 'Logger Level' menu setting in the
#       main menu -> Debug sub-menu.  Use the terminal/console window to see
#       the output.

import gpi


class ExternalNode(gpi.NodeAPI):
    """This example demonstrates the logging interface.
    """

    def initUI(self):
        '''This is where UI elements such as widgets and ports are declared.
        '''
        # Widgets
        self.addWidget('ExclusivePushButtons', 'Log Level',
                       buttons=['debug', 'info', 'node', 'warn', 'error', 'critical'],
                       val=0)

    def compute(self):
        '''This is where the main algorithm should be implemented.
        '''

        self.starttime()  # time your code, NODE level log

        # produce different log level messages, some of these can be paired
        # with the appropriate return code.
        log = self.getVal('Log Level')
        if log == 0:
            self.log.debug('Very low level minutia.')
        if log == 1:
            self.log.info('Tell the user things are working correctly.')
        if log == 2:
            self.log.node('Tell the user node stuff is working correctly.')
        if log == 3:
            self.log.warn('A problem that wont crash GPI or the node.')
        if log == 4:
            self.log.error('A problem that would crash GPI or the node.')
        if log == 5:
            self.log.critical('A crash is imminent.')

        self.endtime('validate()')  # endtime w/ message
        self.endtime()  # endtime w/o message

        return 0  # success
