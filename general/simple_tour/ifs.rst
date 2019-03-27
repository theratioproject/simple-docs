
.. index:: 
	single: Ifs
	
Ifs
===========

If statement can be defined like below

.. code-block:: simple

	block main()
		number = 12
		if number > 10 {
			display "The number is 12 "
		}
		
		
If..Else
----------

The statement in the else block is executed if the condition of the ``if`` block is not satisfied

.. code-block:: simple

	block main()
		number = 12
		if number == 10 {
			display "The number is 10 "
			
		else
			display "Not determined. Number=" + number
		}
		

If..Elif..Else
---------------

Chains of if elif else can be combined to create a more option conditional block

.. code-block:: simple

	block main()
		number = 12
		if number == 10 {
			display "The number is 10 "
			
		elif number == 11
			display "The number is 11 "
			
		elif number == 12
			display "The number is 12 "
			
		elif number == 13
			display "The number is 13 "
			
		else
			display "Not determined. Number=" + number
		}
