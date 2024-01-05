<script>
	import { ShopS } from '../../ShopS';
	import { onMount } from 'svelte';
	import axios from 'axios';
	let loading = true;

	onMount(async function () {
		if (!$ShopS.length) {
			const endpoint = 'http://localhost:8000/api/products/';
			await axios
				.get(endpoint)
				.then((response) => {
					ShopS.set(response.data);
					loading = false;
				})
				.catch((err) => {
					loading = false;
					console.log('Error:', err);
				});
		}
	loading=false});
</script>

<div>
	<h2 class="my-4">Products</h2>
	{#if loading}
		<div
			class="d-flex flex-column align-items-center justify-content-center"
			style="height: 100vh;"
		>
			<div class="spinner-border text-primary" role="status" />
			<p>Loading...</p>
		</div>
	{:else if !loading}
		<div class="my-4 row">
			{#each $ShopS as item}
				<div class="col-12 col-sm-6 col-md-4">
					<div class="card w-100 h-100">
						<img
							class="card-img-top"
							style="height: 300px; object-fit: cover"
							src={item.image}
							alt="item"
						/>

						<div class="card-body d-flex flex-column justify-content-between gap-4">
							<div>
								<h5 class="card-title">{item.name}</h5>
								<i class="card-text">Seller: <b>{item.seller.username}</b></i>
							</div>

							<div>
								<a href="/shop/{item.id}" class="btn btn-info">View</a>
							</div>
						</div>
					</div>
				</div>
			{/each}
		</div>
	{/if}
</div>
