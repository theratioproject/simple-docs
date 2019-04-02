
.. index:: 
	single: simple.util.ConsoleColor

=========================
simple.util.ConsoleColor
=========================

This module holds the color values for the terminal. It does not use the Red-Green-Blue (RGB) 
standard it rather uses color bit of 5 to determine and differentiate between foreground 
and background of the color. 

The color can be used as first argument for the `simple.io.PrintWriter.printfc(...)`_ and 
`simple.io.PrintWriter.printbc(...)`_ , the first which deal with the forground and the 
later to change the background.

Example 

.. code-block:: simple

  call simple.util.Console
  import simple.core
	
  stdout.printfc()
	
The color will only be applied to the terminal or console if it is supported, the console color
will be neglected if the standard stream it not supported like logging to file or usage in CGI.  

:copyright: 2018-2019, Azeez Adewale
:license: MIT License Copyright (c) 2018 simple
:author: Azeez Adewale <azeezadewale98@gmail.com>
:date: 11 Febuary 2017
:time: 
:filename: ConsoleColor.sim


================
Table Of Content
================
========================================= =============================================================================
 Fields/Blocks/Classes                     Summary                                                                     
========================================= =============================================================================
 `final ConsoleColorNone`_                 Constant for the default console color of the terminal                      
 `final ConsoleColorBlack`_                Constant for console color black                                            
 `final ConsoleColorDarkRed`_              Constant for console color dark red                                         
 `final ConsoleColorDarkGreen`_            Constant for console color dark green                                       
 `final ConsoleColorDarkYellow`_           Constant for console color dark yellow                                      
 `final ConsoleColorDarkBlue`_             Constant for console color dark blue                                        
 `final ConsoleColorDarkMagenta`_          Constant for console color dark magenta                                     
 `final ConsoleColorDarkCyan`_             Constant for console color dark cyan                                        
 `final ConsoleColorGray`_                 Constant for console color gray                                             
 `final ConsoleColorDarkGray`_             Constant for console color dark gray                                        
 `final ConsoleColorRed`_                  Constant for console color red                                              
 `final ConsoleColorGreen`_                Constant for console color green                                            
 `final ConsoleColorYellow`_               Constant for console color yellow                                           
 `final ConsoleColorBlue`_                 Constant for console color blue                                             
 `final ConsoleColorMagenta`_              Constant for console color magenta                                          
 `final ConsoleColorCyan`_                 Constant for console color cyan                                             
 `final ConsoleColorWhite`_                Constant for console color white                                            
 `class ConsoleColor inherit Object`_      The class that holds the console color constants for usage as field calls   
 `final None`_                                 Constant for the default console color of the terminal                  
 `final Black`_                                Constant for console color black                                        
 `final DarkRed`_                              Constant for console color dark red                                     
 `final DarkGreen`_                            Constant for console color dark green                                   
 `final DarkYellow`_                           Constant for console color dark yellow                                  
 `final DarkBlue`_                             Constant for console color dark blue                                    
 `final DarkMagenta`_                          Constant for console color dark magenta                                 
 `final DarkCyan`_                             Constant for console color dark cyan                                    
 `final Gray`_                                 Constant for console color gray                                         
 `final DarkGray`_                             Constant for console color dark gray                                    
 `final Red`_                                  Constant for console color red                                          
 `final Green`_                                Constant for console color green                                        
 `final Yellow`_                               Constant for console color yellow                                       
 `final Blue`_                                 Constant for console color blue                                         
 `final Magenta`_                              Constant for console color magenta                                      
 `final Cyan`_                                 Constant for console color cyan                                         
 `final White`_                                Constant for console color white                                        
 `final none`_                                 Constant for the default console color of the terminal                  
 `final black`_                                Constant for console color black                                        
 `final darkred`_                              Constant for console color dark red                                     
 `final darkgreen`_                            Constant for console color dark green                                   
 `final darkyellow`_                           Constant for console color dark yellow                                  
 `final darkblue`_                             Constant for console color dark blue                                    
 `final darkmagenta`_                          Constant for console color dark magenta                                 
 `final darkcyan`_                             Constant for console color dark cyan                                    
 `final gray`_                                 Constant for console color gray                                         
 `final darkgray`_                             Constant for console color dark gray                                    
 `final red`_                                  Constant for console color red                                          
 `final green`_                                Constant for console color green                                        
 `final yellow`_                               Constant for console color yellow                                       
 `final blue`_                                 Constant for console color blue                                         
 `final magenta`_                              Constant for console color magenta                                      
 `final cyan`_                                 Constant for console color cyan                                         
 `final white`_                                Constant for console color white                                        
