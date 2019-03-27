
.. index:: 
	single: Dictionary
	
Dictionary
===========

A list can be created in such a way it function as a map or dictionary with a key map to a value 

.. code-block:: simple

	block main()
		list = [
				["Home Key", "The House Value "], 
				["Office Key", "The Office Value "]
			]
		display list["Home Key"]
		display list["Office Key"]
		
The value can also be changed at any point in the program

.. code-block:: simple

	block main()
		list = []
		list["Home Key"] = "The House Value "
		list["Office Key"] = "The Office Value "
	
		display list["Home Key"]
		display list["Office Key"]