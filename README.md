# S-expression Calculator
A simple command line program that takes in a single expression as a string, calculates it, and prints the result:

```
$ ./calc.py "(add 2 2)"
4

$ ./calc.py "1234"
1234
```
</br></br>
## Expression Structure
---
The program accepts expressions in two forms:
### Integers
An integer consists of a sequence of digits:
```
4567
```

### Function Calls
A function call requires a FUNCTION, and two or more EXPR (expressions):
```
(FUNCTION EXPR EXPR)
```
- FUNCTION: may consist of either `add` or `multiply`, and must be enclosed in parentheses `(` `)`
- EXPR: may consist of an **integer**, `4567` or a **function call**, `(add 1 1)` 
- each FUNCTION and EXPR must be separated by a single space

### Add
Examples of `add`:
```
(add 2 2)
4

(add 2 (add 1 1) 3)
7
```

### Multiply
Examples of `multiply`:
```
(multiply 2 2)
4
(multiply 2 (multiply 3 2))
12
```

### Combination of functions
Functions may also be combined within an expression:
```
(add 1 (multiply 2 2) 4)
9  
```
</br></br>
## Extensibility
---
This program will accept any number of `add` or `multiply` function calls:
```
(add 1 (add 2 (multiply 3 (multiply 2 2) add(2 2) 5)
243
```

### Additional Functions
Additional functions may be easily implemented within the code to extend the program's capabilities.
Below is an example of an implementation of a `subtract` function:

1. Create the `subtract` function:
```python
def subtract(INTEGERS):
    result = 0
    for INTEGER in INTEGERS:
        result -= int(INTEGER)
    return result
```

2. Call the `subtract` function within the `calculate_sub_expression()` function as an `elif` statement:
```python
def calculate_sub_expression(sub_expression):
    ...
        if FUNCTION == "add":
            return add(INTEGERS)
        elif FUNCTION == "multiply":
            return multiply(INTEGERS)
        elif FUNCTION == "subtract":    <- 'subtract' 
            return subtract(INTEGERS)
        elif FUNCTION.isnumeric():
            return int(FUNCTION)
```

</br></br>
## Executing the Program
---
The program must be run in the following way:
```
$ ./calc.py "(add 1 1)"
```
- ensure the expression to calculate is enclosed in quotations `"` `"` 

### Help
Should you encounter the following error upon running the program:
```
bash: ./calc.py: Permission denied
```
execute the following code to give the file [executable permissions](https://linuxpip.org/chmod-x-explained-everything-you-need-to-know/):
```
$ chmod +x calc.py
```
</br></br>
## Dependencies
---
This program was created using python 3.9.2 on macOS

</br></br>
## Author
---
I'm Frank Piro, a Software Developer in Barrie, ON, Canada. Thank you for taking the time to learn about my software. I enjoyed creating this program, and am always open to any feedback or suggestions, so please [reach out](mailto:frank.piro@gmail.com)!

