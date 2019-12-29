/* E7_ALGORITHM_KERNEL.CPP
 *
 * author Nick Zwart
 * date 2013oct18
 *
 * A pure R2 algorithm file for porting between GPI and R2.  Assuming the R2
 * libs are included by the PyMOD wrapper.
 */

/* example algorithm */
float alg1(float in)
{
    if (in > 1.)
        return 1.; 
    if (in < 0.)
        return 0.;
    return in;
}
