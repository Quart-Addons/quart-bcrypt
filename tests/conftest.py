"""
Pytest confif file for Quart Bcrypt.
"""
import pytest
import quart
import quart_bcrypt

@pytest.fixture
def app() -> quart.Quart:
    """
    Returns a Quart app for the
    basic test of Quart Bcrypt.
    """
    app = quart.Quart(__name__)
    app.config['BCRYPT_LOG_ROUNDS'] = 6
    app.config['BCRYPT_HASH_PREFIX'] = '2b'
    app.config['BCRYPT_HANDLE_LONG_PASSWORDS'] = False

    return app

@pytest.fixture
def extension() -> quart_bcrypt.Bcrypt:
    """
    Returns a Quart Bcrypt obeject for
    testing.
    """
    bcrypt = quart_bcrypt.Bcrypt()
    return bcrypt