========================================= =============================================================================


.. index:: 
	pair: ConsoleColor.sim; final ConsoleColorNone

=======================
final ConsoleColorNone
=======================
**Source**: `final ConsoleColorNone Source`_.
    
    Constant for the default console color of the terminal


.. index:: 
	pair: ConsoleColor.sim; final ConsoleColorBlack

========================
final ConsoleColorBlack
========================
**Source**: `final ConsoleColorBlack Source`_.
    
    Constant for console color black


.. index:: 
	pair: ConsoleColor.sim; final ConsoleColorDarkRed

==========================
final ConsoleColorDarkRed
==========================
**Source**: `final ConsoleColorDarkRed Source`_.
    
    Constant for console color dark red


.. index:: 
	pair: ConsoleColor.sim; final ConsoleColorDarkGreen

============================
final ConsoleColorDarkGreen
============================
**Source**: `final ConsoleColorDarkGreen Source`_.
    
    Constant for console color dark green


.. index:: 
	pair: ConsoleColor.sim; final ConsoleColorDarkYellow

=============================
final ConsoleColorDarkYellow
=============================
**Source**: `final ConsoleColorDarkYellow Source`_.
    
    Constant for console color dark yellow


.. index:: 
	pair: ConsoleColor.sim; final ConsoleColorDarkBlue

===========================
final ConsoleColorDarkBlue
===========================
**Source**: `final ConsoleColorDarkBlue Source`_.
    
    Constant for console color dark blue


.. index:: 
	pair: ConsoleColor.sim; final ConsoleColorDarkMagenta

==============================
final ConsoleColorDarkMagenta
==============================
**Source**: `final ConsoleColorDarkMagenta Source`_.
    
    Constant for console color dark magenta


.. index:: 
	pair: ConsoleColor.sim; final ConsoleColorDarkCyan

===========================
final ConsoleColorDarkCyan
===========================
**Source**: `final ConsoleColorDarkCyan Source`_.
    
    Constant for console color dark cyan


.. index:: 
	pair: ConsoleColor.sim; final ConsoleColorGray

=======================
final ConsoleColorGray
=======================
**Source**: `final ConsoleColorGray Source`_.
    
    Constant for console color gray


.. index:: 
	pair: ConsoleColor.sim; final ConsoleColorDarkGray

===========================
final ConsoleColorDarkGray
===========================
**Source**: `final ConsoleColorDarkGray Source`_.
    
    Constant for console color dark gray


.. index:: 
	pair: ConsoleColor.sim; final ConsoleColorRed

======================
final ConsoleColorRed
======================
**Source**: `final ConsoleColorRed Source`_.
    
    Constant for console color red


.. index:: 
	pair: ConsoleColor.sim; final ConsoleColorGreen

========================
final ConsoleColorGreen
========================
**Source**: `final ConsoleColorGreen Source`_.
    
    Constant for console color green


.. index:: 
	pair: ConsoleColor.sim; final ConsoleColorYellow

=========================
final ConsoleColorYellow
=========================
**Source**: `final ConsoleColorYellow Source`_.
    
    Constant for console color yellow


.. index:: 
	pair: ConsoleColor.sim; final ConsoleColorBlue

=======================
final ConsoleColorBlue
=======================
**Source**: `final ConsoleColorBlue Source`_.
    
    Constant for console color blue


.. index:: 
	pair: ConsoleColor.sim; final ConsoleColorMagenta

==========================
final ConsoleColorMagenta
==========================
**Source**: `final ConsoleColorMagenta Source`_.
    
    Constant for console color magenta


.. index:: 
	pair: ConsoleColor.sim; final ConsoleColorCyan

=======================
final ConsoleColorCyan
=======================
**Source**: `final ConsoleColorCyan Source`_.
    
    Constant for console color cyan


.. index:: 
	pair: ConsoleColor.sim; final ConsoleColorWhite

