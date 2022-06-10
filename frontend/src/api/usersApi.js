
export const getPersons = async () => {
    renderLocalAPI = true;
    const url = 'http://0.0.0.0:8000/persons/';
    const config = {
        method: 'GET'
    };
    const response = await fetch(url,config);
    responseData = await response.json();
    console.log(responseData);
}