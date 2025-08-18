import sys

class Github:
    @staticmethod
    def log(msg: str) -> None:
        print(msg, flush=True)

    @staticmethod
    def notice(msg: str) -> None:
        print(f"::notice::{msg}", flush=True)

    @staticmethod
    def warning(msg: str) -> None:
        print(f"::warning::{msg}", flush=True)

    @staticmethod
    def error(msg: str) -> None:
        print(f"::error::{msg}", flush=True)

    @staticmethod
    def bail(msg: str) -> None:
        Github.error(msg)
        sys.exit(1)

    class LogGroup:
        def __init__(self, msg: str) -> None:
            self.msg = msg

        def __enter__(self) -> None:
            print(f"::group::{self.msg}", flush=True)

        def __exit__(self, type, value, traceback) -> None:
            print(f"::endgroup::", flush=True)
