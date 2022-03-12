==============
General Useage 
==============

To use the extension simply import the class wrapper and pass the Quart app
object back to here. Do so like this:

.. code-block:: python 

    from quart import Quart
    from quart_bcrypt import Bcrypt

    app = Quart(__name__)
    bcrypt = Bcrypt(app)

If you have your application in a application function or need to pass the Quart
app later:

.. code-block:: python 

    bcrypt.init_app(app)

