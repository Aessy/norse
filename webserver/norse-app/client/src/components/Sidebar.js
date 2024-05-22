import React, { useState } from 'react';
import './Sidebar.css';

const menuItems = [
  {
    title: 'Item 1',
    submenu: ['Subitem 1.1', 'Subitem 1.2']
  },
  {
    title: 'Item 2',
    submenu: ['Subitem 2.1', 'Subitem 2.2']
  },
  {
    title: 'Item 3',
    submenu: ['Subitem 3.1', 'Subitem 3.2']
  }
];

const Sidebar = () => {
  const [expandedMenu, setExpandedMenu] = useState(null);

  const handleMenuClick = (index) => {
    setExpandedMenu(expandedMenu === index ? null : index);
  };

  return (
    <div className="sidebar">
      <ul className="menu">
        {menuItems.map((item, index) => (
          <li key={index}>
            <div onClick={() => handleMenuClick(index)} className="menu-item">
              {item.title}
            </div>
            {expandedMenu === index && (
              <ul className="submenu">
                {item.submenu.map((subitem, subindex) => (
                  <li key={subindex} className="submenu-item">
                    {subitem}
                  </li>
                ))}
              </ul>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Sidebar;