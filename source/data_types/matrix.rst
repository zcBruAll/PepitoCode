========
Matrix<T>
========

Definition
==========

The `Matrix<T>` type represents a two-dimensional array of elements of type `T`, providing various methods to manipulate and perform operations on the matrix. It is commonly used for mathematical computations and operations in multi-dimensional space.

Syntax
======

.. code-block:: pepitoCode

   Matrix<Int> myMatrix = Matrix<Int>(3, 3);  // Creates a 3x3 matrix of integers

Properties
==========

- **Rows:** The number of rows in the matrix.
- **Columns:** The number of columns in the matrix.
- **Default Value:** A matrix with all elements initialized to the default value of `T`.

Methods
=======

Manipulation Methods
---------------------

**Set(Int row, Int column, T element)**

    Sets the element at the specified row and column.

    .. code-block:: pepitoCode

       myMatrix.Set(0, 0, 5);  // Sets the element at (0,0) to 5

**Get(Int row, Int column)**

    Returns the element at the specified row and column.

    .. code-block:: pepitoCode

       Int element = myMatrix.Get(0, 0);  // Gets the element at (0,0), which is 5

**Add(Matrix<T> other)**

    Adds another matrix to this matrix element-wise and returns the result.

    .. code-block:: pepitoCode

       Matrix<Int> result = myMatrix.Add(otherMatrix);  // Adds otherMatrix to myMatrix

**Subtract(Matrix<T> other)**

    Subtracts another matrix from this matrix element-wise and returns the result.

    .. code-block:: pepitoCode

       Matrix<Int> result = myMatrix.Subtract(otherMatrix);  // Subtracts otherMatrix from myMatrix

**Multiply(Matrix<T> other)**

    Multiplies this matrix with another matrix using matrix multiplication and returns the result.

    .. code-block:: pepitoCode

       Matrix<Int> result = myMatrix.Multiply(otherMatrix);  // Multiplies myMatrix with otherMatrix

**ScalarMultiply(T scalar)**

    Multiplies each element of the matrix by the specified scalar value.

    .. code-block:: pepitoCode

       myMatrix.ScalarMultiply(2);  // Multiplies each element of myMatrix by 2

**Transpose()**

    Returns the transpose of the matrix.

    .. code-block:: pepitoCode

       Matrix<Int> transposed = myMatrix.Transpose();  // Transposes myMatrix

Utility Methods
---------------

**RowsCount()**

    Returns the number of rows in the matrix.

    .. code-block:: pepitoCode

       Int rows = myMatrix.RowsCount();  // rows is 3

**ColumnsCount()**

    Returns the number of columns in the matrix.

    .. code-block:: pepitoCode

       Int columns = myMatrix.ColumnsCount();  // columns is 3

**IsSquare()**

    Checks if the matrix is square (i.e., the number of rows is equal to the number of columns).

    .. code-block:: pepitoCode

       Boolean isSquare = myMatrix.IsSquare();  // isSquare is true

Examples
========

.. code-block:: pepitoCode

   Matrix<Int> myMatrix = Matrix<Int>(3, 3);  // Creates a 3x3 matrix
   myMatrix.Set(0, 0, 5);  // Sets the element at (0,0) to 5
   Int element = myMatrix.Get(0, 0);  // Gets the element at (0,0), which is 5
   Matrix<Int> otherMatrix = Matrix<Int>(3, 3);
   otherMatrix.Set(0, 0, 2);
   Matrix<Int> resultAdd = myMatrix.Add(otherMatrix);  // Adds otherMatrix to myMatrix
   Matrix<Int> resultSubtract = myMatrix.Subtract(otherMatrix);  // Subtracts otherMatrix from myMatrix
   Matrix<Int> resultMultiply = myMatrix.Multiply(otherMatrix);  // Multiplies myMatrix with otherMatrix
   myMatrix.ScalarMultiply(2);  // Multiplies each element of myMatrix by 2
   Matrix<Int> transposed = myMatrix.Transpose();  // Transposes myMatrix
   Int rows = myMatrix.RowsCount();  // rows is 3
   Int columns = myMatrix.ColumnsCount();  // columns is 3
   Boolean isSquare = myMatrix.IsSquare();  // isSquare is true

Advanced Features
=================

**Generic Methods**

    The `Matrix<T>` type supports generic methods, allowing for type-safe operations on the elements.

    .. code-block:: pepitoCode

       Matrix<String> stringMatrix = Matrix<String>(2, 2);
       stringMatrix.Set(0, 0, "Hello");
       stringMatrix.Set(1, 1, "World");

Interoperability
================

**Casting**

    You can cast `Matrix<T>.Col()` or `Matrix<T>.Row()` to other collection types if they are compatible.

    .. code-block:: pepitoCode

       Matrix<Int> intMatrix = Matrix<Int>(3, 3);
       List<Int> intList = intMatrix.Col(0);
       Vector<Int> intVector = intMatrix.Row(2);
