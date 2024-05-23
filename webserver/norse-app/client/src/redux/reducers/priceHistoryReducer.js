// Import action types
import {
    FETCH_PRICE_HISTORY_REQUEST,
    FETCH_PRICE_HISTORY_SUCCESS,
    FETCH_PRICE_HISTORY_FAILURE
  } from '../actions/priceHistoryAction';
  
  // Define initial state
  const initialState = {
    loading: false,
    error: '',
    priceHistory: []
  };
  
  // Define price history reducer function
  const priceHistoryReducer = (state = initialState, action) => {
    switch (action.type) {
      case FETCH_PRICE_HISTORY_REQUEST:
        return {
          ...state,
          loading: true
        };
      case FETCH_PRICE_HISTORY_SUCCESS:
        return {
          ...state,
          loading: false,
          priceHistory: action.payload,
          error: ''
        };
      case FETCH_PRICE_HISTORY_FAILURE:
        return {
          ...state,
          loading: false,
          error: action.payload
        };
      default:
        return state;
    }
  };
  
  export default priceHistoryReducer;
  