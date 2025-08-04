import React from 'react';
import { useLanguage } from '../../contexts/LanguageContext';
import './Header.css';

const Header = () => {
  const { language, toggleLanguage, t } = useLanguage();

  return (
    <header className="header">
      <div className="container">
        <div className="header-content">
          <div className="logo">
            <h1>💰 Dinero Sabio</h1>
            <p className="tagline">
              {t('Wise Money for Everyone', 'Dinero Sabio para Todos')}
            </p>
          </div>
          
          <nav className="nav">
            <button 
              className="language-toggle"
              onClick={toggleLanguage}
            >
              {language === 'en' ? '🇪🇸 Español' : '🇺🇸 English'}
            </button>
          </nav>
        </div>
      </div>
    </header>
  );
};

export default Header;