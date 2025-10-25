import axios from "axios";

const apiUrl = import.meta.env.VITE_BASE_API;

export const API = axios.create({
  baseURL: apiUrl,
  timeout: 5000,
  withCredentials: true,
  xsrfCookieName: "csrftoken",
  xsrfHeaderName: "X-CSRFToken",
});

// ✅ เรียกเพื่อให้ backend ส่ง CSRF token cookie
export const initCsrf = async () => {
  await API.get("/csrf/");
};

export const predictImage = async (file: File) => {
  const formData = new FormData();
  formData.append("image", file);
  return API.post("/predict/", formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
};

export const getDiseases = async (page = 1, size = 5) =>
  (await API.get(`/diseases/?page=${page}&size=${size}`)).data;

export const getTreatments = async (diseaseId: number, page = 1, size = 10) =>
  (await API.get(`/treatments/?disease_id=${diseaseId}&page=${page}&size=${size}`)).data;

export const getModels = async (page = 1, size = 5) =>
  (await API.get(`/models/?page=${page}&size=${size}`)).data;