/* E6_MODULE_PYMOD.CPP
 *
 * author Nick Zwart
 * date 2013oct18
 *
 *  A template for the PyFI::Recon2.0 interface.
 */

#include "core/PyFI/PyFI.h" /* PyFI interface, must be the first include */
using namespace PyFI; /* for PyFI::Array */

PYFI_FUNC(myFunc) /* function name available to Python */
{ 
    PYFI_START(); /* This must be the first line */

    PYFI_ERROR("The e6 C++ PyMOD failed to execute.");

    PYFI_END(); /* This must be the last line */
} /* end myFunc() */


/* ##############################################################
 *                  MODULE DESCRIPTION
 * ############################################################## */


/* list of functions to be accessible from python
 */
PYFI_LIST_START_
    PYFI_DESC(myFunc, "myFunc().")
PYFI_LIST_END_
