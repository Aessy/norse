import React, { useState } from 'react';
import './Calendar.css';

const daysOfWeek = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
const monthsOfYear = [
  'January', 'February', 'March', 'April', 'May', 'June',
  'July', 'August', 'September', 'October', 'November', 'December'
];

const Calendar = ({ initialMonth, initialYear, data, onDayClick }) => {
  const [month, setMonth] = useState(initialMonth);
  const [year, setYear] = useState(initialYear);

  console.log(data)

  const getDaysInMonth = (month, year) => {
    return new Date(year, month + 1, 0).getDate();
  };

  const getFirstDayOfMonth = (month, year) => {
    return new Date(year, month, 1).getDay();
  };

  const handlePrevMonth = () => {
    setMonth((prev) => {
      const newMonth = prev === 0 ? 11 : prev - 1;
      if (newMonth === 11) setYear(year - 1);
      return newMonth;
    });
  };

  const handleNextMonth = () => {
    setMonth((prev) => {
      const newMonth = prev === 11 ? 0 : prev + 1;
      if (newMonth === 0) setYear(year + 1);
      return newMonth;
    });
  };

  const handlePrevYear = () => setYear(year - 1);
  const handleNextYear = () => setYear(year + 1);

  const daysInMonth = getDaysInMonth(month, year);
  const firstDayOfMonth = getFirstDayOfMonth(month, year);

  const generateCalendar = () => {
    const days = [];
    for (let i = 0; i < firstDayOfMonth; i++) {
      days.push(<div key={`empty-${i}`} className="calendar-day empty"></div>);
    }
    for (let day = 1; day <= daysInMonth; day++) {
      days.push(
        <div
          key={day}
          className="calendar-day"
          onClick={() => onDayClick(day)}
        >
          <div className="day-number">{day}</div>
          <div className="day-data">{data[day] || ''}</div>
        </div>
      );
    }
    return days;
  };

  return (
    <div className="calendar">
      <div className="calendar-controls">
        <button onClick={handlePrevYear}>Prev Year</button>
        <button onClick={handlePrevMonth}>Prev Month</button>
        <span>{monthsOfYear[month]} {year}</span>
        <button onClick={handleNextMonth}>Next Month</button>
        <button onClick={handleNextYear}>Next Year</button>
      </div>
      <div className="calendar-header">
        {daysOfWeek.map((day, index) => (
          <div key={index} className="calendar-header-day">
            {day}
          </div>
        ))}
      </div>
      <div className="calendar-body">
        {generateCalendar()}
      </div>
    </div>
  );
};

export default Calendar;