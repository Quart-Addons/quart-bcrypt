.. _sync_helpers:

================================
Sync Helper Functions 
================================

Quart-Bcrypt provides sync helper functions that wraps eponymous
method of the Bcrypt class. They are intended as a helper function
at the expense of the configuration variables provided when passing
the Quart app object. In another words these shortcuts does not make
use of the app object at all. 

For generating password hashes use the following:

.. code-block:: python 

    from quart_bcrypt import generate_password_hash

    password = 'bcrypt'

    pw_hash = generate_password_hash(password)

For checking passwords against the hashed password use the following:

.. code-block:: python 

    from quart_bcrypt import generate_password_hash, check_password_hash

    password = 'bcrypt'

    pw_hash = generate_password_hash(passwrd)

    check_password_hash(password, pw_hash)