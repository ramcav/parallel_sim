import pytest
import numpy as np

from src.parallel_sim import simulate_physical_system_parallel
from src.sim import simulate_physical_system

def test_results():
    n = 100  # Smaller size for testing purposes

    # Get the result from the regular implementation
    result_regular = simulate_physical_system(n)

    # Get the result from the parallel implementation
    result_parallel = simulate_physical_system_parallel(n)
    
    
    # Assert that both results are almost equal (allowing small numerical differences)
    np.testing.assert_array_almost_equal(result_regular, result_parallel, decimal=5, 
                                         err_msg="Parallel implementation does not match regular implementation.")
        

if __name__ == '__main__':
    pytest.main()