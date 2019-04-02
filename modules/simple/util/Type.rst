
.. index:: 
	single: simple.util.Type

=================
simple.util.Type
=================

Check the type of an object or character

:copyright: 2018-2019, Abdulazeez Abdulazeez Adeshina
:license: MIT License Copyright (c) 2018 simple
:author:  Abdulazeez Abdulazeez Adeshina
:date: 07 August 2018
:time: 09:01 AM
:filename: Type.sim
:contributors: Azeez Adewale <azeezadewale98@gmail.com>


================
Table Of Content
================
====================================== ==================================================================================================================================================================
 Fields/Blocks/Classes                  Summary                                                                                                                                                          
====================================== ==================================================================================================================================================================
 `block typeOf(object var)`_            Return the type of variable passed to this function.                                                                                                             
 `block __get_var_as_string(var)`_      Get the value of the parameter converted to string, only the number and string is accepted as parameter. Other types are not accepted.                           
 `block isAlphaNum(object var)`_        Check if a Variable is an Alphabet or Numeric. **true** if the variable is ofvalid characters and or digits. The characters can be any of the ANSI recognized    
 `block isAlpha(object var)`_           Check if a Variable is an Alphabet . true if the variable is ofvalid alphabet. The characters can be any of the ANSI recognized                                  
 `block isDigit(object var)`_           Check if a Variable is a Numeric character. true if the variable is ofvalid digit. The character can be any of the numeric digit and or the combination          
 `block isControlChar(object var)`_     Check if a Variable is an Control Characters. true if the variable is acontrol character. The characters can be any of of the control characters such as         
 `block isGraphical(object var)`_       Check if a Variable is has a graphical representation using locale orcan be printed to the standard display output.                                              
 `block isLowerCase(string var)`_       Check if the Variable is in lower case. This is always false for a non stringvariable but a valid check is perform on a string variable                          
 `block isUpperCase(string var)`_       Check if the Variable is in upper case. This is always false for a non stringvariable but a valid check is perform on a string variable                          
 `block isPrintable(object var)`_       Check if the Variable is printable on the standard display output.similar to isGraphical()                                                                       
 `block isWhiteSpace(string var)`_      This blocks check if the variable is a white space. It returns true if the character or all the characters in the string is white-space.                         
 `block __isWhiteSpace(string var)`_    Similar to isWhiteSpace(string var) but efficiently check of a character is a white space	**Parameters**:	                                                       
 `block isPunctuation(object var)`_     Check if a variable is a punctuation character.                                                                                                                  
 `block isHexDigit(object var)`_        Check if a Variable is an Hexadecimal Digit.                                                                                                                     
====================================== ==================================================================================================================================================================


.. index:: 
	pair: Type.sim; block typeOf(object var)

=========================
block typeOf(object var)
=========================
**Source**: `block typeOf(object var) Source`_.
    
    Return the type of variable passed to this function.


.. index:: 
	pair: Type.sim; block __get_var_as_string(var)

===============================
block __get_var_as_string(var)
===============================
**Source**: `block __get_var_as_string(var) Source`_.
    
    Get the value of the parameter converted to string, only the number and string 
    is accepted as parameter. Other types are not accepted.
    
    **Parameters**:	
      var : Object
       the value to convert to string
    
    **Return**:
      the parameter as String


.. index:: 
	pair: Type.sim; block isAlphaNum(object var)

=============================
block isAlphaNum(object var)
=============================
**Source**: `block isAlphaNum(object var) Source`_.
    
    Check if a Variable is an Alphabet or Numeric. **true** if the variable is of
    valid characters and or digits. The characters can be any of the ANSI recognized 
    alphabetic characters and the numeric digit are the combination of numbers through
    
    ::
    
      0 - 9 
      0 1 2 3 4 5 6 7 8 9
    
    **Parameters**:	
      var : Object
       the value to check if it an alphabet or digit
    	
    **Return**:
      true if the parameter is an alphabet or digit


.. index:: 
	pair: Type.sim; block isAlpha(object var)

==========================
block isAlpha(object var)
==========================
**Source**: `block isAlpha(object var) Source`_.
    
    Check if a Variable is an Alphabet . true if the variable is of
    valid alphabet. The characters can be any of the ANSI recognized 
    alphabetic characters 
    
    :: 
    
      ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
      "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    	
    ::
    
      ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
      "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    **Parameters**:	
      var : Object
       the value to check if it an alphabet
    	
    **Return**:
      true if parameter is a valid alphabet


.. index:: 
	pair: Type.sim; block isDigit(object var)

==========================
block isDigit(object var)
==========================
**Source**: `block isDigit(object var) Source`_.
    
    Check if a Variable is a Numeric character. true if the variable is of
    valid digit. The character can be any of the numeric digit and or the combination
    of numbers through 0 - 9
    
    ::
    
      0 - 9 
      0 1 2 3 4 5 6 7 8 9
    	
    **Parameters**:	
      var : Object
       the value to check if it a digit
    	
    **Return**:
      true if parameter is a valid digit


