import { AxiosError } from 'axios';
import { logout } from '@redux/slices/auth';
import { setToastMessage } from '@redux/actions';
import { useDispatch } from 'react-redux';
import { setIsLoading } from '@redux/slices/ui';

import { HttpHook, Request, UseHttpOptions } from './useHttp.types';

export const useHttp = (options?: UseHttpOptions): HttpHook => {
  const dispatch = useDispatch();

  const http: Request = async makeRequest => {
    const withLoading = options?.withLoading ?? true;
    const withToastMessage = options?.withToastMessage ?? true;

    withLoading && dispatch(setIsLoading(true));

    try {
      const response = await makeRequest();

      withLoading && dispatch(setIsLoading(false));

      return response.data;
    } catch (error) {
      const status = (error as AxiosError).response?.status;

      let errorTextKey = 'TRANSLATION_KEY.DefaultError';

      if (status === 401) {
        errorTextKey = 'TRANSLATION_KEY.UnauthorizedError';
        dispatch(logout());
      }

      withToastMessage &&
      setToastMessage({
        text: errorTextKey,
        severity: 'error',
      });

      withLoading && dispatch(setIsLoading(false));

      throw error;
    }
  };

  return { http };
};
