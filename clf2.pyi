from typing import Any, Callable, Optional
from utils import Session
from customWidget import CustomWidget

def solve(
    url: str,
    session: Session = None,
    cw: Optional[CustomWidget] = None,
    show: bool = False,
    delay: float = 1.0,
    f: Optional[Callable[..., Any]] = None,
    timeout: float = 90.0,
    check_body: bool = True,
) -> dict[str, str]:
    """
    Return html after rendering javascript

    Exception:
        raise Exception
    """
    ...
