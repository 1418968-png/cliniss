from __future__ import annotations

import os
import sys
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


def bundle_root() -> Path:
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return Path(sys._MEIPASS)  # type: ignore[attr-defined]
    return Path(__file__).resolve().parents[1]


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


def main() -> None:
    root = bundle_root()
    os.chdir(root)
    root_path = str(root)
    if root_path not in sys.path:
        sys.path.insert(0, root_path)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.test_bundle_settings')
    execute_from_command_line([argv0(), *command_args(sys.argv)])


def argv0() -> str:
    return Path(sys.argv[0]).name or 'cliniss-tests'


if __name__ == '__main__':
    main()
