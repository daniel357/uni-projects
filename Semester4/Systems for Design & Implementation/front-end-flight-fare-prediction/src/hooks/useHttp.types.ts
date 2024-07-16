import { HttpResponse } from '../services/api/api.types';

export type Request = <T>(makeRequest: () => Promise<HttpResponse<T>>) => Promise<T>;

export interface HttpHook {
  http: Request;
}

export interface UseHttpOptions {
  withLoading?: boolean;
  withToastMessage?: boolean;
}
