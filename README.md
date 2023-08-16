# powerlaw-function: A Python Package for Analysing Heavy-Tailed Functions

`powerlaw-function` is a flexible Package that extends the statistical methods developed by [Clauset et al. 2007](https://arxiv.org/abs/0706.1062) and [Virkar and Clauset. 2012](https://arxiv.org/abs/1208.3524) for distribution fitting; i.e., fitting and determining whether the probability distribution of a single variable follows a power law.</b>
The `powerlaw` package is available at [powerlaw](https://github.com/jeffalstott/powerlaw/tree/master).

Here, we are instead interested in modelling a response variable as a function of a predictor variable by finding the best functional approximation. In this context, we are fitting power law functions to data generated by known functions, which is closer to the realm of approximation theory and deterministic modelling as opposed to probabilistic (or stochastic) modelling approaches. 


# Installation 

We recommend Conda for managing Python packages; pip for everything else. To get started, simply install `pip` and run:

  `pip install powerlaw-function`

# Basic Usage 

This tells you everything you need to know for the simplest, typical use cases:

    import powerlaw-function

    # Prepare data
    xy_df = pd.DataFrame({
        'x_values': x,
        'y_values': acf_series
    })

    # Basic Usage
    fit = Fit(xy_df, verbose= True)
    fit.pure_powerlaw.print_fitted_results()

    # Direct comparison against alternative models
    R, p = fit.function_compare('pure_powerlaw', 'exponential_function')
    print('Power law vs. exponential_function')
    print(f'Normalized Likelihood Ratio: {R}, p.value: {p}')
    print('\n')


# Advanced Usage 

    # Define custom power-law model: power-law with exponentially slowly varying function
    def powerlaw_with_exp_svf(x, alpha, beta, lambda_):
        return x ** -(alpha) * sf.exponential_function(x, beta, lambda_)

    custom_powerlaw_funcs = {
        'powerlaw_with_exp_svf': powerlaw_with_exp_svf
    }

    # Fit custom function
    fit.fit_powerlaw_function(custom_powerlaw_funcs)
    fit.powerlaw_with_exp_svf.print_fitted_results()

For more details on how to use the Package, including figures and approach, see the Manuscript and Article Bugaenko et al. 2023 respectively, which illustrate all of the `powerlaw-function` features and provide the mathematical background underlying these methods.

# Power Laws vs. Alternative Models

TODO: Describe process

    # Direct comparison against alternative models
    print('powerlaw_with_exp_svf vs. exponential_function:')
    R, p = fit.function_compare('powerlaw_with_exp_svf', 'exponential_function', nested = True)
    print(f'Normalized Likelihood Ratio: {R}, p.value: {p}')
    
    # Plot
    fit.plot_data(scale='linear')
    fit.exponential_function.plot_fit()
    fit.pure_powerlaw.plot_fit()
    fit.powerlaw_with_exp_svf.plot_fit()

# Further Development

`powerlaw-function is open for further development by the community.  Feel free to raise an issue if you find a problem. If there are additional features you'd like to see developed, please [raise an issue](https://github.com/anabugaenko/powerlaw-function/issues) and/or pull request; this repository is actively being developed and any tickets will be addressed in order of importance. 

# Acknowledgement 

We would like to extend a thank you to Jeff Alstott, Ed Bullmore, Dietmar Plenz for open sourcing the 'powerlaw' Package, their implementations provided a crucial starting point for making `powerlaw-function`. We would also like to Andreas Klaus, Aaron Clauset, Cosma Shalizi, and Adam Ginsburg for their original paper [POWER-LAW DISTRIBUTIONS IN EMPIRICAL DATA](https://arxiv.org/abs/0706.1062)  which serves as a theoretical basis for our approach.

# How to Cite

  Academics, please cite as:
  
    @article{abuga2023power,
      title={Power-laws in deterministic functions,
      author={Ana Bugaenko and Christian Wayi-Wayi},
      journal={In preparation},
      year={2023}
    }


