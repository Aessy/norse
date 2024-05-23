// routesReducer.js
import {
    FETCH_ROUTES_REQUEST,
    FETCH_ROUTES_SUCCESS,
    FETCH_ROUTES_FAILURE,
  } from '../actions/routesActions'
  
  const initialState = {
    loading: false,
    routes: [],
    error: '',
  };
  
  const routesReducer = (state = initialState, action) => {
    switch (action.type) {
      case FETCH_ROUTES_REQUEST:
        return {
          ...state,
          loading: true,
        };
      case FETCH_ROUTES_SUCCESS:
        return {
          loading: false,
          routes: action.payload,
          error: '',
        };
      case FETCH_ROUTES_FAILURE:
        return {
          loading: false,
          routes: [],
          error: action.payload,
        };
      default:
        return state;
    }
  };
  
  export default routesReducer;