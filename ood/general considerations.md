## SOLID 
is an acronym for a set of design principles in object-oriented programming that are intended to make software designs more understandable, flexible, and maintainable. The principles are as follows:

1. **Single Responsibility Principle (SRP)**: A class should have only one reason to change. This means a class should only have one job or responsibility.

2. **Open-Closed Principle (OCP)**: Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. This means that a class should be easily extendable without modifying the class itself.

3. **Liskov Substitution Principle (LSP)**: Subtypes must be substitutable for their base types. This means that if a program is using a base class, it should be able to use any of its subclasses without the program knowing or behaving incorrectly.

4. **Interface Segregation Principle (ISP)**: Clients should not be forced to depend on interfaces they do not use. This means that a class should not have to implement methods it doesn't use. Instead of one big interface, multiple smaller and specific interfaces should be used.

5. **Dependency Inversion Principle (DIP)**: High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions. This means that one should "depend upon abstractions, [not] concretions."

These principles, when combined together, make it easier to avoid code smells, easily refactor code, and are also a part of the agile or adaptive software development.



## Inheritance vs Composition

"is a" relationship vs "has a" relationship

```python
class Vehicle:
    def start(self):
        pass

    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car started")

    def stop(self):
        super().stop()
        print("Car stopped")
```
```python
class Engine:
    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()
```