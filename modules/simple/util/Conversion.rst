
.. index:: 
	single: simple.util.Conversion

=======================
simple.util.Conversion
=======================

Convert between possible different types

:copyright: 2018-2019, Azeez Adewale
:license: MIT License Copyright (c) 2018 simple
:author:  Azeez Adewale
:date: 5 Febuary 2017
:time: 
:filename: Conversion.sim


================
Table Of Content
================
===================================== ========================================================================================================
 Fields/Blocks/Classes                 Summary                                                                                                
===================================== ========================================================================================================
 `block strToCHex(string value)`_      Convert a string to it equivalent C Hexadecimal values                                                 
 `block strToHex(string value)`_       Convert a string to it equivalent Hexadecimal values                                                   
 `block hexToString(string value)`_    Revert the result of the strToHex(string value) function call byconvert Hexadecimal values to string   
 `block strToList(string value)`_      Convert a string to list                                                                               
===================================== ========================================================================================================


.. index:: 
	pair: Conversion.sim; block strToCHex(string value)

==============================
block strToCHex(string value)
==============================
**Source**: `block strToCHex(string value) Source`_.
    
    Convert a string to it equivalent C Hexadecimal values
    
    ::
    	
      cHex = strToCHex("Hello World")
      stdout.println(cHex)
    	
    The above snippet should create the below C hex
    	
    :: 
    
      0x48,0x65,0x6c,0x6c,0x6f,0x20,0x57,0x6f,0x72,0x6c,0x64
    	
    **Parameters**:	
      value : String
       the string value to convert to C Hex
    
    **Return**:
      the C Hexadecimal values for the string


.. index:: 
	pair: Conversion.sim; block strToHex(string value)

=============================
block strToHex(string value)
=============================
**Source**: `block strToHex(string value) Source`_.
    
    Convert a string to it equivalent Hexadecimal values
    
    ::
    
      hex = strToHex("Hello World")
      stdout.println(hex)
    	
    The above snippet should create the below hex
    	
    :: 
    
      48656c6c6f20576f726c64
    	
    **Parameters**:	
      value : String
       the string value to convert to Hexadecimal value
    
    **Return**:
      the Hexadecimal values for the string


.. index:: 
	pair: Conversion.sim; block hexToString(string value)

================================
block hexToString(string value)
================================
**Source**: `block hexToString(string value) Source`_.
    
    Revert the result of the strToHex(string value) function call by
    convert Hexadecimal values to string
    
    ::
    
      hex = hexToString("48656c6c6f20576f726c64")
      stdout.println(hex)
    	
    The above snippet should create the below hex
    	
    :: 
    
      "Hello World"
    	
    **Parameters**:	
      value : String
       the hexadecimal value to convert to string
    
    **Return**:
      the string for the hexadecimal value


.. index:: 
	pair: Conversion.sim; block strToList(string value)

==============================
block strToList(string value)
==============================
**Source**: `block strToList(string value) Source`_.
    
    Convert a string to list
    
    .. note::
      This does not split the string by any character all string is converted 
      to a list with length of 1 
    	
    **Parameters**:	
      value : String
       the hexadecimal value to convert to list
    
    **Return**:
      the list containing the string at index 0



-------

.

	
.. code-block:: simple

  call simple.util.Console
  call simple.util.Conversion
  import simple.core
	
  stdout.println(strToCHex("Hello World"))
  stdout.println(strToHex("Hello World"))
  stdout.println(hexToString("48656c6c6f20576f726c64"))
  stdout.println(strToList("Hello World"))


.

.. _block strToCHex(string value) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Conversion.sim#L36
.. _block strToHex(string value) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Conversion.sim#L60
.. _block hexToString(string value) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Conversion.sim#L85
.. _block strToList(string value) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Conversion.sim#L102

