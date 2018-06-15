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
2. syndax:
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
1. Association: When one class is contained by another, we always use an association.
2. Aggregation: Different form of association, where one class "has" another class, but both exist independently. For example, pond has duck.
3. Composition: Indicating one class cannot exist without the other. A Department is entirely dependent on a University to exist.
4. 

### Lecture 13:
