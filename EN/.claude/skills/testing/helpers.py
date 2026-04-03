import json
import sys


def parse_pytest_results(file_path):
    """
    Parses pytest-json-report and provides a concise
    summary for the LLM agent.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)

        summary = data.get('summary', {})
        failed = [t for t in data.get('tests', []) if t.get('outcome') == 'failed']

        print(f"### Test Summary")
        print(f"Passed: {summary.get('passed', 0)}, Failed: {summary.get('failed', 0)}")

        if failed:
            print("\n#### Failed Test Details:")
            for test in failed:
                # Truncate long error messages for context window efficiency
                error_msg = str(test['call']['longrepr'])[:250]
                print(f"- {test['nodeid']}\n  Error: {error_msg}...")

    except Exception as e:
        print(f"Error parsing test results: {e}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        parse_pytest_results(sys.argv[1])