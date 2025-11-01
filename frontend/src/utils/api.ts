import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add request interceptor for debugging
apiClient.interceptors.request.use(
  (config) => {
    console.log(`Making ${config.method?.toUpperCase()} request to:`, config.url);
    return config;
  },
  (error) => {
    console.error('Request error:', error);
    return Promise.reject(error);
  }
);

// Add response interceptor for debugging
apiClient.interceptors.response.use(
  (response) => {
    console.log('Response received:', response.status, response.data);
    return response;
  },
  (error) => {
    console.error('Response error:', error.response?.status, error.response?.data || error.message);
    return Promise.reject(error);
  }
);

export const sessionApi = {
  start: async () => {
    const response = await apiClient.post('/session/start');
    return response.data;
  },
  
  submitResponse: async (sessionId: string, questionId: string, answer: string | number) => {
    const response = await apiClient.post('/response', {
      session_id: sessionId,
      question_id: questionId,
      answer: answer,
    });
    return response.data;
  },
  
  getResult: async (sessionId: string) => {
    const response = await apiClient.get(`/session/${sessionId}/result`);
    return response.data;
  },
};

