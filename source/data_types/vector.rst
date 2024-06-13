=========
Vector<T>
=========

Definition
==========

The `Vector<T>` type represents a mathematical vector of elements of type `T`, providing various methods to manipulate and perform operations on the vector. It is commonly used for mathematical computations and operations in multi-dimensional space.

Syntax
======

.. code-block:: pepitoCode

   Vector<Int> myVector = Vector<Int>();

Properties
==========

- **Size:** The number of elements in the vector.
- **Default Value:** An empty vector (`[]`).

Methods
=======

Manipulation Methods
---------------------

**Add(T element)**

    Adds an element to the end of the vector.

    .. code-block:: pepitoCode

       myVector.Add(5);  // myVector is now [5]

**Insert(Int dimension, T element)**

    Inserts an element at the specified dimension.

    .. code-block:: pepitoCode

       myVector.Insert(0, 10);  // myVector is now [10, 5]

**Remove(T element)**

    Removes the first occurrence of the specified element.

    .. code-block:: pepitoCode

       myVector.Remove(10);  // myVector is now [5]

**RemoveAt(Int dimension)**

    Removes the element at the specified dimension.

    .. code-block:: pepitoCode

       myVector.RemoveAt(0);  // myVector is now []

**Clear()**

    Removes all elements from the vector.

    .. code-block:: pepitoCode

       myVector.Clear();  // myVector is now []

Access Methods
--------------

**Get(Int dimension)**

    Returns the element at the specified dimension.

    .. code-block:: pepitoCode

       Int element = myVector[0];  // element is 5

**Set(Int dimension, T element)**

    Sets the element at the specified dimension.

    .. code-block:: pepitoCode

       myVector[0] = 15;  // myVector is now [15]

**DimensionOf(T element)**

    Returns the dimension of the first occurrence of the specified element, or -1 if not found.

    .. code-block:: pepitoCode

       Int dimension = myVector.DimensionOf(15);  // dimension is 0

**LastDimensionOf(T element)**

    Returns the dimension of the last occurrence of the specified element, or -1 if not found.

    .. code-block:: pepitoCode

       Int lastDimension = myVector.LastDimensionOf(15);  // lastDimension is 0

Utility Methods
---------------

**Contains(T element)**

    Checks if the vector contains the specified element.

    .. code-block:: pepitoCode

       Boolean contains = myVector.Contains(15);  // contains is true

**Count()**

    Returns the number of dimension in the vector.

    .. code-block:: pepitoCode

       Int count = myVector.Count();  // count is 1

**IsEmpty()**

    Checks if the vector is empty.

    .. code-block:: pepitoCode

       Boolean isEmpty = myVector.IsEmpty();  // isEmpty is false

Mathematical Methods
--------------------

**Dot(Vector<T> other)**

    Computes the dot product of this vector with another vector.

    .. code-block:: pepitoCode

       Int dotProduct = myVector.Dot(otherVector);  // dotProduct is the dot product of myVector and otherVector

**Magnitude()**

    Returns the magnitude (length) of the vector.

    .. code-block:: pepitoCode

       Double magnitude = myVector.Magnitude();  // magnitude is the length of myVector

**Normalize()**

    Normalizes the vector (scales it to have a magnitude of 1).

    .. code-block:: pepitoCode

       myVector.Normalize();  // Normalizes myVector

Examples
========

.. code-block:: pepitoCode

   Vector<Int> myVector = Vector<Int>();
   myVector.Add(5);  // myVector is now [5]
   myVector.Insert(0, 10);  // myVector is now [10, 5]
   myVector.Remove(10);  // myVector is now [5]
   myVector.RemoveAt(0);  // myVector is now []
   myVector.Add(15);  // myVector is now [15]
   Int element = myVector[0];  // element is 15
   myVector[0] = 20;  // myVector is now [20]
   Int dimension = myVector.DimensionOf(20);  // dimension is 0
   Boolean contains = myVector.Contains(20);  // contains is true
   Int count = myVector.Count();  // count is 1
   Boolean isEmpty = myVector.IsEmpty();  // isEmpty is false
   myVector.Sort();  // Sorts the vector
   myVector.Reverse();  // Reverses the vector
   Vector<Int> otherVector = Vector<Int>();
   otherVector.Add(1);
   otherVector.Add(2);
   otherVector.Add(3);
   Int dotProduct = myVector.Dot(otherVector);  // Computes the dot product
   Double magnitude = myVector.Magnitude();  // Computes the magnitude
   myVector.Normalize();  // Normalizes the vector

Advanced Features
=================

**Generic Methods**

    The `Vector<T>` type supports generic methods, allowing for type-safe operations on the elements.

    .. code-block:: pepitoCode

       Vector<String> stringVector = Vector<String>();
       stringVector.Add("Hello");
       stringVector.Add("World");

Interoperability
================

**Casting**

    You can cast `Vector<T>` to other collection types if they are compatible.

    .. code-block:: pepitoCode

       Vector<Int> intVector = Vector<Int>();
       List<Int> intArray = (List<Int>) intVector;
