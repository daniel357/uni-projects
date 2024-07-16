import { combineReducers } from 'redux';
import auth from '@redux/slices/auth';
import ui from '@redux/slices/ui';

const rootReducer = combineReducers({
  auth,
  ui
});

export type RootState = ReturnType<typeof rootReducer>;

export default rootReducer;
