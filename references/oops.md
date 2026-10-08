# OOPs Reference -- Object Oriented Programming

## The Four Pillars

### 1. Encapsulation
Bundling data (fields) and methods that operate on that data into a single unit (class), and restricting direct access to the internal state.
- Achieved via access modifiers: private, protected, public
- Getters and setters provide controlled access
- Interview angle: "It protects object integrity and reduces coupling between components"

### 2. Abstraction
Hiding the complex implementation details and exposing only what the user needs.
- In Java: achieved via abstract classes and interfaces
- Abstract class: can have method bodies, constructors, fields
- Interface: all methods are implicitly abstract (until Java 8 default methods), no state
- Interview angle: "Abstraction reduces complexity and makes code easier to use and maintain"

### 3. Inheritance
A class (child) inheriting properties and behaviours from another class (parent).
- IS-A relationship: Dog IS-A Animal
- Types: Single, Multilevel, Hierarchical (Java does not support multiple inheritance with classes)
- Method overriding: child provides its own implementation of a parent method
- super keyword: access parent class constructor or method
- Interview angle: "Inheritance promotes code reuse but creates tight coupling, so prefer composition when possible"

### 4. Polymorphism
The ability of an object to take many forms.

**Compile-Time (Static) Polymorphism -- Method Overloading**
Same method name, different parameters (number, type, or order)
```java
int add(int a, int b) { return a + b; }
double add(double a, double b) { return a + b; }
```

**Run-Time (Dynamic) Polymorphism -- Method Overriding**
Child class overrides parent method. Decision made at runtime via dynamic dispatch.
```java
Animal a = new Dog(); // upcasting
a.sound(); // calls Dog's sound(), not Animal's
```

---

## Interface vs Abstract Class

| Feature | Interface | Abstract Class |
|---|---|---|
| Methods | All abstract (pre Java 8) | Can have concrete and abstract |
| Variables | public static final only | Any type |
| Constructor | Not allowed | Allowed |
| Multiple inheritance | Yes (implements multiple) | No (extends one) |
| Use when | Define a contract/capability | Provide common base with some default behaviour |

---

## SOLID Principles

**S -- Single Responsibility Principle**
A class should have only one reason to change. Each class does one thing well.

**O -- Open Closed Principle**
Open for extension, closed for modification. Add new behaviour via new classes, not by changing existing ones.

**L -- Liskov Substitution Principle**
Objects of a subclass should be replaceable with objects of the superclass without breaking the program.

**I -- Interface Segregation Principle**
No client should be forced to implement methods it does not use. Prefer small, specific interfaces over large general ones.

**D -- Dependency Inversion Principle**
High-level modules should not depend on low-level modules. Both should depend on abstractions (interfaces).

---

## Design Patterns

### Creational Patterns

**Singleton**
Ensures only one instance of a class exists.
```java
public class Singleton {
    private static Singleton instance;
    private Singleton() {}
    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}
```
Thread-safe version uses double-checked locking or enum.

**Factory Method**
Defines an interface for creating objects but lets subclasses decide which class to instantiate.
```java
interface Shape { void draw(); }
class Circle implements Shape { public void draw() { ... } }
class ShapeFactory {
    public static Shape getShape(String type) {
        if (type.equals("circle")) return new Circle();
        // ...
    }
}
```

**Builder**
Constructs complex objects step by step. Avoids telescoping constructors.
```java
Person p = new Person.Builder("Alice").age(22).city("Delhi").build();
```

### Structural Patterns

**Decorator**
Adds behaviour to objects dynamically by wrapping them, without altering the class.
Example: Java I/O streams (BufferedReader wraps FileReader)

**Adapter**
Converts an incompatible interface into one that a client expects.
Example: Power socket adapters in real life

**Facade**
Provides a simplified interface to a complex subsystem.
Example: A hotel reception that coordinates housekeeping, kitchen, and security internally

### Behavioural Patterns

**Observer**
One object (subject) notifies multiple dependents (observers) when its state changes.
Example: YouTube notification system. Event listeners in UI frameworks.

**Strategy**
Defines a family of algorithms and makes them interchangeable.
Example: Sorting strategy, payment strategy (CreditCard, UPI, NetBanking)

**Command**
Encapsulates a request as an object, allowing parameterization, queuing, and undo.
Example: Remote control buttons

---

## Common Interview Questions

