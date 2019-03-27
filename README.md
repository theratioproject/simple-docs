# simple Documentation

The Documentation for simple (simple intelligent and modular programming language and environment)

This repository contains the documentation for simple in reStructuredText (reST). 

The [modules](./modules/) and [examples](./examples/) reStructuredText docs are auto generated from the 
simple source using the [akosile](https://github.com/simple-lang/akosile) program. 

They are meant to be parsed with the [Sphinx](https://sphinx-doc.org/) documentation builder to build the 
HTML documentation on simple's website.

- [Contributing](#contributing)
- [Editing existing pages](#editing-existing-pages)
- [Adding new pages](#adding-new-pages)
- [Sphinx and reStructuredText syntax](#sphinx-and-restructuredtext-syntax)
- [Adding images and attachments](#adding-images-and-attachments)
- [Generating examples and modules documentation](#generating-examples-and-modules-documentation)
- [Building with Sphinx](#building-with-sphinx)
- [Building with Sphinx on Windows](#building-with-sphinx-on-windows)
- [License](#license)

## Contributing

Pull request should use the master branch by default. Only make Pull request against other branches if the 
changes apply to that specific version.

## Editing existing pages

To edit an existing page, locate its .rst source file and open it in your favorite text editor. 
You can then commit the changes, push them to your fork and make a pull request. 

Note that the pages in [modules](./modules/) and [examples](./examples/) should never be edited here as it is auto generated 
the .rst file to modify from the [modules](./modules/) and [examples](./examples/) folder should be edited in the .sim source 
in the [main simple repository](https://github.com/simple-lang/simple) and send the pull request to the 
[main simple repository](https://github.com/simple-lang/simple).

## Adding new pages

To add a new page, create a .rst file with a meaningful name in the section you want to add a file to, 
e.g. general/about/new_page_doc.rst. Write its content like you would do for any other file, and make sure to define a 
reference name for Sphinx at the beginning of the file (check other files for the syntax).

You should then add your page to the relevant "toctree" (table of contents, e.g. general/about/index.rst). 
By convention, the files used to define the various levels of toctree are prefixed with an underscore. 
so in the above example the file should be referenced in general/about/new_page_doc.rst.. 
Add your new filename to the list on a new line, using a relative path and no extension, e.g. here new_page_doc.

## Sphinx and reStructuredText syntax

Check Sphinx's reST Primer and the official reference for details on the syntax.

Sphinx uses specific reST comments to do specific operations, like defining the table of contents (:toctree:) or 
cross-referencing pages. Check the official Sphinx documentation for more details, or see how things are done 
in existing pages and adapt it to your needs.

## Adding images and attachments

To add images, please put them in an img/ folder next to the .rst file with a meaningful name and include them in your page with:

```rst
.. image:: img/image_name.png
```

Similarly, you can include attachments (like assets as support material for a tutorial) by placing them into a 
files/ folder next to the .rst file, and using this inline markup:

```rst
:download:`myfile.zip <files/myfile.zip>`
```

## Generating examples and modules documentation

To generate the examples/ and modules/ folder documentation clone the [akosile](https://github.com/simple-lang/akosile) 
compile and install the akosile program with:

```
git clone https://github.com/simple-lang/akosile
cd akosile
bake --install akosile.sim
```

The akosile program will be installed to the same folder as simple and can be executed from any folder, 
generate the docs with the following command

```bash
cd simple-docs
akosile conf.sim
```

The examples and modules folder can be generated independently with:

```bash
cd simple/modules
akosile conf.sim
```

```bash
cd simple/examples
akosile conf.sim
```

The build instruction above expects the simple-doc and simple main repository to be cloned in the same directory 

- simple 
	- build
	- modules
	- examples
	- ..
	
- simple-docs
	- ..

## Building with Sphinx

To build the HTML website (or any other format supported by Sphinx, like PDF, EPUB or LaTeX), 
you need to install Sphinx >= 1.3. Only the Python 3 flavor was tested, though the Python 2 versions might work too.

Those tools are best installed using pip, Python's module installer. The Python 3 version might be 
provided (on Linux distros) as pip3 or python3-pip. You can then run:

```bash
pip3 install sphinx
```

You can then build the HTML documentation from the root folder of this repository with:

```bash 
make html
```

## Building with Sphinx on Windows

On Windows, you need to:

- Download the Python installer [here](https://www.python.org/downloads/).
- Install Python. Don't forget to check the "Add Python to PATH" box.
- Use the above pip commands.
	
Building is still done at the root folder of this repository using the provided make.bat:

```powershell
make.bat html
```

Alternatively, you can build with this command instead:

```powershell
sphinx-build -b html ./ _build
```

Note that during the first build, various installation prompts may appear and ask to install LaTeX plugins. 
Make sure you don't miss them, especially if they open behind other windows, else the build may appear to 
hang until you confirm these prompts.

You could also install a normal make toolchain (for example via MinGW) and build the docs using the normal make html.

## License

At the exception of the examples/ and modules/ folder, all the content of this repository is licensed under the 
BSD 3-Clause license and is to be attributed to **Azeez Adewale and the Simple community**. See LICENSE for details.

The files in the examples/ and modules/ folder are derived from simple's main source repository and are 
distributed under the MIT license, with the same authors as above.