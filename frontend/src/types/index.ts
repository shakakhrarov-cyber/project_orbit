export interface Question {
  id: string;
  text: string;
  type: 'multiple_choice' | 'likert' | 'slider' | 'free_text';
  options?: string[] | number[];
}

export interface SessionStartResponse {
  session_id: string;
  question: Question;
}

export interface ResponseRequest {
  session_id: string;
  question_id: string;
  answer: string | number | null;
}

export interface ResponseResponse {
  question?: Question;
  done?: boolean;
  session_id?: string;
  reason?: string;
}

export interface MatchRecommendation {
  rank: number;
  archetype_id: string;
  name: string;
  fit_score: number;
  explanation: string;
}

export interface ResultResponse {
  session_id: string;
  recommendations: MatchRecommendation[];
  confidence?: number;
  average_uncertainty?: number;
  questions_answered: number;
}

