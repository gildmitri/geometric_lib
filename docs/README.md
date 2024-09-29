
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Square: `S = a²`
- Triangle: `S = (a + b + c) / 2`

## Perimeter
- Circle: `P = 2πR`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# General description
This project is a simple calculator for calculating the area and perimeter of geometric shapes such as circles and squares.

The user enters the name of the shape, selects what needs to be calculated (area or perimeter), and enters the necessary dimensions, for example, radius for a circle or side for a square. 

The program uses ready-made mathematical formulas for calculations and outputs the result directly on the command line. 

The main goal of the project is to simplify calculations for the user by providing a simple and intuitive interface.

# Functions, description and examples
## `calculate.py`
### `def calc(fig, func, size):`
- Calculates the value of the specified function for the specified shape based on its dimensions.
- Example of a call:
```python
>> calc('circle', 'area', [5])
78.53981633974483
```
## `circle.py`
### `def area(r):`
- Calculates the area of a circle by a given radius.
- Example of a call:
```python
>> area(5)
78.53981633974483
```
### `def perimeter(r):`
- Calculates the length of a circle (the perimeter of a circle) by a given radius.
- Example of a call:
```python
>> perimeter(5)
31.41592653589793
```
## `square.py`
### `def area(a):`
- Calculates the area of a square along a given side length.
- Example of a call:
```python
>> area(5)
25
```
### `def perimeter(a):`
- Calculates the perimeter of a square along a given side length.
- Example of a call:
```python
>> perimeter(5)
20
```
## `triangle.py`
### `def area(a):`
- Calculates the half-meter (not the area) of a triangle by the specified side lengths.
- Example of a call:
```python
>> area(3, 4, 5)
6.0
```
### `def perimeter(a):`
- Calculates the perimeter of a triangle based on the specified side lengths.
- Example of a call:
```python
>> perimeter(3, 4, 5)
12.0
```

# The history of changing the project with the hashes of the commits
1. **d76db2a** - L-04: Add calculate.py  
   Added the `calculate.py` file for performing calculations.

2. **51c40eb** - L-04: Doc updated for triangle  
   Updated documentation for working with triangles.

3. **d080c78** - L-04: Triangle added  
   Added functionality for working with triangles.

4. **d078c8d** - L-03: Docs added  
   Added documentation for previous functions.

5. **8ba9aeb** - L-03: Circle and square added  
   Added functions for working with circles and squares.
