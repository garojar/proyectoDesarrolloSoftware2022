<script>
    import { Router, Link, Route } from "svelte-routing";
	import { initializeApp } from 'firebase/app';
	
    import Home from './routes/Home.svelte';
	import Login from './routes/Login.svelte';

	let userIsLoggedIn = false;
</script>

<style>
</style>

<main>
<Router >
<div class="navbar pt-5 pb-5 ">
	<h1 color="white">My Svelte App</h1>
	<div class="links">
		<Link to="/home">Home</Link>
		{#if userIsLoggedIn}
			<Link to="/profile">Perfil</Link>
			<Link to="/login">Logout</Link>
		{:else}
			<Link to="/login">Login</Link>
		{/if}
	</div>
</div>
<div class="page mt-5">
		<Route path="/home">
			<Home></Home>
		</Route>
		{#if userIsLoggedIn}
			<Route path="/profile" />
			<Route path="/logout" />
		{:else}
			<Route path="/login">
				<Login bind:userIsLoggedIn></Login>
			</Route>
		{/if}
</div>
</Router>
</main>