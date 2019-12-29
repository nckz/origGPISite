/* E3_MODULE_PYMOD.CPP
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
    PYFI_POSARG(Array<complex<float> >, arr); /* makes arr an R2 array ptr*/
    PYFI_POSARG(Array<int>, arr2);

    /***** PERFORM */
    Array<complex<float> > out(*arr); /* make a copy of arr */
    Array<int> out2(*arr2);

    /* example algorithm */
    out =  (*arr) * (*arr) + complex<float>(1.0);
    out2 = (*arr2) * (*arr2) + (int) 1;

    /* convenience functions */
    deb; /* just print out the line number for debugging */
    coutv(out); /* stringify the name, value, and line number of the variable */
    coutv(out2);

    /***** OUTPUT */
    PYFI_SETOUTPUT(&out); /* copy mode output, requires a pointer */
    PYFI_SETOUTPUT(&out2);

    PYFI_END(); /* This must be the last line */
} /* end myFunc() */


/* ##############################################################
 *                  MODULE DESCRIPTION
 * ############################################################## */


/* list of functions to be accessible from python
 */
PYFI_LIST_START_
    PYFI_DESC(myFunc, "array-complex<float> = myFunc(array-complex<float>).")
PYFI_LIST_END_
