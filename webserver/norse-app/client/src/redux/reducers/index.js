// src/redux/reducers/index.js
import { combineReducers } from 'redux';
import flightReducer from './flightReducer';
import routesReducer from './routesReducer';
import priceHistoryReducer from './priceHistoryReducer';

const rootReducer = combineReducers({
  flights: flightReducer,
  routes: routesReducer,
  price_history: priceHistoryReducer
});

export default rootReducer;