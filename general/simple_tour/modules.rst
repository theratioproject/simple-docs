
.. index:: 
	single: Modules
	
Modules
========

modules are compose of various source code and classes that perform similar functions 

The sample code below uses the `simple.util.Console` module to print to standard output stream 
and use the `sin` block from the `simple.util.Math` module

The Module name is the combination of the path to the source file e.g the `simple.util.Console` 
module 

* simple 
	* util
		* Console.sim 

.. code-block:: simple 

	call simple.util.Console
	call simple.util.Math
	import simple.core

	block main()
		sinFifty = sin(360)
		stdout.println("Sin 360=" + sinFifty)