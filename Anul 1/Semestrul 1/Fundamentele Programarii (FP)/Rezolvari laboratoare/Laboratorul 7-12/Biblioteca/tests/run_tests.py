import unittest
from colorama import Fore, Style


def run_tests_all():
    # Discover and run all tests
    loader = unittest.TestLoader()
    start_dir = 'tests'
    suite = loader.discover(start_dir, pattern='teste_*.py')

    # Create a test runner that will output to console
    runner = unittest.TextTestRunner(verbosity=2)

    print("\n[INFO] Rulare teste...")
    result = runner.run(suite)

    # Print summary with colors
    if result.wasSuccessful():
        print("\n[INFO] " + Fore.GREEN + "Toate testele au rulat cu succes!" + Style.RESET_ALL)
    else:
        print("\n[INFO] " + Fore.RED + f"Au eșuat {len(result.failures)} teste!" + Style.RESET_ALL)

    return result.wasSuccessful()


if __name__ == '__main__':
    run_tests_all()