from enum import Enum

from ._ljm import ffi, lib
from ._version import __version__

__all__ = ["__version__", "__ljm_version__", "ffi", "lib", "CT", "DT"]
__ljm_version__ = lib.LJM_VERSION


def _make_Enum(name, prefix):
    return Enum(
        name,
        (
            (n.removeprefix(prefix), getattr(_ljm.lib, n))
            for n in dir(_ljm.lib)
            if n.startswith(prefix)
        ),
        module=__name__,
    )


DT = _make_Enum("DT", "LJM_dt")
CT = _make_Enum("CT", "LJM_ct")
