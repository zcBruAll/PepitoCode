====
Char
====

Definition
==========

The `Char` type represents a single character. It can be used for text manipulation and mathematical operations involving characters.

Syntax
======

.. code-block:: pepitoCode

   Char myChar = 'A';

Properties
==========

- **Value:** The character value.
- **Default Value:** `'\0'` (the null character).

Methods
=======

Character Manipulation Methods
------------------------------

**ToUpper()**

    Converts the character to its uppercase equivalent.

    .. code-block:: pepitoCode

       Char upper = myChar.ToUpper();  // upper is 'A' if myChar is 'a'

**ToLower()**

    Converts the character to its lowercase equivalent.

    .. code-block:: pepitoCode

       Char lower = myChar.ToLower();  // lower is 'a' if myChar is 'A'

**IsDigit()**

    Checks if the character is a digit.

    .. code-block:: pepitoCode

       Boolean isDigit = myChar.IsDigit();  // isDigit is true if myChar is '0' to '9'

**IsLetter()**

    Checks if the character is a letter.

    .. code-block:: pepitoCode

       Boolean isLetter = myChar.IsLetter();  // isLetter is true if myChar is 'A' to 'Z' or 'a' to 'z'

**IsUpper()**

    Checks if the character is an uppercase letter.

    .. code-block:: pepitoCode

       Boolean isUpper = myChar.IsUpper();  // isUpper is true if myChar is 'A' to 'Z'

**IsLower()**

    Checks if the character is a lowercase letter.

    .. code-block:: pepitoCode

       Boolean isLower = myChar.IsLower();  // isLower is true if myChar is 'a' to 'z'

**ToString()**

    Converts the character to its string representation.

    .. code-block:: pepitoCode

       String charString = myChar.ToString();  // charString is "A"

Mathematical Methods
--------------------

**Add(Char other)**

    Concatenates this character with another character and returns the result as a string.

    .. code-block:: pepitoCode

       String result = myChar.Add('B');  // result is "A+B"

**Multiply(Int times)**

    Multiplies this character by the specified integer, resulting in a string where the character appears in a mathematical notation.

    .. code-block:: pepitoCode

       String result = myChar.Multiply(3);  // result is "3A" if myChar is 'A'

Examples
========

.. code-block:: pepitoCode

   Char myChar = 'A';
   Char upper = myChar.ToUpper();  // upper is 'A'
   Char lower = myChar.ToLower();  // lower is 'a'
   Boolean isDigit = myChar.IsDigit();  // isDigit is false
   Boolean isLetter = myChar.IsLetter();  // isLetter is true
   Boolean isUpper = myChar.IsUpper();  // isUpper is true
   Boolean isLower = myChar.IsLower();  // isLower is false
   String charString = myChar.ToString();  // charString is "A"
   String resultAdd = myChar.Add('B');  // resultAdd is "A+B"
   String resultMultiply = myChar.Multiply(3);  // resultMultiply is "3A"

Advanced Features
=================

**Operator Overloading**

    In `pepitoCode`, you can overload operators for the `Char` type to make operations more intuitive.

    .. code-block:: pepitoCode

       Char a = 'A';
       Char b = 'B';
       String resultAdd = a + b;  // resultAdd is "A+B"
       String resultMultiply = a * 3;  // resultMultiply is "3A"

Interoperability
================

**Casting**

    You can cast `Char` to other types, typically `Int` (to get the ASCII value) and vice versa.

    .. code-block:: pepitoCode

       Int asciiValue = (Int) myChar;  // asciiValue is 65 if myChar is 'A'
       Char fromAscii = (Char) 65;  // fromAscii is 'A'
