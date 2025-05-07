export const formatDate = (string) => {
  const date = new Date(string);
  const year = date.getFullYear();
  const month = date.getMonth();
  const day = date.getDate();

  const hour = date.getHours();
  const minutes = date.getMinutes();
  return `${day}/${month}/${year} ${hour}:${minutes}`;
};
