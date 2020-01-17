# Stubs for fastecdsa.ecdsa (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .curve import Curve, P256
from .point import Point
from .util import RFC6979, msg_bytes
from typing import Any, Tuple, TypeVar

MsgTypes = TypeVar('MsgTypes', str, bytes, bytearray)


class EcdsaError(Exception):
    msg: Any = ...

    def __init__(self, msg: Any) -> None:
        ...


def sign(
    msg: MsgTypes,
    d: int,
    curve: Curve = ...,
    hashfunc: Any = ...,
    prehashed: bool = ...
) -> Any:
    ...


def verify(
    sig: Tuple[int, int],
    msg: MsgTypes,
    Q: Point,
    curve: Curve = ...,
    hashfunc: Any = ...
) -> bool:
    ...
