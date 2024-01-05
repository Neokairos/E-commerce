<script>
// @ts-nocheck

	import { onMount } from 'svelte';
	import { ShopS } from '../../../ShopS';
	import axios from 'axios';

	export let data;
	let product;
	let loading = true

	onMount(async function () {
		if ($ShopS.length) {
			product = $ShopS.find((product) => product.id == data.id);
		} else {
			const endpoint = `http://localhost:8000/api/products/${data.id}/`;
			try {
				let res = await axios.get(endpoint);
				product = res.data;
				ShopS.set(res.data)
				loading = false
			} catch(err) {
                console.table(err)
				product = null;
				loading = false
			}
		}
	loading=false});
</script>

<div class="row mt-4">
{#if loading }
 	<div class="d-flex flex-column align-items-center justify-content-center" style="height: 100vh;">
  		<div class="spinner-border text-primary" role="status"/>
  		<p>Loading...</p>
 	</div>

    {:else if product }
		<h2 class="mb-4">{ product.name }</h2>
		<div class="row mt-4">
			<div class="col-12 col-md-4">
				<img src="{ product.image }" alt="product" class="w-100 mb-3"/>
				<h5 class="mt-4">Seller: {product.seller.username}</h5>
				<a href="/shop/{product.id}/buy" class="btn btn-primary p-8 mt-2 pl-5">Buy</a>
				<a href="/shop" class="btn btn-danger p-8 mt-2 pr-5">Back</a>
			</div>
			<div class="col-12 col-md-8 py-2">
				<p class="mb-2">{ product.description }</p>	
			</div>
		</div>
{:else }
<p>No product was found with ID {data.id}</p>
{/if }
</div>
