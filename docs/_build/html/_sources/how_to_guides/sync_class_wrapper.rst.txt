================================
Sync Functions in Class Wrapper 
================================

The class wrapper provides sync functions to be used in your application. 

For generating password hashes use the following:

.. code-block:: python 

    password = 'bcrypt'

    pw_hash = bcrypt.generate_password_hash(password)

For checking passwords against the hashed password use the following:

.. code-block:: python 

    password = 'bcrypt'

    pw_hash = bcrypt.generate_password_hash(passwrd)

    bcrypt.check_password_hash(password, pw_hash)