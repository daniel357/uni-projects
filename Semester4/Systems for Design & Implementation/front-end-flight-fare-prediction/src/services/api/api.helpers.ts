import axios, { AxiosRequestConfig, Method } from 'axios';

import { HttpResponse } from './api.types';
import { BASE_URL } from '../../globals/constants';

const DEFAULT_HEADERS = {
  'Content-Type': 'application/json',
};

export const request = <T, D>(
  url: string,
  method: Method,
  payload?: T,
  headers?: { [key: string]: string },
  withCredentials = true
): Promise<HttpResponse<D>> => {
  return axios.request({
    headers: { ...DEFAULT_HEADERS, ...headers },
    baseURL: BASE_URL,
    withCredentials,
    url,
    method,
    data: payload,
  });
};

export const genericRequest = <T, D>(config: AxiosRequestConfig<T>): Promise<HttpResponse<D>> => {
  return axios.request(config);
};
