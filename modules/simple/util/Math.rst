
.. index:: 
	single: simple.util.Math

=================
simple.util.Math
=================

This module contains of functions for performing mathematical operations such as logarithm, 
square root, trigonometric e.t.c. 

It is also a wrapper file for the `Mathic dynamic module`_. The module is loaded
once when this file is first call. Using the mathic block directly is not consider safe as
it does not check the parameter for incompatible types or object and can result to runtime 
error. Most of the blocks implemented in this file has a dynamic call but is not consider
safe to call the dynamic blocks directly. 

Usage

  All the blocks are public and does not require any type of initialization  because it has no 
  class. All the function in this file is accessible by calling it.
	
.. code-block:: simple

  call simple.util.Math
	
A more elaborate example is present at `simple.util.Math Test`_

:copyright: 2018-2019, Azeez Adewale
:license: MIT License Copyright (c) 2018 simple
:author: Azeez Adewale <azeezadewale98@gmail.com>
:date: February 5 2017
:filename: Math.sim


================
Table Of Content
================
======================================== ===============================================================================================================================================================================================================================================
 Fields/Blocks/Classes                    Summary                                                                                                                                                                                                                                       
======================================== ===============================================================================================================================================================================================================================================
 `module simple.util`_                                                                                                                                                                                                                                                                  
 `Called Modules`_                                                                                                                                                                                                                                                                      
 `final MathE`_                           Exponential number used in natural log and expApproximation of the mathematical constant *e* to 11 digit after decimal point.                                                                                                                 
 `final MathPI`_                          The ratio of a circle's circumference to its diameter.Approximation of the mathematical constant *pi* / *π* to 11 digit                                                                                                                      
 `final $MathModule`_                     The math module in a printable string **simple.utilites.Math**                                                                                                                                                                                
 `final $MathNotNumber`_                  Exception message to indicate the parameter is not a valid number                                                                                                                                                                             
 `final $MathLessThan`_                   Exception message thrown if the parameter is less than a number                                                                                                                                                                               
 `final $MathLessThanOne`_                Exception message thrown if the parameter is less than 1                                                                                                                                                                                      
 `final $MathLessThanMinusOne`_           Exception message thrown if the parameter is less than -1                                                                                                                                                                                     
 `final $MathNotBetweenOne`_              Exception message thrown if the parameter is not between -1 and 1                                                                                                                                                                             
 `final $MathNotEqual`_                   Exception message to indicate parameter cannot be equal to a number                                                                                                                                                                           
 `block MathE()`_                         Exponential number used in natural log and expApproximation of the mathematical constant *e* to 11 digit after decimal point.                                                                                                                 
 `block MathPI()`_                        The ratio of a circle's circumference to its diameter.Approximation of the mathematical constant *pi* / *π* to 11 digit                                                                                                                      
 `block abs(number)`_                     Determine the absolute value of a number. Determining the absolute number makes it positive.                                                                                                                                                  
 `block min(fNumber, sNumber)`_           Determine the number that is smaller between the two parameters. If both parameter are zerothe first number is negated then the second number is minus from it and the negated result                                                         
 `block max(fNumber, sNumber)`_           Determine the number that is larger between the two parameters. If both parameter are zerothe second number is negated and then minus from the first number to give the correct larger                                                        
 `block sin(number)`_                     Determine the sine trigonometric function *sin* of a number. The sine value of 0 remainsremain 0.                                                                                                                                             
 `block cos(number)`_                     Determine the cosine trigonometric function *cos* of a number. The cosine value of 0 remainsremain 0.                                                                                                                                         
 `block tan(number)`_                     Determine the tangent trigonometric function *tan* of a number. The tangent value of 0 remains 0.                                                                                                                                             
 `block asin(number)`_                    Determine the arc sine trigonometric function *arcsin* of a number. The arc sine value of 0 remains 0. The range of angles returned is -pi/2 to pi/2 radians (-90 to 90 degrees).                                                             
 `block acos(number)`_                    Determine the arc cosine trigonometric function *arccos* of a number. The arc cosine value of 0 remains0. The range of angles returned is -pi/2 to pi/2 radians (-90 to 90 degrees).                                                          
 `block atan(number)`_                    Determine the arc tangent trigonometric function *arctan* of a number. The arc tangent value of 0 remains0. The range of angles returned is -pi/2 to pi/2 radians (-90 to 90 degrees).                                                        
 `block atan2(y, x)`_                     Convert rectangular coordinate **(x, y)** correct quadrant. It calculate the arc tangent of x and y in the range of -180 and 180 degrees.                                                                                                     
 `block sinh(number)`_                    Determine the hyperbolic sine of a number.                                                                                                                                                                                                    
 `block cosh(number)`_                    Determine the hyperbolic cosine of a number.                                                                                                                                                                                                  
 `block tanh(number)`_                    Determine the hyperbolic tangent of a number.                                                                                                                                                                                                 
 `block asinh(number)`_                   Determine the nonnegative area hyperbolic sine of a number.                                                                                                                                                                                   
 `block acosh(number)`_                   Determine the nonnegative area hyperbolic cosine of a number.                                                                                                                                                                                 
 `block atanh(number)`_                   Determine the nonnegative area hyperbolic tangent of a number.                                                                                                                                                                                
 `block exp(number)`_                     Determine the exponential value of a number. The opposite of `block log(number)`_                                                                                                                                                             
 `block log(number)`_                     Determine the natural logarithm (base-e logarithm) of a number. The opposite of `block exp(number)`_                                                                                                                                          
 `block sqrt(number)`_                    Determine the square root of a number. To find cube root of a number call the `block cbrt(number)`_ instead,to determine the other root use ``pow(number, 1/rootNum)``                                                                        
 `block cbrt(number)`_                    Determine the cube root of a number. To find square root of a number call the `block sqrt(number)`_ instead,to determine the other root use ``pow(number, 1/rootNum)``                                                                        
 `block pow(fNumber,sNumber)`_            Raise a number to a power of another number.                                                                                                                                                                                                  
 `block ceil(number)`_                    Determine the nearest integer that is greater than or equal to the number parameter. If the param number is between -1 and 0 the result is -0.                                                                                                
 `block floor(number)`_                   Determine the nearest integer that is less than or equal to the number parameter.                                                                                                                                                             
 `block rint(number)`_                    Determine the value of the number rounded to a nearby integral (as a floating-point value). If the floating-pointsare between two number the Even number will be worked on. It round to the nearest.                                          
 `block round(number)`_                   Determine the value of the number rounded to a nearby integral with halfway cases rounded away from zero. The block function is same as ``floor(number + 0.5f)``. It round to the nearest.                                                    
 `block nearbyint(number)`_               Determine the value of the number rounded to a nearby integral (as a floating-point value). If the floating-pointsare between two number the Even number will be worked on. It round to the nearest. Similar to `block rint(number)`_ block   
 `block fmod(fNumber,sNumber)`_           Determine floating point remainder of the fNumber / sNumber with the quotient truncated (rounded towards zero). It round to the nearest.                                                                                                      
 `block remainder(fNumber,sNumber)`_      Determine floating point remainder of the fNumber / sNumber. It round to the nearest. Similar to `block fmod(fNumber,sNumber)`_ block                                                                                                         
 `block trunc(number)`_                   Determine the nearest integral value that is not larget in magnitude than the number rounding it toward zero                                                                                                                                  
 `block toRadians(number)`_               Convert from degree to radian using the formula `radians = degrees * (pi/180)`                                                                                                                                                                
 `block toDegrees(number)`_               Convert from radian to degree using the formula ``degrees = radians * (180/pi)``                                                                                                                                                              
 `block log10(number)`_                   Determine the base 10 logarithm of a number.                                                                                                                                                                                                  
 `block frexp(number)`_                   Breaks the floating point number into its binary significand (a floating point with an absolute value between 0.5(included) and 1.0(excluded)) and an integral exponent for 2, such that:                                                     
 `block ldexp(number,exp)`_               Deterine the result of multiplying the number (the significand) by 2 raised to the power of exp (the exponent)                                                                                                                                
 `block modf(number)`_                    Breaks the number into an integral and a fractional part. The integer part is stored in the object pointed by intpart, and the fractional part is returned by the function. Both parts have the same sign as the number                       
 `block exp2(number)`_                    Determine the base-2 exponential function of a nuber, which is 2 raised to the power the number: **2x**                                                                                                                                       
 `block expm1(number)`_                   Determine the value of e raised to the power a number minus one: **ex-1**                                                                                                                                                                     
 `block ilogb(number)`_                   Determine the integral part of the logarithm of **x**, using 2 or greater as base for the logarithm.This is the exponent used internally by the machine to express the floating-point value x, when it uses                                   
 `block log1p(number)`_                   Determine the natural logarithm of one plus the number. for small magnitude values of number, `block log1p(number)`_ may be more accurate than `block log(number)`_ ``log( 1 + x )``                                                          
 `block log2(number)`_                    Determine the binary (base-2) logarithm of a number                                                                                                                                                                                           
 `block logb(number)`_                    Determine the the logarithm of a number, using 2 as base for the logarithm. Almost equivalent to `block log2(number)`_ for positive number                                                                                                    
 `block scalbln(number,exp)`_             Scales a number by 2 raised to the power of n, returning the result of computing:                                                                                                                                                             
 `block hypot(x,y)`_                      Determine what would be the square root of the sum of the squares of x and y (as per the Pythagorean theorem), but without incurring in undue overflow or underflow of intermediate values                                                    
 `block numsign(number)`_                 Determine the sign of the number in the following format                                                                                                                                                                                      
 `block vmDecimalPoints(place)`_          By Default all decimal number in simple-lang is round down to 2 floating point. This block changes the number of floating point decimal are rounded to. Using this block make all the number through out the program have the number          
 `block random()`_                        Generate a random number                                                                                                                                                                                                                      
