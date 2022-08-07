"""
quart_bcrypt.core

The core Bcrypt class.
"""
import typing as t
import hmac
import hashlib

import bcrypt
from quart import Quart
from quart.utils import run_sync

class Bcrypt(object):
    '''Bcrypt class container for password hashing and checking logic using
    bcrypt, of course. This class may be used to intialize your Quart app
    object. The purpose is to provide a simple interface for overriding
    Werkzeug's built-in password hashing utilities.

    Although such methods are not actually overriden, the API is intentionally
    made similar so that existing applications which make use of the previous
    hashing functions might be easily adapted to the stronger facility of
    bcrypt.

    To get started you will wrap your application's app object something like
    this::

        app = Quart(__name__)
        bcrypt = Bcrypt(app)

    Now the two primary utility methods are exposed via this object, `bcrypt`.
    So in the context of the application, important data, such as passwords,
    could be hashed using this syntax::

        password = 'hunter2'
        pw_hash = bcrypt.generate_password_hash(password)

    Once hashed, the value is irreversible. However in the case of validating
    logins a simple hashing of candidate password and subsequent comparison.
    Importantly a comparison should be done in constant time. This helps
    prevent timing attacks. A simple utility method is provided for this::

        candidate = 'secret'
        bcrypt.check_password_hash(pw_hash, candidate)

    If both the candidate and the existing password hash are a match
    `check_password_hash` returns True. Otherwise, it returns False.

    .. admonition:: Namespacing Issues

        It's worth noting that if you use the format, `bcrypt = Bcrypt(app)`
        you are effectively overriding the bcrypt module. Though it's unlikely
        you would need to access the module outside of the scope of the
        extension be aware that it's overriden.

        Alternatively consider using a different name, such as `quart_bcrypt
        = Bcrypt(app)` to prevent naming collisions.

    Additionally a configuration value for `BCRYPT_LOG_ROUNDS` may be set in
    the configuration of the Quart app. If none is provided this will
    internally be assigned to 12. (This value is used in determining the
    complexity of the encryption, see bcrypt for more details.)

    You may also set the hash version using the `BCRYPT_HASH_PREFIX` field in
    the configuration of the Quart app. If not set, this will default to `2b`.
    (See bcrypt for more details)

    By default, the bcrypt algorithm has a maximum password length of 72 bytes
    and ignores any bytes beyond that. A common workaround is to hash the
    given password using a cryptographic hash (such as `sha256`), take its
    hexdigest to prevent NULL byte problems, and hash the result with bcrypt.
    If the `BCRYPT_HANDLE_LONG_PASSWORDS` configuration value is set to `True`,
    the workaround described above will be enabled.
    **Warning: do not enable this option on a project that is already using
    Quart-Bcrypt, or you will break password checking.**
    **Warning: if this option is enabled on an existing project, disabling it
    will break password checking.**

    :param app: The Quart application object. Defaults to None.
    '''

    _log_rounds = 12
    _prefix = '2b'
    _handle_long_passwords = False

    def __init__(
        self,
        app: t.Optional[Quart]=None,
        log_rounds: int = 12,
        prefix: str = '2b',
        long_passwords: bool = False
        ) -> None:
        self.app = app

        if app is not None:
            self.init_app(app, log_rounds, prefix, long_passwords)

    def init_app(
        self,
        app: Quart,
        log_rounds: int = 12,
        prefix: str = '2b',
        long_passwords: bool = False
        ) -> None:
        '''Initalizes the application with the extension.

        :param app: The Quart application object.
        '''
        if self.app is None:
            self.app = app

        app.extensions['bcrypt'] = self

        app.config.setdefault('BCRYPT_LOG_ROUNDS', log_rounds)
        self._prefix = app.config.setdefault('BCRYPT_HASH_PREFIX', prefix)
        self._handle_long_passwords = app.config.setdefault(
            'BCRYPT_HANDLE_LONG_PASSWORDS', long_passwords)

    @property
    def _log_rounds(self) -> int:
        """
        Log rounds to use for Bcrypt.
        """
        return self.app.config.get('BCRYPT_LOG_ROUNDS')

    @property
    def _prefix(self) -> str:
        """
        The prefix to use for Bcrypt.
        """
        return self.app.config.get('BCRYPT_HASH_PREFIX')

    @property
    def _handle_long_passwords(self) -> bool:
        """
        Handle long passwords or not.
        """
        return self.app.config.get('BCRYPT_HANDLE_LONG_PASSWORDS')

    def _unicode_to_bytes(self, unicode_string: t.Union[str, bytes]) -> bytes:
        '''Converts a unicode string to a bytes object.

        :param unicode_string: The unicode string to convert.'''

        if isinstance(unicode_string, str):
            bytes_object = bytes(unicode_string, 'utf-8')
        else:
            bytes_object = unicode_string

        return bytes_object

    def generate_password_hash(self, password: str, rounds: t.Optional[int]=None,
                               prefix=None) -> bytes:
        '''Generates a password hash using bcrypt. Specifying `rounds`
        sets the log_rounds parameter of `bcrypt.gensalt()` which determines
        the complexity of the salt. 12 is the default value. Specifying `prefix`
        sets the `prefix` parameter of `bcrypt.gensalt()` which determines the
        version of the algorithm used to create the hash.

        Example usage of :class:`generate_password_hash` might look something
        like this::

            pw_hash = bcrypt.generate_password_hash('secret', 10)

        :param password: The password to be hashed.
        :param rounds: The optional number of rounds.
        :param prefix: The algorithm version to use.
        '''

        if not password:
            raise ValueError('Password must be non-empty.')

        if rounds is None:
            rounds = self._log_rounds
        if prefix is None:
            prefix = self._prefix

        # Python 3 unicode strings must be encoded as bytes before hashing.
        password = self._unicode_to_bytes(password)
        prefix = self._unicode_to_bytes(prefix)

        if self._handle_long_passwords:
            password = hashlib.sha256(password).hexdigest()
            password = self._unicode_to_bytes(password)

        salt = bcrypt.gensalt(rounds=rounds, prefix=prefix)
        return bcrypt.hashpw(password, salt)

    def check_password_hash(self, pw_hash: bytes, password: str) -> bool:
        '''Tests a password hash against a candidate password. The candidate
        password is first hashed and then subsequently compared in constant
        time to the existing hash. This will either return `True` or `False`.

        Example usage of :class:`check_password_hash` would look something
        like this::

            pw_hash = bcrypt.generate_password_hash('secret', 10)
            bcrypt.check_password_hash(pw_hash, 'secret') # returns True

        :param pw_hash: The hash to be compared against.
        :param password: The password to compare.
        '''

        # Python 3 unicode strings must be encoded as bytes before hashing.
        pw_hash = self._unicode_to_bytes(pw_hash)
        password = self._unicode_to_bytes(password)

        if self._handle_long_passwords:
            password = hashlib.sha256(password).hexdigest()
            password = self._unicode_to_bytes(password)

        return hmac.compare_digest(bcrypt.hashpw(password, pw_hash), pw_hash)

    async def async_generate_password_hash(self, password: str, rounds: t.Optional[int]=None,
                                          prefix=None) -> bytes:
        """Wraps the generate_password_hash function in Quarts run_sync function to
        ensure the sync function is run within the event loop.

        Example usage of :class:`async_generate_password_hash` might look something
        like this::

            pw_hash = await bcrypt.async_generate_password_hash('secret', 10)

        :param password: The password to be hashed.
        :param rounds: The optional number of rounds.
        :param prefix: The algorithm version to use.
        """

        return await run_sync(self.generate_password_hash)(password, rounds, prefix)

    async def async_check_password_hash(self, pw_hash: bytes, password: str) -> bool:
        """Wraps the check_password_hash function in Quarts run_sync function to
        ensure the sync function is run within the event loop.

        Example usage of :class:`async_check_password_hash` would look something
        like this::

            pw_hash = await bcrypt.async_generate_password_hash('secret', 10)
            await bcrypt.check_password_hash(pw_hash, 'secret') # returns True

        :param pw_hash: The hash to be compared against.
        :param password: The password to compare.
        """

        return await run_sync(self.check_password_hash)(pw_hash, password)
