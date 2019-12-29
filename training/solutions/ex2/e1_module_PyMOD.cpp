/* E1_MODULE_PYMOD.CPP
 *
 * author Nick Zwart
 * date 2013oct18
 *
 *  A template for the PyFI::Recon2.0 interface.
 */

#include "core/PyFI/PyFI.h" /* PyFI interface, must be the first include */
using namespace PyFI; /* for PyFI::Array */

#include <iostream>
using namespace std;

PYFI_FUNC(myFunc) /* function name available to Python */
{
    PYFI_START(); /* This must be the first line */

    /***** PERFORM */
    //string msg = "hello world form inside a cpp pymod";
    // changed message.
    string msg = "goodbye world form inside a cpp pymod";

    /* convenience functions */
    deb; /* just print out the line number for debugging */
    coutv(msg); /* stringify the name, value, and line number of the variable */

    PYFI_END(); /* This must be the last line */
} /* end myFunc() */


/* ##############################################################
 *                  MODULE DESCRIPTION
 * ############################################################## */


/* list of functions to be accessible from python
 */
PYFI_LIST_START_
    PYFI_DESC(myFunc, "None = myFunc().")
PYFI_LIST_END_