======================================== ===============================================================================================================================================================================================================================================


.. index:: 
	pair: Math.sim; module simple.util

===================
module simple.util
===================
**Source**: `module simple.util Source`_.
    
    


.. index:: 
	pair: Math.sim; Called Modules

===============
Called Modules
===============
**Source**: `Called Modules Source`_.
    
    


.. index:: 
	pair: Math.sim; final MathE

============
final MathE
============
**Source**: `final MathE Source`_.
    
    Exponential number used in natural log and exp
    Approximation of the mathematical constant *e* to 11 digit after decimal point.
    **2.71828182846**. 
    
    The *e* to the first 15 digits after the decimal point is **2.718281828459045**
    


.. index:: 
	pair: Math.sim; final MathPI

=============
final MathPI
=============
**Source**: `final MathPI Source`_.
    
    The ratio of a circle's circumference to its diameter.
    Approximation of the mathematical constant *pi* / *π* to 11 digit 
    after the decimal point **3.14159265359**. 
    The*pi* / *π* constant to the first 50 digits after the decimal point.
    
    **3.14159 26535 89793 23846 26433 83279 50288 41971 69399 37510**
    


.. index:: 
	pair: Math.sim; final $MathModule

==================
final $MathModule
==================
**Source**: `final $MathModule Source`_.
    
    The math module in a printable string **simple.utilites.Math**


