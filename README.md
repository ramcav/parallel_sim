# PARALLEL SIMULATIONS README (REPORT)

This project is a simple example of how to run code in parallel using python. It carries out some simple linear algebra operations on parallel, and runs profiling to compare the performance of the parallel code with the serial code.

## Running the code

To run the code, you need to have python installed in your machine. You can install it from [here](https://www.python.org/downloads/).

After installing python, you can run the code by executing the following command in the terminal from the root directory of the project:

```bash
    cd src
    python parallel_sim.py
```

This code will run the parallel version of the program and store the profiling results in the `results` directory.

If you want to run the serial version of the code, you can execute the following command:

```bash
    cd src
    python serial_sim.py
```

Again, the profiling results will be stored in the `results` directory.

## Techniques Implemented

The linear algebra optimizations were carried out using NumPy, as using a library like BLAS wasn't really necessary as NumPy already uses BLAS under the hood. The parallelization was done using the `multiprocessing` library in python, which allows for easy parallelization of code using the `Pool` class. The dot product and the linear system solver were parallelized using this library, however, the matrix multiplication was not parallelized as it gave issues regarding altering the matrix in place.

For profiling, the `cProfile` library was used to profile the code and store the results in a file. Furthermore, memory profiling was also carried out using the `memory_profiler` library.

## Results

The results can be found in the `results` directory. Despite the parallel code being supposed to be faster, the serial code was actually faster in this case. This is likely due to the overhead of creating the processes and the fact that the operations carried out were not very computationally intensive. However, the parallel code was able to utilize more CPU cores, which is a good sign that it is working as intended. Furthermore, the justification for using parallel code will probably be more evident in more computationally intensive tasks, or if the size of the matrices is increased drastically.

## Conclusion

In conclusion, parallel code can be useful in certain situations, however, it is not always the best solution. It is important to profile the code and see if the parallel code is actually faster than the serial code. Furthermore, the size of the matrices and the computational intensity of the operations should be taken into account when deciding whether to parallelize the code or not.