#!/usr/bin/python3

import os
import sys
import fcntl
import subprocess

def main(argv):
    lockfd = os.open(argv[0], os.O_CREAT | os.O_RDWR, 0o666)
    print("Aquiring lock")
    fcntl.lockf(lockfd, fcntl.LOCK_EX)
    print("Lock aquired")
    try:
        print(subprocess.check_output(argv[1:], universal_newlines=True))
        exitcode=0
    except subprocess.CalledProcessError as err:
        print(err.output)
        exitcode=err.returncode
    fcntl.lockf(lockfd, fcntl.LOCK_UN)
    print("Lock release")
    os.close(lockfd)

if __name__ == "__main__":
    main(sys.argv[1:])