.. index:: 
	pair: Math.sim; final $MathNotNumber

=====================
final $MathNotNumber
=====================
**Source**: `final $MathNotNumber Source`_.
    
    Exception message to indicate the parameter is not a valid number


.. index:: 
	pair: Math.sim; final $MathLessThan

====================
final $MathLessThan
====================
**Source**: `final $MathLessThan Source`_.
    
    Exception message thrown if the parameter is less than a number


.. index:: 
	pair: Math.sim; final $MathLessThanOne

=======================
final $MathLessThanOne
=======================
**Source**: `final $MathLessThanOne Source`_.
    
    Exception message thrown if the parameter is less than 1


.. index:: 
	pair: Math.sim; final $MathLessThanMinusOne

============================
final $MathLessThanMinusOne
============================
**Source**: `final $MathLessThanMinusOne Source`_.
    
    Exception message thrown if the parameter is less than -1


.. index:: 
	pair: Math.sim; final $MathNotBetweenOne

=========================
final $MathNotBetweenOne
=========================
**Source**: `final $MathNotBetweenOne Source`_.
    
    Exception message thrown if the parameter is not between -1 and 1


.. index:: 
	pair: Math.sim; final $MathNotEqual

====================
final $MathNotEqual
====================
**Source**: `final $MathNotEqual Source`_.
    
    Exception message to indicate parameter cannot be equal to a number


.. index:: 
	pair: Math.sim; block MathE()

==============
block MathE()
==============
**Source**: `block MathE() Source`_.
    
    Exponential number used in natural log and exp
    Approximation of the mathematical constant *e* to 11 digit after decimal point.
    **2.71828182846**. 
    
    The *e* to the first 15 digits after the decimal point is **2.718281828459045**
    	
    **Return**:
      the *e* constant with the first 11 digits after the decimal point


.. index:: 
	pair: Math.sim; block MathPI()

===============
block MathPI()
===============
**Source**: `block MathPI() Source`_.
    
    The ratio of a circle's circumference to its diameter.
    Approximation of the mathematical constant *pi* / *π* to 11 digit 
    after the decimal point **3.14159265359** 
    The *pi* / *π* constant to the first 50 digits after the decimal point.
    
    **3.14159 26535 89793 23846 26433 83279 50288 41971 69399 37510**
    
    **Return**:
      the *pi* / *π* constant with the first 11 digits after the decimal point


.. index:: 
	pair: Math.sim; block abs(number)

==================
block abs(number)
==================
**Source**: `block abs(number) Source`_.
    
    Determine the absolute value of a number. Determining the absolute number makes it positive.
    
    **Parameters**:	
      num : Number
       the number to determine it absolute value
    
    **Throws**:	
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a number
    
    **Return**:
      the absolute value of a number


.. index:: 
	pair: Math.sim; block min(fNumber, sNumber)

============================
block min(fNumber, sNumber)
============================
**Source**: `block min(fNumber, sNumber) Source`_.
    
    Determine the number that is smaller between the two parameters. If both parameter are zero
    the first number is negated then the second number is minus from it and the negated result 
    is returned, this deals with -0 and 0 that might behave strangely and can return 0 
    to be smaller than -0
    
    **Parameters**:	
      fNumber : Number
       the first number
      sNumber : Number
       the second number
    
    **Throws**:	
      `final $MathNotNumber`_ with title `final $MathModule`_ if one or all the parameters 
      are not number
    
    **Return**:
      minimum number of the two numbers


.. index:: 
	pair: Math.sim; block max(fNumber, sNumber)