========================
final ConsoleColorWhite
========================
**Source**: `final ConsoleColorWhite Source`_.
    
    Constant for console color white


.. index:: 
	pair: ConsoleColor.sim; class ConsoleColor inherit Object

==================================
class ConsoleColor inherit Object
==================================
**Source**: `class ConsoleColor inherit Object Source`_.
    
    The class that holds the console color constants for usage as field calls


.. index:: 
	pair: ConsoleColor.sim; final None

-----------
final None
-----------
**Source**: `final None Source`_.
    
        Constant for the default console color of the terminal


.. index:: 
	pair: ConsoleColor.sim; final Black

------------
final Black
------------
**Source**: `final Black Source`_.
    
        Constant for console color black


.. index:: 
	pair: ConsoleColor.sim; final DarkRed

--------------
final DarkRed
--------------
**Source**: `final DarkRed Source`_.
    
        Constant for console color dark red


.. index:: 
	pair: ConsoleColor.sim; final DarkGreen

----------------
final DarkGreen
----------------
**Source**: `final DarkGreen Source`_.
    
        Constant for console color dark green


.. index:: 
	pair: ConsoleColor.sim; final DarkYellow

-----------------
final DarkYellow
-----------------
**Source**: `final DarkYellow Source`_.
    
        Constant for console color dark yellow


.. index:: 
	pair: ConsoleColor.sim; final DarkBlue

---------------
final DarkBlue
---------------
**Source**: `final DarkBlue Source`_.
    
        Constant for console color dark blue


.. index:: 
	pair: ConsoleColor.sim; final DarkMagenta

------------------
final DarkMagenta
------------------
**Source**: `final DarkMagenta Source`_.
    
        Constant for console color dark magenta


.. index:: 
	pair: ConsoleColor.sim; final DarkCyan

---------------
final DarkCyan
---------------
**Source**: `final DarkCyan Source`_.
    
        Constant for console color dark cyan


.. index:: 
	pair: ConsoleColor.sim; final Gray

-----------
final Gray
-----------
**Source**: `final Gray Source`_.
    
        Constant for console color gray


.. index:: 
	pair: ConsoleColor.sim; final DarkGray

---------------
final DarkGray
---------------
**Source**: `final DarkGray Source`_.
    
        Constant for console color dark gray


.. index:: 
	pair: ConsoleColor.sim; final Red

----------
final Red
----------
**Source**: `final Red Source`_.
    
        Constant for console color red


.. index:: 
	pair: ConsoleColor.sim; final Green

------------
final Green
------------
**Source**: `final Green Source`_.
    
        Constant for console color green


.. index:: 
	pair: ConsoleColor.sim; final Yellow

-------------
final Yellow
-------------
**Source**: `final Yellow Source`_.
    
        Constant for console color yellow


.. index:: 
	pair: ConsoleColor.sim; final Blue

-----------
final Blue
-----------
**Source**: `final Blue Source`_.
    
        Constant for console color blue


.. index:: 
	pair: ConsoleColor.sim; final Magenta

--------------
final Magenta
--------------
**Source**: `final Magenta Source`_.
    
        Constant for console color magenta


.. index:: 
	pair: ConsoleColor.sim; final Cyan

-----------
final Cyan
-----------
**Source**: `final Cyan Source`_.
    
        Constant for console color cyan


.. index:: 
	pair: ConsoleColor.sim; final White

------------
final White
------------
**Source**: `final White Source`_.
    
        Constant for console color white


.. index:: 
	pair: ConsoleColor.sim; final none

-----------
final none
-----------
**Source**: `final none Source`_.
    
        Constant for the default console color of the terminal


.. index:: 
	pair: ConsoleColor.sim; final black

------------
final black
------------
**Source**: `final black Source`_.
    
        Constant for console color black


.. index:: 
	pair: ConsoleColor.sim; final darkred

--------------
final darkred
--------------
**Source**: `final darkred Source`_.
    
        Constant for console color dark red


.. index:: 
	pair: ConsoleColor.sim; final darkgreen

----------------
final darkgreen
----------------
**Source**: `final darkgreen Source`_.
    
        Constant for console color dark green


.. index:: 
	pair: ConsoleColor.sim; final darkyellow

-----------------
final darkyellow
-----------------
**Source**: `final darkyellow Source`_.
    
        Constant for console color dark yellow


