# OOSD LECTURE SUMMARY

### Lecture 2: String
1. String is a Java class made up of sequence of characters. Also a data type.
2. Escaping: To include "special" characters in a string, use "\\" to escape from the character's normal meaning.
3. use s.contains("Hell") to check substring presence.
4. use s.indexOf("Hell") to find substring location
5. use s.substring(2,7) to get substring
6. use s.length() to find the length of the string
7. use s.toUpperCase() cast to upper case.
8. use s.split(" ") to split string.
9. use == to compare pointers of string, use equals to compare the content of a two strings
10. Wrapper: A class that gives extra functionality to primitives like int, and lets them behave like object.

### Lecture 3: IO
1. Command Line Argument: Information or data provided to a program when it is executed, accessible through the args variable.

### Lecture 4: Arrays
1. Arrays: A sequence of elements of the same type arranged in order in memory.
2. syntax:
    ```JAVA
    int[] ints = {0,1,2,3,4};
    int[] ints = new int[100];
    ```
3. can also define a multi-dimensional array
4. us ints.length **(no bracket after length for array)** to return the length of the array
5. use Arrays.equals(a1,a2) to copare the equality of two array
6. ints = new int\[ints.length + 1\] to resize
7. use Arrays.sort(a1) to sort (ascending order) an array.
8. use System.out.println(Arrays.toString(a1)) to print a array.
9. for each loop, for example, for (int i: ints)

### Lecture 6: Method
1. Return: Indicates that a method end, and in most cases will output a value. A method can have several return statements, but path must reach a return.
2. why method:
    - prevents code duplication
    - improves readability
    - makes code reusable and portable
    - easier to debug
    - give "important code" a useful name
3. Method: The basic unit of abstraction in JAVA; represents performing an action.
4. Static: indicates a constant, variable, or method exists without an object. In other words, you do not need to create a variable to use something define as static.
5. Scope: define when a constant, variable or method can be seen.
6. Method Signature: The name of a method, and the number and type of its parameters.
7. Overloading: When methods share the same name, but differ in the number, or type of arguments in the method signature.

### Lecture 7: Class
1. Class: Fundamental unit of abstraction in Java. Represents an “entity” that is part of a problem.
2. Object is a specific, concrete example of a class.
3. Instance: An object that exist in your code.
4. Class (Static) Variable: A property or attribute that is common to/shared by all instances of a class.
5. Instance Variable: A property or attribute that is unique to each instance (object) of a class.
6. Class (Static) Method: An action that can be performed by a class, or a message that can be sent to it.
7. Instance Method: An action that can be performed by an object, or a message that can be sent to it.
8. Instantiate: To create an object of a class
9. new: Directs the JVM to allocate memory for an object, or instantiate it
10. Constructor: A method used to create and initialise an object.

### Lecture 8: Privacy
1. Mutable: An object is mutable if any of its instance variables can be changed after being initialised.
2. Immutable: Immutable: A class is immutable if all of its attributes are private, it contains no setters, and only returns copies of its (mutable) instance variables.
3. Information Hiding: Using privacy to "hide" the details of a class from the outside world.
4. Access Control: Preventing an outside class from manipulating the properties of another class in undesired way.
5. Private: Only available to method define in the same class; should be applied to almost all (mutable) instance variable, and some method.
6. Package: Default, applied if nothing else specified; available to all classes in the same package.
7. Protected: Available to all classes in the same package and also to any subclasses that inherit from the class.
8. Public: Available at all times, everywhere.
9. Getter/Accessor: A method that returns an instance variable from a class.
10. Setter/Mutator: A method that modifies the value of an instance variable.

### Lecutre 9: Inheritance
1. Inheritance: A form of abstraction that permits “generalisation” of similar attributes/methods of classes; analogous to passing genetics on to your children.
2. Superclass: The “parent” or “base” class in the inheritance relationship; provides general information to its “child” classes.
3. Subclass: The “child” or “derived” class in the inheritance relationship; inherits common attributes and methods from the “parent” class.
    - Subclass automatically contains all instance variables and methods in the base class.
    - Additional methods and/or instance variable can be defined in subclass.
    - Inheritance allows code to be reused.
    - Subclasses should be "more specific" version of a superclass
4. Extends: Indicates one class inherits from another
    - It define a ***is A*** relationship. Only use inheritance when the relationship make sense.
5. Super: Invokes a constructor in the parent class.
    - can also be used to call the method in superclass.
6. Shadowing: When two or more variables are declared with the same name in overlapping scopes; for example, in both a subclass and superclass.
    - the most closest variable to the method will be called.
7. Overriding: Declaring a method that exists in a superclass again in a subclass, with the same signature. Methods can only be overriden by subclasses.
    - can only change the return type to a subclass of the orginal
8. Final: Indicates that a variable, method, or class can only be assigned, declared or defined once.
    - Final classes may not be inherited.


### Lecture 10: Abstract
1. All classes have a toString and equals method
    - but they are pretty useless.