============================
block max(fNumber, sNumber)
============================
**Source**: `block max(fNumber, sNumber) Source`_.
    
    Determine the number that is larger between the two parameters. If both parameter are zero
    the second number is negated and then minus from the first number to give the correct larger 
    number.
    
    **Parameters**:	
      fNumber : Number
       the first number
      sNumber : Number
       the second number
    
    **Throws**:	
      `final $MathNotNumber`_ with title `final $MathModule`_ if one or all the parameters 
      are not number
    
    **Return**:
      larger number of the two numbers


.. index:: 
	pair: Math.sim; block sin(number)

==================
block sin(number)
==================
**Source**: `block sin(number) Source`_.
    
    Determine the sine trigonometric function *sin* of a number. The sine value of 0 remains
    remain 0. 
    
    **Parameters**
      number : Number 
       the number to determine it sin value
    		
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    	
    **Return**
      the sine value of a radian angle number


.. index:: 
	pair: Math.sim; block cos(number)

==================
block cos(number)
==================
**Source**: `block cos(number) Source`_.
    
    Determine the cosine trigonometric function *cos* of a number. The cosine value of 0 remains
    remain 0. 
    
    
    **Parameters**
      number : Number
       the number to determine it cos value
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the cosine value of a radian angle number


.. index:: 
	pair: Math.sim; block tan(number)

==================
block tan(number)
==================
**Source**: `block tan(number) Source`_.
    
    Determine the tangent trigonometric function *tan* of a number. The tangent value of 0 remains 
    0. 
    
    
    **Parameters**
      number : Number
       the number to determine it tan value
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the tangent value of a radian angle number


.. index:: 
	pair: Math.sim; block asin(number)

===================
block asin(number)
===================
**Source**: `block asin(number) Source`_.
    
    Determine the arc sine trigonometric function *arcsin* of a number. The arc sine value of 0 remains 
    0. The range of angles returned is -pi/2 to pi/2 radians (-90 to 90 degrees).
    
    
    **Parameters**
      number : Number
       the number to determine it arc sine value
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the arc sine value of the number in radian 


.. index:: 
	pair: Math.sim; block acos(number)

===================
block acos(number)
===================
**Source**: `block acos(number) Source`_.
    
    Determine the arc cosine trigonometric function *arccos* of a number. The arc cosine value of 0 remains
    0. The range of angles returned is -pi/2 to pi/2 radians (-90 to 90 degrees).
    
    
    **Parameters**
      number : Number
       the number to determine it arc csine value
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the arc cosine value of the number in radian 


.. index:: 
	pair: Math.sim; block atan(number)

===================
block atan(number)
===================
**Source**: `block atan(number) Source`_.
    
    Determine the arc tangent trigonometric function *arctan* of a number. The arc tangent value of 0 remains
    0. The range of angles returned is -pi/2 to pi/2 radians (-90 to 90 degrees).
    
    
    **Parameters**
      number : Number
       the number to determine it arc tangent value
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the arc tangent value of the number in radian 


.. index:: 
	pair: Math.sim; block atan2(y, x)

==================
block atan2(y, x)
==================
**Source**: `block atan2(y, x) Source`_.
    
    Convert rectangular coordinate **(x, y)** correct quadrant. It calculate the arc tangent of x and y 
    in the range of -180 and 180 degrees. 
    
    
    **Parameters**
      y : Number
       the floating point value representing a y-coordinate
      x : Number
       the floating point value representing an x-coordinate
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if one or all the parameters 
      are not number
    
    **Return**
      the arc tangent in radian of x/y based on the signs of both values to determine the correct quadrant


.. index:: 
	pair: Math.sim; block sinh(number)

===================
block sinh(number)
===================
**Source**: `block sinh(number) Source`_.
    
    Determine the hyperbolic sine of a number. 
    
    
    **Parameters**
      number : Number
       the hyperbolic angle
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the hyperbolic sine value of the number 


.. index:: 
	pair: Math.sim; block cosh(number)

===================
block cosh(number)
===================
**Source**: `block cosh(number) Source`_.
    
    Determine the hyperbolic cosine of a number. 
    
    
    **Parameters**
      number : Number
       the hyperbolic angle
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the hyperbolic cosine value of the number 


.. index:: 
	pair: Math.sim; block tanh(number)

===================
block tanh(number)
===================
**Source**: `block tanh(number) Source`_.
    
    Determine the hyperbolic tangent of a number. 
    
    
    **Parameters**
      number : Number
       the hyperbolic angle
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the hyperbolic tangent value of the number 


.. index:: 
	pair: Math.sim; block asinh(number)

====================
block asinh(number)
====================
**Source**: `block asinh(number) Source`_.
    
    Determine the nonnegative area hyperbolic sine of a number. 
    
    
    **Parameters**
      number : Number
       the hyperbolic angle
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the Nonnegative area sine value of the number 


.. index:: 
	pair: Math.sim; block acosh(number)

