
.. index:: 
	single: Loops
	
Loops
===========

simple has various looping constructs. 


For Loop
--------- 

The basic for loop has two component, the declared variable with initial value 
and the expression

.. code-block:: simple

	block main()
		for a = 0 to 100 {
			display a
		}
		
		
For..In Loop 
-------------

The **for..in** loop is used to iterate over a list type of an object that 
added support for iteration through the `operator` method

.. code-block:: simple

	block main()
		for number in [1,2,3,4,5,6,7,8,9,0] {
			display number
		}
		
While Loop
-----------

While loop construct consists of the conditional expression which if satisfied the while 
block will be executed

.. code-block:: simple
	
	block main()
		index = 0
		while index <= 10 {
			display index
			index++
		}
		
		
Do..While Loop
---------------
	
The Do..While loop always executes the block and continue it execution if the while condition is satisfied

.. code-block:: simple

	block main()
		index = 30
		do {
			display index
			index--
			
		} while index > 20
