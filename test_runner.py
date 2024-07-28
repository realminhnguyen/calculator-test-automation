import pytest # Import the pytest module
import time # Import the time module for timing the test run
from io import StringIO # Import the StringIO class from the io module for capturing stdout of the test run
import sys # Import the sys module for redirecting stdout

def run_tests():
    # Redirect stdout to capture pytest output
    captured_output = StringIO() # Create a StringIO object to capture stdout of the test run 
    sys.stdout = captured_output # Redirect stdout to the StringIO object

    # Record start time
    start_time = time.time() # Uses the time.time() function to record the start time of the test run

    # Run pytest
    result = pytest.main(["-v", "test_calculator.py"]) # Run pytest with the -v flag to display verbose output

    # Record end time
    end_time = time.time() # Uses the time.time() function to record the end time of the test run

    # Restore stdout
    sys.stdout = sys.__stdout__ 

    # Extract test results
    output = captured_output.getvalue() # Get the captured stdout output from the StringIO object
    passed = output.count("PASSED") # Count the number of tests that passed
    failed = output.count("FAILED") # Count the number of tests that failed
    errors = output.count("ERROR") # Count the number of tests that resulted in an error
    total = passed + failed + errors # Total number of tests run is equal to the sum of passed, failed, and errors

    # Generate report
    report = f"""
    ============================
    Calculator Test Suite Report
    ============================

    Total tests run: {total}
    Tests passed:    {passed}
    Tests failed:    {failed}
    Errors:          {errors}

    Execution time:  {end_time - start_time:.2f} seconds

    Detailed Results:
    -----------------
    {output}
    """

    return report, result   # Return the report and the pytest exit code

if __name__ == "__main__":
    report, exit_code = run_tests() # Run the tests and get the report and exit code
    print(report)

    # Write report to file
    with open("test_report.txt", "w") as f: # Open a file called 'test_report.txt' in write mode
        f.write(report) # Write the test report to the file

    print(f"Test report has been saved to 'test_report.txt'") 

    # Exit with pytest's exit code
    sys.exit(exit_code)