'''
/* THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING CODE
WRITTEN BY OTHER STUDENTS.
Dillon Wu */
'''

import numpy as np
import numpy.testing as npt
import time


def gen_random_samples():
    """
    Generate 5 million random samples using the
    numpy random.randn module.

    Returns
    ----------
    sample : 1d array of size 5 million
        An array of 5 million random samples
    """
    result = np.random.randn(5000000)
    return result


def sum_squares_for(samples):
    """
    Compute the sum of squares using a forloop

    Parameters
    ----------
    samples : 1d-array with shape n
        An array of numbers.

    Returns
    -------
    ss : float
        The sum of squares of the samples
    timeElapse: float
        The time it took to calculate the sum of squares (in seconds)
    """
    timeElapse = 0
    ss = 0
    ## TODO FILL IN
    #total = 0
    startTime = time.time()
    #Sum of Squares
    for i in range (0, len(samples)):
        ss = samples[i] * samples [i] + ss
    #print(ss)

    '''
    Sum of Square Differences
    for i in range (0, len(samples)):
        total = total + samples[i]
    mean = total / len(samples)
    for i in range (0, len(samples)):
        ss = ss + ( samples[i] - mean ) * (samples[i] - mean )
    '''
    timeElapse = time.time() - startTime

    return ss, timeElapse


def sum_squares_np(samples):
    """
    Compute the sum of squares using Numpy's dot module

    Parameters
    ----------
    samples : 1d-array with shape n
        An array of numbers.

    Returns
    -------
    ss : float
        The sum of squares of the samples
    timeElapse: float
        The time it took to calculate the sum of squares (in seconds)
    """
    timeElapse = 0
    ss = 0
    startTime = time.time()
    ## TODO FILL IN
    total = np.square(samples)
    #print(total)
    for i in total:
        ss = ss + i
    timeElapse = time.time() - startTime
    return ss, timeElapse


def main():
    # generate the random samples
    samples = gen_random_samples()
    # call the sum of squares
    ssFor, timeFor = sum_squares_for(samples)
    # call the numpy version
    ssNp, timeNp = sum_squares_np(samples)
    # make sure they're the same value
    npt.assert_almost_equal(ssFor, ssNp, decimal=5)
    # print out the values
    print("Time [sec] (for loop):", timeFor)
    print("Time [sec] (np loop):", timeNp)


if __name__ == "__main__":
    main()
