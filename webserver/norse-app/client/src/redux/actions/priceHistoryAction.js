// actions.js
import axios from 'axios';

// Action types
export const FETCH_PRICE_HISTORY_REQUEST = 'FETCH_PRICE_HISTORY_REQUEST';
export const FETCH_PRICE_HISTORY_SUCCESS = 'FETCH_PRICE_HISTORY_SUCCESS';
export const FETCH_PRICE_HISTORY_FAILURE = 'FETCH_PRICE_HISTORY_FAILURE';

// Action creators
export const fetchPriceHistoryRequest = () => ({
  type: FETCH_PRICE_HISTORY_REQUEST,
});

export const fetchPriceHistorySuccess = (priceHistory) => ({
  type: FETCH_PRICE_HISTORY_SUCCESS,
  payload: priceHistory,
});

export const fetchPriceHistoryFailure = (error) => ({
  type: FETCH_PRICE_HISTORY_FAILURE,
  payload: error,
});

// Thunk action creator
export const fetchPriceHistory = (origin, destination, startDate, endDate) => {
  return async (dispatch) => {
    dispatch(fetchPriceHistoryRequest());
    try {
      const response = await axios.get('http://localhost:5000/api/price-history', {
        params: { origin, destination, startDate, endDate }
      });
      dispatch(fetchPriceHistorySuccess(response.data));
    } catch (error) {
      dispatch(fetchPriceHistoryFailure(error.message));
    }
  };
};