1. What is the difference between overloading and overriding?
2. Can we override a static method in Java? (No, static methods are resolved at compile time)
3. Can we override a private method? (No, private methods are not visible to subclasses)
4. What is the diamond problem and how does Java handle it? (Java avoids it by not allowing multiple class inheritance, but interfaces can have default methods, resolved by explicit override)
5. What is an abstract class with no abstract methods? (Valid, prevents direct instantiation)
6. What is covariant return type? (An overriding method can return a subtype of the return type of the overridden method)
7. What is the difference between IS-A and HAS-A relationships?
8. When would you use composition over inheritance? (When you want flexibility and want to avoid tight coupling)
9. What is method hiding vs method overriding? (Static methods are hidden, not overridden)
10. What is the role of the final keyword in OOPs? (final class cannot be inherited, final method cannot be overridden, final variable is a constant)

---

## Advanced OOP Interview Q Bank

### Composition vs Inheritance
- Inheritance = IS-A, compile-time fixed, white-box reuse, breaks encapsulation (fragile base class problem).
- Composition = HAS-A, runtime swappable, black-box reuse via delegation. Prefer it unless a true IS-A and LSP hold.
- Example: Car HAS-A Engine (inject different Engine); do not make Car extend Engine.

### Diamond Problem
A inherits B and C, both override A.f(); D inherits B and C: which f()?
- Java: no multiple class inheritance. Interface default method clash is a compile error unless D overrides; call `B.super.f()` to pick one.
- C++: allows multiple inheritance; D gets two copies of A (ambiguous). Fix with `virtual` inheritance (`class B : virtual public A`) so one shared A subobject.
- Python: allows it; resolved by MRO (C3 linearization), see `D.__mro__`; `super()` follows MRO.

### Overloading vs Overriding Rules
| | Overloading | Overriding |
|---|---|---|
| Signature | Same name, different params | Same name and params |
| Return type | Can differ (alone is not enough) | Same or covariant subtype |
| Binding | Compile time | Run time |
| Access | Any | Cannot be more restrictive |
| Exceptions | Any | Cannot throw broader checked exceptions |
| Not allowed | - | static, private, final methods (static is hidden) |
- Use `@Override` so the compiler catches signature typos.

### Static vs Dynamic Binding
- Static (early): resolved at compile time. Overloaded, static, private, final methods and fields.
- Dynamic (late): resolved at runtime from the actual object type. Overridden instance methods.
- Fields are never polymorphic: `Animal a = new Dog(); a.name` uses Animal's field.

### Virtual Functions (C++)
- `virtual` method: call goes through vptr -> vtable of the actual object type. Non-virtual: bound at compile time on the pointer type.
- Pure virtual `= 0` makes a class abstract. Java instance methods are virtual by default.
- Base class with virtual functions needs a virtual destructor, else `delete base_ptr` is undefined behaviour (derived part not destroyed).
- Virtual calls inside constructors/destructors do not reach the derived override (C++); in Java they can see uninitialised derived fields.

### Constructor and Destructor Order
- Construction: base first, then members, then derived body. Destruction: exact reverse.
- Java: `super(...)` must be first statement; field initialisers and init blocks run before the constructor body. Java has no destructors (finalize deprecated; use try-with-resources/AutoCloseable).
- C++ members are constructed in declaration order, not initializer-list order.

### Copy Constructor: Shallow vs Deep Copy
- Shallow: copies field values; pointer/reference fields share the same target (aliasing, double free in C++).
- Deep: copies the pointed-to data too. In C++ follow the Rule of Three/Five: if you define destructor, copy ctor or copy assignment, define all (plus move ops).
- Java: `clone()` is shallow by default; prefer a copy constructor or copy factory.

### Immutability
- Java recipe: final class, private final fields, no setters, defensive copies of mutable inputs/outputs.
- Benefits: thread-safe without locks, safe as HashMap keys, cacheable. Cost: new object per change.
- Examples: String, Integer, LocalDate. A `final` reference does not make the object immutable.

### Object Slicing (C++)
Assigning/passing a derived object by value to a base type copies only the base part; derived data and overrides are lost.
```cpp
Derived d; Base b = d;   // sliced
void f(Base b);          // sliced on call; use Base& or Base*
```

### Coupling and Cohesion
- Coupling: dependence between modules. Want LOW (depend on interfaces, not concretions).
- Cohesion: how related a module's responsibilities are. Want HIGH (SRP).
- Rule: high cohesion inside, loose coupling between.

### Law of Demeter (Least Knowledge)
A method should call only: itself, its parameters, objects it creates, its fields. Avoid `a.getB().getC().doX()`; add a delegating method instead ("talk to friends, not strangers").

