import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api/learning';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const learningAPI = {
  // Get all modules
  getModules: () => api.get('/modules/'),
  
  // Get specific module with lessons
  getModule: (id) => api.get(`/modules/${id}/`),
  
  // Get categories
  getCategories: () => api.get('/modules/categories/'),
  
  // Get lessons for a module
  getModuleLessons: (moduleId) => api.get(`/modules/${moduleId}/lessons/`),
  
  // Get all lessons
  getLessons: () => api.get('/lessons/'),
};

export default api;