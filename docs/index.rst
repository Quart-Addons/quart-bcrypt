:orphan:

.. title:: Quart Bcrypt Documentation

.. image:: _static/logo.png
   :width: 300px
   :alt: Quart Bcrypt logo
   :align: right

============
Quart-Bcrypt
============

Quart-Bcrypt is a Quart extension that provides bcrypt hashing utilities for
your application. It provides sync and async capabilities for your application. 

Due to the recent increased prevalence of powerful hardware, such as modern
GPUs, hashes have become increasingly easy to crack. A proactive solution to
this is to use a hash that was designed to be "de-optimized". Bcrypt is such
a hashing facility; unlike hashing algorithms such as MD5 and SHA1, which are
optimized for speed, bcrypt is intentionally structured to be slow.

For sensitive data that must be protected, such as passwords, bcrypt is an
advisable choice.

Quart-Bcrypt is developed on github, `here <https://github.com/crood58/quart-bcrypt>`_ . 

For more information on Quart, `click here <https://pgjones.gitlab.io/quart/>`_ .

Quart-Bcrypt is based on `Flask-Bcrypt <https://github.com/maxcountryman/flask-bcrypt>`_ by maxcountryman. 

Tutorials
---------

.. toctree::
   :maxdepth: 2

   tutorials/index.rst

How to guides
-------------

.. toctree::
   :maxdepth: 2

   how_to_guides/index.rst

References
----------

.. toctree::
   :maxdepth: 2

   references/index.rst