.. index:: 
	pair: ConsoleColor.sim; final darkblue

---------------
final darkblue
---------------
**Source**: `final darkblue Source`_.
    
        Constant for console color dark blue


.. index:: 
	pair: ConsoleColor.sim; final darkmagenta

------------------
final darkmagenta
------------------
**Source**: `final darkmagenta Source`_.
    
        Constant for console color dark magenta


.. index:: 
	pair: ConsoleColor.sim; final darkcyan

---------------
final darkcyan
---------------
**Source**: `final darkcyan Source`_.
    
        Constant for console color dark cyan


.. index:: 
	pair: ConsoleColor.sim; final gray

-----------
final gray
-----------
**Source**: `final gray Source`_.
    
        Constant for console color gray


.. index:: 
	pair: ConsoleColor.sim; final darkgray

---------------
final darkgray
---------------
**Source**: `final darkgray Source`_.
    
        Constant for console color dark gray


.. index:: 
	pair: ConsoleColor.sim; final red

----------
final red
----------
**Source**: `final red Source`_.
    
        Constant for console color red


.. index:: 
	pair: ConsoleColor.sim; final green

------------
final green
------------
**Source**: `final green Source`_.
    
        Constant for console color green


.. index:: 
	pair: ConsoleColor.sim; final yellow

-------------
final yellow
-------------
**Source**: `final yellow Source`_.
    
        Constant for console color yellow


.. index:: 
	pair: ConsoleColor.sim; final blue

-----------
final blue
-----------
**Source**: `final blue Source`_.
    
        Constant for console color blue


.. index:: 
	pair: ConsoleColor.sim; final magenta

--------------
final magenta
--------------
**Source**: `final magenta Source`_.
    
        Constant for console color magenta


.. index:: 
	pair: ConsoleColor.sim; final cyan

-----------
final cyan
-----------
**Source**: `final cyan Source`_.
    
        Constant for console color cyan


.. index:: 
	pair: ConsoleColor.sim; final white

------------
final white
------------
**Source**: `final white Source`_.
    
        Constant for console color white



-------

.


.. _simple.io.PrintWriter.printfc(...): ../io/PrintWriter.html#printfc
.. _simple.io.PrintWriter.printbc(...): ../io/PrintWriter.html#printbc


.

.. _final ConsoleColorNone Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L41
.. _final ConsoleColorBlack Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L46
.. _final ConsoleColorDarkRed Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L51
.. _final ConsoleColorDarkGreen Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L56
.. _final ConsoleColorDarkYellow Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L61
.. _final ConsoleColorDarkBlue Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L66
.. _final ConsoleColorDarkMagenta Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L71
.. _final ConsoleColorDarkCyan Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L76
.. _final ConsoleColorGray Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L81
.. _final ConsoleColorDarkGray Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L86
.. _final ConsoleColorRed Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L91
.. _final ConsoleColorGreen Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L96
.. _final ConsoleColorYellow Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L101
.. _final ConsoleColorBlue Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L106
.. _final ConsoleColorMagenta Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L111
.. _final ConsoleColorCyan Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L116
.. _final ConsoleColorWhite Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L121
.. _class ConsoleColor inherit Object Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L126
.. _final None Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L131
.. _final Black Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L136
.. _final DarkRed Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L141
.. _final DarkGreen Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L146
.. _final DarkYellow Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L151
.. _final DarkBlue Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L156
.. _final DarkMagenta Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L161
.. _final DarkCyan Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L166
.. _final Gray Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L171
.. _final DarkGray Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L176
.. _final Red Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L181
.. _final Green Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L186
.. _final Yellow Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L191
.. _final Blue Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L196
.. _final Magenta Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L201
.. _final Cyan Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L206
.. _final White Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L211
.. _final none Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L216
.. _final black Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L221
.. _final darkred Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L226
.. _final darkgreen Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L231
.. _final darkyellow Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L236
.. _final darkblue Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L241
.. _final darkmagenta Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L246
.. _final darkcyan Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L251
.. _final gray Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L256
.. _final darkgray Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L261
.. _final red Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L266
.. _final green Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L271
.. _final yellow Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L276
.. _final blue Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L281
.. _final magenta Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L286
.. _final cyan Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L291
.. _final white Source: https://github.com/simple-lang/simple/tree/master/modules/simple/util/ConsoleColor.sim#L296

