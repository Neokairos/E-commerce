<script>
// @ts-nocheck

   import { goto } from '$app/navigation';
   import axios from "axios";
	import { ShopS, isLoggedOut,isLoggedIn } from '../../../../ShopS';

   // @ts-ignore
   let username;
   // @ts-ignore
   let password;
   let seePassword = false

   function toggleSeePassword() {
    seePassword = !seePassword;}


   // @ts-ignore
   async function handleSubmit(event) {
       event.preventDefault();
       username = username.replace(/ /g, "_"); // Replace spaces with underscores
       const endpoint = 'http://localhost:8000/api/register/';
       try {
           const response = await axios.post(endpoint, { username, password });
           if (response.status === 201) {
                const userData = response.data;
                ShopS.set({userData})
                $isLoggedOut.set(false)
                $isLoggedIn.set(true)
                goto('/shop');
                alert(`User ${userData.username} Created`);
           }
       } catch (err) {
           console.log(err);
           alert('An Error has occured')
       }
   };
</script>


<title>Register</title>
<h2 class="mb-2">Register Page</h2>
<div>
	<form on:submit={handleSubmit}>
		<div class="mb-5">
			<input class="form-control" type="text" placeholder="Name" bind:value={username} />
		</div>
        {#if !seePassword}
            <div class="input-wrapper mb-5">
                <input class="form-control" type="text" placeholder="Password" bind:value={password} />
                <button on:click={toggleSeePassword} class="btn btn-info icon-button"><i class="far fa-eye-slash"></i></button>
            </div>
        {:else}
            <div class="input-wrapper mb-5">
                <input class="form-control" type="password" placeholder="Password" bind:value={password} />
                <button on:click={toggleSeePassword} class="btn btn-info icon-button"><i class="fas fa-eye"></i></button>
            </div>
        {/if}
		<button type="submit" class="btn btn-success" style="color: black;">Submit</button>
	</form>
</div>
