<script>
    import { Router, Link, Route } from "svelte-routing";
    import Home from './routes/Home.svelte';
</script>

<div>
	<h1>App</h1>
	<Router>
		<Link to="/home">Home</Link>
		<Link to="/login">Login</Link>
		<Link to="/profile">Perfil</Link>

		<Route path="/home" component={Home}/>
		<Route path="/login" />
		<Route path="/profile" />
	</Router>
</div>