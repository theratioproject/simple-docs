
.. index:: 
	single: Switch
	
Switch
===========

switch in simple is just the ones in other languages with the exception that only the 
satisfied case is run and no break is required in a case. 

The cases can be anything evaluated function, string, number, list e.t.c

.. code-block:: simple

	block main()
		number = 5
		
		switch number {
		case 1
			display "Number 1"
			
		case check(2, 3)
			display "Number is 5"
			
		case 30
			display "Number is 30"
			
		default
			display "Unknown Number=" + number
			
		}
		
		block check(x, y)
			return x + y