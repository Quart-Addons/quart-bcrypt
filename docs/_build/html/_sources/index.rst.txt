Quart-Bcrypt
=============

.. module:: quart_bcrypt

Quart-Bcrypt is a Quart extension that provides bcrypt hashing utilities for
your application.

Due to the recent increased prevalence of powerful hardware, such as modern
GPUs, hashes have become increasingly easy to crack. A proactive solution to
this is to use a hash that was designed to be "de-optimized". Bcrypt is such
a hashing facility; unlike hashing algorithms such as MD5 and SHA1, which are
optimized for speed, bcrypt is intentionally structured to be slow.

For sensitive data that must be protected, such as passwords, bcrypt is an
advisable choice.

.. _Quart-Bcrypt: https://github.com/crood58/quart-bcrypt
.. _Quart: https://pgjones.gitlab.io/quart/

Installation
------------

Install the extension with one of the following commands:

    $ pip3 install quart-bcrypt

.. note::
    You need Python Development Headers to install py-bcrypt package, needed
    as a dependency. If you are on Mac OS or Windows, you probably have it
    already installed. Otherwise look for python-dev package for Debian-based
    distributives and for python-devel package for RedHat-based.

Usage
-----

To use the extension simply import the class wrapper and pass the Quart app
object back to here. Do so like this::
    
    from quart import Quart
    from quart_bcrypt import Bcrypt
    
    app = Quart(__name__)
    bcrypt = Quart(app)

Two primary hashing methods are now exposed by way of the bcrypt object.

    pw_hash = pw_hash = bcrypt.generate_password_hash('hunter2').decode('utf-8')
    bcrypt.check_password_hash(pw_hash, 'hunter2') # returns True
    
Note you need to use decode('utf-8') on generate_password_hash(), like below:

    pw_hash = bcrypt.generate_password_hash('hunter2').decode('utf-8')

API
-----
.. autoclass:: quart_bcrypt.Bcrypt
    :members:

.. autofunction:: quart_bcrypt.generate_password_hash

.. autofunction:: quart_bcrypt.check_password_hash