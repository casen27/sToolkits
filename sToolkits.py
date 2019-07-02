import os

# from stlib.st_tkui_core import run_tkui
from stlib.st_qtui_core import run_qtui


def main():
    workDir = os.getcwd()
    # run_tkui(workDir)
    run_qtui(workDir)


if __name__ == "__main__":
    main()
