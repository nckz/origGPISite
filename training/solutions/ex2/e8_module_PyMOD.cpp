/* E8_MODULE_PYMOD.CPP
 *
 * author Nick Zwart
 * date 2013oct18
 *
 *  A template for the PyFI::Recon2.0 interface.
 */

#include "core/PyFI/PyFI.h" /* PyFI interface, must be the first include */
using namespace PyFI; /* for PyFI::Array */

extern "C"
{
    /* pull in threading interface */
    #include "core/multiproc/threads.c"
}

/* This function represents the operations performed in a single thread.
 * This function could be directly ported to the R2 framework without modification.
 */
void doSomething(int *num_threads, int *cur_thread, Array<float> *arr)
{
    /* threading indices:
     *  In this case, treat the array as 1D (regardless of the dimensionality).
     *  Figure out how many elements to loop over for each thread.  Use 
     *  unsigned long 
     */
    unsigned long numChunks = arr->size() / *num_threads;
    unsigned long start =(*cur_thread    * numChunks);
    unsigned long end   =((*cur_thread+1) * numChunks);

    /* Perform the threaded operation only on the data
     * designated for THIS thread (i.e. cur_thread).
     */
    for (unsigned long i=start; i<end; i++)
    {
        /* Access the R2 array as a 1D array by 
         * only using one arg in parenthesis.
         */
        (*arr)(i) += 1.0;
        cout << "thread: " << *cur_thread << ", val[" << i << "] = " << (*arr)(i) << endl;
    }
}

PYFI_FUNC(myFunc) /* function name available to Python */
{ 
    PYFI_START(); /* This must be the first line */

    PYFI_POSARG(Array<float>, arr);

    /* make the output array the same size as the input */
    PYFI_SETOUTPUT_ALLOC(Array<float>, out, arr->dimensions_vector());

    /* copy elements to output array */
    out = arr;

    /* set the number threads to be spawned */
    int num_threads = 4;

    /* spawn threaded method, print out before 
     * and after to check the result.  Note: the create_threads<n>()
     * interface requires all input variables to be pointers.
     */
    coutv(*out);
    create_threads1(num_threads, doSomething, out);
    coutv(*out);

    /* run the R2 portable function as a single thread (no POSIX libs needed) */
    coutv(*out);
    num_threads = 1;
    int cur_thread = 0;
    doSomething(&num_threads, &cur_thread, out);
    coutv(*out);

    
    PYFI_END(); /* This must be the last line */
} /* end myFunc() */


/* ##############################################################
 *                  MODULE DESCRIPTION
 * ############################################################## */


/* list of functions to be accessible from python
 */
PYFI_LIST_START_
    PYFI_DESC(myFunc, "Array<float> = myFunc(Array<float>).")
PYFI_LIST_END_
