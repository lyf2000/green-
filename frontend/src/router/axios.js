import axios from "axios";
import LocalStorageService from "../store/LocalStorageService";
import router from "./index";

const AXIOS = axios.create({
    baseURL: 'http://127.0.0.1:8000/api'
});

// LocalstorageService
const localStorageService = LocalStorageService.getService();
// Add a request interceptor
AXIOS.interceptors.request.use(
    config => {
        const token = localStorageService.getAccessToken();
        if (token) {
            config.headers['Authorization'] = 'Bearer ' + token;
        } else {
            localStorageService.clearToken();
        }
        config.headers['Content-Type'] = 'application/json';
        return config;
    },
    error => {
        Promise.reject(error)
    });


//Add a response interceptor

AXIOS.interceptors.response.use((response) => {
    return response
}, function (error) {
    console.log('in resp');
    const originalRequest = error.config;
    if (error.response.status === 401
        // && originalRequest.url ===
        // 'http://127.0.0.1:8000/api/token/'
    ) {
        localStorageService.clearToken();
        router.push('/login');
        return Promise.reject(error);
    }

    // const refreshToken = localStorageService.getRefreshToken();
    // if (error.response.status === 401 && refreshToken && refreshToken !== 'undefined') {
    //     console.log('retry');
    //
    //     return AXIOS.post('/token/refresh/',
    //         {
    //             "refresh": refreshToken
    //         })
    //         .then(function (res) {
    //             if (res.status === 201 || res.status === 200) {
    //                 localStorageService.setToken(res.data);
    //                 AXIOS.defaults.headers.common['Authorization'] = 'Bearer ' + localStorageService.getAccessToken();
    //                 return AXIOS(originalRequest);
    //             }
    //         })
    //         .catch(function (err) {
    //             localStorageService.clearToken();
    //             router.push('/login')
    //         })
    // }
    // localStorageService.clearToken();
    // router.push('/login');
    return Promise.reject(error);
});
export default AXIOS