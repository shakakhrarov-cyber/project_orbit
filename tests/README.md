# Browser Testing Agent for ORBIT

## Overview

The browser testing agent automates end-to-end testing of the ORBIT interview workflow using Cursor's built-in browser automation tools. It navigates through the frontend, answers questions, handles errors with retries, and verifies successful completion by taking a screenshot of the results page.

## Files

- `browser_test_agent.py` - Main agent class that generates test plans and provides logging
- `browser_test_executor.py` - Executor script that provides execution instructions
- `browser_test_logs/` - Directory containing test logs and screenshots (auto-created)

## Usage

### Manual Execution

To run the test agent manually:

```bash
# Basic usage (defaults to http://localhost:5173)
python tests/browser_test_agent.py

# Specify custom frontend URL
python tests/browser_test_agent.py http://localhost:3000
```

The script will generate a test plan and log file. To actually execute the test, ask Cursor's AI assistant:

> "Execute the browser test agent for ORBIT workflow"

The AI assistant will use Cursor's browser automation tools (`mcp_CursorBrowser_*`) to:
1. Navigate to the frontend URL
2. Click "Start Interview" button
3. Answer questions sequentially (detecting type: multiple_choice, likert, or slider)
4. Continue until the results page appears
5. Take a screenshot of the results page
6. Log all actions and errors

### CI/CD Integration

For CI/CD pipelines, you can integrate the test agent:

```bash
# Run test and exit with error code if failed
python tests/browser_test_agent.py && echo "Test passed" || echo "Test failed"
```

## Test Workflow

1. **Navigation**: Navigates to frontend URL (default: http://localhost:5173)
2. **Session Start**: Waits for and clicks "Start Interview" button
3. **Question Answering**: 
   - Detects question type from UI
   - Answers accordingly:
     - Multiple choice: Clicks first option
     - Likert scale: Clicks first numeric option
     - Slider: Clicks Continue button
4. **Error Handling**: 
   - Retries failed actions with exponential backoff (max 3 retries)
   - Logs all errors with details
   - Handles missing elements and timeouts
5. **Completion**: 
   - Detects results page ("Your Recommendations" heading)
   - Takes screenshot
   - Verifies recommendations are displayed

## Logging

All test runs are logged to `tests/browser_test_logs/`:

- `test_YYYYMMDD_HHMMSS.log` - Detailed execution log
- `test_plan_YYYYMMDD_HHMMSS.json` - Test plan JSON
- Screenshots saved when test completes or fails

## Error Handling

The agent handles:

- Frontend not running (connection errors)
- Backend API errors (500, 404, etc.)
- Missing UI elements (timeouts)
- Network interruptions
- Session completion detection failures

All errors are logged with full context for debugging.

## Configuration

Default settings (can be modified in code):

- `frontend_url`: `http://localhost:5174` (can be overridden via command line)
- `max_questions`: 50
- `timeout`: 300 seconds (5 minutes)
- `max_retries`: 3
- `retry_delay`: 1 second (base, exponential backoff)

## Requirements

- Python 3.7+
- Cursor with browser automation tools enabled
- ORBIT frontend running on specified URL
- ORBIT backend API running and accessible

## Notes

- The agent uses Cursor's browser automation tools, so it must be executed within Cursor
- Ensure both frontend and backend are running before executing tests
- Test logs are saved for debugging and analysis
- Screenshots are taken automatically on success and failure

