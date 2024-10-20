
import numpy as np
import cProfile
import pstats
 
def simulate_physical_system(n):
   A = np.random.rand(n, n)
   B = np.random.rand(n, n)
   C = np.random.rand(n, n)
 
   # Perform matrix multiplication
   D = np.dot(A, B)
 
   # Element-wise operations
   E = D * C
 
   # Solve a linear system
   x = np.linalg.solve(E, np.ones(n))
 
   return x
 
def main():
   # Test the function with a large input size
   result = simulate_physical_system(1000)

   profiler = cProfile.Profile()
   profiler.enable()

   simulate_physical_system(10000)

   profiler.disable()

   with open('../results/profile_output_regular.txt', 'w') as f:
      ps = pstats.Stats(profiler, stream=f)
      ps.strip_dirs().sort_stats('cumtime').print_stats()
      
if __name__ == "__main__":
    main()