import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
import numpy as np

def path(dist_list,length):
    # Initialize fitness function object using dist_list
    fitness_dists = mlrose.TravellingSales(distances = dist_list)
    problem_fit = mlrose.TSPOpt(length = length, fitness_fn = fitness_dists, maximize=False)

    # Solve problem using the genetic algorithm
    Best_state, Best_fitness = mlrose.genetic_alg(problem_fit, random_state = 2)

    return Best_state, Best_fitness
