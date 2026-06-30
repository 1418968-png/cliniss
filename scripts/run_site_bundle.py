from __future__ import annotations

import os
import socket
import sys
import threading
import traceback
import webbrowser
from contextlib import contextmanager, redirect_stderr, redirect_stdout
from pathlib import Path


DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 8000


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


def data_dir() -> Path:
    preferred = executable_dir()
    if is_writable_dir(preferred):
        return preferred

    fallback = Path(os.environ.get('LOCALAPPDATA', Path.home())) / 'Cliniss'
    fallback.mkdir(parents=True, exist_ok=True)
    return fallback


def is_writable_dir(path: Path) -> bool:
    try:
        path.mkdir(parents=True, exist_ok=True)
        probe = path / '.cliniss-write-test'
        probe.write_text('ok', encoding='utf-8')
        probe.unlink(missing_ok=True)
        return True
    except OSError:
        return False


def log_path(base_dir: Path) -> Path:
    return base_dir / 'cliniss-site.log'


@contextmanager
def tee_output(path: Path):
    with path.open('w', encoding='utf-8') as log_file:
        stdout = Tee(sys.stdout, log_file)
        stderr = Tee(sys.stderr, log_file)
        with redirect_stdout(stdout), redirect_stderr(stderr):
            yield


def setup_environment(base_dir: Path) -> None:
    root = bundle_root()
    os.chdir(root)
    root_path = str(root)
    if root_path not in sys.path:
        sys.path.insert(0, root_path)
    os.environ.setdefault('CLINISS_SITE_DATA_DIR', str(base_dir))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.site_bundle_settings')


def host() -> str:
    return os.environ.get('CLINISS_SITE_HOST', DEFAULT_HOST)


def port() -> int:
    raw_port = os.environ.get('CLINISS_SITE_PORT')
    if raw_port:
        return int(raw_port)
    return find_free_port(host(), DEFAULT_PORT)


def find_free_port(host_name: str, start_port: int) -> int:
    for candidate in range(start_port, start_port + 100):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.2)
            if sock.connect_ex((host_name, candidate)) != 0:
                return candidate
    raise RuntimeError(f'No free port found from {start_port} to {start_port + 99}')


def open_browser_later(url: str) -> None:
    if os.environ.get('CLINISS_SITE_NO_BROWSER') == '1':
        return
    threading.Timer(1.5, lambda: webbrowser.open(url)).start()


def run_server() -> int:
    import django
    from django.core.management import call_command

    django.setup()

    bind_host = host()
    bind_port = port()
    url = f'http://{bind_host}:{bind_port}/'

    print('Applying database migrations...')
    call_command('migrate', interactive=False, verbosity=0)
    print()
    print(f'Cliniss site is running: {url}')
    print('Press Ctrl+C to stop the server.')
    print()

    open_browser_later(url)
    call_command('runserver', f'{bind_host}:{bind_port}', use_reloader=False)
    return 0


def main() -> None:
    base_dir = data_dir()
    path = log_path(base_dir)
    setup_environment(base_dir)

    exit_code = 0
    with tee_output(path):
        print(f'Log file: {path}')
        print(f'Data directory: {base_dir}')
        try:
            exit_code = run_server()
        except KeyboardInterrupt:
            print()
            print('Server stopped.')
        except BaseException:
            exit_code = 1
            traceback.print_exc()

    if exit_code:
        print()
        print(f'Лог сохранен: {path}')
        input('Нажмите Enter, чтобы закрыть окно...')

    raise SystemExit(exit_code)


if __name__ == '__main__':
    main()
