import sys
import subprocess
import pkg_resources

from requirements import requirements


def check_and_setup_modules():
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = requirements - installed
    if missing:
        python = sys.executable
        return subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
