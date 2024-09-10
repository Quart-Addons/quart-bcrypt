"""
Tests Quart Bcrypt Async functions for the long test.
"""
import pytest
import quart

from quart_bcrypt import Bcrypt


@pytest.fixture
def bcrypt(app: quart.Quart, extension: Bcrypt) -> Bcrypt:
    """
    Returns a Quart Bcrypt obeject for
    testing.
    """
    app.config['BCRYPT_HANDLE_LONG_PASSWORDS'] = True

    extension.init_app(app)

    return extension


@pytest.mark.asyncio
async def test_long_password(bcrypt: Bcrypt) -> None:
    """
    Test the work around bcrypt maximum password length.
    """
    # Create a password with a 72 bytes length
    password = 'A' * 72
    pw_hash = await bcrypt.async_generate_password_hash(password)

    # Ensure that a longer password **do not** yield the same hash
    res = await bcrypt.async_check_password_hash(pw_hash, 'A' * 80)
    assert res is False