2. getClass: Returns a Class object representing the class of an object.
3. instanceof: Returns true if an object A is an instance of the same class as object B, or a class that inherits from B.
4. Upcasting: When an object of a child class is assigned to a variable of an ancestor class.
5. Downcasting: When an object of an ancestor class is assigned to a variable of a child class. Only makes sense if the underlying object is actually of that class. Why?
6. Polymorphism: The ability to use objects or methods in many different ways; roughly means “multiple forms”.
    - Overloading: method use depends on signature.
    - Overriding: method use depends on the class that was instantiate.
    - Substitution: subclass taking the place of superclass.
    - Generics: defining parametrised methods/class.
7. abstract: Defines a superclass method that is common to all subclasses, but has no implementation. Each subclass then provides it’s own implementation through overriding.
    - Classes with abstract method must be abstract class
    - abstract class can have no abstract methods.
8. Concrete class: Any class that is not abstract, and has well-define, specific implementations for all actions it can take.

### Lecture 11: Inheritance
1. Interface: Declears a set of constant and/or methods that define the behaviour of an object.
    - Methods never have any code.
    - All methods are implied to be abstract.
    - All attributes are implied to be static final.
    - All methods and attributes are implied to be public.
    - Class that don't implement all methods must be abstract.
2. implements: Declares that a class implements all the functionality expected by an interface.
3.default: Indicates a standard implementation of a method, that can be overridden if the behaviour doesn’t match what is expected of the implementing class.
3. difference bewteen Interface and Inheritance
    - Inheritance represents passing shared information from a parent to child. Fundamentally an "IS A" relationship.
    - Interface: Represents the ability of a class to perform an action. Fundamentally a "Can do" relationship.

### Lecture 12: UML
1. Association: When one class is contained by another, we always use an association. It implies that one class (arrow end) is an instance variable of the other class.
2. Aggregation: Different form of association, where one class "has" another class, but both exist independently. For example, pond has duck.
3. Composition: Indicating one class cannot exist without the other. A Department is entirely dependent on a University to exist.
4. Multiplicity: a number or range at the end of an association. Multiplicity indicates that one class has an array, list, or similar data structure to store multiple instances of another class.
5. Abstract: indicated by italicised text on a class or method name
6. Interface: an interface is defined like a class, with the keyword \<\<interface\>\>. A link from a class that implements an interface is drawn with a dashed line, and empty triangle.

### Lecture 13: Generics
1. ArrayList:
    - a.add(index(not mendatory),content) to add content
    - use a.got(index) to get the content at index
    - use Collections.sort(a) to sort a ArrayList
    - use a.remove(index) to remove the contect at index
    - use a.contains(content) to detect if content is in the ArrayList
    - use a.size() to return the size of the ArrayList
    - can be iterated using for-each
2. collections: A framework that permits storing, accessing and manipulating collections of similar objects.

### Lecture 14: Exceptions
1. syntax Error: Errors where what you write isn't legal code; identified by the editor/compiler.
2. Semantic Error: Code runs to completion, but results in incorrect output/operation; identified through software testing.
3. Runtime Error: An error that causes your program to end prematurely(crash and burn); identified through execution.
4. Exceptions: An error state created by a runtime error in your code; an exceptions. Can also represent an object created by JAVA to represet the error that was encountered.
5. Exception Handling: Code that actively protects your program in the case of exceptions.
6. the stucture is like try...catch...final...
7. try: Attempt to execute some code that may result in an error state (exception).
8. catch: Deal with the exception. This could be recovery (ask the user to input again, adjust an index) or failure (output an error message and exit).
9. finally: Perform clean up (like closing files) assuming the code didn’t exit.
10. throw: Respond to an error state by creating an exception object.
11. throws: Indicate a method has the potential to create an exception, and can’t be bothered to deal with it, or that the exact response varies by application.
12. Checked: Must be handled by the programmer explicitly by the programmer in some way; the compiler gives an error if a checked exception is ignored.
13. Unchecked: Can be safely ignored by the programmer; most Java exceptions are unchecked, because you aren’t forced to protect against them.

### Lecture 15: Testing
1. Poor Design Symptoms
    - Rigidity: Hard to modify the system because changes in one class/method cascade to many others.
    - Fragility: Changing one part of the system causes unrelated part to break.
    - Immobility: Cannot decompose the system into reusable modules.
    - Viscosity: Writing "hacks" when adding code in order to preserve the design.
    - Complexity: Lots of clever code that isn't necessary right now; premature optimisation is bad.
    - Repetition: Code looks like it was written by Cut and Paste.
    - Opacity: Lots of convoluted logic, design is hard to follow.
