=============
Configuration  
=============

The following configurations values can be set with the application configuration, 
which will be set in Quart-Bcrypt when the Quart App is passed to the extesnion. 

+--------------------------------+------+---------+-------------------------------+
| Config Variable                | Type | Default | Description                   |
+================================+======+=========+===============================+
| `BCRYPT_LOG_ROUNDS`            | int  | 12      | Number of rounds              |
+--------------------------------+------+---------+-------------------------------+
| `BCRYPT_HASH_PREFIX`           | str  | '2b'    | Algorithm version to use.     |
+--------------------------------+------+---------+-------------------------------+
| `BCRYPT_HANDLE_LONG_PASSWORDS` | bool | False   | Handle long passwords or not. |
+--------------------------------+------+---------+-------------------------------+

.. code-block:: python 

    from quart import Quart
    from quart_bcrypt import Bcrypt

    BCRYPT_LOG_ROUNDS = 12 
    BCRYPT_HASH_PREFIX = '2b'
    BCRYPT_HANDLE_LONG_PASSWORDS = False

    app = Quart(__name__)
    app.config.from_file(__name__)
    bcrypt = Bcrypt(app)
