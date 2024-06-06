Int
===

Definition
----------

The `Int` type represents integer numbers.

Syntax
------

.. code-block:: pepitoCode

   Int myInt = 2;

Properties
----------

- **Range:** Typically -2^31 to 2^31-1 (for 32-bit integers).
- **Default Value:** 0

Functions/Methods
-----------------

- **abs():** Returns the absolute value of the integer.

  .. code-block:: pepitoCode

     Int absValue = myInt.abs();

- **toString():** Converts the integer to a string.

  .. code-block:: pepitoCode

     String intString = myInt.toString();

- **add(Int other):** Adds another integer to this integer.

  .. code-block:: pepitoCode

     Int sum = myInt.add(5);

Examples
--------

.. code-block:: pepitoCode

   Int myInt = 2;
   Int absValue = myInt.abs();  // absValue is 2
   String intString = myInt.toString();  // intString is "2"
   Int sum = myInt.add(3);  // sum is 5
