# PYTHON - TEST DRIVEN DEVELOPMENT

## Python programming is awesome for several reasons:

### Simplicity: 

Python has a clear and readable syntax, making it easy to learn and understand. It emphasizes simplicity and readability, which results in more efficient development and collaboration.

### Versatility: 

Python is a versatile language that can be used for a wide range of applications, including web development, data analysis, machine learning, artificial intelligence, and automation. It has a vast ecosystem of libraries and frameworks that support various domains.

### Large community and resources: 

Python has a thriving community of developers who contribute to its growth. This leads to an abundance of resources, such as libraries, frameworks, documentation, and online communities, which makes it easier to find help and support.

### Extensive libraries: 

Python offers a rich collection of libraries for almost any task you can imagine. Whether you need to manipulate data, build web applications, or perform complex mathematical calculations, chances are there's a Python library available to help you.

### Readability: 

Python's emphasis on readability makes it easier to write and maintain code. Its indentation-based syntax enforces consistent code formatting, which enhances code readability and reduces errors.

### Iterative Tests

An interactive test is a type of test where you can interact with the code or application being tested in real-time. It allows you to provide input and observe the output, helping you validate the behavior of the code during development. Interactive tests are commonly used for debugging or exploring code functionality.

### Why bother with tests in Python?

Tests are important in software development for the following reasons:

### Verification: 

Tests help verify that your code behaves as expected. By writing tests, you can ensure that your functions, classes, or modules produce the correct output for a given input or scenario.

### Validation: 

Tests validate that your code meets the desired requirements or specifications. They act as a safety net, catching potential bugs and issues before they reach production environments.

### Refactoring: 

Tests provide confidence when refactoring or modifying existing code. With a comprehensive test suite, you can make changes to your codebase and run the tests to ensure that everything still works correctly.

### Collaboration: 

Tests facilitate collaboration among developers. They serve as documentation for the expected behavior of the code, making it easier for team members to understand and contribute to the project.

### How To Write DOcstrings

#### To write Docstrings to create tests, you can follow these steps:

- Define the function or method you want to test.
- Add a Docstring to the function, describing its purpose and expected behavior.
- Within the Docstring, specify the inputs and expected outputs for different test cases.
- Use a testing framework like unittest or pytest to write actual test cases based on the information provided in the Docstring.
- Run the tests and ensure they pass.

### Documentation Best Practices 

#### When writing documentation for each module and function, you can follow these best practices:

- Use descriptive and meaningful names for modules, functions, and variables.
- Include a brief summary of the module's or function's purpose.
- Explain the expected inputs and outputs, including their data types and formats.
- Provide examples or code snippets to demonstrate how to use the module or function.
- Document any important considerations, limitations, or potential issues users should be aware of.
- Use consistent formatting and style to improve readability.

#### Basic option flags to create tests depend on the testing framework you're using. Here are a few commonly used flags:

- -v or --verbose: Provides detailed output during test execution, showing individual test results.
- -q or --quiet: Suppresses most of the output during test execution, showing only summary information.
- -x or --exitfirst: Stops test execution on the first failure or error encountered.
- -k EXPRESSION or --keyword=EXPRESSION: Runs only tests that match the given expression or keyword.
- -m MARKEXPR or --mark=MARKEXPR: Runs only tests with specific markers or attributes.

## To find edge cases, you can consider the following strategies:

### Input boundaries: 

Identify the minimum and maximum valid values for each input parameter and test with those values. For example, if a function accepts integers, test with the lowest possible value (e.g., -2^31) and the highest possible value (e.g., 2^31-1).

### Invalid inputs: 

Test the behavior of your code with invalid inputs, such as passing None, empty strings, or unexpected data types. This helps uncover potential issues with input validation or error handling.

### Corner cases: 

Identify special cases or scenarios that may have unique behavior or potential pitfalls. Test with inputs that trigger these corner cases to ensure your code handles them correctly.

### Boundary conditions: 

Test the behavior of your code at the boundaries of its expected range. For example, if your code processes a list, test with an empty list, a list with one element, and a list with a large number of elements.

### Random or generated inputs: 

Use random or generated inputs to simulate a wide range of scenarios and ensure your code handles them appropriately. This approach can help uncover unexpected issues or performance problems.
 
Remember that finding edge cases is an iterative process, and it's important to continually expand and refine your test suite to cover as many scenarios as possible.
