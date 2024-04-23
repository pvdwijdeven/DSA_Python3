from typing import List, Dict, Tuple, Callable, Any
import timeit
from statistics import mean, median
import re
from Logger import ColorLogger


def open_file_with_encoding(
    filename: str, encodings: List[str] | None = None, logger: ColorLogger | None = None
) -> str | None:
    """
    Open a file with different encodings.

    This function tries to open a file with a list of encodings, starting with the most commonly used ones.
    If the file cannot be opened with an encoding, it prints an error message and tries the next one.
    If the file cannot be opened with any of the provided encodings, it prints a final error message and returns None.

    Args:
        filename (str): The path to the file to open.
        encodings (List[str], optional): The list of encodings to try. If not provided, a default list of encodings is used.

    Returns:
        Optional[str]: The content of the file if it was able to be opened and read with one of the provided encodings, or None otherwise.
    """
    if encodings is None:
        encodings = [
            "utf-8",
            "latin1",
            "iso-8859-1",
            "iso-8859-15",
            "cp1252",
            "cp1256",
            "ascii",
            "utf_32",
            "utf_32_be",
            "utf_32_le",
            "utf_16",
            "utf_16_be",
            "utf_16_le",
            "utf_7",
            "utf_8",
            "utf_8_sig",
            "latin_1",
            "iso8859_2",
            "iso8859_3",
            "iso8859_4",
            "iso8859_5",
            "iso8859_6",
            "iso8859_7",
            "iso8859_8",
            "iso8859_9",
            "iso8859_10",
            "iso8859_13",
            "iso8859_14",
            "iso8859_15",
            "iso8859_16",
            "big5",
            "big5hkscs",
            "cp037",
            "cp424",
            "cp437",
            "cp500",
            "cp720",
            "cp737",
            "cp775",
            "cp850",
            "cp852",
            "cp855",
            "cp856",
            "cp857",
            "cp858",
            "cp860",
            "cp861",
            "cp862",
            "cp863",
            "cp864",
            "cp865",
            "cp866",
            "cp869",
            "cp874",
            "cp875",
            "cp932",
            "cp949",
            "cp950",
            "cp1006",
            "cp1026",
            "cp1140",
            "cp1250",
            "cp1251",
            "cp1253",
            "cp1254",
            "cp1255",
            "cp1257",
            "cp1258",
            "euc_jp",
            "euc_jis_2004",
            "euc_jisx0213",
            "euc_kr",
            "gb2312",
            "gbk",
            "gb18030",
            "hz",
            "iso2022_jp",
            "iso2022_jp_1",
            "iso2022_jp_2",
            "iso2022_jp_2004",
            "iso2022_jp_3",
            "iso2022_jp_ext",
            "iso2022_kr",
            "johab",
            "koi8_r",
            "koi8_t",
            "koi8_u",
            "kz1048",
            "mac_cyrillic",
            "mac_greek",
            "mac_iceland",
            "mac_latin2",
            "mac_roman",
            "mac_turkish",
            "ptcp154",
            "shift_jis",
            "shift_jis_2004",
            "shift_jisx0213",
        ]
    if logger is None:
        clog: ColorLogger = ColorLogger(
            level_file=ColorLogger.DEBUG, level_console=ColorLogger.INFO
        )
    else:
        clog = logger
    for encoding in encodings:
        try:
            with open(file=filename, mode="r", encoding=encoding) as file:
                content: str = file.read()
            clog.info(msg=f"Encoding used: {encoding}")
            return content
        except UnicodeDecodeError:
            clog.info(
                msg=f"UnicodeDecodeError: Can't decode file {filename} using {encoding} encoding."
            )
        except Exception as e:
            clog.error(msg=f"An error occurred while opening the file {filename}: {e}")
            return None

    clog.error(
        msg=f"Failed to read file {filename} with any of the provided encodings."
    )
    return None


def round_to_nearest_zero(number) -> str:
    n: float = abs(number)
    if n < 1:
        # Find the first non-zero digit.
        # We want 3 digits, starting at that location.
        s: str = f"{n:.99f}"
        res: re.Match[str] | None = re.search(pattern="[1-9]", string=s)
        assert res
        index: int = res.start()
        return s[: index + 3]
    else:
        # We want 2 digits after decimal point.
        return str(object=round(number=n, ndigits=2))


def measure_speed(repeat_count: int = 5, test_count: int = 1000):
    """
    A decorator for measuring the execution speed of a function.

    This decorator runs a function multiple times and calculates the average execution time.
    It uses the `timeit` module to measure the execution time.

    Args:
        repeat_count (int, optional): The number of times the function execution is repeated. Defaults to 5.
        test_count (int, optional): The number of times the function is executed in each repetition. Defaults to 1000.

    Returns:
        Callable[..., Any]: The decorated function which will print the average execution time when called.
    """

    def decorator(func: Callable[..., Any]):
        def wrapper(*args, **kwargs):
            timer = timeit.Timer(stmt=lambda: func(*args, **kwargs))
            times: List[float] = timer.repeat(repeat=repeat_count, number=test_count)
            print(
                f"Function '{func.__name__}' has been tested {repeat_count} times with {test_count} tests per run."
            )
            print(f"mean   : {round_to_nearest_zero(number=mean(times))} sec.")
            print(f"median : {round_to_nearest_zero(number=median(data=times))} sec.")
            print(f"fastest: {round_to_nearest_zero(number=min(times))} sec.")
            print(f"slowest: {round_to_nearest_zero(number=max(times))} sec.")
            return func(*args, **kwargs)

        return wrapper

    return decorator


if __name__ == "__main__":

    @measure_speed()
    def test() -> int:
        x = 0
        for x in range(10):
            x += 1
        return x

    test()
