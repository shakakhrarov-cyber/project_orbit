import React from 'react';
import { Question } from '../types';

interface QuestionDisplayProps {
  question: Question;
  onSubmit: (answer: string | number) => void;
  isLoading?: boolean;
}

export const QuestionDisplay: React.FC<QuestionDisplayProps> = ({
  question,
  onSubmit,
  isLoading = false,
}) => {
  return (
    <div className="max-w-2xl mx-auto px-6 py-12">
      <div className="bg-white rounded-lg shadow-sm p-8 mb-8">
        <h2 className="text-2xl font-light text-gray-800 mb-8 leading-relaxed">
          {question.text}
        </h2>
        
        {question.type === 'multiple_choice' && question.options && (
          <div className="space-y-3">
            {(question.options as string[]).map((option, index) => (
              <button
                key={index}
                onClick={() => onSubmit(option)}
                disabled={isLoading}
                className="w-full text-left px-6 py-4 border border-gray-200 rounded-lg hover:border-gray-300 hover:bg-gray-50 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {option}
              </button>
            ))}
          </div>
        )}
        
        {question.type === 'likert' && question.options && (
          <div className="space-y-3">
            {(question.options as number[]).map((value) => (
              <button
                key={value}
                onClick={() => onSubmit(value)}
                disabled={isLoading}
                className="w-full text-left px-6 py-4 border border-gray-200 rounded-lg hover:border-gray-300 hover:bg-gray-50 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {value}
              </button>
            ))}
          </div>
        )}
        
        {question.type === 'slider' && (
          <div className="py-4">
            <input
              type="range"
              min="0"
              max="1"
              step="0.01"
              defaultValue="0.5"
              onChange={(e) => onSubmit(parseFloat(e.target.value))}
              disabled={isLoading}
              className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
            />
            <div className="flex justify-between text-sm text-gray-500 mt-2">
              <span>0</span>
              <span>1</span>
            </div>
            <button
              onClick={(e) => {
                const slider = e.currentTarget.previousElementSibling?.previousElementSibling as HTMLInputElement;
                onSubmit(parseFloat(slider.value));
              }}
              disabled={isLoading}
              className="mt-6 w-full px-6 py-3 bg-gray-900 text-white rounded-lg hover:bg-gray-800 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Continue
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

