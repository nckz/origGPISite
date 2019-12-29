/* E5_MODULE_PYMOD.CPP
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
    PYFI_KWARG(long, myKwArg, 1L); /* makes myKwArg a long ptr and defaults to 1 */

    /* An R2 Array keyword-arg example */
    Array<float> arr_def(2L, 2L);  /* generate a 2x2 array */
    arr_def = -1.0;
    PYFI_KWARG(Array<float>, arr, arr_def);

    /***** PERFORM */
    double out = (*myArg) * (*myArg); /* example algorithm */

    /* convenience functions */
    deb; /* just print out the line number for debugging */
    coutv(*myArg); /* stringify the name, value, and line number of the variable */
    coutv(*myKwArg);
    coutv(*arr);

    /***** OUTPUT */
    PYFI_SETOUTPUT(&out); /* requires a pointer */

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
