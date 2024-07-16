import { ReactNode } from 'react';

export interface ToastMessage {
  text: string;
  severity?: 'error' | 'info' | 'success' | 'warning';
}

export interface Ui {
  toastMessage: ToastMessage;
  overlayComponent?: ReactNode;
  isLoading: boolean;
}
