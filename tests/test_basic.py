"""
Basic test of Quart Bcrypt.
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
    app.config['BCRYPT_HANDLE_LONG_PASSWORDS'] = False

    bcrypt = extension.init_app(app)

    return bcrypt

def test_is_string(bcrypt):
    """
    Test if a string can generate a password hash.
    """
    pw_hash = bcrypt.generate_password_hash('secret')
    assert isinstance(pw_hash, bytes) is True

def test_custom_rounds(bcrypt):
    """
    Tests custom rounds
    """
    password = 'secret'
    pw_hash = bcrypt.generate_password_hash(password, 5)
    assert password != pw_hash

def test_check_hash(bcrypt):
    """
    Tests password hashing
    """
    password = 'secret'
    pw_hash = bcrypt.generate_password_hash(password)

    # check a correct password
    res = bcrypt.check_password_hash(pw_hash, password)
    assert res is True

    # check an incorrect password
    res = bcrypt.check_password_hash(pw_hash, 'hunter2')
    assert res is False

    # check unicode 
    password = '\u2603'
    pw_hash = bcrypt.generate_password_hash(password)
    res = bcrypt.check_password_hash(pw_hash, password)
    assert res is True

    # check helper function
    password = 'hunter2'
    pw_hash = quart_bcrypt.generate_password_hash(password)
    res = quart_bcrypt.check_password_hash(pw_hash, password)
    assert res is True

def test_check_hash_unicode_is_utf8(bcrypt):
    """
    Tests the checked hash unicode is utf-8
    """
    password = '\u2603'
    pw_hash = bcrypt.generate_password_hash(password)

    res = bcrypt.check_password_hash(pw_hash, b'\xe2\x98\x83')
    assert res is True

def test_rounds_set(bcrypt):
    """
    Tests if the rounds are set in the
    `Bcrypt` object.
    """
    rounds = bcrypt._log_rounds
    assert rounds == 6

def test_unicode_hash(bcrypt):
    """
    Tests a password hash using a unicode.
    """
    password = '東京'
    pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    res = bcrypt.check_password_hash(pw_hash, password)
    assert res is True

def test_long_password(bcrypt):
    """
    Test bcrypt maximum password length.

    The bcrypt algorithm has a maximum password length of 72 bytes, and
    ignores any bytes beyond that.
    """
    password = 'A' * 72
    pw_hash = bcrypt.generate_password_hash(password)

    res = bcrypt.check_password_hash(pw_hash, password)
    assert res is True
