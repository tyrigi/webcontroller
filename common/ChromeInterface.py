import os, platform, subprocess, time, socket
from subprocess import PIPE

try:
    from subprocess import DEVNULL
    _DEVNULL_PRESENT = True
except ImportError:
    DEVNULL = -3
    _DEVNULL_PRESENT = False

class ChromeInterface(object):

    def __init__(self, executable):
        self.path = executable


    def start(self):
        free_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        free_socket.bind(('0.0.0.0', 0))
        free_socket.listen(5)
        port = free_socket.getsockname()[1]
        free_socket.close()

        cmd = [self.path, '--port='+str(port)]
        self.process = subprocess.Popen(cmd, env=os.environ, close_fds=platform.system()!='Windows')
        start = time.time()
        while True:
            return_val = self.process.poll()
            if return_val is not None:
                raise Exception
            try:
                socket_ = socket.create_connection(('localhost', port), 1)
                socket_.close()
                break
            except socket.error:
                pass
            if time.time() - start > 30:
                raise Exception

    def stop(self):
        try:
            if self.process:
                for stream in [self.process.stdin,
                                self.process.stdout,
                                self.process.stderr]:
                    try:
                        stream.close()
                    except AttributeError:
                        pass
                self.process.terminate()
                self.process.wait()
                self.process.kill()
                self.process = None
        except OSError:
            pass