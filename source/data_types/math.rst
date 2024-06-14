====
Math
====

Definition
==========

The `Math` type provides a collection of static methods for performing various mathematical operations, such as logarithms, trigonometric functions, and exponentiation.

Syntax
======

.. code-block:: pepitoCode

   Int result = Math.Log(10, 2);

Methods
=======

Logarithmic Functions
---------------------

**Log(Double value, Double base)**

    Calculates the logarithm of a given value with the specified base.

    .. code-block:: pepitoCode

       Double logResult = Math.Log(10, 2);  // logResult is approximately 3.32193

**Ln(Double value)**

    Calculates the natural logarithm (base e) of a given value.

    .. code-block:: pepitoCode

       Double lnResult = Math.Ln(2.71828);  // lnResult is approximately 1

Exponential Functions
---------------------

**Exp(Double value)**

    Calculates e raised to the power of the given value.

    .. code-block:: pepitoCode

       Double expResult = Math.Exp(1);  // expResult is approximately 2.71828

**Pow(Double base, Double exponent)**

    Calculates the base raised to the power of the exponent.

    .. code-block:: pepitoCode

       Double powResult = Math.Pow(2, 3);  // powResult is 8

Trigonometric Functions
-----------------------

**Sin(Double angle)**

    Calculates the sine of the specified angle (in radians).

    .. code-block:: pepitoCode

       Double sinResult = Math.Sin(Math.PI / 2);  // sinResult is 1

**Cos(Double angle)**

    Calculates the cosine of the specified angle (in radians).

    .. code-block:: pepitoCode

       Double cosResult = Math.Cos(0);  // cosResult is 1

**Tan(Double angle)**

    Calculates the tangent of the specified angle (in radians).

    .. code-block:: pepitoCode

       Double tanResult = Math.Tan(Math.PI / 4);  // tanResult is 1

**Asin(Double value)**

    Calculates the arcsine of the specified value, returning an angle in radians.

    .. code-block:: pepitoCode

       Double asinResult = Math.Asin(1);  // asinResult is approximately Math.PI / 2

**Acos(Double value)**

    Calculates the arccosine of the specified value, returning an angle in radians.

    .. code-block:: pepitoCode

       Double acosResult = Math.Acos(1);  // acosResult is 0

**Atan(Double value)**

    Calculates the arctangent of the specified value, returning an angle in radians.

    .. code-block:: pepitoCode

       Double atanResult = Math.Atan(1);  // atanResult is approximately Math.PI / 4

Utility Methods
---------------

**PI**

    Returns the value of π (approximately 3.14159).

    .. code-block:: pepitoCode

       Double pi = Math.PI;  // pi is 3.14159...

**E**

    Returns the value of e (approximately 2.71828).

    .. code-block:: pepitoCode

       Double e = Math.E;  // e is 2.71828...

Examples
========

.. code-block:: pepitoCode

   Double logResult = Math.Log(10, 2);  // logResult is approximately 3.32193
   Double lnResult = Math.Ln(2.71828);  // lnResult is approximately 1
   Double expResult = Math.Exp(1);  // expResult is approximately 2.71828
   Double powResult = Math.Pow(2, 3);  // powResult is 8
   Double sinResult = Math.Sin(Math.PI / 2);  // sinResult is 1
   Double cosResult = Math.Cos(0);  // cosResult is 1
   Double tanResult = Math.Tan(Math.PI / 4);  // tanResult is 1
   Double asinResult = Math.Asin(1);  // asinResult is approximately Math.PI / 2
   Double acosResult = Math.Acos(1);  // acosResult is 0
   Double atanResult = Math.Atan(1);  // atanResult is approximately Math.PI / 4
   Double pi = Math.PI;  // pi is 3.14159...
   Double e = Math.E;  // e is 2.71828...

Interoperability
================

**Using with Other Types**

    The `Math` type can be used with other numeric types in `pepitoCode`.

    .. code-block:: pepitoCode

       Int intResult = Math.Pow(2, 3);  // intResult is 8
       Float floatResult = Math.Sin(1.0);  // floatResult is approximately 0.84147
       Double doubleResult = Math.Exp(1);  // doubleResult is approximately 2.71828
