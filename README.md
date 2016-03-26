## Python to C++ Translator
Our goal is to be able to automatically translate a subset of Python code to C++.
We will focus on lists, dicts, classes, paramater passing, and file reading.
Throughout this project we may alter our constraits.

## Authors
Rajan Khullar


## Project Layout
There should be three branches so far.
Examples is for our manual conversion from python to c++.
The analyzer and builder are two sepeate phases of our program.
Both directories should be packages that contain python modules.

## Analyzer
Should be able to read a single python module and extract the internal logic.
This includes the classes, the functions, variables, statements, etc.
The logic should be represented with a common string fromat such as json, xml, or yml.
We will be using xml for this project.

## Builder
This library will be responsible for creating the C++ project from the xml logic string.
We should create our own generic lists and dictionary class in C++ to serve as a template if required by the logic.
The builder will create one .cc and .h file for each class found in the logic string.
The main program should be a single .cc file. Any subprograms that are not part of a class should be generated in one seperate .cc and .h file.

## Examples
Moving forward we still have a lot of work to do for examples.
So far there is one box example that shows how object oriented programming is done in python and c++.
