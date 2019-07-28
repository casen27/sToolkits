import os
import sys

from stlib.st_ui import run

if __name__ == "__main__":
    app = sys.argv[0]
    work_dir = os.path.dirname(app)
    run(work_dir)
