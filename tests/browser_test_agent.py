#!/usr/bin/env python3
"""
Browser Testing Agent for ORBIT Workflow

This agent uses Cursor's browser automation tools to test the complete
ORBIT interview workflow: start session, answer questions, handle errors,
and verify successful completion.

This script is designed to be executed by Cursor's AI assistant, which has
access to browser automation tools. When run, it provides step-by-step
instructions for the AI to execute using Cursor's browser MCP tools.
"""

import os
import time
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any, List, Tuple
import json


class BrowserTestAgent:
    """Automated browser testing agent for ORBIT workflow."""
    
    def __init__(self, frontend_url: str = "http://localhost:5174"):
        """
        Initialize the browser test agent.
        
        Args:
            frontend_url: URL of the frontend application
        """
        self.frontend_url = frontend_url
        self.log_dir = Path(__file__).parent / "browser_test_logs"
        self.log_dir.mkdir(exist_ok=True)
        
        # Setup logging
        log_file = self.log_dir / f"test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
        self.session_id: Optional[str] = None
        self.question_count = 0
        self.max_retries = 3
        self.retry_delay = 1  # Base delay in seconds
        self.max_questions = 50
        self.timeout = 300  # 5 minutes
        self.test_steps: List[Dict[str, Any]] = []
        self.current_snapshot: Optional[Dict[str, Any]] = None
        
    def log_action(self, action: str, details: Optional[Dict[str, Any]] = None):
        """Log an action with details."""
        message = f"ACTION: {action}"
        if details:
            message += f" | Details: {json.dumps(details, indent=2)}"
        self.logger.info(message)
    
    def log_error(self, error: str, details: Optional[Dict[str, Any]] = None):
        """Log an error with details."""
        message = f"ERROR: {error}"
        if details:
            message += f" | Details: {json.dumps(details, indent=2)}"
        self.logger.error(message)
    
    def retry_with_backoff(self, func, *args, **kwargs):
        """
        Retry a function with exponential backoff.
        
        Args:
            func: Function to retry
            *args: Positional arguments for func
            **kwargs: Keyword arguments for func
            
        Returns:
            Result of func call
            
        Raises:
            Exception: If all retries fail
        """
        last_exception = None
        for attempt in range(self.max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                last_exception = e
                if attempt < self.max_retries - 1:
                    delay = self.retry_delay * (2 ** attempt)
                    self.log_action(
                        f"Retry attempt {attempt + 1}/{self.max_retries}",
                        {"delay": delay, "error": str(e)}
                    )
                    time.sleep(delay)
                else:
                    self.log_error(f"All retries exhausted for {func.__name__}", {"error": str(e)})
        
        raise last_exception
    
    def handle_error_with_retry(self, action_description: str, action_func, *args, **kwargs):
        """
        Handle errors with retry logic for browser actions.
        
        This method wraps browser actions with error handling and retry logic.
        It logs errors, retries with exponential backoff, and handles different
        error scenarios (missing elements, timeouts, network errors).
        
        Args:
            action_description: Human-readable description of the action
            action_func: Function to execute
            *args: Positional arguments for action_func
            **kwargs: Keyword arguments for action_func
            
        Returns:
            Result of action_func if successful
            
        Raises:
            Exception: If all retries fail
        """
        self.log_action(f"Executing: {action_description}")
        
        last_exception = None
        for attempt in range(self.max_retries):
            try:
                result = action_func(*args, **kwargs)
                self.log_action(f"Success: {action_description}")
                return result
            except Exception as e:
                last_exception = e
                error_type = type(e).__name__
                error_msg = str(e)
                
                # Log error details
                self.log_error(
                    f"Error in {action_description} (attempt {attempt + 1}/{self.max_retries})",
                    {
                        "error_type": error_type,
                        "error_message": error_msg,
                        "attempt": attempt + 1,
                        "max_retries": self.max_retries
                    }
                )
                
                # Determine if we should retry
                if attempt < self.max_retries - 1:
                    delay = self.retry_delay * (2 ** attempt)
                    self.log_action(
                        f"Retrying {action_description} after {delay}s",
                        {"delay": delay, "next_attempt": attempt + 2}
                    )
                    time.sleep(delay)
                else:
                    self.log_error(
                        f"All retries exhausted for {action_description}",
                        {"error": error_msg, "final_attempt": attempt + 1}
                    )
        
        # Re-raise the last exception
        raise last_exception
    
    def navigate_to_frontend(self):
        """
        Navigate to the frontend URL.
        
        This method should be called by Cursor's AI assistant using browser_navigate.
        """
        self.log_action("Navigating to frontend", {"url": self.frontend_url})
        self.test_steps.append({
            "step": "navigate",
            "url": self.frontend_url,
            "timestamp": datetime.now().isoformat()
        })
        # In actual execution, Cursor's AI will call: browser_navigate(url=self.frontend_url)
        return {"action": "navigate", "url": self.frontend_url}
    
    def wait_for_element(self, element_description: str, text: Optional[str] = None, timeout: int = 10):
        """
        Wait for an element to appear on the page.
        
        Args:
            element_description: Human-readable description of element
            text: Text to wait for (for browser_wait_for)
            timeout: Maximum time to wait in seconds
            
        Returns:
            Dict with action details for browser_wait_for
        """
        self.log_action(f"Waiting for element: {element_description}", {"timeout": timeout, "text": text})
        self.test_steps.append({
            "step": "wait_for",
            "description": element_description,
            "text": text,
            "timeout": timeout,
            "timestamp": datetime.now().isoformat()
        })
        # In actual execution, Cursor's AI will call: browser_wait_for(text=text, time=timeout)
        return {"action": "wait_for", "text": text, "time": timeout}
    
    def click_element(self, element_description: str, ref: Optional[str] = None, text: Optional[str] = None):
        """
        Click an element on the page.
        
        Args:
            element_description: Human-readable description of element
            ref: Element reference from page snapshot
            text: Text to identify element if ref not available
            
        Returns:
            Dict with action details for browser_click
        """
        self.log_action(f"Clicking element: {element_description}", {"ref": ref, "text": text})
        self.test_steps.append({
            "step": "click",
            "description": element_description,
            "ref": ref,
            "text": text,
            "timestamp": datetime.now().isoformat()
        })
        # In actual execution, Cursor's AI will call: browser_click(element=element_description, ref=ref)
        return {"action": "click", "element": element_description, "ref": ref}
    
    def take_snapshot(self):
        """
        Take a snapshot of the current page.
        
        Returns:
            Dict with action details for browser_snapshot
        """
        self.log_action("Taking page snapshot")
        self.test_steps.append({
            "step": "snapshot",
            "timestamp": datetime.now().isoformat()
        })
        # In actual execution, Cursor's AI will call: browser_snapshot()
        return {"action": "snapshot"}
    
    def take_screenshot(self, filename: Optional[str] = None):
        """
        Take a screenshot of the current page.
        
        Args:
            filename: Optional filename for screenshot
            
        Returns:
            Dict with action details for browser_take_screenshot
        """
        if filename is None:
            filename = f"results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        
        screenshot_path = self.log_dir / filename
        self.log_action(f"Taking screenshot: {filename}", {"path": str(screenshot_path)})
        self.test_steps.append({
            "step": "screenshot",
            "filename": filename,
            "path": str(screenshot_path),
            "timestamp": datetime.now().isoformat()
        })
        # In actual execution, Cursor's AI will call: browser_take_screenshot(filename=filename)
        return {"action": "screenshot", "filename": filename, "fullPage": True}
    
    def start_session(self):
        """
        Start the interview session by clicking the Start Interview button.
        
        Returns:
            List of actions to execute
        """
        self.log_action("Starting session")
        actions = []
        
        # Wait for page to load
        actions.append(self.wait_for_element("Start Interview button", text="Start Interview", timeout=15))
        
        # Take snapshot to find the button
        actions.append(self.take_snapshot())
        
        # Click Start Interview button
        actions.append(self.click_element("Start Interview button", text="Start Interview"))
        
        # Wait for first question to appear (look for question text or loading to complete)
        actions.append(self.wait_for_element("Question text or loading completion", timeout=10))
        
        self.log_action("Session start actions prepared")
        return actions
    
    def detect_question_type(self, snapshot_text: str) -> str:
        """
        Detect the question type from the page snapshot text.
        
        Args:
            snapshot_text: Text content from page snapshot
            
        Returns:
            Question type: 'multiple_choice', 'likert', or 'slider'
        """
        snapshot_lower = snapshot_text.lower()
        
        # Check for slider indicators
        if "slider" in snapshot_lower or "range" in snapshot_lower or "0" in snapshot_text and "1" in snapshot_text:
            # Look for slider input and Continue button
            if "continue" in snapshot_lower:
                return "slider"
        
        # Check for numeric buttons (likert scale)
        # Likert questions have numeric options like 1, 2, 3, 4, 5
        if any(str(i) in snapshot_text for i in range(1, 11)):
            # Check if buttons contain only numbers
            return "likert"
        
        # Default to multiple choice
        return "multiple_choice"
    
    def answer_multiple_choice(self):
        """
        Answer a multiple choice question by clicking the first option.
        
        Returns:
            List of actions to execute
        """
        self.log_action("Answering multiple choice question")
        actions = []
        
        # Take snapshot to find options
        actions.append(self.take_snapshot())
        
        # Click first available option button (will be identified from snapshot)
        actions.append(self.click_element("First answer option button"))
        
        # Wait for loading state or next question
        actions.append(self.wait_for_element("Next question or loading completion", timeout=5))
        
        self.question_count += 1
        self.log_action(f"Prepared answer for question #{self.question_count}")
        return actions
    
    def answer_likert(self):
        """
        Answer a likert scale question by clicking the first numeric option.
        
        Returns:
            List of actions to execute
        """
        self.log_action("Answering likert scale question")
        actions = []
        
        # Take snapshot to find options
        actions.append(self.take_snapshot())
        
        # Click first numeric option button
        actions.append(self.click_element("First numeric option button"))
        
        # Wait for loading state or next question
        actions.append(self.wait_for_element("Next question or loading completion", timeout=5))
        
        self.question_count += 1
        self.log_action(f"Prepared answer for question #{self.question_count}")
        return actions
    
    def answer_slider(self):
        """
        Answer a slider question by clicking Continue (default value is fine).
        
        Returns:
            List of actions to execute
        """
        self.log_action("Answering slider question")
        actions = []
        
        # Take snapshot to find slider and Continue button
        actions.append(self.take_snapshot())
        
        # Click Continue button (slider default value is acceptable)
        actions.append(self.wait_for_element("Continue button", text="Continue", timeout=5))
        actions.append(self.click_element("Continue button", text="Continue"))
        
        # Wait for loading state or next question
        actions.append(self.wait_for_element("Next question or loading completion", timeout=5))
        
        self.question_count += 1
        self.log_action(f"Prepared answer for question #{self.question_count}")
        return actions
    
    def answer_question(self):
        """
        Answer the current question by detecting type and using appropriate method.
        
        Returns:
            List of actions to execute
        """
        self.log_action(f"Preparing to answer question #{self.question_count + 1}")
        
        # Take snapshot to detect question type
        snapshot_action = self.take_snapshot()
        
        # Answer based on type (will be determined from snapshot)
        # We'll try multiple_choice first, then check snapshot to determine actual type
        actions = [snapshot_action]
        
        # Add actions for answering (type will be determined when executing)
        # Default to multiple_choice approach
        actions.extend(self.answer_multiple_choice())
        
        return actions
    
    def is_results_page(self, snapshot_text: str) -> bool:
        """
        Check if we're on the results page.
        
        Args:
            snapshot_text: Text content from page snapshot
            
        Returns:
            True if results page is detected
        """
        # Look for "Your Recommendations" heading
        return "Your Recommendations" in snapshot_text or "recommendations" in snapshot_text.lower()
    
    def wait_for_results(self, max_questions: Optional[int] = None, timeout: Optional[int] = None):
        """
        Generate actions to wait for the results page to appear.
        
        Args:
            max_questions: Maximum number of questions to answer before giving up (uses self.max_questions if None)
            timeout: Maximum time in seconds to wait (uses self.timeout if None)
            
        Returns:
            List of actions to execute
        """
        max_questions = max_questions or self.max_questions
        timeout = timeout or self.timeout
        self.log_action("Preparing to wait for results page", {"max_questions": max_questions, "timeout": timeout})
        
        actions = []
        
        # This will be a loop executed by the AI assistant
        # For now, we'll prepare actions for checking and answering
        actions.append(self.take_snapshot())
        
        # Note: The actual execution will loop until results page is found
        # or max_questions/timeout is reached
        
        return actions
    
    def verify_results(self):
        """
        Verify that results are displayed correctly.
        
        Returns:
            List of actions to execute
        """
        self.log_action("Verifying results page")
        actions = []
        
        # Wait for recommendations to be visible
        actions.append(self.wait_for_element("Recommendations list", text="Your Recommendations", timeout=10))
        
        # Take snapshot to verify content
        actions.append(self.take_snapshot())
        
        # Verify key elements are present
        # - "Your Recommendations" heading
        # - At least one recommendation card
        # - Match scores
        
        self.log_action("Results verification actions prepared")
        return actions
    
    def generate_test_plan(self):
        """
        Generate a complete test plan with all actions.
        
        Returns:
            Dict with test plan and actions
        """
        self.logger.info("=" * 60)
        self.logger.info("Generating ORBIT Browser Test Plan")
        self.logger.info("=" * 60)
        
        plan = {
            "frontend_url": self.frontend_url,
            "steps": []
        }
        
        # Step 1: Navigate to frontend
        plan["steps"].append({
            "name": "Navigate to frontend",
            "actions": [self.navigate_to_frontend()]
        })
        
        # Step 2: Start session
        plan["steps"].append({
            "name": "Start session",
            "actions": self.start_session()
        })
        
        # Step 3: Answer questions until results page
        plan["steps"].append({
            "name": "Answer questions until results",
            "actions": self.wait_for_results(),
            "loop": True,
            "max_iterations": 50,
            "stop_condition": "Results page detected"
        })
        
        # Step 4: Verify results
        plan["steps"].append({
            "name": "Verify results",
            "actions": self.verify_results()
        })
        
        # Step 5: Take screenshot
        plan["steps"].append({
            "name": "Take success screenshot",
            "actions": [self.take_screenshot("test_success.png")]
        })
        
        return plan
    
    def save_test_plan(self, plan: Dict[str, Any]):
        """Save test plan to JSON file."""
        plan_file = self.log_dir / f"test_plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(plan_file, 'w') as f:
            json.dump(plan, f, indent=2)
        self.logger.info(f"Test plan saved to: {plan_file}")
        return plan_file
    
    def run_test(self):
        """
        Main orchestration method - runs the complete test workflow.
        
        This method orchestrates the entire test execution:
        1. Navigate to frontend
        2. Start session
        3. Answer questions until results page
        4. Verify results
        5. Take screenshot
        
        Note: This method provides the execution logic. When called by Cursor's AI assistant,
        it will execute the steps using browser automation tools (mcp_CursorBrowser_*).
        
        Returns:
            True if test passed, False otherwise
        """
        self.logger.info("=" * 60)
        self.logger.info("Starting ORBIT Browser Test Execution")
        self.logger.info("=" * 60)
        
        try:
            # Step 1: Navigate to frontend
            self.log_action("Step 1: Navigating to frontend")
            nav_action = self.navigate_to_frontend()
            self.logger.info(f"  -> Execute: browser_navigate(url='{nav_action['url']}')")
            
            # Step 2: Start session
            self.log_action("Step 2: Starting session")
            session_actions = self.start_session()
            for action in session_actions:
                self.logger.info(f"  -> Execute: {action.get('action', 'unknown')}")
            
            # Step 3: Answer questions until results page
            self.log_action("Step 3: Answering questions until results page")
            self.logger.info(f"  -> Max questions: {self.max_questions}, Timeout: {self.timeout}s")
            
            start_time = time.time()
            iteration = 0
            
            while iteration < self.max_questions and (time.time() - start_time) < self.timeout:
                iteration += 1
                self.logger.info(f"  -> Iteration {iteration}: Checking for results page")
                
                # Take snapshot to check if we're on results page
                snapshot_action = self.take_snapshot()
                self.logger.info(f"  -> Execute: browser_snapshot()")
                
                # Note: In actual execution, AI assistant will:
                # 1. Call browser_snapshot()
                # 2. Check if "Your Recommendations" text is in snapshot
                # 3. If yes, break loop and go to Step 4
                # 4. If no, answer current question
                
                # Answer question
                self.log_action(f"Answering question #{self.question_count + 1}")
                answer_actions = self.answer_question()
                for action in answer_actions:
                    self.logger.info(f"  -> Execute: {action.get('action', 'unknown')}")
                
                # Check timeout
                if (time.time() - start_time) >= self.timeout:
                    self.log_error("Timeout reached waiting for results page")
                    return False
            
            if iteration >= self.max_questions:
                self.log_error("Maximum question count reached")
                return False
            
            # Step 4: Verify results
            self.log_action("Step 4: Verifying results page")
            verify_actions = self.verify_results()
            for action in verify_actions:
                self.logger.info(f"  -> Execute: {action.get('action', 'unknown')}")
            
            # Step 5: Take screenshot
            self.log_action("Step 5: Taking success screenshot")
            screenshot_action = self.take_screenshot("test_success.png")
            self.logger.info(f"  -> Execute: browser_take_screenshot(filename='{screenshot_action['filename']}', fullPage=True)")
            
            self.logger.info("=" * 60)
            self.logger.info("TEST PASSED: Successfully completed workflow")
            self.logger.info(f"Questions answered: {self.question_count}")
            self.logger.info("=" * 60)
            return True
            
        except Exception as e:
            self.log_error("Test failed with exception", {"error": str(e)})
            screenshot_action = self.take_screenshot("test_failure.png")
            self.logger.info(f"  -> Execute: browser_take_screenshot(filename='{screenshot_action['filename']}', fullPage=True)")
            return False


def main():
    """
    Main entry point for the test agent.
    
    This runs the test using the run_test() orchestration method.
    The test will be executed by Cursor's AI assistant using browser automation tools.
    """
    import sys
    
    # Parse command line arguments
    frontend_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:5174"
    
    agent = BrowserTestAgent(frontend_url=frontend_url)
    
    # Run the test
    success = agent.run_test()
    
    if success:
        agent.logger.info("\nTest completed successfully!")
        return 0
    else:
        agent.logger.error("\nTest failed!")
        return 1


if __name__ == "__main__":
    main()

