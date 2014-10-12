# INTRODUCTION:
Parte is a testing tool for testing of programs written for various competitive programming sites like spoj, codechef etc.

# IDEA/ABILITY:
Parte provides an iterface to generate random/custom inputs, run it on your code-to-be-tested and a brute-force/known-to-be-correct-solution and compare their outputs.
You can do rigorous testing of your program and if it fails at for some input, parte can report the correct output, the faulty output and the input.

# LIMITATIONS:
Currently available only for c++ programs. Will be extending for all languages in future.


# USAGE:
1. Put your to-be-tested file in code folder. Let it be "`X.cpp`".
2. Name your brute-force/known-to-be-correct solution in code folder and name it "`X_test.cpp`".
3. Write your input generator code in the `process()` function of `input/PartIn.py`.
4. Start the testing by running the `Parte.py` file in main folder. Look at the various options you need to provide by running:`python Parte.py -h`
5. To test `X.cpp` for 1 input, run: `python Parte.py -i X.cpp -r`
6. To test it for multiple inputs, run: `python Parte.py -i X.cpp -m 100`
7. You can choose more options as pointed out by: `python Parte.py -h`
