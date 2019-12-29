/* E7_ALGORITHM_KERNEL.CPP
 *
 * author Nick Zwart
 * date 2013oct18
 *
 * A pure R2 algorithm file for porting between GPI and R2.  Assuming the R2
 * libs are included by the PyMOD wrapper.
 */

/* example algorithm */
Array<float> alg1(Array<int64_t> &in, float val)
{
    /* allocate a new array based on input dimensions array */
    Array<float> arr(DA(in));

    /* do something */
    arr = val;

    /* pass it back */
    return arr;
}