.. index:: 
	pair: Type.sim; block isControlChar(object var)

================================
block isControlChar(object var)
================================
**Source**: `block isControlChar(object var) Source`_.
    
    Check if a Variable is an Control Characters. true if the variable is a
    control character. The characters can be any of of the control characters such as 
    
    ::
    
      \b	-	Backspace
      \a	-	Alert
      \f	-	Form Feed
      \n	-	New Line
      \r	-	Carriage Return
      \t	-	Horizontal Tab
      \v	-	Vertical Tab
      \0	-	Null Character
    	
    **Parameters**:	
      var : Object
       the value to check if it a control character
    	
    **Return**:
      true if parameter is a control character


.. index:: 
	pair: Type.sim; block isGraphical(object var)

==============================
block isGraphical(object var)
==============================
**Source**: `block isGraphical(object var) Source`_.
    
    Check if a Variable is has a graphical representation using locale or
    can be printed to the standard display output. 
    
    **Parameters**:	
      var : Object
       the value to check if has a graphical representation 
    	
    **Return**:
      true if parameter has graphical representation 


.. index:: 
	pair: Type.sim; block isLowerCase(string var)

==============================
block isLowerCase(string var)
==============================
**Source**: `block isLowerCase(string var) Source`_.
    
    Check if the Variable is in lower case. This is always false for a non string
    variable but a valid check is perform on a string variable
    
    **Parameters**:	
      var : String
       the value to check if it is in lower case
    	
    **Return**:
      true if variable is in lower case


.. index:: 
	pair: Type.sim; block isUpperCase(string var)

==============================
block isUpperCase(string var)
==============================
**Source**: `block isUpperCase(string var) Source`_.
    
    Check if the Variable is in upper case. This is always false for a non string
    variable but a valid check is perform on a string variable
    
    **Parameters**:	
      var : String
       the value to check if it is in upper case
    	
    **Return**:
      true if variable is in upper case


.. index:: 
	pair: Type.sim; block isPrintable(object var)

==============================
block isPrintable(object var)
==============================
**Source**: `block isPrintable(object var) Source`_.
    
    Check if the Variable is printable on the standard display output.
    similar to isGraphical()
    
    **Parameters**:	
      var : Object
       the value to check if it printable
    	
    **Return**:
      true if the character is printable


.. index:: 
	pair: Type.sim; block isWhiteSpace(string var)

===============================
block isWhiteSpace(string var)
===============================
**Source**: `block isWhiteSpace(string var) Source`_.
    
    This blocks check if the variable is a white space. It returns true if the character or 
    all the characters in the string is white-space. 
    
    **Parameters**:	
      var : String
       the value to check if it white-space
    	
    **Return**:
      true if the characters is white-space or are white-spaces


.. index:: 
	pair: Type.sim; block __isWhiteSpace(string var)

=================================
block __isWhiteSpace(string var)
=================================
**Source**: `block __isWhiteSpace(string var) Source`_.
    
    Similar to isWhiteSpace(string var) but efficiently check of a character is a white space	
    **Parameters**:	
      var : String
       the value to check if it white-space
    	
    **Return**:
      true if the characters is white-space or are white-spaces


.. index:: 
	pair: Type.sim; block isPunctuation(object var)

================================
block isPunctuation(object var)
================================
**Source**: `block isPunctuation(object var) Source`_.
    
    Check if a variable is a punctuation character. 
    
    **Parameters**:	
      var : Object
       the value to check if it consists of punctuation
    	
    **Return**:
      true if the character consists of punctuation


.. index:: 
	pair: Type.sim; block isHexDigit(object var)

=============================
block isHexDigit(object var)
=============================
**Source**: `block isHexDigit(object var) Source`_.
    
    Check if a Variable is an Hexadecimal Digit.
    
    **Parameters**:	
      var : String
       the value to check if it a set of hexadecimal digit
    	
    **Return**:
      true if the parameter is a set of hexadecimal digit



-------

.

	
.. code-block:: simple

  call simple.util.Console
  call simple.util.Type
  import simple.core
	
  stdout.println(isPunctuation("%#%#&$%"))
  stdout.println(isAlphaNum("ABCD1234abcd"))
  stdout.println(isWhiteSpace("  		"))

.. make object into string|number


.

.. _block typeOf(object var) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Type.sim#L19
.. _block __get_var_as_string(var) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Type.sim#L44
.. _block isAlphaNum(object var) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Type.sim#L65
.. _block isAlpha(object var) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Type.sim#L91
.. _block isDigit(object var) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Type.sim#L112
.. _block isControlChar(object var) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Type.sim#L138
.. _block isGraphical(object var) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Type.sim#L153
.. _block isLowerCase(string var) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Type.sim#L168
.. _block isUpperCase(string var) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Type.sim#L182
.. _block isPrintable(object var) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Type.sim#L196
.. _block isWhiteSpace(string var) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Type.sim#L211
.. _block __isWhiteSpace(string var) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Type.sim#L223
.. _block isPunctuation(object var) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Type.sim#L242
.. _block isHexDigit(object var) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Type.sim#L256

