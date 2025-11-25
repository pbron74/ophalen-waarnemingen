import sys
from vallenplan import start_gui

def main():
    if "--run-vallenplan" in sys.argv:
        start_gui()
    elif __name__ == "__main__":
        start_gui()

if __name__ == "__main__":
    main()