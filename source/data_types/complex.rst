=======
Complex
=======

Definition
==========

The `Complex` type represents a complex number with a real part and an imaginary part. It is used for mathematical computations involving complex numbers.

Syntax
======

.. code-block:: pepitoCode

   Complex myComplex = Complex(2, 3);  // Represents the complex number 2 + 3i

Properties
==========

- **Real:** The real part of the complex number.
- **Imaginary:** The imaginary part of the complex number.
- **Default Value:** `0 + 0i`

Methods
=======

Arithmetic Methods
------------------

**Add(Complex other)**

    Adds another complex number to this complex number and returns the result.

    .. code-block:: pepitoCode

       Complex result = myComplex.Add(Complex(1, 1));  // result is 3 + 4i

**Subtract(Complex other)**

    Subtracts another complex number from this complex number and returns the result.

    .. code-block:: pepitoCode

       Complex result = myComplex.Subtract(Complex(1, 1));  // result is 1 + 2i

**Multiply(Complex other)**

    Multiplies this complex number by another complex number and returns the result.

    .. code-block:: pepitoCode

       Complex result = myComplex.Multiply(Complex(1, 1));  // result is -1 + 5i

**Divide(Complex other)**

    Divides this complex number by another complex number and returns the result.

    .. code-block:: pepitoCode

       Complex result = myComplex.Divide(Complex(1, 1));  // result is 2.5 + 0.5i

Utility Methods
---------------

**Conjugate()**

    Returns the complex conjugate of this complex number.

    .. code-block:: pepitoCode

       Complex conjugate = myComplex.Conjugate();  // conjugate is 2 - 3i

**Magnitude()**

    Returns the magnitude (absolute value) of the complex number.

    .. code-block:: pepitoCode

       Double magnitude = myComplex.Magnitude();  // magnitude is sqrt(13)

**Phase()**

    Returns the phase (argument) of the complex number in radians.

    .. code-block:: pepitoCode

       Double phase = myComplex.Phase();  // phase is atan2(3, 2)

**ToString()**

    Converts the complex number to its string representation.

    .. code-block:: pepitoCode

       String complexString = myComplex.ToString();  // complexString is "2 + 3i"

Examples
========

.. code-block:: pepitoCode

   Complex myComplex = Complex(2, 3);  // Represents the complex number 2 + 3i
   Complex resultAdd = myComplex.Add(Complex(1, 1));  // resultAdd is 3 + 4i
   Complex resultSubtract = myComplex.Subtract(Complex(1, 1));  // resultSubtract is 1 + 2i
   Complex resultMultiply = myComplex.Multiply(Complex(1, 1));  // resultMultiply is -1 + 5i
   Complex resultDivide = myComplex.Divide(Complex(1, 1));  // resultDivide is 2.5 + 0.5i
   Complex conjugate = myComplex.Conjugate();  // conjugate is 2 - 3i
   Double magnitude = myComplex.Magnitude();  // magnitude is sqrt(13)
   Double phase = myComplex.Phase();  // phase is atan2(3, 2)
   String complexString = myComplex.ToString();  // complexString is "2 + 3i"

Advanced Features
=================

**Complex Arithmetic**

    The `Complex` type supports advanced arithmetic operations involving complex numbers.

    .. code-block:: pepitoCode

       Complex a = Complex(1, 2);
       Complex b = Complex(3, 4);
       Complex sum = a + b;  // sum is 4 + 6i
       Complex product = a * b;  // product is -5 + 10i

Interoperability
================

**Casting**

    You can cast `Complex` to other numeric types if the imaginary part is zero, or vice versa.

    .. code-block:: pepitoCode

       Double realPart = (Double) myComplex.Real;
       Double imaginaryPart = (Double) myComplex.Imaginary;
       Complex fromReal = (Complex) 5;  // Represents the complex number 5 + 0i
