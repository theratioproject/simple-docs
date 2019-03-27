
.. index:: 
	single: Imports
	
Imports
========

The ``import`` keyword is used to import a module into the current source. 
All global variable from the module will be added to the global context of the 
current source 

the two import statement can be written in one line as ``import simple.core, simple.io``

.. code-block:: simple 

	call "simple/io/File.sim"
	import simple.core
	import simple.io

	block main()
		file = new File("../testfiles/text.txt")
		display file.toString()