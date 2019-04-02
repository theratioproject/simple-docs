
.. index:: 
	single: simple.util.Length

===================
simple.util.Length
===================

Get the length and size of any type of object the 

:copyright: 2018-2019, Azeez Adewale
:license: MIT License Copyright (c) 2018 simple
:author: Abdulazeez Abdulazeez Adeshina
:date: 04 April 2018
:filename: Length.sim


================
Table Of Content
================
======================================= ======================================================================================================
 Fields/Blocks/Classes                   Summary                                                                                              
======================================= ======================================================================================================
 `block getTypeLength(object obj)`_      Get the length and size of any type of object. The length is determined by the type of the object    
======================================= ======================================================================================================


.. index:: 
	pair: Length.sim; block getTypeLength(object obj)

================================
block getTypeLength(object obj)
================================
**Source**: `block getTypeLength(object obj) Source`_.
    
    Get the length and size of any type of object. The length is determined by the type 
    of the object 
    
    ======== ====================================================================
    String    The number of characters in the string
    List      The number of item in the list 
    Number    The number return itself
    Object    If the class treats the **legthOf** operator the value is returned 
    ======== ====================================================================
    
    **Parameters**:	
      obj : object
       the object to determine it length
    		
    **Return**:
      the length of any object



-------

.
.

.. _block getTypeLength(object obj) Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/Length.sim#L30

