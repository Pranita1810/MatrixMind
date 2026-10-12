# Object-Oriented Programming (OOP) in Python

This folder contains architectural guides, conceptual notes, and practical interview questions on **Object-Oriented Programming (OOP)** in Python.

---

## 📚 Curriculum Roadmap

```mermaid
flowchart LR
    A["1. Classes & Instances"] --> B["2. The 4 Pillars"]
    B --> C["3. Methods & Properties"]
    C --> D["4. Dunder Methods & Metaprogramming"]
    D --> E["5. Design Patterns & Architecture"]
```

### Module 1: The Four Pillars of OOP
* **Abstraction**: Hiding low-level complexity via interfaces and the `abc` module (`@abstractmethod`).
* **Encapsulation**: State protection using private mangling (`__attribute`), protected convention (`_attribute`), and `@property` getters/setters.
* **Inheritance**: Subclassing, Method Resolution Order (`MRO` via C3 Linearization), and `super()`.
* **Polymorphism**: Method overriding, dynamic dispatch, and Pythonic duck typing.

### Module 2: Method Types & Special Mechanisms
* **Instance Methods**: Bound to object instance via `self`.
* **Class Methods**: Decorated with `@classmethod`, bound to class object via `cls`. Ideal for alternative factory constructors.
* **Static Methods**: Decorated with `@staticmethod`, independent utility functions within class namespace.
* **Special Dunder Methods**:
  * Initialization: `__init__`, `__new__`
  * Representation: `__repr__`, `__str__`
  * Emulating Containers: `__len__`, `__getitem__`, `__setitem__`
  * Operator Overloading: `__add__`, `__sub__`, `__eq__`

---

## 📂 Contents
* [Fundamentals.txt](file:///C:/Users/PANRIT/ALL/Pranit%20Main/Study/python/OOPS/Fundamentals.txt): Complete conceptual reference for OOP principles, terminology, and dunder methods.
* [Technical_QA.ipynb](file:///C:/Users/PANRIT/ALL/Pranit%20Main/Study/python/OOPS/Technical_QA.ipynb): Real-world interview technical questions, code scenarios, and solutions.
* [test.py](file:///C:/Users/PANRIT/ALL/Pranit%20Main/Study/python/OOPS/test.py): Scratchpad for OOP implementation testing.
