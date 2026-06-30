from __future__ import annotations

import os
import sys
import traceback
from contextlib import contextmanager, redirect_stderr, redirect_stdout
from pathlib import Path

from django.core.management import execute_from_command_line


APP_TEST_LABELS = {
    'content': 'content.tests',
    'core': 'core.tests',
    'leads': 'leads.tests',
    'pages': 'pages.tests',
}
DEFAULT_TEST_LABELS = list(APP_TEST_LABELS.values())
OPTIONS_WITH_VALUES = {
    '--exclude-tag',
    '--parallel',
    '--pattern',
    '--tag',
    '--testrunner',
    '--verbosity',
    '-k',
    '-p',
    '-v',
}


class Tee:
    def __init__(self, *streams):
        self.streams = [stream for stream in streams if stream is not None]

    def write(self, data: str) -> int:
        for stream in self.streams:
            stream.write(data)
        return len(data)

    def flush(self) -> None:
        for stream in self.streams:
            stream.flush()


def bundle_root() -> Path:
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return Path(sys._MEIPASS)  # type: ignore[attr-defined]
    return Path(__file__).resolve().parents[1]


def executable_dir() -> Path:
    if getattr(sys, 'frozen', False):
        return Path(sys.executable).resolve().parent
    return Path.cwd()


def log_path() -> Path | None:
    preferred = executable_dir() / 'cliniss-tests.log'
    try:
        preferred.parent.mkdir(parents=True, exist_ok=True)
        with preferred.open('a', encoding='utf-8'):
            pass
        return preferred
    except OSError:
        try:
            import tempfile

            return Path(tempfile.gettempdir()) / 'cliniss-tests.log'
        except OSError:
            return None


@contextmanager
def tee_output(path: Path | None):
    if path is None:
        yield
        return

    with path.open('w', encoding='utf-8') as log_file:
        stdout = Tee(sys.stdout, log_file)
        stderr = Tee(sys.stderr, log_file)
        with redirect_stdout(stdout), redirect_stderr(stderr):
            yield


def command_args(argv: list[str]) -> list[str]:
    args = argv[1:]
    if not args:
        return ['test', *DEFAULT_TEST_LABELS]
    if args[0] == 'check':
        return args
    if args[0] == 'test':
        if has_test_labels(args[1:]):
            return ['test', *normalize_test_labels(args[1:])]
        return ['test', *DEFAULT_TEST_LABELS, *args[1:]]
    if args[0].startswith('-'):
        return ['test', *DEFAULT_TEST_LABELS, *args]
    return ['test', *normalize_test_labels(args)]


def has_test_labels(args: list[str]) -> bool:
    skip_next = False
    for arg in args:
        if skip_next:
            skip_next = False
            continue
        if arg == '--':
            return False
        if arg.startswith('-'):
            option = arg.split('=', 1)[0]
            if '=' not in arg and option in OPTIONS_WITH_VALUES:
                skip_next = True
            continue
        return True
    return False


def normalize_test_labels(args: list[str]) -> list[str]:
    return [APP_TEST_LABELS.get(arg, arg) for arg in args]


def run_django() -> int:
    root = bundle_root()
    os.chdir(root)
    root_path = str(root)
    if root_path not in sys.path:
        sys.path.insert(0, root_path)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.test_bundle_settings')
    try:
        execute_from_command_line([argv0(), *command_args(sys.argv)])
    except SystemExit as exc:
        if exc.code in (None, 0):
            return 0
        if isinstance(exc.code, int):
            return exc.code
        print(exc.code, file=sys.stderr)
        return 1
    except BaseException:
        traceback.print_exc()
        return 1
    return 0


def main() -> None:
    path = log_path()
    with tee_output(path):
        if path is not None:
            print(f'Log file: {path}')
        exit_code = run_django()

    if should_pause(exit_code):
        print()
        if path is not None:
            print(f'Лог сохранен: {path}')
        input('Нажмите Enter, чтобы закрыть окно...')
    raise SystemExit(exit_code)


def should_pause(exit_code: int) -> bool:
    return os.environ.get('CLINISS_TEST_PAUSE') == '1' or launched_from_explorer(exit_code)


def launched_from_explorer(exit_code: int) -> bool:
    if os.name != 'nt':
        return False
    try:
        import ctypes

        processes = (ctypes.c_ulong * 64)()
        count = ctypes.windll.kernel32.GetConsoleProcessList(processes, 64)
    except OSError:
        return exit_code != 0
    return count <= 1


def argv0() -> str:
    return Path(sys.argv[0]).name or 'cliniss-tests'


if __name__ == '__main__':
    main()
