import React, { useState } from 'react';

const Tabs = ({ tabs }) => {
  const [activeTab, setActiveTab] = useState(0);

  const handleTabClick = (index) => {
    setActiveTab(index);
  };

  return (
    <div>
      <div>
        {tabs.map((tab, index) => (
          <button
            key={index}
            onClick={() => handleTabClick(index)}
            className={index === activeTab ? 'active' : ''}
          >
            {tab.label}
          </button>
        ))}
      </div>
      <div>{tabs[activeTab].content}</div>
    </div>
  );
};

export default Tabs;