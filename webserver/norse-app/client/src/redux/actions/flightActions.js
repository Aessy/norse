// src/redux/actions/flightActions.js
export const FETCH_FLIGHTS_REQUEST = 'FETCH_FLIGHTS_REQUEST';
export const FETCH_FLIGHTS_SUCCESS = 'FETCH_FLIGHTS_SUCCESS';
export const FETCH_FLIGHTS_FAILURE = 'FETCH_FLIGHTS_FAILURE';

const fetchFlightsRequest = () => ({
  type: FETCH_FLIGHTS_REQUEST,
});

const fetchFlightsSuccess = (flights) => ({
  type: FETCH_FLIGHTS_SUCCESS,
  payload: flights,
});

const fetchFlightsFailure = (error) => ({
  type: FETCH_FLIGHTS_FAILURE,
  payload: error,
});

export const fetchFlights = () => {
  console.log("Fetching flights")
  return async (dispatch) => {
    dispatch(fetchFlightsRequest());
    try {
      const response = await fetch('http://37.27.24.1:8080/flights');
      const data = await response.json();
      console.log(data)
      dispatch(fetchFlightsSuccess(data));
    } catch (error) {
      dispatch(fetchFlightsFailure(error));
    }
  };
};
