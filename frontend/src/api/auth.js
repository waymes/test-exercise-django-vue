import request from './request';

export const login = ({ email, password }) => {
  return request
    .post(`/users/api/token/`, { email, password })
    .then((response) => response.data);
};