====================
block acosh(number)
====================
**Source**: `block acosh(number) Source`_.
    
    Determine the nonnegative area hyperbolic cosine of a number. 
    
    
    **Parameters**
      number : Number
       value whose area hyperbolic cosine is computed
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
      `final $MathLessThanOne`_ with title `final $MathModule`_ if the parameter is less than 1
    
    **Return**
      Nonnegative area hyperbolic cosine of number, in the interval [0,+INFINITY] 


.. index:: 
	pair: Math.sim; block atanh(number)

====================
block atanh(number)
====================
**Source**: `block atanh(number) Source`_.
    
    Determine the nonnegative area hyperbolic tangent of a number. 
    
    
    **Parameters**
      number : Number
       the value whose area hyperbolic tangent is computed, in the interval [-1,+1]
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
      `final $MathNotEqual`_ -1 or 1 with title `final $MathModule`_ if the parameter is -1 or 1
    
    **Return**
      the Nonnegative area  tangent value of the number 


.. index:: 
	pair: Math.sim; block exp(number)

==================
block exp(number)
==================
**Source**: `block exp(number) Source`_.
    
    Determine the exponential value of a number. The opposite of `block log(number)`_
    
    
    **Parameters**
      number : Number
       the number to raise to the power of
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the exponential value of the number 


.. index:: 
	pair: Math.sim; block log(number)

==================
block log(number)
==================
**Source**: `block log(number) Source`_.
    
    Determine the natural logarithm (base-e logarithm) of a number. The opposite of `block exp(number)`_
    
    
    **Parameters**
      number : Number
       the number to get the natural log of
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the natural logarithm (base-e logarithm) of number


.. index:: 
	pair: Math.sim; block sqrt(number)

===================
block sqrt(number)
===================
**Source**: `block sqrt(number) Source`_.
    
    Determine the square root of a number. To find cube root of a number call the `block cbrt(number)`_ instead,
    to determine the other root use ``pow(number, 1/rootNum)``
    
    
    **Parameters**
      number : Number
       the number to get the square root of
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the square root of the number


.. index:: 
	pair: Math.sim; block cbrt(number)

===================
block cbrt(number)
===================
**Source**: `block cbrt(number) Source`_.
    
    Determine the cube root of a number. To find square root of a number call the `block sqrt(number)`_ instead,
    to determine the other root use ``pow(number, 1/rootNum)``
    
    
    **Parameters**
      number : Number
       the number to get the cube root of
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the cube root of the number


.. index:: 
	pair: Math.sim; block pow(fNumber,sNumber)

===========================
block pow(fNumber,sNumber)
===========================
**Source**: `block pow(fNumber,sNumber) Source`_.
    
    Raise a number to a power of another number.
    
    
    **Parameters**
      fNumber : Number
       the first number to be raised 
      sNumber : Number
       the number to be raised to it power
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if one or all the parameters 
      are not number
    
    **Return**
      fNumber raised to the power of sNumber


.. index:: 
	pair: Math.sim; block ceil(number)

===================
block ceil(number)
===================
**Source**: `block ceil(number) Source`_.
    
    Determine the nearest integer that is greater than or equal to the number parameter. If the param number 
    is between -1 and 0 the result is -0.
    
    .. note:: 
      ceil(number) == floor(-number)
    
    **Parameters**
      number : Number
       the number to be worked on
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the nearest integer value greater than or equal to the number


.. index:: 
	pair: Math.sim; block floor(number)

====================
block floor(number)
====================
**Source**: `block floor(number) Source`_.
    
    Determine the nearest integer that is less than or equal to the number parameter. 
    
    .. note::
      ceil(number) == floor(-number)
    
    **Parameters**
      number : Number
       the number to be worked on
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the largest integer value less than or equal to the number


.. index:: 
	pair: Math.sim; block rint(number)

===================
block rint(number)
===================
**Source**: `block rint(number) Source`_.
    
    Determine the value of the number rounded to a nearby integral (as a floating-point value). If the floating-points
    are between two number the Even number will be worked on. It round to the nearest.
    
    
    **Parameters**
      number : Number
       the number to be rounded
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the number rounded to nearby integral 


.. index:: 
	pair: Math.sim; block round(number)

====================
block round(number)
====================
**Source**: `block round(number) Source`_.
    
    Determine the value of the number rounded to a nearby integral with halfway cases rounded away from zero. 
    The block function is same as ``floor(number + 0.5f)``. It round to the nearest.
    
    
    **Parameters**
      number : Number
       the number to be rounded
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the number rounded to nearby integral 


.. index:: 
	pair: Math.sim; block nearbyint(number)

========================
block nearbyint(number)
========================
**Source**: `block nearbyint(number) Source`_.
    
    Determine the value of the number rounded to a nearby integral (as a floating-point value). If the floating-points
    are between two number the Even number will be worked on. It round to the nearest. Similar to `block rint(number)`_ block
    
    
    **Parameters**
      number : Number
       the number to be rounded
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the number rounded to nearby integral 


.. index:: 
	pair: Math.sim; block fmod(fNumber,sNumber)

