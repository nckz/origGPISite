/* E4_MODULE_PYMOD.CPP
 *
 * author Nick Zwart
 * date 2013oct18
 *
 *  A template for the PyFI::Recon2.0 interface.
 */

#include "core/PyFI/PyFI.h" /* PyFI interface, must be the first include */
using namespace PyFI; /* for PyFI::Array */

#include <vector> 

PYFI_FUNC(myFunc) /* function name available to Python */
{ 
    PYFI_START(); /* This must be the first line */

    /***** POSITIONAL ARGS */
    PYFI_POSARG(Array<complex<float> >, arr); /* makes arr an R2 array ptr*/

    /***** Pre-ALLOCATE and SET OUTPUT (preferred method) */
    /* -copies the dimensions using the dimensions_vector() method 
     * -this function tells python to pre-allocate, so no copy is needed at
     *  the end (as with PYFI_SETOUTPUT()).
     */
    PYFI_SETOUTPUT_ALLOC(Array<complex<float> >, out, arr->dimensions_vector());

    /* Pre-ALLOCATE using a vector */
    std::vector<uint64_t> out3_dims;
    out3_dims.push_back(2); /* set dim length to 2 (i.e. 0 to (n-1)) */
    out3_dims.push_back(4);
    out3_dims.push_back(4);
    PYFI_SETOUTPUT_ALLOC(Array<complex<float> >, out3, out3_dims);

    /* Pre-ALLOCATE using an R2 array (preferred method) */
    Array<int64_t> out4_dims(3);
    out4_dims(0) = 2;
    out4_dims(1) = 4;
    out4_dims(2) = 4;
    PYFI_SETOUTPUT_ALLOC(Array<complex<float> >, out4, DA(out4_dims));

    /***** PERFORM */
    /* example algorithm */
    (*out) =  (*arr) * (*arr) + complex<float>(1.0);
    *out3 = complex<float>(6);
    *out4 = complex<float>(7.0 + 1.1i);

    /* convenience functions */
    deb; /* just print out the line number for debugging */
    coutv(*out); /* stringify the name, value, and line number of the variable */
    coutv(*out3);
    coutv(*out4);

    double out2 = 111;
    PYFI_SETOUTPUT(&out2); /* append to output list, requires a pointer */

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
