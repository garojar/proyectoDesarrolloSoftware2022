import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

export const firebaseConfig = {
    apiKey: "AIzaSyDiFQNJFYyD9KP_AT0UlpJ32hDxmvgxwzM",
    authDomain: "projecttest-02-2022.firebaseapp.com",
    projectId: "projecttest-02-2022",
    storageBucket: "projecttest-02-2022.appspot.com",
    messagingSenderId: "1026906033821",
    appId: "1:1026906033821:web:8eb594ffb226b17910ce74",
    measurementId: "G-GS11E5F1YJ"
};

let app = initializeApp(firebaseConfig);
const auth = getAuth(app);

export {
    auth,
}