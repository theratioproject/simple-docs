
.. index:: 
	single: Constants
	
Constants
===========

Constants in simple are variables which does not change in the program and it can be declared 
using the ``final`` keyword, 

A constant can be of any data type

.. code-block:: simple

	final Const = 123
	
	block main()
		final LocalConst = "local"
		display Const
		display LocalConst
		Const = 30 #error
		