2. GRASP Basic
    - Cohesion: **Classes are designed to solve clear, focused problems.** The class' methods/attributes are related to and work towards, this objective. Design should have maximum cohesion.
    - Coupling: **The degree of interaction between classes**; invoking another class' method or accessing/modifying its variable. Design should have minimum coupling.
    - Open-Closed Principle: Classes should be open to extension, but closed to modification. (better to use inheritance instead of modify the original one)
    - Abstraction: Solving problems by **creating abstract data types to represent problem components**
        - Achieved in Java through classes, which represent data and actions.
    - Encapsulation: The details of a class should be kept hidden or private, and the user's ability to access the hidden details is restricted or controlled. **Also known as data or information hidden.**
    - Polymorphism: The ability to use an object or method in many different ways.
        - achieved in Java through ad hoc (overloading), subtype (overriding, substitution), and parametric (generics) polymorphism.
    - Delegation: **Keeping classes focused by passing work to other classes.** Computations should be performed in the class with the greatest amount of relevent information.
3. Software Testing
    - Unit: A Small, well-define component of a software system with one, or a small number, of responsibility.
    - Unit Test: Verifying the operation of a unit by testing a single unit case(input/output), intending for it to fail.
    - Unit Testing: Identifying bugs in software by subjecting every unit to a suite of tests.
4. Unit tests
    - Manual Testing: Testing code manually, in an ad-hoc manner. Generally difficult to reach all edge cases, and not scalable for large projects.
    - Automated Testing: Testing code with automated, purpose built software. Generally faster, more reliable, and less reliant on humans.
5. JUnit Automated Testing
    - assert: A true or false statement that indicates the success or failure of a test case.
    - TestCase class: A class dedicated to testing a single unit.
    - TestRunner class: A class dedicated to executing the tests on a unit.
    - Advantages:
        - Easy to set up
        - Scalable
        - Repeatable
        - Not human intensive
        - Incredibly powerful
        - Finds bug

### Lecture 16 Patterns
1. Factory Pattern
    - Factory: A general technique for manufacturing(creating) objects.
    - Product: An abstract class that generalises the objects being created/produced by the factory.
    - Creator: An abstract class that generalises the objects that will consume/produce products.
        - generally have some operation that will invoke the factory method.

2. Analysis a pattern
    - Intent: The goal of the pattern, why it exists.
    - Motivation: A scenario that highlights a need for the pattern
    - Applicability: General situations where you can use the pattern
    - Structure: Graphical representations of the pattern, likely a UML class diagram
    - Participants: List of classes/objects and their roles in the pattern
    - Collaboration: How the objects in the pattern interact
    - Consequences: A description of the results, side effects, and tradeoffs when using the pattern
    - Implementation: Example of “solving a problem” with the pattern
    - Known Uses: Specific, real-world examples of using the pattern
3. Observer pattern
    - Subject: An "important" object, whose state (or change in state) determines the actions of other classes.
    - Observer: An object that monitors the subject in order to respond to its state, and any changes made to it.


### Lecturne 17 Games
1. Sequential Programming: A sequential program is run top to bottom, starting at the beginning of the main method, and concluding at its end.
    - useful for "static" programs
    - Constanct, unchangeable logic
    - Execution is the same (or vary similar) each time.
2. Even-Driven Programming
    - State: The properties that define an object or device, for example, whether it is "active".
    - Event: Create when the state of an object/device/etc is altered.
    - Callback: A method triggered by an event.
    - definition: Using events and callbacks to control the flow of a program's execution.
3. The event loop
    - Polling (also call sampling): relies on the program actively enquiring about the state of object/device/etc.
4. Asynchronous Programming
    - Interrupt: A signal generated by hardware or software indicating an event that needs immediate CPU attention.
    - Interrupt Service Routine: Event-handling code to respond to interrupt signals.
5. Game design
    - Enetity-Component approach
        - seperate complex inheritance diagram into *Entity* object which are collections Component objects. We can easily reuse Components between different *Entitys*. This is called entity-component approach.

### Lecture 19 Advance
1. enum: A class that consists of a finits list of constants.
2. Functional Interface: An interface that contains only single abstract method.
    - Also called a single abstract method interface.
    - Predicate functional interface
        - Represents a predicate, a function that accepts one argument, and returns true or false.
        - Executes the boolean test(T t) method on a single object.
        - Can be combined with other predicates using *and*, *or*, and *negate* methods.
    - UnaryOperator function interface
        - Represents a unary (single argument) function that accepts one arguments, and returns an object of the same type
        - Executes the T apply(T t) method on single elements.
3. Lambda Expression: A technique that treats code as data that can be used as an “object”; for example, allows us to instantiate an interface without implementing it.
4. Method Reference: An object that stores a method.
    - Can take the place of a lambda expression if that lambda expression is only used to call a single method.
5. Streaming: A series of elements given in sequence, that are automatically put through a pipeline of operations.
    - map: convert input to output
    - filter: select elements with condition
    - limit: perform a maximum number of iterations
    - collect: gather all elements and output in a list, array, String.
    - reduce: aggregate a stream into a single value.
6. Variadic Method: A method that takes an unknown number of arguments.
    - Variadic methods implicitly convert the input arguments into an array.
