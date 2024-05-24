// src/App.js
import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector, connect } from 'react-redux';
import { fetchFlights } from './redux/actions/flightActions';
import { fetchRoutes } from './redux/actions/routesActions';
import { fetchPriceHistory } from './redux/actions/priceHistoryAction';
import Sidebar from './components/Sidebar';
import Calendar from 'react-calendar'
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
    dispatch(fetchPriceHistory("OSL", "BKK", "2024-06-01", "2025-06-30"))
  };

  const handleRouteClicked = (route) => {
    dispatch(fetchPriceHistory(route.origin, route.destination, "2024-06-01", "2025-06-30"))
  }

  const formatWeekday = (locale, date) => {

    let price = null
    for(let i = 0; i < priceHistoryState.priceHistory.length; i++) {
      let history_date = priceHistoryState.priceHistory[i]
      let new_date = new Date(history_date.departureDate)

      console.log(new_date)
      if (new_date.getTime() == date.getTime()) {
        console.log("equal")
        //price = history_date.economy.fareTotal
        price = history_date.prices.at(-1).fareTotal
      }
    }
    return (
      <div>
        {date.getDate()}
        <p/>
        {price}
      </div>
    )
  }

  return (
    <div className="App">
      <Sidebar routes={routesState.routes} onRouteClicked={handleRouteClicked} />

      <div className="Sample">
      <header>
        <h1>Norse price history</h1>
      </header>
      <div className="Sample__container">
        <main className="Sample__container__content">
        <Calendar formatDay={formatWeekday}/>
        </main>
      </div>
    </div>

    </div>
  );
};
export default App;