============================
block fmod(fNumber,sNumber)
============================
**Source**: `block fmod(fNumber,sNumber) Source`_.
    
    Determine floating point remainder of the fNumber / sNumber with the quotient truncated (rounded towards zero). 
    It round to the nearest.
    
    
    **Parameters**
      fNumber : Number
       value of the quotient numerator
      sNumber : Number
       value of the quotient denominator
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the remainder of dividing the fNumber and sNumber parameters


.. index:: 
	pair: Math.sim; block remainder(fNumber,sNumber)

=================================
block remainder(fNumber,sNumber)
=================================
**Source**: `block remainder(fNumber,sNumber) Source`_.
    
    Determine floating point remainder of the fNumber / sNumber. It round to the nearest. Similar to 
    `block fmod(fNumber,sNumber)`_ block
    
    
    **Parameters**
      fNumber : Number
       value of the quotient numerator
      sNumber : Number
       value of the quotient denominator
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the remainder of dividing the fNumber and sNumber parameters


.. index:: 
	pair: Math.sim; block trunc(number)

====================
block trunc(number)
====================
**Source**: `block trunc(number) Source`_.
    
    Determine the nearest integral value that is not larget in magnitude than the number rounding it toward zero
    
    
    **Parameters**
      number : Number
       the number to be truncated
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the number with the floating points truncated


.. index:: 
	pair: Math.sim; block toRadians(number)

========================
block toRadians(number)
========================
**Source**: `block toRadians(number) Source`_.
    
    Convert from degree to radian using the formula `radians = degrees * (pi/180)`
    
    
    **Parameters**
      number : Number
       the angle in degrees
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the angle in radians


.. index:: 
	pair: Math.sim; block toDegrees(number)

========================
block toDegrees(number)
========================
**Source**: `block toDegrees(number) Source`_.
    
    Convert from radian to degree using the formula ``degrees = radians * (180/pi)``
    
    
    **Parameters**
      number : Number
       the angle in radians
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the angle in degrees


.. index:: 
	pair: Math.sim; block log10(number)

====================
block log10(number)
====================
**Source**: `block log10(number) Source`_.
    
    Determine the base 10 logarithm of a number.
    
    
    **Parameters**
      number : Number
       number to get it base 10 logarithm of
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the base 10 logarithm of the number


.. index:: 
	pair: Math.sim; block frexp(number)

====================
block frexp(number)
====================
**Source**: `block frexp(number) Source`_.
    
    Breaks the floating point number into its binary significand (a floating point with an absolute value 
    between 0.5(included) and 1.0(excluded)) and an integral exponent for 2, such that:
    
    .. code-block:: simple
    
      number = significand * 2 ^ exponent 
    
    The exponent is stored in the location pointed by exp, and the **significand** is the value returned 
    by the function
    If the number is zero, both parts (significand and exponent) are zero. If the number is negative, the 
    significand returned by this function is negative
    
    
    **Parameters**
      number : Number
       value to be decomposed
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      a list with binary significand of the number at the first index and the value where the exponent 
      is stored at the second index


.. index:: 
	pair: Math.sim; block ldexp(number,exp)

========================
block ldexp(number,exp)
========================
**Source**: `block ldexp(number,exp) Source`_.
    
    Deterine the result of multiplying the number (the significand) by 2 raised to the power of exp (the exponent)
    
    
    **Parameters**
      number : Number
       point value representing the significand
      exp : Number
       value of the exponent
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      number * 2 ^ exp  


.. index:: 
	pair: Math.sim; block modf(number)

===================
block modf(number)
===================
**Source**: `block modf(number) Source`_.
    
    Breaks the number into an integral and a fractional part. The integer part is stored in the object pointed 
    by intpart, and the fractional part is returned by the function. Both parts have the same sign as the number
    
    
    **Parameters**
      number : Number
       the floating point value to break into parts
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the fractional part of x, with the same sign  


.. index:: 
	pair: Math.sim; block exp2(number)

===================
block exp2(number)
===================
**Source**: `block exp2(number) Source`_.
    
    Determine the base-2 exponential function of a nuber, which is 2 raised to the power the number: **2x**
    
    
    **Parameters**
      number : Number
       the value of the exponent
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      2 raised to the power of the number  


.. index:: 
	pair: Math.sim; block expm1(number)

====================
block expm1(number)
====================
**Source**: `block expm1(number) Source`_.
    
    Determine the value of e raised to the power a number minus one: **ex-1**
    
    
    **Parameters**
      number : Number
       the value of the exponent
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      e raised to the power of the number, minus one  


.. index:: 
	pair: Math.sim; block ilogb(number)

====================
block ilogb(number)
====================
**Source**: `block ilogb(number) Source`_.
    
    Determine the integral part of the logarithm of **x**, using 2 or greater as base for the logarithm.
    This is the exponent used internally by the machine to express the floating-point value x, when it uses 
    a significand between 1.0 and 2, so that, for a positive number 
    
    .. code-block:: simple
    
      x = significand * 2 ^ exponent 
    
    the value returned by this function is one less than the exponent obtained with `block frexp(number)`_ (because 
    of the different significand normalization as [1.0,2.0) instead of [0.5,1.0))
    
    
    **Parameters**
      number : Number
       the value whose ilogb is returned
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the base-2 logarithm of the number 


