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

  const handleRouteClicked = (route) => {
    dispatch(fetchPriceHistory(route.origin, route.destination, "2024-06-01", "2025-06-30"))
  }

  const [prices, setPrices] = useState([]);

  const findPrices = (date) => {
    for(let i = 0; i < priceHistoryState.priceHistory.length; i++) {
      let history_date = priceHistoryState.priceHistory[i]
      let new_date = new Date(history_date.departureDate)

      if (new_date.getTime() == date.getTime()) {
        return history_date
      }
    }

    return null
  }

  const onClickDay = (value, event) => {
    const new_prices = findPrices(value)
    if (new_prices != null) {
      setPrices(new_prices.prices)
    }

    console.log(prices)
  }

  const formatWeekday = (locale, date) => {

    let price = null
    let price_count = null

    let diff = 0

    const prices = findPrices(date)

    if (prices != null) {
        price_count = prices.prices.length
        price = prices.prices.at(-1).fareTotal
    }

    if (price != null) {
      const prices_count = prices.prices.length
      if (prices_count > 1) {
        let last_diff = prices.prices.at(prices_count-2)
        if (last_diff.fareTotal != null) {
          console.log(last_diff)
          diff = price - last_diff.fareTotal
        }
      }
    }

    return (
      <div>
        {date.getDate()}
        <p/>
        NOK  {price}
        <p/>
        {diff}
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
        <Calendar formatDay={formatWeekday}
                   onClickDay={onClickDay}/>
        </main>
      </div>
    </div>
        <ul>
          {prices.map((item, index) => (
            <li>
              {item.timestamp}: {item.fareTotal}
            </li>
          ))}
        </ul>

    </div>
  );
};
export default App;