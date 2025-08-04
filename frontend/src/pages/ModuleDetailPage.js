import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { useLanguage } from '../contexts/LanguageContext';
import { learningAPI } from '../services/api';
import LessonCard from '../components/modules/LessonCard';
import './ModuleDetailPage.css';

const ModuleDetailPage = () => {
  const { id } = useParams();
  const { language, t } = useLanguage();
  const [module, setModule] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchModule = async () => {
      try {
        setLoading(true);
        const response = await learningAPI.getModule(id);
        setModule(response.data);
      } catch (err) {
        setError(t(
          'Failed to load module details. Please try again.',
          'Error al cargar los detalles del módulo. Por favor intenta de nuevo.'
        ));
        console.error('Error fetching module:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchModule();
  }, [id, t]);

  if (loading) {
    return (
      <div className="container">
        <div className="loading">
          {t('Loading module...', 'Cargando módulo...')}
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="container">
        <div className="error">{error}</div>
        <Link to="/" className="btn btn-primary">
          {t('Back to Home', 'Volver al Inicio')}
        </Link>
      </div>
    );
  }

  if (!module) {
    return (
      <div className="container">
        <div className="error">
          {t('Module not found.', 'Módulo no encontrado.')}
        </div>
        <Link to="/" className="btn btn-primary">
          {t('Back to Home', 'Volver al Inicio')}
        </Link>
      </div>
    );
  }

  const title = language === 'es' ? module.title_es : module.title;
  const description = language === 'es' ? module.description_es : module.description;

  return (
    <div className="container">
      <div className="module-detail-page">
        <div className="breadcrumb">
          <Link to="/">{t('Home', 'Inicio')}</Link>
          <span> / </span>
          <span>{title}</span>
        </div>

        <div className="module-header">
          <div className="module-icon-large">{module.icon}</div>
          <div className="module-info">
            <h1 className="module-title">{title}</h1>
            <p className="module-description">{description}</p>
            
            <div className="module-stats">
              <div className="stat">
                <span className="stat-label">
                  {t('Difficulty', 'Dificultad')}:
                </span>
                <span className="stat-value">
                  {module.difficulty_level === 1 ? t('Beginner', 'Principiante') :
                   module.difficulty_level === 2 ? t('Intermediate', 'Intermedio') :
                   t('Advanced', 'Avanzado')}
                </span>
              </div>
              <div className="stat">
                <span className="stat-label">
                  {t('Time', 'Tiempo')}:
                </span>
                <span className="stat-value">
                  {module.estimated_time} {t('minutes', 'minutos')}
                </span>
              </div>
              <div className="stat">
                <span className="stat-label">
                  {t('Lessons', 'Lecciones')}:
                </span>
                <span className="stat-value">
                  {module.lessons.length}
                </span>
              </div>
            </div>
          </div>
        </div>

        <div className="lessons-section">
          <h2 className="section-title">
            {t('Lessons', 'Lecciones')}
          </h2>
          
          <div className="lessons-list">
            {module.lessons.map((lesson, index) => (
              <LessonCard 
                key={lesson.id} 
                lesson={lesson} 
                index={index + 1}
              />
            ))}
          </div>

          {module.lessons.length === 0 && (
            <p className="no-lessons">
              {t(
                'No lessons available for this module yet.',
                'Aún no hay lecciones disponibles para este módulo.'
              )}
            </p>
          )}
        </div>
      </div>
    </div>
  );
};

export default ModuleDetailPage;