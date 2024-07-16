import { UserDetails } from 'src/services/auth/auth.types';

export interface AuthState {
  isAuth: boolean;
  user: UserDetails | null;
}
