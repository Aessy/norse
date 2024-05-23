// src/App.js
import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector, connect } from 'react-redux';
import { fetchFlights } from './redux/actions/flightActions';
import { fetchRoutes } from './redux/actions/routesActions';
import { fetchPriceHistory } from './redux/actions/priceHistoryAction';
import Sidebar from './components/Sidebar';
import Calendar from './components/Calendar';
import './App.css';

const App = () => {
  const dispatch = useDispatch();
  const priceHistoryState = useSelector((state) => state.price_history);
  const routesState = useSelector((state) => state.routes);

  useEffect(() => {
    console.log("Use Effect")
    dispatch(fetchRoutes());
  }, [dispatch]);

  const [calendarData, setCalendarData] = useState({
    1: 'Event 1',
    2: 'Event 2',
    15: 'Event 3'
  });

  const handleDayClick = (day) => {
    dispatch(fetchPriceHistory("OSL", "BKK", "2024-06-01", "2024-06-30"))
  };

  const handleRouteClicked = (route) => {
    dispatch(fetchPriceHistory(route.origin, route.destination, "2024-06-01", "2024-06-30"))
  }


  return (
    <div className="App">
      <Sidebar routes={routesState.routes} onRouteClicked={handleRouteClicked} />
      <div className="main-content">
        <Calendar
                initialMonth={new Date().getMonth()}
                initialYear={new Date().getFullYear()}
                data={[priceHistoryState.priceHistory]}
                onDayClick={handleDayClick}
              />
      </div>
    </div>
  );
};
export default App;