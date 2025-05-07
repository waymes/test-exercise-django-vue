import request from './request';

export const fetchApartments = (queryParams = {}) => {
  const query = new URLSearchParams(queryParams).toString();
  return request
    .get(`/apartments/apartments?${query}`)
    .then((response) => response.data)
    .catch((error) => console.log(error));
};

export const fetchApartmentDetails = (slug) => {
  return request
    .get(`/apartments/apartments/${slug}`)
    .then((response) => response.data)
    .catch((error) => console.log(error));
};
