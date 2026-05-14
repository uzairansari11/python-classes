# Python Classes Learning Notes

This repository is my step-by-step learning path for Python classes.

## Goal

Build strong confidence in Python classes for:

- Python interviews
- real projects
- Django development

## Covered Topics

### Foundations

1. Classes and objects
2. `__init__`
3. Instance attributes
4. Class attributes
5. Instance methods
6. Class methods
7. Static methods

### Core OOP

8. `__str__`
9. `__repr__`
10. Inheritance
11. Method overriding
12. Encapsulation
13. Protected and private attributes
14. Getters, setters, and `@property`
15. Abstraction with `ABC` and `@abstractmethod`
16. Polymorphism

### Intermediate and Advanced Classes

17. Operator overloading with `__add__` and `__eq__`
18. Composition
19. Aggregation
20. Multiple inheritance
21. MRO (Method Resolution Order)
22. `super()` in inheritance chains
23. Mixins
24. Dataclasses
25. Callable objects with `__call__`
26. Custom iterators with `__iter__` and `__next__`
27. Custom exceptions
28. Context managers with `__enter__` and `__exit__`
29. Container magic methods:
   - `__len__`
   - `__getitem__`
   - `__contains__`

## Concepts I Should Be Comfortable With

By this stage, I should be able to:

- create and use classes confidently
- understand `self`, `cls`, and `super()`
- tell the difference between instance and class data
- use inheritance properly
- override methods safely
- write reusable mixin-style behavior
- use special methods when needed
- read framework-style class code more easily

## Why This Matters for Django

Django uses classes everywhere:

- models
- forms
- admin classes
- class-based views
- mixins
- managers

The most important class topics for Django are:

- inheritance
- overriding methods
- `super()`
- mixins
- class vs instance attributes
- composition
- abstraction of reusable behavior

## Practice Style

My learning approach:

1. Learn one topic clearly
2. Solve a small problem
3. Get review and rating
4. Fix mistakes
5. Move to the next concept

## Files

- [basic.py](./basic.py): practice exercises and solutions from the learning sessions

## Recommended Next Steps

To gain real mastery:

1. Re-solve the exercises without looking at the answers
2. Write 20 to 30 more class problems
3. Start using classes inside Django projects
4. Practice:
   - model methods
   - overriding `save()`
   - class-based views
   - mixins
   - reusable helper classes

## Optional Advanced Topics for Later

These are useful, but not required immediately for Django:

- `__new__`
- `__slots__`
- descriptors
- metaclasses
- advanced decorator patterns

## Progress Snapshot

Current level: solid intermediate in Python classes, moving toward advanced practical fluency.

That means I am ready to:

- continue advanced Python class practice
- start Django class-based concepts
- keep improving fluency with repetition

## DRF Learning Progress Snapshot

After finishing the Python class topics, I started learning Django REST Framework class-based concepts.

Current DRF class learning level: around 75% complete.

### DRF Topics Completed

1. `serializer_class`
2. Dynamic `get_serializer_class()`
3. `permission_classes`
4. Multiple permissions
5. `authentication_classes`
6. Authentication vs permission
7. `perform_create()`
8. `perform_update()`
9. `get_serializer_context()`
10. `queryset`
11. Dynamic `get_queryset()` with current user filtering
12. `APIView`
13. `ListAPIView`
14. `CreateAPIView`
15. `RetrieveAPIView`
16. `UpdateAPIView`

### DRF Topics Still Left

1. `DestroyAPIView`
2. `ListCreateAPIView`
3. `RetrieveUpdateDestroyAPIView`
4. `ViewSet`
5. `ModelViewSet`
6. DRF mixins:
   - `ListModelMixin`
   - `CreateModelMixin`
   - `RetrieveModelMixin`
   - `UpdateModelMixin`
   - `DestroyModelMixin`
7. Routers
8. Custom actions with `@action`
9. Override rules:
   - `list()` vs `get_queryset()`
   - `create()` vs `perform_create()`
   - `update()` vs `perform_update()`
   - `destroy()` vs `perform_destroy()`
   - `retrieve()` vs `get_object()`

### Next Topic To Continue From

Continue from:

```text
DRF DestroyAPIView
```

The last completed topic was:

```text
DRF UpdateAPIView
```

### Important Pattern Learned

Most DRF class concepts follow the same OOP pattern:

```text
Parent class controls the main flow.
Child class sets class attributes or overrides small methods.
DRF calls those methods internally.
```

Examples:

- `queryset` tells DRF what data to use.
- `serializer_class` tells DRF which serializer to use.
- `permission_classes` tells DRF who can access the API.
- `get_queryset()` is used for dynamic filtering.
- `get_serializer_class()` is used when serializer changes by action.
- `get_serializer_context()` sends extra data to the serializer.
- `perform_create()` customizes saving during create.
- `perform_update()` customizes saving during update.
