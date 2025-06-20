# This script runs all tests inside test_cases folder using Pytest
import os

def run_tests():
    os.system('pytest test_cases/ --maxfail=5 --disable-warnings --tb=short')

if __name__ == '__main__':
    run_tests()
