import React from 'react';
import { MatchRecommendation } from '../types';

interface ResultsPageProps {
  recommendations: MatchRecommendation[];
  questionsAnswered: number;
}

export const ResultsPage: React.FC<ResultsPageProps> = ({
  recommendations,
  questionsAnswered,
}) => {
  return (
    <div className="max-w-4xl mx-auto px-6 py-12">
      <div className="text-center mb-12">
        <h1 className="text-4xl font-light text-gray-800 mb-4">
          Your Recommendations
        </h1>
        <p className="text-gray-600">
          Based on your {questionsAnswered} responses, here are your top matches:
        </p>
      </div>
      
      <div className="space-y-6">
        {recommendations.map((rec) => (
          <div
            key={rec.rank}
            className="bg-white rounded-lg shadow-sm p-8 border border-gray-100"
          >
            <div className="flex items-start justify-between mb-4">
              <div>
                <div className="flex items-center gap-3 mb-2">
                  <span className="text-sm font-medium text-gray-500">
                    #{rec.rank}
                  </span>
                  <h2 className="text-2xl font-light text-gray-800">
                    {rec.name}
                  </h2>
                </div>
                <div className="text-sm text-gray-600 mb-4">
                  {rec.explanation}
                </div>
              </div>
              <div className="text-right">
                <div className="text-3xl font-light text-gray-800">
                  {(rec.fit_score * 100).toFixed(0)}%
                </div>
                <div className="text-xs text-gray-500 mt-1">Match</div>
              </div>
            </div>
            
            <div className="w-full bg-gray-200 rounded-full h-2">
              <div
                className="bg-gray-900 h-2 rounded-full transition-all"
                style={{ width: `${rec.fit_score * 100}%` }}
              />
            </div>
          </div>
        ))}
      </div>
      
      <div className="mt-12 text-center text-gray-500 text-sm">
        <p>Thank you for using ORBIT!</p>
      </div>
    </div>
  );
};

