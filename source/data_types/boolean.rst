========
Boolean
========

Definition
==========

The `Boolean` type represents a value that can be either `true` or `false`, used for logical operations and conditions.

Syntax
======

.. code-block:: pepitoCode

   Boolean myBoolean = true;

Properties
==========

- **Possible Values:** `true` or `false`
- **Default Value:** `false`

Methods
=======

Logical Methods
---------------

**And(Boolean other)**

    Performs a logical AND operation with another boolean and returns the result.

    .. code-block:: pepitoCode

       Boolean result = myBoolean.And(false);  // result is false

**Or(Boolean other)**

    Performs a logical OR operation with another boolean and returns the result.

    .. code-block:: pepitoCode

       Boolean result = myBoolean.Or(true);  // result is true

**Not()**

    Returns the logical negation of this boolean.

    .. code-block:: pepitoCode

       Boolean result = myBoolean.Not();  // result is false if myBoolean is true

**Xor(Boolean other)**

    Performs a logical XOR operation with another boolean and returns the result.

    .. code-block:: pepitoCode

       Boolean result = myBoolean.Xor(true);  // result is false if myBoolean is true

Comparison Methods
------------------

**Equals(Boolean other)**

    Checks if this boolean is equal to another boolean.

    .. code-block:: pepitoCode

       Boolean isEqual = myBoolean.Equals(true);  // isEqual is true if myBoolean is true

**CompareTo(Boolean other)**

    Compares this boolean to another boolean (returns 0 if equal, -1 if this is false and other is true, 1 if this is true and other is false).

    .. code-block:: pepitoCode

       Int comparison = myBoolean.CompareTo(false);  // comparison is 1 if myBoolean is true

Conversion Methods
------------------

**ToString()**

    Converts the boolean to its string representation (`"true"` or `"false"`).

    .. code-block:: pepitoCode

       String boolString = myBoolean.ToString();  // boolString is "true"

Utility Methods
---------------

**Toggle()**

    Toggles the value of the boolean.

    .. code-block:: pepitoCode

       myBoolean.Toggle();  // myBoolean becomes false if it was true

Examples
========

.. code-block:: pepitoCode

   Boolean myBoolean = true;
   Boolean resultAnd = myBoolean.And(false);  // resultAnd is false
   Boolean resultOr = myBoolean.Or(false);  // resultOr is true
   Boolean resultNot = myBoolean.Not();  // resultNot is false
   Boolean resultXor = myBoolean.Xor(true);  // resultXor is false
   Boolean isEqual = myBoolean.Equals(true);  // isEqual is true
   Int comparison = myBoolean.CompareTo(false);  // comparison is 1
   String boolString = myBoolean.ToString();  // boolString is "true"
   myBoolean.Toggle();  // myBoolean becomes false

Advanced Features
=================

**Operator Overloading**

    In `pepitoCode`, you can overload operators for the `Boolean` type to make logical operations more intuitive.

    .. code-block:: pepitoCode

       Boolean a = true;
       Boolean b = false;
       Boolean resultAnd = a && b;  // resultAnd is false
       Boolean resultOr = a || b;  // resultOr is true
       Boolean resultNot = !a;  // resultNot is false

Interoperability
================

**Casting**

    You can cast `Boolean` to other types, typically `Int` (with `false` as 0 and `true` as 1) and vice versa.

    .. code-block:: pepitoCode

       Int myInt = (Int) myBoolean;  // myInt is 1 if myBoolean is true
       Boolean myBoolean = (Boolean) 1;  // myBoolean is true if 1 is non-zero
