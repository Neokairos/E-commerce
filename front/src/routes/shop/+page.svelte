<script>
    import {ShopS} from '../../ShopS'
    import {onMount} from 'svelte'
    import axios from 'axios';

    onMount(async function () {
        if (!$ShopS.length) {
            const endpoint = 'http://localhost:8000/api/products/'
            axios.get(endpoint).then(response => {
              ShopS.set(response.data)
          }).catch(err => {
            console.log('Error:',err);
          })
        
        }

    })
</script>


<div>
    <h2 class="my-4">Products</h2>
    
    <div class="my-4 row">
        {#each $ShopS as item}
        <div class="col-12 col-sm-6 col-md-4">
            
            <div class="card w-100 h-100">
                <img class="card-img-top" style="height: 300px; object-fit: cover" 
                    src="{item.image}" 
                    alt="item">
                <div class="card-body d-flex flex-column justify-content-between gap-4">
					<div>
                        <h5 class="card-title">{ item.name }</h5>
                        <p class="card-text">Seller: { item.user}</p>
                    </div>
                    <div>
                        <a href="/items/{item.id}" class="btn btn-primary">View</a>
					</div>
                </div>
              </div>

        </div>
        {/each}
    </div>
    
</div>