// actions.js
import axios from 'axios';

// Action types
export const FETCH_ROUTES_REQUEST = 'FETCH_ROUTES_REQUEST';
export const FETCH_ROUTES_SUCCESS = 'FETCH_ROUTES_SUCCESS';
export const FETCH_ROUTES_FAILURE = 'FETCH_ROUTES_FAILURE';

// Action creators
export const fetchRoutesRequest = () => ({
  type: FETCH_ROUTES_REQUEST,
});

export const fetchRoutesSuccess = (routes) => ({
  type: FETCH_ROUTES_SUCCESS,
  payload: routes,
});

export const fetchRoutesFailure = (error) => ({
  type: FETCH_ROUTES_FAILURE,
  payload: error,
});

// Thunk action creator
export const fetchRoutes = () => {
  return async (dispatch) => {
    dispatch(fetchRoutesRequest());
    try {
      const response = await axios.get('http://37.27.24.1:8080/api/unique-routes');
      dispatch(fetchRoutesSuccess(response.data));
    } catch (error) {
      dispatch(fetchRoutesFailure(error.message));
    }
  };
};
