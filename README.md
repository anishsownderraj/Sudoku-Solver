# Sudoku Solver
This is a sudoku solver using the Backtracking algorithm.

## Getting Started
## Requirements
* `python` 3.x
* `pip`
* [`virtualenv`](https://virtualenv.pypa.io/en/latest/)
## Instructions
1. Clone the Repository using the URL
```sh
$ git clone https://github.com/anishsownderraj/Sudoku-Solver
```
2. Set up an virtual environment(found below)

3. Install the requirements.txt file(found below)




## Create a new virtual environment
The following command creates a new virtual environment named `venv` in the current directory, usually this will be your project's directory.
```sh
$ virtualenv venv
```

## Activate virtual environment
The following commands [activate](https://virtualenv.pypa.io/en/latest/userguide/#activate-script) an existing virtual environment on Windows and Unix systems. The command assume that the virtual environment is named `venv` and that its location is in a subdirectory `path/to/` of the current directory. 
```sh
# Windows (CMD.exe)
$ path\to\venv\Scripts\activate.bat
# Unix
$ source path/to/venv//bin/activate
```
Once the virtual environment has been actiated your console cursor might prepend the name of the virtual environment as shown below.
```sh
$ (venv) echo 'Hello World!'
```

## Deactivate virtual environment
The following command deactivates the current virtual environment, any dependency installed after this command will be installed globally.
```sh
$ (venv) deactivate
```

## Requirements.txt
To install dependencies in the current environment from a `requirements.txt` file the command below can be used.
```sh
$ (venv) pip install -r requirements.txt
```

## Tests

### Sample Input
```sh
board = [[0, 0, 0, 0, 4, 7, 0, 1, 6],
         [5, 0, 1, 0, 0, 0, 7, 0, 0],
         [0, 6, 3, 0, 2, 0, 8, 0, 0],
         [0, 0, 0, 6, 3, 1, 0, 2, 7],
         [0, 0, 7, 9, 0, 2, 4, 0, 0],
         [3, 9, 0, 4, 7, 5, 0, 0, 0],
         [0, 0, 5, 0, 9, 0, 2, 6, 0],
         [0, 0, 6, 0, 0, 0, 5, 0, 8],
         [2, 8, 0, 3, 5, 0, 0, 0, 0]]
```
### Sample Output
```sh
8 2 9 | 5 4 7 | 3 1 6
5 4 1 | 8 6 3 | 7 9 2
7 6 3 | 1 2 9 | 8 4 5
---------------------
4 5 8 | 6 3 1 | 9 2 7
6 1 7 | 9 8 2 | 4 5 3
3 9 2 | 4 7 5 | 6 8 1
---------------------
1 3 5 | 7 9 8 | 2 6 4
9 7 6 | 2 1 4 | 5 3 8
2 8 4 | 3 5 6 | 1 7 9
```

## Compiling and Executing Program
```sh
$ (venv) python3 Sudoku.py
```







