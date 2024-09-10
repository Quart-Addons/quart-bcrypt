"""
quart_bcrypt.helpers
"""
import typing as t

from .core import Bcrypt


def generate_password_hash(
        password: t.Union[str, bytes],
        rounds: t.Optional[int] = None
) -> bytes:
    '''
    This helper function wraps the eponymous method of :class:`Bcrypt`. It
    is intended to be used as a helper function at the expense of the
    configuration variable provided when passing back the app object. In other
    words this shortcut does not make use of the app object at all.

    To use this function, simply import it from the module and use it in a
    similar fashion as the original method would be used. Here is a quick
    example::

        from quart_bcrypt import generate_password_hash
        pw_hash = generate_password_hash('hunter2', 10)

    :param password: The password to be hashed.
    :param rounds: The optional number of rounds.
    '''
    return Bcrypt().generate_password_hash(password, rounds)


def check_password_hash(
        pw_hash: t.Union[str, bytes],
        password: t.Union[str, bytes]
) -> bool:
    '''
    This helper function wraps the eponymous method of :class:`Bcrypt.` It
    is intended to be used as a helper function at the expense of the
    configuration variable provided when passing back the app object. In other
    words this shortcut does not make use of the app object at all.

    To use this function, simply import it from the module and use it in a
    similar fashion as the original method would be used. Here is a quick
    example::

        from quart_bcrypt import check_password_hash
        check_password_hash(pw_hash, 'hunter2') # returns True

    :param pw_hash: The hash to be compared against.
    :param password: The password to compare.
    '''
    return Bcrypt().check_password_hash(pw_hash, password)


async def async_generate_password_hash(
        password: str, rounds: t.Optional[int] = None
) -> bytes:
    """
    This async helper function wraps the eponymous method of :class:`Bcrypt`.
    It is intended to be used as a helper function at the expense of the
    configuration variable provided when passing back the app object. In other
    words this shortcut does not make use of the app object at all.

    To use this function, simply import it from the module and use it in a
    similar fashion as the original method would be used. Here is a quick
    example::

        from quart_bcrypt import async_generate_password_hash
        pw_hash = await generate_password_hash('hunter2', 10)

    :param password: The password to be hashed.
    :param rounds: The optional number of rounds.
    """
    return await Bcrypt().async_generate_password_hash(password, rounds)


async def async_check_password_hash(pw_hash: bytes, password: str) -> bool:
    """This async helper function wraps the eponymous method of
    :class:`Bcrypt.` It is intended to be used as a helper function at the
    expense of the configuration variable provided when passing back the app
    object. In other words this shortcut does not make use of the app object
    at all.

    To use this function, simply import it from the module and use it in a
    similar fashion as the original method would be used. Here is a quick
    example::

        from quart_bcrypt import async_check_password_hash
        await async_check_password_hash(pw_hash, 'hunter2') # returns True

    :param pw_hash: The hash to be compared against.
    :param password: The password to compare.
    """
    return await Bcrypt().async_check_password_hash(pw_hash, password)
