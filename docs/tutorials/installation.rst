.. _installation:

============
Installation
============

Quart-Bcrypt is only compatible with Python 3.7 or higher, since this is 
what Quart supports. It can be installed using pip or your favorite python 
package manager.

.. code-block:: console

    pip install quart-bcrypt

.. note::
    If you do not have Python 3.7 or better an error message ``Python 3.7
    is the minimum required version`` will be displayed.

.. note::
    You need Python Development Headers to install py-bcrypt package, needed
    as a dependency. If you are on Mac OS or Windows, you probably have it
    already installed. Otherwise look for python-dev package for Debian-based
    distributives and for python-devel package for RedHat-based.

Dependencies
------------

Quart Uploads depends on the following packages, which will automatically
be installed with the extension.

- `Quart <https://quart.palletsprojects.com>`_
- `bcrypt <https://github.com/pyca/bcrypt/>`_ 
