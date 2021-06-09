"""
Author: Ryu JuHeon(@SaidBySolo)

Not all implemented.

It is designed to provide minimal help for users when writing scripts.
"""
from __future__ import annotations
from size import Size
from customWidget import CustomWidget
from bs4 import BeautifulSoup
import requests
from typing import (
    Any,
    AnyStr,
    Callable,
    Literal,
    NoReturn,
    Optional,
    Type,
    TypeVar,
    Union,
    overload,
)

DONLOADER_CLASS = TypeVar("DONLOADER_CLASS", bound=Type[Downloader])
LAZY_URL_CLASS = TypeVar("LAZY_URL_CLASS", bound=Type[LazyUrl])

# url, key_id, fix_url was removed
class Downloader:
    instances: list[object] = []
    waiting_init: bool = False
    mainWindow: Any = None
    types: dict[str, str] = {}
    fix_urls: dict[str, str] = {}
    key_ids: dict[str, str] = {}
    MAX_CORE: int = 16
    MAX_PARALLEL: int = 4
    MAX_SPEED: Optional[float] = None
    URLS: Optional[list[str]] = None
    type: Optional[str] = None
    icon: Optional[str] = None
    single: bool = False
    session: Optional[Session] = None
    lock: bool = False
    detect_removed: bool = True
    detect_local_lazy: bool = True
    _title: Optional[str] = None
    _icon: Optional[str] = None
    user_agent: Optional[str] = None
    referer: Optional[str] = None
    header: Optional[dict[str, str]] = None
    status: Literal["ready", "working", "done", "error"] = "ready"
    update_filesize: bool = True
    size: Optional[Size] = None
    _artist: Optional[str] = None
    display_name: Optional[str] = None
    keep_date: bool = False
    strip_header: bool = True
    atts: list[str] = []
    _enabled: bool = True
    @classmethod
    def register(cls, D: DONLOADER_CLASS) -> DONLOADER_CLASS:
        """
        Decorator.
        Register the class to the downloader.
        """
        ...
    @classmethod
    def get(cls, type) -> Optional[str]:
        """
        dict.get() in types
        """
        return
    @classmethod
    def count(cls) -> dict[str, int]:
        """
        Unknown
        """
        ...
    @property
    def url(self) -> str:
        """
        Url
        """
        ...
    @url.setter
    def url(self, value: Any) -> str: ...
    @property
    def title(self) -> str:
        """
        Title
        """
        ...
    @title.setter
    def title(self, value: Any) -> str: ...
    @property
    def artist(self) -> str:
        """
        Artist
        """
        ...
    @artist.setter
    def artist(self, value: Any) -> str: ...
    @property
    def urls(self) -> list[str]:
        """
        List with links to download
        """
        ...
    @urls.setter
    def urls(self, value: Any): ...
    @property
    def filenames(self) -> dict[str, str]:
        """
        dictionary for specifying file names
        """
        ...
    @filenames.setter
    def filenames(self, value: Any): ...
    @property
    def enableSegment(self) -> Any: ...
    @property
    def disableSegment(self) -> Any: ...
    @property
    def dir(self) -> str:
        """
        Return save folder
        """
        ...
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
    @property
    def cw(self) -> CustomWidget:
        """
        return CustomWidget
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
    def init(self) -> None:
        """
        Must be implemented
        """
        ...
    def read(self) -> None:
        """
        Must be implemented
        """
        ...
    def on_error(self, e: Type[Exception]) -> NoReturn:
        """
        Handle error
        """
        ...
    def fix_dirname(self, title: Optional[str] = None) -> None: ...

class Nothing(object): ...
class Session(requests.Session): ...

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
    def dump(self) -> dict[Any, str]:
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

def query_url(url: str) -> dict[Any, str]:
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

def get_print(cw: CustomWidget):
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

def check_alive(cw: CustomWidget) -> NoReturn:
    """
    check CustomWidget is alive
    """
    ...

def generate_csrf_token() -> int:
    """
    generate random csrf token
    """
    ...

def atoi(text: str) -> Union[int, str]:
    """
    if text is digit return int
    else return text
    """
    ...
