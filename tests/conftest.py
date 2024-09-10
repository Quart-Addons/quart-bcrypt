"""
tests.conftest
"""
import pytest
from quart import Quart
from quart_bcrypt import Bcrypt


@pytest.fixture
def app() -> Quart:
    """
    Returns a Quart app for the
    basic test of Quart Bcrypt.
    """
    app = Quart(__name__)
    app.config['BCRYPT_LOG_ROUNDS'] = 6
    app.config['BCRYPT_HASH_PREFIX'] = '2b'
    return app


@pytest.fixture
def extension() -> Bcrypt:
    """
    Returns a Quart Bcrypt obeject for
    testing.
    """
    bcrypt = Bcrypt()
    return bcrypt
