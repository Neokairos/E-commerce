<script>
    import { onMount } from 'svelte';
    import { ShopS } from '../../ShopS.js'
    import axios from 'axios';


    onMount(async function () {
        if (!$ShopS.length) {
            const endpoint = 'http://localhost:8000/api/shop/'
            const response = axios.get(endpoint);
            ShopS.set(response.data)

        }
     });
    let products = []
</script>
   

   <!-- Display each product in a Bootstrap card -->
   {#each products as product}
    <div class="card" style="width: 18rem;">
      <img src={product.image} class="card-img-top" alt={product.name}>
      <div class="card-body">
        <h5 class="card-title">{product.name}</h5>
        <p class="card-text">{product.description}</p>
        <p class="card-text"><small class="text-muted">${product.price}</small></p>
        <a href="/detail/{product.id}" class="btn btn-primary">Go to Detail</a>
      </div>
    </div>
   {/each}
   