.. index:: 
	pair: Math.sim; block log1p(number)

====================
block log1p(number)
====================
**Source**: `block log1p(number) Source`_.
    
    Determine the natural logarithm of one plus the number. for small magnitude values of number, 
    `block log1p(number)`_ may be more accurate than `block log(number)`_ ``log( 1 + x )``
    
    
    **Parameters**
      number : Number
       the value whose logarithm is calculated
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
      `final $MathLessThanMinusOne`_ with title `final $MathModule`_ if the parameter is less than -1
      `final $MathNotEqual`_ -1 with title `final $MathModule`_ if the parameter is equals -1
    
    **Return**
      the natural logarithm of ( 1 + number ) 


.. index:: 
	pair: Math.sim; block log2(number)

===================
block log2(number)
===================
**Source**: `block log2(number) Source`_.
    
    Determine the binary (base-2) logarithm of a number
    
    
    **Parameters**
      number : Number
       the value whose logarithm is calculated
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
      `final $MathLessThan`_ 0 with title `final $MathModule`_ if the parameter is less than 0
      `final $MathNotEqual`_ -1 with title `final $MathModule`_ if the parameter is equals -1
    
    **Return**
      binary logarithm of the number : **log2x** 


.. index:: 
	pair: Math.sim; block logb(number)

===================
block logb(number)
===================
**Source**: `block logb(number) Source`_.
    
    Determine the the logarithm of a number, using 2 as base for the logarithm. Almost equivalent to 
    `block log2(number)`_ for positive number
    
    
    **Parameters**
      number : Number
       the value whose logarithm is calculated
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      base 2 algorith of a nuber  


.. index:: 
	pair: Math.sim; block scalbln(number,exp)

==========================
block scalbln(number,exp)
==========================
**Source**: `block scalbln(number,exp) Source`_.
    
    Scales a number by 2 raised to the power of n, returning the result of computing:
    
    .. code-block:: simple
    	
      scalbn(x,n) = x * 2
    
    Presumably, the number and n are the components of a floating-point number in the system; In such a case, this 
    block may be optimized to be more efficient than the theoretical operations to compute the value explicitly
    
    
    **Parameters**
      number : Number
       the value representing the significand
      exp : Number 
       the value of the exponent
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      x * 2 ^ n  


.. index:: 
	pair: Math.sim; block hypot(x,y)

=================
block hypot(x,y)
=================
**Source**: `block hypot(x,y) Source`_.
    
    Determine what would be the square root of the sum of the squares of x and y (as per the Pythagorean theorem), 
    but without incurring in undue overflow or underflow of intermediate values
    
    **Parameters**
      x : Number
       the floating point values corresponding to x of a right-angled triangle
      y : Number
       the floating point values corresponding to y of a right-angled triangle
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the hypotenuse of a right-angled triangle whose legs are x and y


.. index:: 
	pair: Math.sim; block numsign(number)

======================
block numsign(number)
======================
**Source**: `block numsign(number) Source`_.
    
    Determine the sign of the number in the following format
    
    * If the number is greater than zero, 1.0 is returned
    * If the number is less than zero, -1.0 is returned
    * If the number is 1.0 or -1.0 the same value is returned
    
    
    **Parameters**
      number : Number
       the number
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number
    
    **Return**
      the sign of the number


.. index:: 
	pair: Math.sim; block vmDecimalPoints(place)

=============================
block vmDecimalPoints(place)
=============================
**Source**: `block vmDecimalPoints(place) Source`_.
    
    By Default all decimal number in simple-lang is round down to 2 floating point. This block changes the number of 
    floating point decimal are rounded to. Using this block make all the number through out the program have the number
    of floating point sent as paraneter.
    
    **Parameters**
      place : Number
       the number of floating point for all numbers
    
    **Throws**
      `final $MathNotNumber`_ with title `final $MathModule`_ if the parameter is not a Number


.. index:: 
	pair: Math.sim; block random()

===============
block random()
===============
**Source**: `block random() Source`_.
    
    Generate a random number



-------

.

Below are blocks exposed from the `Mathic dynamic module`_

