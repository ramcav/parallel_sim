import numpy as np
from memory_profiler import profile
import cProfile
import pstats

from multiprocessing import  Pool

@profile
def generate_matrices(n):
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)
    C = np.random.rand(n, n)
    
    return A, B, C

@profile
def parallel_dot(args):
    A, B = args
    return np.dot(A, B)

@profile
def parallel_lin_solv(args):
    A, n = args
    return np.linalg.solve(A, np.ones(n))
 
@profile
def simulate_physical_system_parallel(n):
    
    A, B, C = generate_matrices(n)
    
    # In this case, it is really not necessary to use locks
    # because Pool already implements underlying mechanisms
    # to avoid deadlocks, according to my research
 
    # Perform matrix multiplication (i fixed the n_processes to 2 for now)
    with Pool(2) as pool:
        D = pool.map(parallel_dot, [(A, B)])
    
    D = D[0]
 
    # Element-wise operations (I changed to use NumPy for better performance)
    # I tried to parallelize this operation but it gave issues because
    # this particular operation is done in place
    E = np.multiply(D,C, out=C)
 
    # Solve a linear system
    with Pool(2) as pool:
        x = pool.map(parallel_lin_solv, [(A, n)])
 
    return x

def main():
    profiler = cProfile.Profile()
    profiler.enable()

    simulate_physical_system_parallel(10000)

    profiler.disable()

    with open('../results/profile_output_parallel.txt', 'w') as f:
        ps = pstats.Stats(profiler, stream=f)
        ps.strip_dirs().sort_stats('cumtime').print_stats()

if __name__ == "__main__":
    main()