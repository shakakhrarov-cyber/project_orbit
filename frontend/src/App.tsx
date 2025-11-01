import React, { useState } from 'react';
import { useMutation } from '@tanstack/react-query';
import { QuestionDisplay } from './components/QuestionDisplay';
import { ResultsPage } from './components/ResultsPage';
import { sessionApi } from './utils/api';
import { Question, ResponseResponse, ResultResponse } from './types';

const App: React.FC = () => {
  const [sessionId, setSessionId] = useState<string | null>(null);
  const [currentQuestion, setCurrentQuestion] = useState<Question | null>(null);
  const [isComplete, setIsComplete] = useState(false);
  const [result, setResult] = useState<ResultResponse | null>(null);

  // Start session mutation
  const startSessionMutation = useMutation({
    mutationFn: sessionApi.start,
    onSuccess: (data) => {
      console.log('Session started successfully!', data);
      setSessionId(data.session_id);
      setCurrentQuestion(data.question);
    },
    onError: (error: any) => {
      console.error('Failed to start session:', error);
      console.error('Error details:', {
        message: error.message,
        response: error.response?.data,
        status: error.response?.status,
        config: error.config
      });
      // Show user-friendly error message
      const errorMessage = error.response?.data?.detail || error.message || 'Failed to connect to server. Please check if the backend is running.';
      alert(`Error: ${errorMessage}`);
    },
  });

  // Submit response mutation
  const submitResponseMutation = useMutation({
    mutationFn: ({ sessionId, questionId, answer }: { sessionId: string; questionId: string; answer: string | number }) =>
      sessionApi.submitResponse(sessionId, questionId, answer),
    onSuccess: (data: ResponseResponse) => {
      if (data.done) {
        setIsComplete(true);
        // Fetch results
        if (data.session_id) {
          fetchResult(data.session_id);
        }
      } else if (data.question) {
        setCurrentQuestion(data.question);
      }
    },
    onError: (error: any) => {
      console.error('Failed to submit response:', error);
      const errorMessage = error.response?.data?.detail || error.message || 'Failed to submit answer. Please try again.';
      alert(`Error: ${errorMessage}`);
    },
  });

  // Fetch result query
  const fetchResult = async (sid: string) => {
    try {
      const data = await sessionApi.getResult(sid);
      setResult(data);
    } catch (error) {
      console.error('Failed to fetch result:', error);
    }
  };

  const handleStart = () => {
    console.log('=== handleStart called ===');
    console.log('API Base URL:', import.meta.env.VITE_API_URL || 'http://localhost:8000');
    console.log('Mutation state:', {
      isPending: startSessionMutation.isPending,
      isError: startSessionMutation.isError,
      isSuccess: startSessionMutation.isSuccess
    });
    try {
      startSessionMutation.mutate();
      console.log('Mutation called successfully');
    } catch (error) {
      console.error('Error calling mutation:', error);
    }
  };

  const handleAnswer = (answer: string | number) => {
    if (!sessionId || !currentQuestion) return;
    
    submitResponseMutation.mutate({
      sessionId,
      questionId: currentQuestion.id,
      answer,
    });
  };

  // Initial state - show start button
  if (!sessionId && !startSessionMutation.isPending) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="text-center">
          <h1 className="text-5xl font-light text-gray-800 mb-8">
            ORBIT
          </h1>
          <p className="text-gray-600 mb-8 text-lg">
            Discover hobbies and roles that match your preferences
          </p>
          <button
            onClick={(e) => {
              e.preventDefault();
              console.log('Start button clicked!'); // Debug log
              console.log('API Base URL:', import.meta.env.VITE_API_URL || 'http://localhost:8000');
              handleStart();
            }}
            className="px-8 py-4 bg-gray-900 text-white rounded-lg hover:bg-gray-800 transition-colors text-lg cursor-pointer"
            type="button"
          >
            Start Interview
          </button>
        </div>
      </div>
    );
  }

  // Loading state
  if (startSessionMutation.isPending || submitResponseMutation.isPending) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-gray-900 mx-auto mb-4"></div>
          <p className="text-gray-600">Loading...</p>
        </div>
      </div>
    );
  }

  // Results page
  if (isComplete && result) {
    return <ResultsPage recommendations={result.recommendations} questionsAnswered={result.questions_answered} />;
  }

  // Question display
  if (currentQuestion) {
    return (
      <div className="min-h-screen bg-gray-50">
        <QuestionDisplay
          question={currentQuestion}
          onSubmit={handleAnswer}
          isLoading={submitResponseMutation.isPending}
        />
      </div>
    );
  }

  return null;
};

export default App;

