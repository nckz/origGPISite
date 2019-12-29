/* E2_MODULE_PYMOD.CPP
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

    /***** POSITIONAL ARGS */
    PYFI_POSARG(double, myArg); /* makes myArg a double ptr */
    PYFI_POSARG(long, myArg2); /* makes myArg a double ptr */

    /***** PERFORM */
    double out = (*myArg) * (*myArg); /* example algorithm */
    long out2 = (*myArg2) * (*myArg2) + 2;

    /* convenience functions */
    deb; /* just print out the line number for debugging */
    coutv(*myArg); /* stringify the name, value, and line number of the variable */
    coutv(*myArg2);

    /***** OUTPUT */
    PYFI_SETOUTPUT(&out); /* requires a pointer */
    PYFI_SETOUTPUT(&out2); /* requires a pointer */

    PYFI_END(); /* This must be the last line */
} /* end myFunc() */


/* ##############################################################
 *                  MODULE DESCRIPTION
 * ############################################################## */


/* list of functions to be accessible from python
 */
PYFI_LIST_START_
    PYFI_DESC(myFunc, "double = myFunc(double).")
PYFI_LIST_END_
