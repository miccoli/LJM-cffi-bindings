from ._ljm import ffi, lib
from ._version import __version__

__all__ = ["__version__", "__ljm_version__", "ffi", "lib"]
__ljm_version__ = lib.LJM_VERSION
