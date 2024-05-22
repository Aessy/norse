// src/redux/reducers/flightReducer.js
import {
  FETCH_FLIGHTS_REQUEST,
  FETCH_FLIGHTS_SUCCESS,
  FETCH_FLIGHTS_FAILURE,
} from '../actions/flightActions';

const initialState = {
  loading: false,
  flights: [],
  error: null,
};

const flightReducer = (state = initialState, action) => {
  switch (action.type) {
    case FETCH_FLIGHTS_REQUEST:
      return {
        ...state,
        loading: true,
      };
    case FETCH_FLIGHTS_SUCCESS:
      return {
        loading: false,
        flights: action.payload,
        error: null,
      };
    case FETCH_FLIGHTS_FAILURE:
      return {
        loading: false,
        flights: [],
        error: action.payload,
      };
    default:
      return state;
  }
};

export default flightReducer;