# Quart-Bcrypt

![Quart Bcrypt Logo](logos/logo.png)

Quart-Bcrypt is a Quart extension that provides bcrypt hashing utilities for
your application. Orginal code from Flash-Bcrypt, which can be found at
https://github.com/maxcountryman/flask-bcrypt

Due to the recent increased prevelance of powerful hardware, such as modern
GPUs, hashes have become increasingly easy to crack. A proactive solution to
this is to use a hash that was designed to be "de-optimized". Bcrypt is such
a hashing facility; unlike hashing algorithms such as MD5 and SHA1, which are
optimized for speed, bcrypt is intentionally structured to be slow.

For sensitive data that must be protected, such as passwords, bcrypt is an
advisable choice.

## Installation

Install the extension with the following command:

    $ pip3 install quart-bcrypt

## Usage

To use the extension simply import the class wrapper and pass the Quart app
object back to here. Do so like this:

    from quart import Quart
    from quart_bcrypt import Bcrypt
    
    app = Quart(__name__)
    bcrypt = Bcrypt(app)

Two primary hashing methods are now exposed by way of the bcrypt object. Note that you
need to use decode('utf-8') on generate_password_hash().

    pw_hash = bcrypt.generate_password_hash('hunter2').decode('utf-8')
    bcrypt.check_password_hash(pw_hash, 'hunter2') # returns True

## Documentation

View documentation at https://quart-bcrypt.readthedocs.io/en/latest/