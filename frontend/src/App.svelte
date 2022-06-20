<script>
    import { Router, Link, Route } from "svelte-routing";
	import {
		Container,
		Collapse,
		Navbar,
		NavbarBrand,
		Nav,
		Styles,
	} from 'sveltestrap';

    import Home from './routes/Home.svelte';
	import Login from './routes/Login.svelte';
	let userIsLoggedIn = false;
	let isOpen = false;

</script>
<Styles/>

<style>
	:global(body) {
		padding:0px;
	}
	:global(.nav-links) {
		color:white!important;
		margin-right: 10rem;
		align-items: center;
	}
	:global(.nav-link) {
		margin-right:1rem;
	}
	.page {
		background: rgb(255,255,255);
		background: linear-gradient(180deg, rgba(255,255,255,1) 89%, rgba(242,172,147,1) 95%, rgba(253,63,0,1) 100%);
		min-height: 100vh;
	}
	.nav-brand{
		padding-left:10vh;
	}
	.footer {
		background: #fd3f00;
		min-height: 10vh;
	}
</style>

<Router>
<div style:background-color="#fd3f00" class="pb-3 pt-3">
	<Navbar dark expand="lg" >
	<div class="nav-brand"><NavbarBrand href="/">My Svelte App</NavbarBrand></div>
	<Collapse {isOpen} navbar expand="md" on:update={() => {}}>
		<Nav class="ms-auto nav-links" navbar>
			<Link class="nav-link" to="/">Home</Link>
			{#if userIsLoggedIn}
				<Link class="nav-link" to="/profile">Perfil</Link>
				<Link class="nav-link" to="/login">Logout</Link>
			{:else}
				<Link class="nav-link" to="/login">Login</Link>
			{/if}
		</Nav>
	</Collapse>
	</Navbar>
</div>
<div class="page mt-5 p-8">
	<Route path="/">
		<Home></Home>
	</Route>
	{#if userIsLoggedIn}
		<Route path="/profile" />
		<Route path="/logout" />
	{:else}
		<Route path="/login">
			<Login></Login>
		</Route>
	{/if}
</div>
</Router>

<div class="footer pt-3">
	<Container>
		ACA VA EL FOOTER
	</Container>
</div>
