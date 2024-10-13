# deamon process and API of Pygit++
# EL DEMONIO
#
# Version: pre-v-0.0.0.01
#
# WARN: THIS CODE MAYBE HIGHLY UNSTABLE.
#
# WARN: known problems: (0)

import psutil
import subprocess
import os
import sys
from utils.debug import debug

ERROR_FILE_PATH = os.path.expanduser("~/.pygit/cache/demonioApi.txt")


class Demonio:
    def __init__(self):
        if len(sys.argv) == 1:
            if not self.is_running():
                self.demonio = self.summon()
            else:
                debug("Daemon already running.", "E")
                debug("Exiting", "I")

        if "stop" in sys.argv:
            self.stop()

        elif "reinit" in sys.argv:
            self.restart()

        elif "help" in sys.argv:
            self.print_help()

    def summon(self):
        """ Inicia el proceso del daemon """
        try:
            with open(ERROR_FILE_PATH, 'a') as error_file:
                process = subprocess.Popen(
                    ["python", "API/main.py"],
                    stdout=subprocess.DEVNULL,
                    stderr=error_file,
                )
            debug("Daemon is up and running", "I")
            debug("Pass 'info' to see more information", "I")
            return process

        except Exception as e:
            debug(f"Failed to start daemon: {e}", "E")
            raise

    def is_running(self):
        pid = self.get_pid()

        if pid:
            return True

        return False

    def get_pid(self):
        for proc in psutil.process_iter(['pid', 'cmdline']):
            if 'API/main.py' in proc.info['cmdline']:
                return proc.info['pid']

    def stop(self):
        pid = self.get_pid()
        if pid:
            proc = psutil.Process(pid)
            proc.terminate()
            proc.wait()
            debug("Daemon stopped", "I")
        else:
            debug("No daemon process found to stop.", "E")

    def restart(self):
        self.stop()
        self.demonio = self.summon()

    def print_help(self):
        """ Muestra ayuda sobre los comandos """
        msg = """
Demonio V-0.0.01

Usage: python demonio.py <command>

Available commands:

stop - Stops daemon process
restore - Restarts daemon process
        """
        print(msg)


if __name__ == "__main__":
    demonio = Demonio()
