Mathematical Functions
======================

This section covers the mathematical functions available in the language.

Logarithmic Functions
---------------------

.. function:: log(x, base)

    Computes the logarithm of *x* to the given *base*.
    
    **Parameters:**
    
    - **x**: The number to compute the logarithm for.
    - **base**: The base of the logarithm. If omitted, the natural logarithm is computed.
    
    **Returns:**
    
    The logarithm of *x* to the specified base.
    
    **Examples:**
    
    .. code-block:: mylang
    
        log(8, 2)  # Returns 3.0
        log(8)     # Returns 2.0794415416798357

.. function:: ln(x)

    Computes the natural logarithm of *x*.
    
    **Parameters:**
    
    - **x**: The number to compute the natural logarithm for.
    
    **Returns:**
    
    The natural logarithm of *x*.
    
    **Examples:**
    
    .. code-block:: mylang
    
        ln(8)  # Returns 2.0794415416798357

.. function:: log10(x)

    Computes the base-10 logarithm of *x*.
    
    **Parameters:**
    
    - **x**: The number to compute the base-10 logarithm for.
    
    **Returns:**
    
    The base-10 logarithm of *x*.
    
    **Examples:**
    
    .. code-block:: mylang
    
        log10(100)  # Returns 2.0
