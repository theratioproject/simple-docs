
.. index:: 
	single: Calls
	
Calls
========

The ``call`` statement behavior is different from the ``import`` in simple. ``call`` read the 
source of the called file into the current source at compile time while ``import`` try to resolve 
module at runtime

.. code-block:: simple 

	call "simple/util/Math.sim"
	import simple.util

	block main()
		display cos(30) + sin(50)

Calling a module with literal will require the modules in the called file to be imported manually.
To compactly import the Math module below the call statement can be written as 

.. code-block:: simple 

	call simple.util.Math 

	block main()
		display cos(30) + sin(50)