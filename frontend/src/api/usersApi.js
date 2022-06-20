import axios from 'axios';
export const getPersons = async () => {

    const url = 'http://localhost:8000/persons/';
    const config = {
        method: 'GET'
    };
    const response = await fetch(url,config);
    const responseData = await response.json();
    console.log(responseData);
};

// Alternatively
export const axiosGetPersons = async () => {
    const url = 'http://127.0.0.1:8000/persons/';
    const response = await axios({
        method: 'GET',
        url,
    });

    console.log(response);

}