<script>
    import {
        Input,
        FormGroup,
        Label,
        Button,
    } from 'sveltestrap';
    export let userIsLoggedIn;

    const submit = () => {
        userIsLoggedIn = true;
    };
</script>

<h1>Login</h1>
<FormGroup>
    <Label for="exampleEmail">Username</Label>
    <Input plaintext placeholder="Ingresa tu usuario" />
</FormGroup>

<FormGroup>
    <Label for="exampleEmail">Password</Label>
    <Input password placeholder="Ingresa tu contraseña" />
</FormGroup>

<Button on:click={submit}> Iniciar Sesion </Button>