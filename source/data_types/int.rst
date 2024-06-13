===
Int
===

Definition
==========

The `Int` type represents 32-bit integer numbers, suitable for a wide range of arithmetic operations and general-purpose usage.

Syntax
======

.. code-block:: pepitoCode

   Int myInt = 2;

Properties
==========

- **Range:** -2^31 to 2^31-1 (−2147483648 to 2147483647).
- **Default Value:** 0
- **Size:** 32 bits (4 bytes)

Methods
=======

Arithmetic Methods
------------------

**Add(Int other)**

    Adds another integer to this integer and returns the result.

    .. code-block:: pepitoCode

       Int sum = myInt.Add(5);

**Subtract(Int other)**

    Subtracts another integer from this integer and returns the result.

    .. code-block:: pepitoCode

       Int difference = myInt.Subtract(3);

**Multiply(Int other)**

    Multiplies this integer by another integer and returns the result.

    .. code-block:: pepitoCode

       Int product = myInt.Multiply(4);

**Divide(Int other)**

    Divides this integer by another integer and returns the result.

    .. code-block:: pepitoCode

       Int quotient = myInt.Divide(2);

**Modulo(Int other)**

    Returns the remainder of the division of this integer by another integer.

    .. code-block:: pepitoCode

       Int remainder = myInt.Modulo(3);

**Negate()**

    Returns the negation of this integer.

    .. code-block:: pepitoCode

       Int negative = myInt.Negate();

**Pow(Int exponent)**

    Raises the integer to the specified power.

    .. code-block:: pepitoCode

       Int power = myInt.Pow(3);  // If myInt is 5, power will be 125

Comparison Methods
------------------

**Equals(Int other)**

    Checks if this integer is equal to another integer.

    .. code-block:: pepitoCode

       Boolean isEqual = myInt.Equals(2);

**CompareTo(Int other)**

    Compares this integer to another integer (returns -1 if less, 0 if equal, 1 if greater).

    .. code-block:: pepitoCode

       Int comparison = myInt.CompareTo(3);

**GreaterThan(Int other)**

    Checks if this integer is greater than another integer.

    .. code-block:: pepitoCode

       Boolean isGreaterThan = myInt.GreaterThan(1);

**LessThan(Int other)**

    Checks if this integer is less than another integer.

    .. code-block:: pepitoCode

       Boolean isLessThan = myInt.LessThan(5);

**GreaterThanOrEqual(Int other)**

    Checks if this integer is greater than or equal to another integer.

    .. code-block:: pepitoCode

       Boolean isGreaterThanOrEqual = myInt.GreaterThanOrEqual(2);

**LessThanOrEqual(Int other)**

    Checks if this integer is less than or equal to another integer.

    .. code-block:: pepitoCode

       Boolean isLessThanOrEqual = myInt.LessThanOrEqual(4);

Conversion Methods
------------------

**ToString()**

    Converts the integer to its string representation.

    .. code-block:: pepitoCode

       String intString = myInt.ToString();

**ToFloat()**

    Converts the integer to a floating-point number.

    .. code-block:: pepitoCode

       Float myFloat = myInt.ToFloat();

**ToDouble()**

    Converts the integer to a double-precision floating-point number.

    .. code-block:: pepitoCode

       Double myDouble = myInt.ToDouble();

**ToBoolean()**

    Converts the integer to a boolean value (0 as false, non-zero as true).

    .. code-block:: pepitoCode

       Boolean myBoolean = myInt.ToBoolean();

Utility Methods
---------------

**Abs()**

    Returns the absolute value of the integer.

    .. code-block:: pepitoCode

       Int absValue = myInt.Abs();

**Clamp(Int min, Int max)**

    Clamps the integer value to be within the specified range.

    .. code-block:: pepitoCode

       Int clampedValue = myInt.Clamp(0, 10);

**IsEven()**

    Checks if the integer is even.

    .. code-block:: pepitoCode

       Boolean isEven = myInt.IsEven();

**IsOdd()**

    Checks if the integer is odd.

    .. code-block:: pepitoCode

       Boolean isOdd = myInt.IsOdd();

Error Handling
==============

**Overflow**

    If an operation results in a value outside the range of `Int`, an overflow error is raised.

    .. code-block:: pepitoCode

       try {
           Int largeValue = 2147483647;
           Int overflowValue = largeValue.Add(1);
       } catch (OverflowException e) {
           // Handle overflow error
       }

Examples
========

.. code-block:: pepitoCode

   Int myInt = 2;
   Int absValue = myInt.Abs();  // absValue is 2
   String intString = myInt.ToString();  // intString is "2"
   Int sum = myInt.Add(3);  // sum is 5
   Int difference = myInt.Subtract(1);  // difference is 1
   Int product = myInt.Multiply(4);  // product is 8
   Int quotient = myInt.Divide(2);  // quotient is 1
   Int remainder = myInt.Modulo(3);  // remainder is 2
   Int negative = myInt.Negate();  // negative is -2
   Boolean isEqual = myInt.Equals(2);  // isEqual is true
   Int comparison = myInt.CompareTo(3);  // comparison is -1
   Boolean isGreaterThan = myInt.GreaterThan(1);  // isGreaterThan is true
   Boolean isLessThan = myInt.LessThan(5);  // isLessThan is true
   Boolean isGreaterThanOrEqual = myInt.GreaterThanOrEqual(2);  // isGreaterThanOrEqual is true
   Boolean isLessThanOrEqual = myInt.LessThanOrEqual(4);  // isLessThanOrEqual is true
   Float myFloat = myInt.ToFloat();  // myFloat is 2.0
   Double myDouble = myInt.ToDouble();  // myDouble is 2.0
   Boolean myBoolean = myInt.ToBoolean();  // myBoolean is true
   Int power = myInt.Pow(3);  // power is 8
   Int clampedValue = myInt.Clamp(0, 10);  // clampedValue is 2
   Boolean isEven = myInt.IsEven();  // isEven is true
   Boolean isOdd = myInt.IsOdd();  // isOdd is false

Advanced Features
=================

**Operator Overloading**

    In `pepitoCode`, you can overload operators for the `Int` type to make arithmetic operations more intuitive.

    .. code-block:: pepitoCode

       Int a = 5;
       Int b = 3;
       Int sum = a + b;  // sum is 8
       Int product = a * b;  // product is 15

Interoperability
================

**Casting**

    You can cast `Int` to other numeric types and vice versa.

    .. code-block:: pepitoCode

       Float myFloat = (Float) myInt;
       Double myDouble = (Double) myInt;
