=======
List<T>
=======

Definition
==========

The `List<T>` type represents a dynamic array of elements of type `T`, providing various methods to manipulate the list.

Syntax
======

.. code-block:: pepitoCode

   List<Int> myList = List<Int>();

Properties
==========

- **Size:** The number of elements in the list.
- **Default Value:** An empty list (`[]`).

Methods
=======

Manipulation Methods
---------------------

**Add(T element)**

    Adds an element to the end of the list.

    .. code-block:: pepitoCode

       myList.Add(5);  // myList is now [5]

**Insert(Int index, T element)**

    Inserts an element at the specified index.

    .. code-block:: pepitoCode

       myList.Insert(0, 10);  // myList is now [10, 5]

**Remove(T element)**

    Removes the first occurrence of the specified element.

    .. code-block:: pepitoCode

       myList.Remove(10);  // myList is now [5]

**RemoveAt(Int index)**

    Removes the element at the specified index.

    .. code-block:: pepitoCode

       myList.RemoveAt(0);  // myList is now []

**Clear()**

    Removes all elements from the list.

    .. code-block:: pepitoCode

       myList.Clear();  // myList is now []

Access Methods
--------------

**Get(Int index)**

    Returns the element at the specified index.

    .. code-block:: pepitoCode

       Int element = myList.Get(0);  // element is 5

**Set(Int index, T element)**

    Sets the element at the specified index.

    .. code-block:: pepitoCode

       myList.Set(0, 15);  // myList is now [15]

**IndexOf(T element)**

    Returns the index of the first occurrence of the specified element, or -1 if not found.

    .. code-block:: pepitoCode

       Int index = myList.IndexOf(15);  // index is 0

**LastIndexOf(T element)**

    Returns the index of the last occurrence of the specified element, or -1 if not found.

    .. code-block:: pepitoCode

       Int lastIndex = myList.LastIndexOf(15);  // lastIndex is 0

Utility Methods
---------------

**Contains(T element)**

    Checks if the list contains the specified element.

    .. code-block:: pepitoCode

       Boolean contains = myList.Contains(15);  // contains is true

**Count()**

    Returns the number of elements in the list.

    .. code-block:: pepitoCode

       Int count = myList.Count();  // count is 1

**IsEmpty()**

    Checks if the list is empty.

    .. code-block:: pepitoCode

       Boolean isEmpty = myList.IsEmpty();  // isEmpty is false

**Sort()**

    Sorts the elements in the list in ascending order.

    .. code-block:: pepitoCode

       myList.Sort();  // Sorts the list

**Reverse()**

    Reverses the order of the elements in the list.

    .. code-block:: pepitoCode

       myList.Reverse();  // Reverses the list

Examples
========

.. code-block:: pepitoCode

   List<Int> myList = List<Int>();
   myList.Add(5);  // myList is now [5]
   myList.Insert(0, 10);  // myList is now [10, 5]
   myList.Remove(10);  // myList is now [5]
   myList.RemoveAt(0);  // myList is now []
   myList.Add(15);  // myList is now [15]
   Int element = myList.Get(0);  // element is 15
   myList.Set(0, 20);  // myList is now [20]
   Int index = myList.IndexOf(20);  // index is 0
   Boolean contains = myList.Contains(20);  // contains is true
   Int count = myList.Count();  // count is 1
   Boolean isEmpty = myList.IsEmpty();  // isEmpty is false
   myList.Sort();  // Sorts the list
   myList.Reverse();  // Reverses the list

Advanced Features
=================

**Generic Methods**

    The `List<T>` type supports generic methods, allowing for type-safe operations on the elements.

    .. code-block:: pepitoCode

       List<String> stringList = List<String>();
       stringList.Add("Hello");
       stringList.Add("World");

Interoperability
================

**Casting**

    You can cast `List<T>` to other collection types if they are compatible.

    .. code-block:: pepitoCode

       List<Int> intList = List<Int>();
       Vector<Int> intArray = (Vector<Int>) intList;
