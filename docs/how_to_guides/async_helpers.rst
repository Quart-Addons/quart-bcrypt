.. _async_helpers:

================================
Async Helper Functions 
================================

Quart-Bcrypt provides async helper functions that wraps the
method of the Bcrypt class. They are intended as a helper function
at the expense of the configuration variables provided when passing
the Quart app object. In another words these shortcuts does not make
use of the app object at all. 

For generating password hashes use the following:

.. code-block:: python 

    from quart_bcrypt import async_generate_password_hash

    password = 'bcrypt'

    pw_hash = await async_generate_password_hash(password)

For checking passwords against the hashed password use the following:

.. code-block:: python 

    from quart_bcrypt import async_generate_password_hash, async_check_password_hash

    password = 'bcrypt'

    pw_hash = await async_generate_password_hash(passwrd)

    await async_check_password_hash(password, pw_hash)

.. Note::
    Quart-Bcrypt uses Quarts run_sync method to wrap the generate password 
    hash and check password hash functions, so they run within the event loop. 
    Refer to the `Quart how to guide <https://quart.palletsprojects.com/en/latest/how_to_guides/sync_code.html>`_  
    for additional information. 