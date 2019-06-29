import os

from stlib import MainWindow


def main():
    workDir = os.getcwd()
    mw = MainWindow(workDir=workDir)
    mw.run()


if __name__ == "__main__":
    main()
