Error Handling
==============

Exceptions
----------

.. code-block:: pepitoCode

   try {
       // code that may throw an exception
   } catch (Exception e) {
       // code to handle the exception
   }

Examples
--------

.. code-block:: pepitoCode

   try {
       Int result = 10 / 0;
   } catch (DivideByZeroException e) {
       print("Cannot divide by zero.");
   }
