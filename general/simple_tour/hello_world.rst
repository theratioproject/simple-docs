
.. index:: 
	single: Hello World
	
Hello World
=============

The traditional hello world program can be written in simple in just one line using the built in **display** keyword 
which can also function as a block call. 

Using display Keyword
------------------------

.. code-block:: simple

	display "hello world!"
	
Using Built-in display Block
-----------------------------

.. code-block:: simple

	display("hello world!")
	

Using simple.util.Console module
---------------------------------

.. code-block:: simple

	call simple.util.Console 
	import simple.core
	
	stdout.println("hello world!")