======
String
======

Definition
==========

The `String` type represents a sequence of characters, used for storing and manipulating text.

Syntax
======

.. code-block:: pepitoCode

   String myString = "Hello, World!";

Properties
==========

- **Length:** Number of characters in the string.
- **Default Value:** `""` (an empty string)

Methods
=======

String Manipulation Methods
----------------------------

**Concat(String other)**

    Concatenates this string with another string and returns the result.

    .. code-block:: pepitoCode

       String result = myString.Concat(" How are you?");  // result is "Hello, World! How are you?"

**SubString(Int start, Int length)**

    Returns a substring starting from the specified position with the specified length.

    .. code-block:: pepitoCode

       String sub = myString.SubString(7, 5);  // sub is "World"

**Replace(String oldValue, String newValue)**

    Replaces all occurrences of a specified string in this string with another string.

    .. code-block:: pepitoCode

       String replaced = myString.Replace("World", "Pepito");  // replaced is "Hello, Pepito!"

**ToLower()**

    Converts all characters in the string to lowercase.

    .. code-block:: pepitoCode

       String lower = myString.ToLower();  // lower is "hello, world!"

**ToUpper()**

    Converts all characters in the string to uppercase.

    .. code-block:: pepitoCode

       String upper = myString.ToUpper();  // upper is "HELLO, WORLD!"

**Trim()**

    Removes leading and trailing whitespace from the string.

    .. code-block:: pepitoCode

       String trimmed = myString.Trim();  // trimmed is "Hello, World!" if there were leading or trailing spaces

**Split(Char delimiter)**

    Splits the string into an array of substrings based on the specified delimiter.

    .. code-block:: pepitoCode

       List<String> parts = myString.Split(' ');  // parts are ["Hello,", "World!"]

**Join(List<String> parts)**

    Joins a list of strings into a single string with this string as the delimiter.

    .. code-block:: pepitoCode

       String joined = ", ".Join(parts);  // joined is "Hello, World!"

**Contains(String value)**

    Checks if the string contains the specified value.

    .. code-block:: pepitoCode

       Boolean contains = myString.Contains("World");  // contains is true

**StartsWith(String value)**

    Checks if the string starts with the specified value.

    .. code-block:: pepitoCode

       Boolean startsWith = myString.StartsWith("Hello");  // startsWith is true

**EndsWith(String value)**

    Checks if the string ends with the specified value.

    .. code-block:: pepitoCode

       Boolean endsWith = myString.EndsWith("!");  // endsWith is true

**IndexOf(String value)**

    Returns the index of the first occurrence of the specified value, or -1 if not found.

    .. code-block:: pepitoCode

       Int index = myString.IndexOf("World");  // index is 7

**LastIndexOf(String value)**

    Returns the index of the last occurrence of the specified value, or -1 if not found.

    .. code-block:: pepitoCode

       Int lastIndex = myString.LastIndexOf("l");  // lastIndex is 9

Comparison Methods
------------------

**Equals(String other)**

    Checks if this string is equal to another string.

    .. code-block:: pepitoCode

       Boolean isEqual = myString.Equals("Hello, World!");  // isEqual is true

**CompareTo(String other)**

    Compares this string to another string lexicographically (returns -1 if less, 0 if equal, 1 if greater).

    .. code-block:: pepitoCode

       Int comparison = myString.CompareTo("Hello");  // comparison is 1

Conversion Methods
------------------

**ToInt()**

    Converts the string to an integer.

    .. code-block:: pepitoCode

       Int myInt = "123".ToInt();  // myInt is 123

**ToFloat()**

    Converts the string to a floating-point number.

    .. code-block:: pepitoCode

       Float myFloat = "123.45".ToFloat();  // myFloat is 123.45

**ToDouble()**

    Converts the string to a double-precision floating-point number.

    .. code-block:: pepitoCode

       Double myDouble = "123.45".ToDouble();  // myDouble is 123.45

**ToBoolean()**

    Converts the string to a boolean value (`"true"` as true, `"false"` as false).

    .. code-block:: pepitoCode

       Boolean myBoolean = "true".ToBoolean();  // myBoolean is true

Utility Methods
---------------

**Length()**

    Returns the length of the string.

    .. code-block:: pepitoCode

       Int length = myString.Length();  // length is 13 for "Hello, World!"

**IsEmpty()**

    Checks if the string is empty.

    .. code-block:: pepitoCode

       Boolean isEmpty = myString.IsEmpty();  // isEmpty is false

Examples
========

.. code-block:: pepitoCode

   String myString = "Hello, World!";
   String result = myString.Concat(" How are you?");  // result is "Hello, World! How are you?"
   String sub = myString.SubString(7, 5);  // sub is "World"
   String replaced = myString.Replace("World", "Pepito");  // replaced is "Hello, Pepito!"
   String lower = myString.ToLower();  // lower is "hello, world!"
   String upper = myString.ToUpper();  // upper is "HELLO, WORLD!"
   String trimmed = myString.Trim();  // trimmed is "Hello, World!" if there were leading or trailing spaces
   List<String> parts = myString.Split(' ');  // parts are ["Hello,", "World!"]
   String joined = ", ".Join(parts);  // joined is "Hello, World!"
   Boolean contains = myString.Contains("World");  // contains is true
   Boolean startsWith = myString.StartsWith("Hello");  // startsWith is true
   Boolean endsWith = myString.EndsWith("!");  // endsWith is true
   Int index = myString.IndexOf("World");  // index is 7
   Int lastIndex = myString.LastIndexOf("l");  // lastIndex is 9
   Boolean isEqual = myString.Equals("Hello, World!");  // isEqual is true
   Int comparison = myString.CompareTo("Hello");  // comparison is 1
   Int myInt = "123".ToInt();  // myInt is 123
   Float myFloat = "123.45".ToFloat();  // myFloat is 123.45
   Double myDouble = "123.45".ToDouble();  // myDouble is 123.45
   Boolean myBoolean = "true".ToBoolean();  // myBoolean is true
   Int length = myString.Length();  // length is 13 for "Hello, World!"
   Boolean isEmpty = myString.IsEmpty();  // isEmpty is false

Advanced Features
=================

**Operator Overloading**

    In `pepitoCode`, you can overload operators for the `String` type to make string operations more intuitive.

    .. code-block:: pepitoCode

       String a = "Hello";
       String b = "World";
       String result = a + " " + b + "!";  // result is "Hello World!"

Interoperability
================

**Casting**

    You can cast `String` to other types, typically numeric types if the string represents a valid number.

    .. code-block:: pepitoCode

       Int myInt = (Int) "123";
       Float myFloat = (Float) "123.45";
