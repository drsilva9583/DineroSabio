import React, { useState } from 'react';
import { useLanguage } from '../../contexts/LanguageContext';
import './LessonCard.css';

const LessonCard = ({ lesson, index }) => {
  const { language, t } = useLanguage();
  const [isExpanded, setIsExpanded] = useState(false);

  const title = language === 'es' ? lesson.title_es : lesson.title;
  const content = language === 'es' ? lesson.content_es : lesson.content;

  const getLessonTypeIcon = (type) => {
    const icons = {
      content: '📖',
      calculator: '🧮',
      story: '📚',
      quiz: '❓'
    };
    return icons[type] || '📖';
  };

  const getLessonTypeLabel = (type) => {
    const labels = {
      content: t('Educational Content', 'Contenido Educativo'),
      calculator: t('Interactive Calculator', 'Calculadora Interactiva'),
      story: t('Story/Example', 'Historia/Ejemplo'),
      quiz: t('Quiz/Assessment', 'Quiz/Evaluación')
    };
    return labels[type] || t('Content', 'Contenido');
  };

  return (
    <div className="lesson-card">
      <div className="lesson-header" onClick={() => setIsExpanded(!isExpanded)}>
        <div className="lesson-number">{index}</div>
        <div className="lesson-info">
          <h3 className="lesson-title">
            {getLessonTypeIcon(lesson.lesson_type)} {title}
          </h3>
          <span className="lesson-type">
            {getLessonTypeLabel(lesson.lesson_type)}
          </span>
        </div>
        <button className="expand-button">
          {isExpanded ? '▼' : '▶'}
        </button>
      </div>

      {isExpanded && (
        <div className="lesson-content">
          <div className="lesson-description">
            <p>{content}</p>
          </div>

          {lesson.tips && lesson.tips.length > 0 && (
            <div className="lesson-tips">
              <h4>{t('Tips', 'Consejos')}:</h4>
              <ul>
                {lesson.tips.map(tip => (
                  <li key={tip.id} className={tip.is_highlighted ? 'highlighted-tip' : ''}>
                    {language === 'es' ? tip.tip_text_es : tip.tip_text}
                  </li>
                ))}
              </ul>
            </div>
          )}

          {lesson.quizzes && lesson.quizzes.length > 0 && (
            <div className="lesson-quizzes">
              <h4>{t('Quick Quiz', 'Quiz Rápido')}:</h4>
              {lesson.quizzes.map(quiz => (
                <div key={quiz.id} className="quiz-item">
                  <p className="quiz-question">
                    <strong>
                      {t('Myth or Reality?', '¿Mito o Realidad?')}
                    </strong><br />
                    {language === 'es' ? quiz.question_es : quiz.question}
                  </p>
                  <div className="quiz-answer">
                    <span className={`answer-badge ${quiz.is_myth ? 'myth' : 'reality'}`}>
                      {quiz.is_myth ? t('Myth', 'Mito') : t('Reality', 'Realidad')}
                    </span>
                    <p className="quiz-explanation">
                      {language === 'es' ? quiz.explanation_es : quiz.explanation}
                    </p>
                  </div>
                </div>
              ))}
            </div>
          )}

          {lesson.examples && lesson.examples.length > 0 && (
            <div className="lesson-examples">
              <h4>{t('Examples', 'Ejemplos')}:</h4>
              {lesson.examples.map(example => (
                <div key={example.id} className="example-item">
                  <h5>{language === 'es' ? example.title_es : example.title}</h5>
                  <p className="example-scenario">
                    <strong>{t('Scenario', 'Escenario')}:</strong><br />
                    {language === 'es' ? example.scenario_es : example.scenario}
                  </p>
                  <p className="example-analogy">
                    <strong>{t('How it relates', 'Cómo se relaciona')}:</strong><br />
                    {language === 'es' ? example.analogy_es : example.analogy}
                  </p>
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default LessonCard;