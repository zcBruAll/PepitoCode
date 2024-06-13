======
Double
======

Definition
==========

The `Double` type represents double-precision floating-point numbers, suitable for a wide range of mathematical calculations requiring greater precision than `Float`.

Syntax
======

.. code-block:: pepitoCode

   Double myDouble = 3.141592653589793;

Properties
==========

- **Precision:** Approximately 15-17 decimal digits.
- **Default Value:** 0.0
- **Size:** 64 bits (8 bytes)

Methods
=======

Arithmetic Methods
------------------

**Add(Double other)**

    Adds another double to this double and returns the result.

    .. code-block:: pepitoCode

       Double sum = myDouble.Add(2.718281828459045);

**Subtract(Double other)**

    Subtracts another double from this double and returns the result.

    .. code-block:: pepitoCode

       Double difference = myDouble.Subtract(1.414213562373095);

**Multiply(Double other)**

    Multiplies this double by another double and returns the result.

    .. code-block:: pepitoCode

       Double product = myDouble.Multiply(2.0);

**Divide(Double other)**

    Divides this double by another double and returns the result.

    .. code-block:: pepitoCode

       Double quotient = myDouble.Divide(1.5);

**Modulo(Double other)**

    Returns the remainder of the division of this double by another double.

    .. code-block:: pepitoCode

       Double remainder = myDouble.Modulo(1.2);

**Negate()**

    Returns the negation of this double.

    .. code-block:: pepitoCode

       Double negative = myDouble.Negate();

**Pow(Double exponent)**

    Raises the double to the specified power.

    .. code-block:: pepitoCode

       Double power = myDouble.Pow(2.0);

Comparison Methods
------------------

**Equals(Double other)**

    Checks if this double is equal to another double.

    .. code-block:: pepitoCode

       Boolean isEqual = myDouble.Equals(3.141592653589793);

**CompareTo(Double other)**

    Compares this double to another double (returns -1 if less, 0 if equal, 1 if greater).

    .. code-block:: pepitoCode

       Int comparison = myDouble.CompareTo(2.718281828459045);

**GreaterThan(Double other)**

    Checks if this double is greater than another double.

    .. code-block:: pepitoCode

       Boolean isGreaterThan = myDouble.GreaterThan(1.0);

**LessThan(Double other)**

    Checks if this double is less than another double.

    .. code-block:: pepitoCode

       Boolean isLessThan = myDouble.LessThan(4.0);

**GreaterThanOrEqual(Double other)**

    Checks if this double is greater than or equal to another double.

    .. code-block:: pepitoCode

       Boolean isGreaterThanOrEqual = myDouble.GreaterThanOrEqual(3.0);

**LessThanOrEqual(Double other)**

    Checks if this double is less than or equal to another double.

    .. code-block:: pepitoCode

       Boolean isLessThanOrEqual = myDouble.LessThanOrEqual(3.5);

Conversion Methods
------------------

**ToString()**

    Converts the double to its string representation.

    .. code-block:: pepitoCode

       String doubleString = myDouble.ToString();

**ToInt()**

    Converts the double to an integer (truncates the decimal part).

    .. code-block:: pepitoCode

       Int myInt = myDouble.ToInt();

**ToFloat()**

    Converts the double to a floating-point number with single precision.

    .. code-block:: pepitoCode

       Float myFloat = myDouble.ToFloat();

**ToBoolean()**

    Converts the double to a boolean value (0.0 as false, non-zero as true).

    .. code-block:: pepitoCode

       Boolean myBoolean = myDouble.ToBoolean();

Utility Methods
---------------

**Abs()**

    Returns the absolute value of the double.

    .. code-block:: pepitoCode

       Double absValue = myDouble.Abs();

**Clamp(Double min, Double max)**

    Clamps the double value to be within the specified range.

    .. code-block:: pepitoCode

       Double clampedValue = myDouble.Clamp(0.0, 1.0);

**Round(Int decimals)**

    Rounds the double to the specified number of decimal places.

    .. code-block:: pepitoCode

       Double roundedValue = myDouble.Round(2);

Error Handling
==============

**Overflow**

    If an operation results in a value outside the representable range of `Double`, an overflow error is raised.

    .. code-block:: pepitoCode

       try {
           Double largeValue = 1e308;
           Double overflowValue = largeValue.Multiply(1e308);
       } catch (OverflowException e) {
           // Handle overflow error
       }

**Underflow**

    If an operation results in a value too small to be represented as a `Double`, an underflow error is raised.

    .. code-block:: pepitoCode

       try {
           Double smallValue = 1e-308;
           Double underflowValue = smallValue.Divide(1e308);
       } catch (UnderflowException e) {
           // Handle underflow error
       }

Examples
========

.. code-block:: pepitoCode

   Double myDouble = 3.141592653589793;
   Double absValue = myDouble.Abs();  // absValue is 3.141592653589793
   String doubleString = myDouble.ToString();  // doubleString is "3.141592653589793"
   Double sum = myDouble.Add(2.718281828459045);  // sum is 5.859874482048838
   Double difference = myDouble.Subtract(1.414213562373095);  // difference is 1.727379091216698
   Double product = myDouble.Multiply(2.0);  // product is 6.283185307179586
   Double quotient = myDouble.Divide(1.5);  // quotient is 2.094395102393195
   Double remainder = myDouble.Modulo(1.2);  // remainder is 0.941592653589793
   Double negative = myDouble.Negate();  // negative is -3.141592653589793
   Boolean isEqual = myDouble.Equals(3.141592653589793);  // isEqual is true
   Int comparison = myDouble.CompareTo(2.718281828459045);  // comparison is 1
   Boolean isGreaterThan = myDouble.GreaterThan(1.0);  // isGreaterThan is true
   Boolean isLessThan = myDouble.LessThan(4.0);  // isLessThan is true
   Boolean isGreaterThanOrEqual = myDouble.GreaterThanOrEqual(3.0);  // isGreaterThanOrEqual is true
   Boolean isLessThanOrEqual = myDouble.LessThanOrEqual(3.5);  // isLessThanOrEqual is true
   Int myInt = myDouble.ToInt();  // myInt is 3
   Float myFloat = myDouble.ToFloat();  // myFloat is 3.1415927
   Boolean myBoolean = myDouble.ToBoolean();  // myBoolean is true
   Double power = myDouble.Pow(2.0);  // power is 9.869604401089358
   Double clampedValue = myDouble.Clamp(0.0, 1.0);  // clampedValue is 1.0
   Double roundedValue = myDouble.Round(2);  // roundedValue is 3.14

Advanced Features
=================

**Operator Overloading**

    In `pepitoCode`, you can overload operators for the `Double` type to make arithmetic operations more intuitive.

    .. code-block:: pepitoCode

       Double a = 3.0;
       Double b = 1.5;
       Double sum = a + b;  // sum is 4.5
       Double product = a * b;  // product is 4.5

Interoperability
================

**Casting**

    You can cast `Double` to other numeric types and vice versa.

    .. code-block:: pepitoCode

       Int myInt = (Int) myDouble;
       Float myFloat = (Float) myDouble;
