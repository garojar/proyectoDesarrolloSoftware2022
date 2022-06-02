<script>
    import {
        Alert,
        Container,
        Styles,
        Button,
        Table,
    } from 'sveltestrap';

    let header = "Probando svelte";
    let posts = [];
    let renderLocalAPI = false;
    let responseData = [];

    const cambiarNombre = () => {
        header = `Titulo ${counter}`;
        counter += 1;
    }


    const getPosts = async () => {
        renderLocalAPI = false;
        const url = 'https://jsonplaceholder.typicode.com/posts';
        const config = {
            method: 'GET'
        };
        const response = await fetch(url,config);
        responseData = await response.json();
        posts = responseData;
    };

    const getPersons = async () => {
        renderLocalAPI = true;
        const url = 'http://0.0.0.0:8000/persons/';
        const config = {
            method: 'GET'
        };
        const response = await fetch(url,config);
        responseData = await response.json();
        console.log(responseData);
    }

    const showAlert = () => alertStates.test = !alertStates.test;
</script>
<Styles/>

<main>
<Container>
        <h1>{header}</h1>
        <p> Este es un elemento p</p>
        <Table bordered>
            <thead>
              <tr>
                <th>{ renderLocalAPI ? 'id' : 'UserId'}</th>
                <th>{ renderLocalAPI ? 'Name' : 'id'}</th>
                <th>{ renderLocalAPI ? 'Rut' : 'title'}</th>
              </tr>
            </thead>
            <tbody>
              {#each responseData as data}
                <tr>
                    <td>{ renderLocalAPI ? data.id : data.userId}</td>
                    <td>{ renderLocalAPI ? data.first_name : data.id}</td>
                    <td>{ renderLocalAPI ? data.rut : data.title}</td>
                </tr>
              {/each}
            </tbody>
          </Table>
        <Button color='primary' on:click={getPosts}> Obtener posts</Button>
        <Button color='primary' on:click={getPersons}> Obtener personas (API LOCAL)</Button>
</Container>
</main>