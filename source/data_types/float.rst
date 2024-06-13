=====
Float
=====

Definition
==========

The `Float` type represents single-precision floating-point numbers, suitable for a wide range of mathematical calculations requiring moderate precision.

Syntax
======

.. code-block:: pepitoCode

   Float myFloat = 3.14;

Properties
==========

- **Precision:** Approximately 6-9 decimal digits.
- **Default Value:** 0.0
- **Size:** 32 bits (4 bytes)

Methods
=======

Arithmetic Methods
------------------

**Add(Float other)**

    Adds another float to this float and returns the result.

    .. code-block:: pepitoCode

       Float sum = myFloat.Add(2.71);

**Subtract(Float other)**

    Subtracts another float from this float and returns the result.

    .. code-block:: pepitoCode

       Float difference = myFloat.Subtract(1.41);

**Multiply(Float other)**

    Multiplies this float by another float and returns the result.

    .. code-block:: pepitoCode

       Float product = myFloat.Multiply(2.0);

**Divide(Float other)**

    Divides this float by another float and returns the result.

    .. code-block:: pepitoCode

       Float quotient = myFloat.Divide(1.5);

**Modulo(Float other)**

    Returns the remainder of the division of this float by another float.

    .. code-block:: pepitoCode

       Float remainder = myFloat.Modulo(1.2);

**Negate()**

    Returns the negation of this float.

    .. code-block:: pepitoCode

       Float negative = myFloat.Negate();

**Pow(Float exponent)**

    Raises the float to the specified power.

    .. code-block:: pepitoCode

       Float power = myFloat.Pow(2.0);

Comparison Methods
------------------

**Equals(Float other)**

    Checks if this float is equal to another float.

    .. code-block:: pepitoCode

       Boolean isEqual = myFloat.Equals(3.14);

**CompareTo(Float other)**

    Compares this float to another float (returns -1 if less, 0 if equal, 1 if greater).

    .. code-block:: pepitoCode

       Int comparison = myFloat.CompareTo(2.71);

**GreaterThan(Float other)**

    Checks if this float is greater than another float.

    .. code-block:: pepitoCode

       Boolean isGreaterThan = myFloat.GreaterThan(1.0);

**LessThan(Float other)**

    Checks if this float is less than another float.

    .. code-block:: pepitoCode

       Boolean isLessThan = myFloat.LessThan(4.0);

**GreaterThanOrEqual(Float other)**

    Checks if this float is greater than or equal to another float.

    .. code-block:: pepitoCode

       Boolean isGreaterThanOrEqual = myFloat.GreaterThanOrEqual(3.0);

**LessThanOrEqual(Float other)**

    Checks if this float is less than or equal to another float.

    .. code-block:: pepitoCode

       Boolean isLessThanOrEqual = myFloat.LessThanOrEqual(3.5);

Conversion Methods
------------------

**ToString()**

    Converts the float to its string representation.

    .. code-block:: pepitoCode

       String floatString = myFloat.ToString();

**ToInt()**

    Converts the float to an integer (truncates the decimal part).

    .. code-block:: pepitoCode

       Int myInt = myFloat.ToInt();

**ToDouble()**

    Converts the float to a double-precision floating-point number.

    .. code-block:: pepitoCode

       Double myDouble = myFloat.ToDouble();

**ToBoolean()**

    Converts the float to a boolean value (0.0 as false, non-zero as true).

    .. code-block:: pepitoCode

       Boolean myBoolean = myFloat.ToBoolean();

Utility Methods
---------------

**Abs()**

    Returns the absolute value of the float.

    .. code-block:: pepitoCode

       Float absValue = myFloat.Abs();

**Clamp(Float min, Float max)**

    Clamps the float value to be within the specified range.

    .. code-block:: pepitoCode

       Float clampedValue = myFloat.Clamp(0.0, 1.0);

**Round(Int decimals)**

    Rounds the float to the specified number of decimal places.

    .. code-block:: pepitoCode

       Float roundedValue = myFloat.Round(2);

Error Handling
==============

**Overflow**

    If an operation results in a value outside the representable range of `Float`, an overflow error is raised.

    .. code-block:: pepitoCode

       try {
           Float largeValue = 1e38;
           Float overflowValue = largeValue.Multiply(1e38);
       } catch (OverflowException e) {
           // Handle overflow error
       }

**Underflow**

    If an operation results in a value too small to be represented as a `Float`, an underflow error is raised.

    .. code-block:: pepitoCode

       try {
           Float smallValue = 1e-38;
           Float underflowValue = smallValue.Divide(1e38);
       } catch (UnderflowException e) {
           // Handle underflow error
       }

Examples
========

.. code-block:: pepitoCode

   Float myFloat = 3.14;
   Float absValue = myFloat.Abs();  // absValue is 3.14
   String floatString = myFloat.ToString();  // floatString is "3.14"
   Float sum = myFloat.Add(2.71);  // sum is 5.85
   Float difference = myFloat.Subtract(1.41);  // difference is 1.73
   Float product = myFloat.Multiply(2.0);  // product is 6.28
   Float quotient = myFloat.Divide(1.5);  // quotient is 2.0933333
   Float remainder = myFloat.Modulo(1.2);  // remainder is 0.74
   Float negative = myFloat.Negate();  // negative is -3.14
   Boolean isEqual = myFloat.Equals(3.14);  // isEqual is true
   Int comparison = myFloat.CompareTo(2.71);  // comparison is 1
   Boolean isGreaterThan = myFloat.GreaterThan(1.0);  // isGreaterThan is true
   Boolean isLessThan = myFloat.LessThan(4.0);  // isLessThan is true
   Boolean isGreaterThanOrEqual = myFloat.GreaterThanOrEqual(3.0);  // isGreaterThanOrEqual is true
   Boolean isLessThanOrEqual = myFloat.LessThanOrEqual(3.5);  // isLessThanOrEqual is true
   Int myInt = myFloat.ToInt();  // myInt is 3
   Double myDouble = myFloat.ToDouble();  // myDouble is 3.14
   Boolean myBoolean = myFloat.ToBoolean();  // myBoolean is true
   Float power = myFloat.Pow(2.0);  // power is 9.8596
   Float clampedValue = myFloat.Clamp(0.0, 1.0);  // clampedValue is 1.0
   Float roundedValue = myFloat.Round(2);  // roundedValue is 3.14

Advanced Features
=================

**Operator Overloading**

    In `pepitoCode`, you can overload operators for the `Float` type to make arithmetic operations more intuitive.

    .. code-block:: pepitoCode

       Float a = 3.0;
       Float b = 1.5;
       Float sum = a + b;  // sum is 4.5
       Float product = a * b;  // product is 4.5

Interoperability
================

**Casting**

    You can cast `Float` to other numeric types and vice versa.

    .. code-block:: pepitoCode

       Int myInt = (Int) myFloat;
       Double myDouble = (Double) myFloat;
