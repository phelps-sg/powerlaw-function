import numpy as np
from typing import List, Tuple, Callable
from scipy.stats import ks_2samp
from util.goodness_of_fit import loglikelihoods
from util.non_linear_fit import least_squares_fit, mle_fit


def find_xmin(y_values: List[float], x_values: List[float], function: Callable) -> int:
    """
    Find the value of x_min that minimizes the KS statistic.

    Parameters:
    y_values (List[float]): The dependent variable values.
    x_values (List[float]): The independent variable values.
    function (Callable): The function to fit.

    Returns:
    int: The value of x_min that minimizes the KS statistic.

    """
    results_dict = {}

    # Don't look at last xmin, as that's also the xmax, and we want to have at least few points to fit!
    for x_min_indx in range(len(x_values) - 3):
        data = y_values[x_min_indx:]

        # Skip when data becomes empty
        if len(data) == 0:
            continue

        # Adjust lags to match the size of data
        x_adjusted = x_values[x_min_indx:]
        residuals, params, model_predictions = mle_fit(x_adjusted, data, function)

        # Compute the KS statistic and p-value
        result = ks_2samp(data, model_predictions, alternative='two-sided')
        D = result.statistic

        results_dict[x_min_indx+1] = D

    min_x_min = min(results_dict, key=results_dict.get)
    return min_x_min


# An implementation of find_xmin using BIC as described in https://arxiv.org/abs/0706.1062. Depricated due to issues
# when run on negatively corrrelated datasets.
# def find_xmin(y_values: List[float], x_values: List[float], function: Callable) -> int:
#     """
#     Estimate the onset (x_min) of the power-law behavior in the data by maximizing a modified Bayesian Information Criterion (BIC).
#     See https://arxiv.org/abs/0706.1062, specifically section 3.3. Estimating the lower bound on power-law behavior.
#     Overview:
#     - **Generalized Model:**
#       * Above x_min: Modeled by a standard discrete power-law distribution.
#       * Below x_min: The (x_min - 1) discrete values are represented by distinct probabilities.
#
#     - **Parameter Count Issue:**
#       Directly correlates x_min with the number of model parameters. Increasing x_min can elevate likelihood, challenging the conventional maximum likelihood approach.
#
#     - **Marginal Likelihood:**
#       An approximation to the likelihood of data based on varying model parameter counts.
#
#     - **BIC Formulation:**
#       The modified BIC is expressed as: lnPr(x|x_min) ≈ L - (x_min / 2) * ln(n). The goal here is to maximize this BIC to ascertain x_min.
#
#     This approach deviates from traditional BIC formulations, aiming to best suit the power-law distributions' unique nature and the generalized model.
#
#     Parameters:
#     - y_values (List[float]): The y-values (observational data) of the dataset.
#     - x_values (List[float]): The x-values (observational data) of the dataset.
#     - function (Callable): The function used for fitting. This is typically a power-law function.
#
#     Returns:
#     - int: The x_min index which best fits the power-law behavior for the given data.
#     """
#
#     results_dict = {}
#
#     # Iterating over the x_values, considering each x as a potential x_min
#     for x_min_indx in range(len(x_values) - 3):
#         data = y_values[x_min_indx:]
#
#         # Skip if the adjusted data becomes empty
#         if len(data) == 0:
#             continue
#
#         # Adjust x-values to match the size of the current data
#         x_adjusted = x_values[x_min_indx:]
#
#         # Perform nonlinear least squares fit using the provided function (e.g., power law)
#         residuals, params, _ = least_squares_fit(x_adjusted, data, function)
#
#         # Compute the Sum of Squared Errors
#         #sse = np.sum(residuals ** 2)
#
#         # Compute the log-likelihood from residuals
#         log_likelihoods = loglikelihoods(residuals)
#         log_likelihood = np.sum(log_likelihoods)
#
#         # If SSE is non-positive or data length is 0, we skip the current x_min value
#         # if sse <= 0 or len(data) <= 0:
#         #     continue
#
#         # Compute custom Bayesian Information Criterion (BIC)
#         n = len(data)
#         bic = log_likelihood - x_min_indx / 2 * np.log(n)
#
#         results_dict[x_min_indx] = bic
#
#     # Return x_min value with the maximum BIC
#     max_x_min = max(results_dict, key=results_dict.get)
#     return max_x_min
