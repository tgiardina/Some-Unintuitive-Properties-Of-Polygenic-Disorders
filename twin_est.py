import numpy as np
from scipy.stats import norm
from argparse import ArgumentParser

if __name__ == "__main__":
    # Create the parser
    parser = ArgumentParser()
    parser.add_argument('--heritability', type=float, required=False, default=0.79)  # Scz heritability.
    parser.add_argument('--pop-avg', type=float, required=False, default=0.009)  # Scz prevalence.
    parser.add_argument('--percent-environment-shared', type=float, required=False, default=0)
    parser.add_argument('--N', type=int, required=False, default=1000000)
    args = parser.parse_args()
    heritability = args.heritability
    pop_avg = args.pop_avg
    percent_environment_shared = args.percent_environment_shared
    N = args.N

    # Create the covariance mxs.
    genetic_covariance_mx = heritability * np.array([[1, 1], [1, 1]])  # Identical twins share ~100% of their genome.
    environmental_covariance_mx = (1 - heritability) * np.array([  # Identical twins share some percent of their env.
        [1, percent_environment_shared],
        [percent_environment_shared, 1],
    ])

    # Simulate the twins.
    means = np.array([0, 0])
    genetic_liability_mx = np.random.multivariate_normal(
        means,
        genetic_covariance_mx,
        N,
    )
    environmental_liability_mx = np.random.multivariate_normal(
        means,
        environmental_covariance_mx,
        N,
    )
    total_liability_mx = genetic_liability_mx + environmental_liability_mx

    # Calculate the phenotypes.
    threshold = norm.ppf(1 - pop_avg)
    phenotype_mx = total_liability_mx > threshold

    # Calculate percentages.
    percent_twins_of_affected_affected = \
        100 * np.sum(phenotype_mx[:, 1] & phenotype_mx[:, 0]) / np.sum(phenotype_mx[:, 0])

    # Print results.
    print(f"Percent of twins of affected individuals affected: {percent_twins_of_affected_affected}")
