# Command-Line Arguments

## **About**

- Collection of basic Python programs demonstrating command-line argument handling
- Uses the `sys` module for terminal input processing
- Foundation for building automation scripts with CLI capabilities

## **Purpose**

- Learn and practice command-line argument handling with `sys.argv`
- Understand how to accept user input through the terminal
- Build interactive automation scripts and CLI utilities

## **Programs Included**

**1. CommandLine1.py**

- Takes two numbers as standard input
- Performs addition operation
- Prints the sum result

**2. CommandLine2.py**

- Demonstrates `sys.argv` basics
- Displays script name using `sys.argv[0]`
- Shows total argument count using `len(sys.argv)`

**3. CommandLine3.py**

- Iterates through all command-line arguments
- Displays each argument individually
- Uses a loop to process the `sys.argv` list

**4. CommandLine4.py**

- Accepts two numbers as command-line arguments
- Converts arguments to integers
- Performs addition and displays the result

## **How to Run**

**CommandLine1.py**

```bash
python CommandLine1.py
```

**CommandLine2.py**

```bash
python CommandLine2.py
```

**CommandLine3.py**

```bash
python CommandLine3.py arg1 arg2 arg3
```

**CommandLine4.py**
```bash
python CommandLine4.py 11 10
```

## **Key Concepts**
- sys.argv: List containing command-line arguments
- sys.argv[0]: Script name
- sys.argv[1]: First command-line argument
- len(sys.argv): Total number of command-line arguments
- Type Conversion: Converting string arguments to integers
- Argument Indexing: Accessing arguments using index values
- Argument Iteration: Processing multiple command-line arguments using loops

## **Technologies Used**
- Python 3.x
- sys module
- Basic input/output operations

## **Learning Path**
- Start with CommandLine1.py for basic input and addition
- Progress to CommandLine2.py for sys.argv introduction
- Practice CommandLine3.py for argument iteration
- Complete CommandLine4.py for practical command-line argument processing