============= ====================================================================================================================
 __sin         Determine sine of a number. Use `block sin(number)`_
 __cos         Determine cosine of a number. `block cos(number)`_ 
 __tan         Determine tangent of a number. Use `block tan(number)`_
 __asin        Determine arc sine of a number. Use `block asin(number)`_
 __acos        Determine arc cosine of a number. Use `block acos(number)`_
 __atan        Determine arc tangent of a number. Use `block atan(number)`_
 __atan2       Determine arc tangent of a number with two parameters . Use `block atan2(y, x)`_
 __sinh        Determine hyperbolic sine of a number. Use `block sinh(number)`_
 __cosh        Determine hyperbolic cosine of a number. Use `block cosh(number)`_
 __tanh        Determine hyperbolic tangent of a number . Use `block tanh(number)`_
 __asinh       Determine area hyperbolic sine of a number. Use `block asinh(number)`_
 __acosh       Determine area hyperbolic cosine of a number. Use `block acosh(number)`_
 __atanh       Determine area hyperbolic tangent of a number . Use `block atanh(number)`_
 __rint        Round a number to integral value. Use `block rint(number)`_
 __round       Round a number to nearest. Use `block round(number)`_
 __floor       Round a number down. Use `block floor(number)`_
 __ceil        Round a number up. Use `block ceil(number)`_
 __fmod        Determine remainder of division . Use `block fmod(fNumber,sNumber)`_
 __trunc       Truncate a number . Use `block trunc(number)`_
 __remainder   Determine remainder of an operation. Use `block remainder(fNumber,sNumber)`_
 __exp         Determine a number exponential value . Use `block exp(number)`_
 __log         Determine a number natural logarithm . Use `block log(number)`_
 __log10       Determine a number common logarithm. Use `block log10(number)`_
 __frexp       Get a number significand and exponent. Use `block frexp(number)`_
 __ldexp       Generate value from a significand and exponent. Use `block ldexp(number,exp)`_
 __modf        Break a number into fractional and integral parts. Use `block modf(number)`_
 __exp2        Determine a number binary logarithm. Use `block exp2(number)`_
 __expm1       Compute a number exponential minus one. Use `block expm1(number)`_
 __ilogb       Determine a number integer binary logarithm. Use `block ilogb(number)`_
 __log1p       Compute a number logarithm plus one. Use `block log1p(number)`_
 __log2        Determine a number binary logarithm . Use `block log2(number)`_
 __logb        Determine a number floating-point base logarithm. Use `block logb(number)`_
 __scalbn      Determine a number scale significand using floating-point base exponent. Use `block scalbln(number,exp)`_
 __scalbln     Determine a number scale significand using floating-point base exponent (long). Use `block scalbln(number,exp)`_
 __pow         Raise a number to a power. Use `block pow(fNumber,sNumber)`_
 __sqrt        Compute a number square root. Use `block sqrt(number)`_
 __cbrt        Compute a number cube root. Use `block cbrt(number)`_
 __hypot       Determine a number hypotenuse value. Use `block hypot(x,y)`_
 __rand        Generate a random number. Use `block random()`_
 __decimals    Change the number of floating point of decimal numbers. Use `block vmDecimalPoints(place)`_
 __fabs        Compute a number absolute value. Use `block abs(number)`_
============= ====================================================================================================================

.. _Mathic dynamic module: https://github.com/simple-lang/simple/tree/master/modules/dynamic_modules/mathic
.. _simple.util.Math Test: https://github.com/simple-lang/simple/blob/master/examples/modules_test/simple/util/math.sim


.

.. _module simple.util Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L31
.. _Called Modules Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L36
.. _final MathE Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L47
.. _final MathPI Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L58
.. _final $MathModule Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L63
.. _final $MathNotNumber Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L68
.. _final $MathLessThan Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L73
.. _final $MathLessThanOne Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L78
.. _final $MathLessThanMinusOne Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L83
.. _final $MathNotBetweenOne Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L89
.. _final $MathNotEqual Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L94
.. _block MathE() Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L106
.. _block MathPI() Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L120
.. _block abs(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L137
.. _block min(fNumber, sNumber) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L165
.. _block max(fNumber, sNumber) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L195
.. _block sin(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L221
.. _block cos(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L243
.. _block tan(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L264
.. _block asin(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L285
.. _block acos(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L306
.. _block atan(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L327
.. _block atan2(y, x) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L352
.. _block sinh(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L373
.. _block cosh(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L393
.. _block tanh(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L413
.. _block asinh(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L434
.. _block acosh(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L455
.. _block atanh(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L482
.. _block exp(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L509
.. _block log(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L530
.. _block sqrt(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L551
.. _block cbrt(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L572
.. _block pow(fNumber,sNumber) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L596
.. _block ceil(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L620
.. _block floor(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L643
.. _block rint(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L664
.. _block round(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L685
.. _block nearbyint(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L706
.. _block fmod(fNumber,sNumber) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L729
.. _block remainder(fNumber,sNumber) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L752
.. _block trunc(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L772
.. _block toRadians(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L792
.. _block toDegrees(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L812
.. _block log10(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L833
.. _block frexp(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L864
.. _block ldexp(number,exp) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L887
.. _block modf(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L908
.. _block exp2(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L929
.. _block expm1(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L949
.. _block ilogb(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L978
.. _block log1p(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L1001
.. _block log2(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L1029
.. _block logb(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L1057
.. _block scalbln(number,exp) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L1086
.. _block hypot(x,y) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L1108
.. _block numsign(number) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L1133
.. _block vmDecimalPoints(place) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L1156
.. _block random() Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Math.sim#L1165

