# Calculator

Calculator with basic functions: add, subtract, multiply, divide and take (n) root from number. Also has a memory of last result which can be reset to zero if necessary. 

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Code Examples](#code-examples)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
Calculator was written for learning purposes.  
If two numbers are given, calculator make an action in between of them. If one - takes a second number from it's memory.   
All inputs and outputs are float type. 

## Technologies
* Python - version 3.8

## Setup
- to your notebook:
```python
!pip install git+https://github.com/JusteGA1/calculator

from calculator.calculator import Calculator
```

## Code Examples
```python
calculator = Calculator()
calculator.add(5, 7)
calculator.subtract(3)
calculator.reset_memory()
```

## Features: _functions_
* Addition / Subtraction: _add / subtract_
* Multiplication / Division: _multiply / divide_
* Take (n) root of number: _take_root_
* Memory of last result: _reset_memory_

## Status
Project is: _finished_

## Inspiration
Learning @Turing College

## Contact
Created by [Juste Gaviene](mailto:juste.gaviene@gmail.com?subject=[GitHub]%20Source%20Han%20Sans)
