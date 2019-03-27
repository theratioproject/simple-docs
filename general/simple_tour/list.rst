
.. index:: 
	single: List
	
List
===========

List is a true type in simple and can hold any value or object

.. code-block:: simple

	block main()
		list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		display list
		
A list can be created then populated with values, the **:** can be used to between a start and end 
number to create a list

.. code-block:: simple

	block main()
		list = 0:1
		list[0] = "Hello "
		list[1] = "World!"
		
		display list[0] + list [1]
		
