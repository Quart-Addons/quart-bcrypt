.. _async_class_wrapper:

================================
Async Functions in Class Wrapper 
================================

The class wrapper provides async functions to be used in your application. 

For generating password hashes use the following:

.. code-block:: python

    password = 'bcrypt'

    pw_hash = await bcrypt.async_generate_password_hash(password)

For checking passwords against the hashed password use the following:

.. code-block:: python

    password = 'bcrypt'

    pw_hash = await bcrypt.async_generate_password_hash(password)

    await bcrypt.async_check_password_hash(password, pw_hash)

.. Note::
    Quart-Bcrypt uses Quarts run_sync method to wrap the generate password 
    hash and check password hash functions, so they run within the event loop. 
    Refer to the `Quart how to guide <https://quart.palletsprojects.com/en/latest/how_to_guides/sync_code.html>`_  
    for additional information. 


