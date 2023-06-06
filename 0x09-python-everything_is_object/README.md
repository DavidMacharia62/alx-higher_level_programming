# Python - Object Oriented Programming (OOP)

## Python programming is awesome for several reasons:

### Readability: 

Python emphasizes code readability and uses a clean and expressive syntax, making it easier to write and understand code.

### Simplicity: 

Python has a simple and straightforward syntax, which reduces the complexity of the code and makes it easier to learn and use.

### Versatility: 

Python can be used for a wide range of applications, including web development, data analysis, machine learning, scientific computing, and more.

### Large Standard Library: 

Python comes with a vast standard library that provides a wide range of modules and functions, saving developers time and effort by providing pre-built tools for common tasks.

### Third-Party Libraries: 

Python has a rich ecosystem of third-party libraries and frameworks, such as NumPy, Pandas, TensorFlow, Django, and Flask, which extend its capabilities and make it a powerful language for various domains.

### Platform Independence: 

Python is a platform-independent language, meaning that Python code can run on different operating systems without any modifications.

## What is an Object 

An object in programming refers to a particular instance of a class. It can be a data structure, a variable, a function, or any other entity that can be manipulated in a program. Objects have attributes (variables) and behaviors (methods/functions) associated with them.

## What is a Class?

In Python, a class is a blueprint or a template that defines the attributes and behaviors that an object of that class will have. An object, also called an instance, is created from a class. In simple terms, a class is a definition, and an object is an instance of that definition.

## Difference between class and object? 

The difference between a class and an object can be understood as follows: 
* A class is like a blueprint or a template that defines the structure and behavior of objects. It specifies what attributes and methods an object will have. 
* On the other hand, an object is an instance of a class. It is a concrete entity that can be created based on the defined class.

### What is an Immutable Object?

An immutable object is an object whose state cannot be modified after it is created. Immutable objects are fixed and cannot be changed. Examples of immutable objects in Python include integers, floats, strings, and tuples.

### What is a mutable object?

A mutable object, on the other hand, is an object whose state can be modified after it is created. Mutable objects can be changed or updated. Examples of mutable objects in Python include lists, dictionaries, and sets.

### References in Python

In Python, a reference is a way to access or refer to an object in memory. When you assign a value to a variable in Python, you are creating a reference to the object that holds that value. References allow you to work with objects without directly manipulating their memory addresses.

### Assignment in Python

An assignment in Python is a statement that assigns a value to a variable. It associates a name (variable) with a value. For example, x = 5 assigns the value 5 to the variable x.

### Alias in Python

An alias refers to multiple variables that are bound to the same object. In other words, an alias means having multiple names for the same object. When you create an alias, changes made to the object through one name will be reflected when accessed through another name.

#### How to Check if variables are identical: 

To check if two variables are identical in Python, you can use the is operator. For example, x is y will return True if x and y refer to the same object, and False otherwise.

#### How to check if variables are linked to the same object

To check if two variables are linked to the same object, you can also use the id() function. The id() function returns the unique identifier (memory address) of an object. If the id() of two variables is the same, it means they are linked to the same object. For example:

##### Example

x = [1, 2, 3]
y = x
print(id(x) == id(y))  # True

To display the memory address (variable identifier) of an object in the CPython implementation, you can use the id() function as shown in the previous example.

In Python, mutable objects can be modified or changed after they are created, while immutable objects cannot be modified once they are created.

Built-in mutable types in Python include lists, dictionaries, and sets.

Built-in immutable types in Python include integers, floats, strings, tuples, and frozensets.

In Python, variables are passed to functions by object reference. When a variable is passed to a function, the reference to the object it points to is passed, not the actual object itself. Any changes made to the object within the function will be reflected outside the function since they refer to the same object in memory. However, if the function reassigns the variable to a new object, it won't affect the original object outside the function.
