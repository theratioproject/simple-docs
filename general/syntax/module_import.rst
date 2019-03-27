
.. index:: 
	single: module and import
	
module and import
==================

simple encourages organization such that you can write clean code that is structural arranged. 
Program can be group into modules which can be called into other code using the ``import`` keyword. 
A ``module`` can be imported before it is declared, module not found exception will be thrown if the 
module is not defined in the program.


module
-------

A module can be declared using the ``module`` keyword at any location in a source program. A single 
source code can contain more than one module that can be accessed by importing the module within the 
source or using the absolute value.

.. code-block:: simple 

	import internal.deep.package
	
		block main()
			m = new InternalClass
			
	module internal.deep.package

		class InternalClass
		
The above program can also be re written by using the absolute class name instead of importing the module 

.. code-block:: simple 

	block main()
		m = new internal.deep.package.InternalClass
			
	module internal.deep.package

		class InternalClass
		
.. Expand please


import
-------