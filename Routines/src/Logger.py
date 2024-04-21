import logging
from logging.handlers import RotatingFileHandler


class CustomFormatter(logging.Formatter):
    def __init__(
        self,
        fmt="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    ) -> None:
        super().__init__(fmt=fmt, datefmt=datefmt)

    green: str = "\x1b[32;1m"
    grey: str = "\x1b[38;20m"
    yellow: str = "\x1b[33;20m"
    red: str = "\x1b[31;20m"
    bold_red: str = "\x1b[31;1m"
    reset: str = "\x1b[0m"

    format_debug: str = "%(levelname)s: %(message)s on line %(lineno)d (%(filename)s)"
    format_info: str = "%(message)s"
    format_warning: str = "%(levelname)s: %(message)s"
    format_error: str = "%(levelname)s: %(message)s"
    format_critical: str = "%(levelname)s - %(message)s (%(filename)s: line %(lineno)d)"
    FORMATS: dict[int, str] = {
        logging.DEBUG: green + format_debug + reset,
        logging.INFO: grey + format_info + reset,
        logging.WARNING: yellow + format_warning + reset,
        logging.ERROR: red + format_error + reset,
        logging.CRITICAL: bold_red + format_critical + reset,
    }

    def format(self, record) -> str:
        log_fmt: str | None = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(fmt=log_fmt)
        return formatter.format(record=record)


def setup_logger(
    level_file: int = logging.DEBUG,
    level_console: int = logging.INFO,
    filename: str = "my_log.log",
) -> logging.Logger:
    """
    Set up a logger with file and console handlers.

    This function sets up a logger with a rotating file handler and a console handler.
    The file handler writes log messages to a file, and the console handler writes log messages to
    the console using colors.

    Args:
        level_file (int, optional): The log level for the file handler. Defaults to logging.DEBUG.
        level_console (int, optional): The log level for the console handler. Defaults to logging.INFO.
        filename (str, optional): The name of the log file. Defaults to "my_log.log".

    Returns:
        logging.Logger: The set up logger.
    """
    log_formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(message)s (%(filename)s: line %(lineno)d)",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    max_log_size = 5 * 1024 * 1024
    backup_count = 3
    file_handler = RotatingFileHandler(
        filename=filename, maxBytes=max_log_size, backupCount=backup_count
    )
    file_handler.setFormatter(fmt=log_formatter)

    logger: logging.Logger = logging.getLogger(name="my_logger")
    logger.setLevel(level=level_file)
    logger.addHandler(hdlr=file_handler)

    # Define a Handler for console output
    console = logging.StreamHandler(stream=None)
    console.setLevel(level=level_console)
    console.setFormatter(fmt=CustomFormatter())
    logger.addHandler(hdlr=console)
    return logger


def main() -> None:
    logger: logging.Logger = setup_logger(filename="Playground/logtest.log")
    logger.debug(msg="This is a debug message")
    logger.info(msg="This is an info message")
    logger.warning(msg="This is a warning message")
    logger.error(msg="This is an error message")
    logger.critical(msg="This is a critical message")


if __name__ == "__main__":
    main()
