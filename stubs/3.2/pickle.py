# Stubs for pickle

# NOTE: These are incomplete!

from typing import Any, BinaryIO

def dumps(obj: Any, protocol: int = None, *,
          fix_imports: bool = True) -> bytes: pass
def loads(p: bytes, *, fix_imports: bool = True,
          encoding: str = 'ASCII', errors: str = 'strict') -> Any: pass
def load(file: BinaryIO, *, fix_imports: bool = True, encoding: str = 'ASCII',
         errors: str = 'strict') -> Any: pass
