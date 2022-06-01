<script>
	import {
		Alert,
		Button,
		Styles,
		Accordion,
		AccordionItem,
	} from 'sveltestrap';

	export let name;
	let coins = '';

	let thisProps = {
		alertState: false,
	}
	const fetchCoins = async () => {
		const response = await fetch(
			"http://0.0.0.0:8000/persons",
			{
				method: 'GET',
				headers: {
					'Content-Type': 'application/json',
				}
			},
		);
		const data = await response.json();
		coins = data;
 	}

</script>
<Styles />

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}
</style>

<h1>Hello {name}!</h1>
<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
{#each coins as coin}
	<p>Nombre: {coin.first_name}</p>
{/each}
<p>{coins}</p>
<Button color="primary" outline on:click={fetchCoins}> Show alert</Button>
<Alert color="info" dismissible isOpen={thisProps.alertState} toggle={() => (thisProps.alertState = false)}>I am an alert and I can be dismissed!</Alert>
<!-- <Accordion>
	<AccordionItem active header="Home">Fallbrook</AccordionItem>
	<AccordionItem header="School"><a href="#home">Buena Vista Elementary</a></AccordionItem>
	<AccordionItem header="Library">UCSB Library</AccordionItem>
</Accordion> -->
