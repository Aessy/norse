// src/App.js
import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchFlights } from './redux/actions/flightActions';
import Sidebar from './components/Sidebar';
import Calendar from './components/Calendar';
import './App.css';

const App = () => {
  const dispatch = useDispatch();
  const { flights, loading, error } = useSelector((state) => state.flights);

  useEffect(() => {
    dispatch(fetchFlights());
  }, [dispatch]);

  const [calendarData, setCalendarData] = useState({
    1: 'Event 1',
    2: 'Event 2',
    15: 'Event 3'
  });

  const handleDayClick = (day) => {
    alert(`You clicked on day ${day}`);
  };


  return (
    <div className="App">
      <Sidebar />
      <div className="main-content">
        <Calendar
                initialMonth={new Date().getMonth()}
                initialYear={new Date().getFullYear()}
                data={calendarData}
                onDayClick={handleDayClick}
              />
      </div>
    </div>
  );
};

export default App;