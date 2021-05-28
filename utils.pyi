"""
Author: Ryu JuHeon(@SaidBySolo)

Not all implemented.

It is designed to provide minimal help for users when writing scripts.
"""

from bs4 import BeautifulSoup

from typing import (
    Any,
    AnyStr,
    Callable,
    Dict,
    List,
    Literal,
    Optional,
    Type,
    TypeVar,
    Union,
    overload,
)

DONLOADER_CLASS = TypeVar("DONLOADER_CLASS", bound=Type[Downloader])
LAZY_URL_CLASS = TypeVar("LAZY_URL_CLASS", bound=Type[LazyUrl])

class Downloader(object):
    @classmethod
    def register(cls, D: DONLOADER_CLASS) -> DONLOADER_CLASS:
        """
        Decorator.
        Register the class to the downloader.
        """
        ...
    @property
    def url(self) -> str: ...
    @url.setter
    def url(self, value: Any) -> str: ...
    @property
    def title(self): ...
    @title.setter
    def title(self, value: Any) -> str: ...
    @property
    def artist(self) -> str: ...
    @artist.setter
    def artist(self, value: Any) -> str: ...
    @property
    def urls(self) -> List[str]:
        """
        List with links to download
        """
        ...
    @urls.setter
    def urls(self, value: Any): ...
    @property
    def filenames(self) -> dict[str, str]:
        """
        Dictionary for specifying file names
        """
        ...
    @filenames.setter
    def filenames(self, value: Any): ...
    @classmethod
    def fix_url(cls, url: str):
        """
        Executed when the class is registered.
        """
        ...
    @classmethod
    def key_id(cls, url: str):
        """
        Executed when the class is registered.
        """
        ...
    def Invalid(
        self, s: str = "", e: Type[BaseException] = None, fail: bool = False
    ) -> None:
        """
        Notifies the user that an exception has occurred.
        """
        ...
    def print_(self, s: str) -> None:
        """
        Print the string received in the job information.
        """
    def read(self):
        """
        Must be implemented
        """
        ...

class Nothing(object): ...

class Soup(BeautifulSoup):
    def __init__(
        self,
        html: Any,
        parser: str = "html.parser",
        unescape: bool = False,
        apply_css: bool = False,
    ):
        """
        Return BeautifulSoup
        """
        ...

class LazyUrl(object):
    type: Optional[str] = None
    def dump(self) -> Dict[Any, str]:
        """
        If you call the register method, you need to implement this function in the class to be registered.
        """
        ...
    @classmethod
    def register(cls, L):
        """
        Decorator.
        Register the class to the LazyUrl.
        """
        ...

def urljoin(a: AnyStr, b: AnyStr):
    """
    https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urljoin
    """
    ...

def query_url(url: str) -> Dict[Any, str]:
    """
    ?key=value
    &key=value

    Returns the value in the query string as {key:value}.
    """
    ...

def try_n(
    n: int, sleep: Union[Callable[..., Any], int] = None, out: Any = Nothing
) -> Any:
    """
    Decorator.
    When an exception occurs, it tries again n times.
    """
    ...

@overload
def clean_title(
    title: str,
    mode: Literal["soft", "hard", "safe"],
    allow_dot: bool = False,
    n: Optional[int] = None,
) -> str:
    """
    Return the string after post-processing.
    """
    ...

@overload
def clean_title(
    title: None,
    mode: Literal["soft", "hard", "safe"],
    allow_dot: bool = False,
    n: Optional[int] = None,
) -> None: ...
def Invalid(
    self, s: str = "", e: Type[BaseException] = None, fail: bool = False
) -> None:
    """
    Notifies the user that an exception has occurred.
    """
    ...

def get_print(cw):
    """
    Get print function.
    """
    ...

def format_filename(title: str, id: Any, ext: str = ".", dirFormat=None):
    """
    ext is Extension name
    """
    ...

def get_ext(url: str) -> str:
    """
    Get extension name
    """
    ...
