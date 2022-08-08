.. _cheatsheet:

==========
Cheatsheet
==========

Basic App
---------

.. code-block:: python

    from quart import Quart, render_template, redirect
    from quart_uploads import Bcrypt

    app = Quart(__name__)

    bcrypt = Bcrypt(app)

    @app.route("/register")
    async def register():
        if request.method == 'POST':
            form = await request.form
            password = form.get('password')
            pw_hash = await bcrypt.async_generate_password_hash(password)
            return redirect(url_for('login'))
        return await render_template('register.html')

    @app.route('/login', methods=['GET', 'POST'])
    async def login():
        """User login route."""
        if session.get('logged_in'):
            await flash("You are already logged in")
            return redirect(url_for('index'))
        if request.method == 'POST':
            form = await request.form
            username = form.get('username')
            password = form.get('password')
            pw_hash = app.config['ADMIN_PASSWORD_HASH']
            res = await bcrypt.async_check_password_hash(pw_hash, password)
            if (username == app.config['ADMIN_USERNAME'] and res):
                session['logged_in'] = True
                await flash("Successfully logged in", "success")
                return redirect(url_for('index'))
            else:
                await flash("Those credentials were incorrect", "danger")
        return await render_template('login.html')

Large Applications
------------------

.. code-block:: python
    :caption: yourapplication/extensions.py

    from quart_bcrypt import Bcrypt

    bcrypt = Bcrypt()

.. code-block:: python
    :caption: youapplication/app.py

    from quart import Quart
    from .extensions import bcrypt

    def create_app() -> Quart:
        app = Quart(__name__)

        bcrypt.init_app(app)

        # Other app registration here. 
        
        return app

Sync Helpers
------------

.. code-block:: python 
    
    from quart_bcrypt import generate_password_hash, check_password_hash
    
    password = 'WowThisIsAwesome100'

    pw_hash = generate_password_hash(password) # Generate the password hash

    if check_password_hash(pw_hash, password):
        # Then do something.

Async Helpers
-------------

.. code-block:: python 
    
    from quart_bcrypt import async_generate_password_hash, async_check_password_hash
    
    password = 'WowThisIsAwesome100'

    pw_hash = await async_generate_password_hash(password) # Generate the password hash

    if await async_check_password_hash(pw_hash, password):
        # Then do something.
