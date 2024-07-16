import { PayloadAction, createSlice } from '@reduxjs/toolkit';
import { ReactNode } from 'react';

import { Ui, ToastMessage } from './types';

const initialState: Ui = {
  toastMessage: { text: '', severity: undefined },
  isLoading: false,
};

const ui = createSlice({
  name: 'ui',
  initialState,
  reducers: {
    setToastMessage: (state, { payload }: PayloadAction<ToastMessage>) => {
      state.toastMessage.text = payload.text;
      state.toastMessage.severity = payload.severity;
    },
    setIsLoading: (state, { payload }: PayloadAction<boolean>) => {
      state.isLoading = payload;
    },
  },
});

export const { setToastMessage, setIsLoading } = ui.actions;

export default ui.reducer;
