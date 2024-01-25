import numpy as np
from scipy.stats import norm
from argparse import ArgumentParser

if __name__ == "__main__":
    # Create the parser
    parser = ArgumentParser()
    parser.add_argument('--heritability', type=float, required=False, default=0.79)
    parser.add_argument('--pop-avg', type=float, required=False, default=0.01)
    parser.add_argument('--percent-environment-shared', type=float, required=False, default=0)
    parser.add_argument('--N', type=int, required=False, default=1000000)
    args = parser.parse_args()
    heritability = args.heritability
    pop_avg = args.pop_avg
    percent_environment_shared = args.percent_environment_shared
    N = args.N

    # Create the covariance mxs.
    genetic_covariance_mx = heritability * np.array([
        [1, 0.5, 0.5],  # Child shares 50% of genome w/ parents.
        [0.5, 1, 0],  # Parent shares 50% of genome w/ their child (and we hope are not related to their spouse).
        [0.5, 0, 1]
    ])
    environmental_covariance_mx = (1 - heritability) * np.array([  # Identical twins share some percent of their env.
        [1, percent_environment_shared, percent_environment_shared],
        [percent_environment_shared, 1, 0],
        [percent_environment_shared, 0, 1],
    ])

    # Simulate the twins.
    means = np.array([0, 0 ,0])
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
    percent_affected_children_from_unaffected_parents = \
        100 * np.sum(phenotype_mx[:, 0] & ~phenotype_mx[:, 1] & ~phenotype_mx[:, 2]) \
        / np.sum(~phenotype_mx[:, 1] & ~phenotype_mx[:, 2])

    # Print results.
    print(f"Percent of affected children from unaffected parents: {round(percent_affected_children_from_unaffected_parents,2)}%")
