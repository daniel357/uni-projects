import { PayloadAction, createSlice } from '@reduxjs/toolkit';
import { UserDetails } from 'src/services/auth/auth.types';

import { AuthState } from './types';

const initialState: AuthState = {
  isAuth: false,
  user: null
};

const auth = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    login: (state, { payload }: PayloadAction<UserDetails>) => {
      state.isAuth = true;
      state.user = payload;
    },
    logout: state => {
      state.isAuth = false;
      state.user = null;
    },
  },
});

export const { login, logout } = auth.actions;

export default auth.reducer;