### DRY / KISS / YAGNI
- DRY: one authoritative place for each piece of knowledge (not just no copy-paste; avoid wrong abstraction).
- KISS: simplest design that works.
- YAGNI: do not build features/abstractions until needed.

### Dependency Injection vs Dependency Inversion
- Dependency Inversion (principle, the D in SOLID): both high and low level depend on an abstraction owned by the high level.
- Dependency Injection (technique): dependencies are supplied from outside (constructor > setter > interface injection) instead of `new` inside. DI helps achieve DIP and testability (mocks).
- IoC container (Spring) automates DI. Service Locator is the contrasting, hidden-dependency approach.

### Remaining Design Patterns (not covered above)
**Creational**
- Abstract Factory: create families of related objects without naming concrete classes. Use: cross-platform UI kit (WinButton+WinCheckbox vs MacButton+MacCheckbox).
- Prototype: create objects by cloning an existing instance. Use: costly-to-build objects, game unit spawning.

**Structural**
- Proxy: stand-in controlling access to another object. Use: lazy loading, access control, caching, remote proxy (RPC stubs).
- Composite: treat single objects and trees uniformly. Use: file system, UI component tree.
- Bridge: split abstraction from implementation so both vary independently. Use: Shape x Renderer.
- Flyweight: share intrinsic state to save memory. Use: characters in a text editor, Java String pool/Integer cache.

**Behavioural**
- State: object changes behaviour when internal state changes, each state a class. Use: vending machine, order lifecycle, TCP connection.
- Template Method: skeleton algorithm in base class, subclasses fill steps. Use: frameworks, data-processing pipelines.
- Chain of Responsibility: pass request along handlers until one handles it. Use: servlet filters, logging levels, approval flows.
- Iterator: sequential access without exposing structure. Use: Java Iterable/for-each.
- Mediator: central object coordinates peers so they do not reference each other. Use: chat room, air traffic control.
- Memento: capture and restore state without breaking encapsulation. Use: undo, snapshots.
- Visitor: add operations to a class hierarchy without modifying it (double dispatch). Use: AST traversal, tax calculation across item types.
- Interpreter: grammar as classes to evaluate sentences. Use: regex, expression evaluators.
- Quick distinction: Strategy = swap algorithm from outside; State = object swaps its own behaviour; Decorator adds behaviour, Proxy controls access, Adapter changes interface.

### 20 Tricky Q&As
1. Can a constructor be virtual/overridden? No. Constructors are not inherited; C++ has no virtual constructors (use a virtual clone/factory).
2. Can an abstract class have a constructor? Yes, called via super() when subclasses are built.
3. Can an interface have a constructor? No. It has no state to initialise.
4. Does overloading depend on return type? No; two methods differing only by return type will not compile.
5. What if the child override throws a broader checked exception? Compile error. Unchecked exceptions are fine.
6. `Parent p = new Child(); p.staticMethod()`? Parent's version (static is hidden, resolved by reference type).
7. Is a `private` method call polymorphic? No; private methods are not inherited, bound statically.
8. Can we override a `final` method? No. Can we overload it? Yes.
9. Why must the base destructor be virtual in C++? So deleting via base pointer runs the derived destructor.
10. Why is a Java String immutable? String pool sharing, hash caching, thread safety, security (class names, paths, URLs).
11. `==` vs `equals()`? `==` compares references (or primitives); `equals` compares logical content if overridden. Override `hashCode` with `equals`.
12. What breaks if equals is overridden without hashCode? Equal objects land in different HashMap buckets; lookups fail.
13. Does Square extend Rectangle violate any principle? LSP: setting width alters height, breaking Rectangle's contract.
14. Abstract class vs interface today? Interface (default methods) = capability, multiple allowed, no instance state; abstract class = shared state and partial implementation.
15. What is a marker interface? Empty interface that tags a class (Serializable, Cloneable); annotations are the modern alternative.
16. Can a class be both abstract and final? No, contradictory.
17. Output order for `new Child()` with static blocks, instance blocks and constructors? Parent static, Child static (once at class load), Parent instance block, Parent ctor, Child instance block, Child ctor.
18. Why does Singleton need `volatile` in double-checked locking? Prevents reordering where another thread sees a non-null but partly constructed instance.
19. Can Singleton be broken? Yes: reflection, serialization, cloning, multiple classloaders. Enum singleton resists reflection and serialization.
20. Is `protected` accessible in the same package in Java? Yes; protected = package + subclasses (in C++ it is subclasses/friends only).
