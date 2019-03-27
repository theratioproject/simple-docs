
.. index:: 
	single: Functions
	
Functions
==========

Functions are pure first-class citizen in simple

A function is declared with the keyword `block`

.. code-block:: simple

	block main()

A function can take zero or more argument

.. code-block:: simple 

	block main()
		display sum(50, 50)
		
	block sum(a, b)
		return a + b
		
Though type is not currently enforced in simple, types can be hinted  

.. code-block:: simple
	
	block sum(int a, int b)
		return a + b
		
Functions can be declared like a variable and called using the ``invoke`` keyword

.. code-block:: simple

	sum = block (a, b) { return a+b }
	
	display (invoke sum(50, 50))

Functions can be sent as parameter, invoke and returned from within another function 

.. code-block:: simple 

	block main()
		value = sum(50, 50, block (x, y) { return x * y } )
		display value
			
	block sum(a, b, func)
		value = a + b
		return invoke func(value, 10) 
		