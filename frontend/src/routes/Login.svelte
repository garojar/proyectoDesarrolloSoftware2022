<script>
    import {
        Container,
        Input,
        FormGroup,
        Label,
        Button,
    } from 'sveltestrap';
    import { createUserWithEmailAndPassword } from 'firebase/auth';
    import { auth } from '../firebase';
    import { getPersons, axiosGetPersons } from '../api/usersApi';

    let emailValue = '';
    let passwordValue = '';


    const useFirebase = async () => {
        let userAppCreator = await createUserWithEmailAndPassword(
            auth,
            emailValue,
            passwordValue,
        );
    }


</script>

<Container>
    <h1>Login</h1>
    <FormGroup>
        <Label for="username">Email</Label>
        <Input type="email" on:change={() => console.log(emailValue)} bind:value={emailValue} placeholder="Ingresa tu usuario" />
    </FormGroup>

    <FormGroup>
        <Label for="password">Password</Label>
        <Input bind:value={passwordValue} type="password" placeholder="Ingresa tu contraseña" />
    </FormGroup>

    <Button on:click={getPersons} color="primary"> Iniciar Sesion </Button>
    <Button on:click={axiosGetPersons} color="secondary"> Use Firebase </Button>
</Container>
