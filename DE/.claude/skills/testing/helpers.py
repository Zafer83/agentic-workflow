import json
import sys


def parse_pytest_results(file_path):
    """
    Parst pytest-json-report und gibt eine kompakte
    Zusammenfassung für den LLM-Agenten aus.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)

        summary = data.get('summary', {})
        failed = [t for t in data.get('tests', []) if t.get('outcome') == 'failed']

        print(f"### Test Summary")
        print(f"Passed: {summary.get('passed', 0)}, Failed: {summary.get('failed', 0)}")

        if failed:
            print("\n#### Failed Details:")
            for test in failed:
                print(f"- {test['nodeid']}: {test['call']['longrepr'][:200]}...")

    except Exception as e:
        print(f"Error parsing results: {e}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        parse_pytest_results(sys.argv[1])