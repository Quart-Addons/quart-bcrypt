"""
Tests Quart Bcrypt Async functions for the basic test.
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

    extension.init_app(app)

    return extension

@pytest.mark.asyncio
async def test_is_string(bcrypt):
    """
    Test if a string can generate a password hash.
    """
    pw_hash = await bcrypt.async_generate_password_hash('secret')
    assert isinstance(pw_hash, bytes) is True

@pytest.mark.asyncio
async def test_custom_rounds(bcrypt):
    """
    Tests custom rounds
    """
    password = 'secret'
    pw_hash = await bcrypt.async_generate_password_hash(password, 5)
    assert password != pw_hash

@pytest.mark.asyncio
async def test_check_hash(bcrypt):
    """
    Tests password hashing
    """
    password = 'secret'
    pw_hash = await bcrypt.async_generate_password_hash(password)

    # check a correct password
    res = await bcrypt.async_check_password_hash(pw_hash, password)
    assert res is True

    # check an incorrect password
    res = await bcrypt.async_check_password_hash(pw_hash, 'hunter2')
    assert res is False

    # check unicode
    password = '\u2603'
    pw_hash = await bcrypt.async_generate_password_hash(password)
    res = await bcrypt.async_check_password_hash(pw_hash, password)
    assert res is True

    # check helper function
    password = 'hunter2'
    pw_hash = await quart_bcrypt.async_generate_password_hash(password)
    res = await quart_bcrypt.async_check_password_hash(pw_hash, password)
    assert res is True

@pytest.mark.asyncio
async def test_check_hash_unicode_is_utf8(bcrypt):
    """
    Tests the checked hash unicode is utf-8
    """
    password = '\u2603'
    pw_hash = await bcrypt.async_generate_password_hash(password)

    res = await bcrypt.async_check_password_hash(pw_hash, b'\xe2\x98\x83')
    assert res is True

@pytest.mark.asyncio
async def test_unicode_hash(bcrypt):
    """
    Tests a password hash using a unicode.
    """
    password = '東京'
    pw_hash = (await bcrypt.async_generate_password_hash(password)).decode('utf-8')

    res = await bcrypt.async_check_password_hash(pw_hash, password)
    assert res is True

@pytest.mark.asyncio
async def test_long_password(bcrypt):
    """
    Test bcrypt maximum password length.

    The bcrypt algorithm has a maximum password length of 72 bytes, and
    ignores any bytes beyond that.
    """
    password = 'A' * 72
    pw_hash = await bcrypt.async_generate_password_hash(password)

    res = await bcrypt.async_check_password_hash(pw_hash, password)
    assert res is True
