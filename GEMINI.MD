### Code Generation Rules
Always use context7 when I need code generation, setup, configuration, planning steps, or library/API documentation. This means you should automatically use the Context7 MCP tools to resolve library id and get library docs without me having to explicitly ask.

### Development Conventions

* Don’t try to be clever
* Build the simplest code possible that will pass the test
* With each change practice self reflection:
    - How difficult was it to write?
    - How hard is it to understand?
    - How expensive will it be to change?
* Code should be concrete enough to be understood while simultaneously being abstract enough to	allow for change.
* Code is easy to understand when it clearly reflects the problem it’s solving, and thus openly	exposes that problem’s domain.
* Isolate things that change from things that don’t change (high cohesion, loose coupling)
* Each method should have a Single Responsibility and methods should be consistent. Consistent code enables future refactorings.
* Seek stable landing points and create a git commit when the application complies and tests pass before moving on to the next functional change.

### Project creation
* Remove any unused boiler plate code generated from new project creation by the frameworks.

### Test Driven Development

All development should be done using red-green-refactor test driven development. 

* Write tests that confirm what your code does first without any knowledge of how your code does it.
* Tests are not the place for abstractions—they are the place for concretions. Abstractions belong in code.
* When faced with a new requirement, first rearrange the existing code such that it's open to the new feature, and once that's complete, then add the new code
* When refactoring, follow the flocking rules: 
    1. Select the things that are most alike.
    2. Find the smallest difference between them.
    3. Make the simplest change to remove that difference
