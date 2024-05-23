import React, { useState } from 'react';
import './Sidebar.css';


const Sidebar = ({routes, onRouteClicked}) => {
  const [expandedMenu, setExpandedMenu] = useState(null);

  const handleMenuClick = (item) => {
    onRouteClicked(item)
  };

  const menuItems = [
    /*
    {
      title: 'Item 1',
      submenu: ['Subitem 1.1', 'Subitem 1.2']
    }
    */
  ];
  routes.map((route, index) => {
    menuItems.push({title: route.origin + "-" + route.destination, submenu: ['test']})
  })

  return (
    <div className="sidebar">
      <ul className="menu">
        {routes.map((item, index) => (
          <li key={index}>
            <div onClick={() => handleMenuClick(item)} className="menu-item">
              {item.origin + "-" + item.destination}
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Sidebar;