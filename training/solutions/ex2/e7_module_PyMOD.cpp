/* E7_MODULE_PYMOD.CPP
 *
 * author Nick Zwart
 * date 2013oct18
 *
 *  A template for the PyFI::Recon2.0 interface.
 */

#include "core/PyFI/PyFI.h" /* PyFI interface, must be the first include */
using namespace PyFI; /* for PyFI::Array */

/* pull the pure-algorithm kernel into this wrapper */
#include "solutions/ex2/e7_algorithm_kernel.cpp"

PYFI_FUNC(myFunc) /* function name available to Python */
{ 
    PYFI_START(); /* This must be the first line */

    PYFI_POSARG(double, input);
    PYFI_POSARG(Array<int64_t>, input_dims);

    /* call kernel */
    Array<float> out = alg1(*input_dims, *input);

    PYFI_SETOUTPUT(&out);

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
