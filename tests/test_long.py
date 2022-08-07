"""
Password long test of Quart Bcrypt.
"""
import pytest
import quart
import quart_bcrypt

@pytest.fixture
def bcrypt(app: quart.Quart, extension: quart_bcrypt.Bcrypt) -> quart_bcrypt.Bcrypt:
    """
    Returns a Quart Bcrypt obeject for
    testing.
    """
    app.config['BCRYPT_HANDLE_LONG_PASSWORDS'] = True

    bcrypt = extension.init_app(app)

    return bcrypt

def test_long_password(bcrypt):
    """
    Test the work around bcrypt maximum password length.
    """
    # Create a password with a 72 bytes length
    password = 'A' * 72
    pw_hash = bcrypt.generate_password_hash(password)

    # Ensure that a longer password **do not** yield the same hash
    res = bcrypt.check_password_hash(pw_hash, 'A' * 80)
    assert res is False
