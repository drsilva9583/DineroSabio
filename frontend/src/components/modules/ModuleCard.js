import React from 'react';
import { Link } from 'react-router-dom';
import { useLanguage } from '../../contexts/LanguageContext';
import './ModuleCard.css';

const ModuleCard = ({ module }) => {
  const { language, t } = useLanguage();

  const title = language === 'es' ? module.title_es : module.title;
  const description = language === 'es' ? module.description_es : module.description;

  const getDifficultyLabel = (level) => {
    const labels = {
      1: t('Beginner', 'Principiante'),
      2: t('Intermediate', 'Intermedio'),
      3: t('Advanced', 'Avanzado')
    };
    return labels[level] || t('Beginner', 'Principiante');
  };

  return (
    <div className="module-card">
      <div className="module-icon">{module.icon}</div>
      
      <div className="module-content">
        <h3 className="module-title">{title}</h3>
        <p className="module-description">{description}</p>
        
        <div className="module-meta">
          <span className="difficulty">
            📚 {getDifficultyLabel(module.difficulty_level)}
          </span>
          <span className="time">
            ⏱️ {module.estimated_time} {t('min', 'min')}
          </span>
          <span className="lessons-count">
            📖 {module.lessons_count} {t('lessons', 'lecciones')}
          </span>
        </div>
      </div>
      
      <Link to={`/module/${module.id}`} className="module-link">
        <button className="btn btn-primary">
          {t('Start Learning', 'Comenzar a Aprender')}
        </button>
      </Link>
    </div>
  );
};

export default ModuleCard;