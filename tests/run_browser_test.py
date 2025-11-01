#!/usr/bin/env python3
"""
Direct Browser Test Agent - Executes tests using Cursor's browser tools.

This script provides a simple interface for executing the ORBIT browser test.
When run, it outputs instructions for Cursor's AI to execute using browser tools.
"""

import sys
import time
from datetime import datetime
from pathlib import Path


def print_instructions(frontend_url: str = "http://localhost:5173"):
    """Print step-by-step instructions for test execution."""
    
    print("=" * 70)
    print("ORBIT Browser Test Agent - Execution Instructions")
    print("=" * 70)
    print(f"\nFrontend URL: {frontend_url}")
    print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n" + "=" * 70)
    print("STEP-BY-STEP EXECUTION PLAN")
    print("=" * 70)
    
    steps = [
        {
            "num": 1,
            "title": "Navigate to Frontend",
            "actions": [
                "Call: mcp_CursorBrowser_browser_navigate(url='{}')".format(frontend_url)
            ]
        },
        {
            "num": 2,
            "title": "Wait for Page Load and Start Session",
            "actions": [
                "Call: mcp_CursorBrowser_browser_wait_for(text='Start Interview', time=15)",
                "Call: mcp_CursorBrowser_browser_snapshot()",
                "Call: mcp_CursorBrowser_browser_click(element='Start Interview button', text='Start Interview')",
                "Wait for loading to complete (wait for 'Loading...' text to disappear)"
            ]
        },
        {
            "num": 3,
            "title": "Answer Questions Loop",
            "loop": True,
            "max_iterations": 50,
            "actions": [
                "Call: mcp_CursorBrowser_browser_snapshot()",
                "Check snapshot text for 'Your Recommendations'",
                "If found: Break loop and go to Step 4",
                "If not found:",
                "  - Detect question type from snapshot:",
                "    * Multiple choice: Click first option button",
                "    * Likert: Click first numeric option button",
                "    * Slider: Click 'Continue' button",
                "  - Wait for next question or loading to complete",
                "  - Increment question counter",
                "  - Repeat"
            ]
        },
        {
            "num": 4,
            "title": "Verify Results Page",
            "actions": [
                "Call: mcp_CursorBrowser_browser_wait_for(text='Your Recommendations', time=10)",
                "Call: mcp_CursorBrowser_browser_snapshot()",
                "Verify snapshot contains:",
                "  - 'Your Recommendations' heading",
                "  - Recommendation cards with match scores",
                "  - Questions answered count"
            ]
        },
        {
            "num": 5,
            "title": "Take Success Screenshot",
            "actions": [
                "Call: mcp_CursorBrowser_browser_take_screenshot(",
                "    filename='test_success_{}.png',".format(int(time.time())),
                "    fullPage=True",
                ")"
            ]
        }
    ]
    
    for step in steps:
        print(f"\n[{step['num']}] {step['title']}")
        print("-" * 70)
        if step.get('loop'):
            print(f"  Loop: Max {step.get('max_iterations', 50)} iterations")
            print(f"  Stop condition: Results page detected")
        for action in step['actions']:
            print(f"  {action}")
    
    print("\n" + "=" * 70)
    print("ERROR HANDLING")
    print("=" * 70)
    print("""
- Retry failed actions up to 3 times with exponential backoff
- Log all errors with full context
- If element not found: Wait longer, retry, or log error
- If timeout: Log error and continue or abort based on severity
- Take failure screenshot if test fails
    """)
    
    print("=" * 70)
    print("LOG OUTPUT")
    print("=" * 70)
    print("""
- Log all actions taken with timestamps
- Log question count after each answer
- Log errors with full details
- Log completion status
- Save logs to: tests/browser_test_logs/
    """)
    
    print("=" * 70)
    print("\nReady to execute! Ask Cursor AI to follow these instructions.")
    print("=" * 70)


if __name__ == "__main__":
    frontend_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:5173"
    print_instructions(frontend_url)

