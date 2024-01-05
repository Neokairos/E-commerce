<script>
// @ts-nocheck

	import { goto } from '$app/navigation';
	import axios from 'axios';
	import { onMount } from 'svelte';
    import { isLoggedOut,isLoggedIn } from '../../../../ShopS';
	
	let loading = true;

	onMount(async () => {
		const endpoint = 'http://localhost:8000/api/logout';
		try {
			const response = await axios.get(endpoint);
			if (response.data === true)
                $isLoggedOut.set(true) 
                $isLoggedIn.set(false)
                loading = false;
                goto('/shop');
                alert('you was logged out nigga');
            
		} catch (err) {
			console.log('Error :', err);
			loading = false;
		}
	});
</script>

{#if loading}
  <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh;">
      <p class="text-outline-secondary mb-10 me-10">Logging Out..</p>
      <div class="lds-ellipsis">
          <div></div>
          <div></div>
          <div></div>
          <div></div>
      </div>
  </div>
{/if}
