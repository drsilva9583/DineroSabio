import React, { useState, useEffect } from 'react';
import { useLanguage } from '../contexts/LanguageContext';
import { learningAPI } from '../services/api';
import ModuleCard from '../components/modules/ModuleCard';
import './HomePage.css';

const HomePage = () => {
  const { t } = useLanguage();
  const [modules, setModules] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchModules = async () => {
      try {
        setLoading(true);
        const response = await learningAPI.getModules();
        setModules(response.data);
      } catch (err) {
        setError(t(
          'Failed to load learning modules. Please try again.',
          'Error al cargar los módulos de aprendizaje. Por favor intenta de nuevo.'
        ));
        console.error('Error fetching modules:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchModules();
  }, [t]);

  if (loading) {
    return (
      <div className="container">
        <div className="loading">
          {t('Loading learning modules...', 'Cargando módulos de aprendizaje...')}
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="container">
        <div className="error">{error}</div>
      </div>
    );
  }

  return (
    <div className="container">
      <div className="home-page">
        <section className="hero">
          <h1 className="hero-title">
            {t(
              'Start Your Financial Journey Today',
              'Comienza tu Jornada Financiera Hoy'
            )}
          </h1>
          <p className="hero-subtitle">
            {t(
              'Learn saving and investing through culturally relevant examples and practical advice.',
              'Aprende a ahorrar e invertir a través de ejemplos culturalmente relevantes y consejos prácticos.'
            )}
          </p>
        </section>

        <section className="modules-section">
          <h2 className="section-title">
            {t('Learning Modules', 'Módulos de Aprendizaje')}
          </h2>
          
          <div className="modules-grid">
            {modules.map(module => (
              <ModuleCard key={module.id} module={module} />
            ))}
          </div>

          {modules.length === 0 && (
            <p className="no-modules">
              {t(
                'No learning modules available at the moment.',
                'No hay módulos de aprendizaje disponibles en este momento.'
              )}
            </p>
          )}
        </section>
      </div>
    </div>
  );
};

export default HomePage;