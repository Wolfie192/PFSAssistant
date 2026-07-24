import sys
import argparse
import ui

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PFS Assistant")
    parser.add_argument("--dev", action="store_true", help="Enable developer mode to access un-implemented scenarios.")
    args = parser.parse_args()