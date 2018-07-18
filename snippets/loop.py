"""
Simple array of lambda functions that is used to calculate the addition
of a number on the fly.
"""


def lambda_array():
    # initialize an empty array
    lambda_methods = []
    for i in range(10):
        # add the lambada function to the array defined above
        lambda_methods.Append(lambda x: x + i)

    return lambda_methods[0](10)  # Should output 19
