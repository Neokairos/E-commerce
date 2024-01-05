<script>
	// @ts-nocheck
	import axios from 'axios';
	import { onMount } from 'svelte';
	import { ShopS,isLoggedOut,isLoggedIn } from '../../ShopS';

	

	

	async function checkLogin() {
		
			const endpoint = 'http://localhost:8000/api/islogged';
			try {
				const response = await axios.get(endpoint);
				if (response.data === true) {
					if ($isLoggedOut === false){
					$isLoggedIn.set(true);
				}}
			} catch (err) {
				console.log('error in login auth Error:', err);
			}
		}
	

	onMount(() => {
		(async () => {
			await checkLogin();
		})();
	});
</script>

<nav class="navbar navbar-expand-lg navbar-dark bg-black">
	<div class="container-fluid">
		<a class="navbar-brand" href="/shop">Navbar</a>
		<button
			class="navbar-toggler"
			type="button"
			data-bs-toggle="collapse"
			data-bs-target="#navbarNav"
			aria-controls="navbarNav"
			aria-expanded="false"
			aria-label="Toggle navigation"
		>
			<span class="navbar-toggler-icon"></span>
		</button>
		<div class="collapse navbar-collapse" id="navbarNav">
			<ul class="navbar-nav">
				<li class="nav-item">
					<a class="nav-link btn btn-outline-primary" href="/shop">Shop</a>
				</li>
				{#if !$isLoggedIn}
					<li class="nav-item">
						<a class="nav-link btn btn-outline-primary" href="/shop/auth/login">Login</a>
					</li>
					<ul class="navbar-nav me-20">
						<li class="nav-item">
							<a class="nav-link btn btn-outline-info text-warning" href="/shop/auth/register"
								>Register</a
							>
						</li>
					</ul>
				{:else}
					<ul class="navbar-nav me-20">
						<li class="nav-item">
							<a class="nav-link btn btn-outline-info text-warning" href="/shop/add"
								>Add a Product</a
							>
						</li>
					</ul>
				{/if}
			</ul>
		</div>
	</div>
	<div>
		{#if $isLoggedIn}
			<a href="/user" class="ml-auto ">
				<img class="zoom-effect" src="user.png" alt={'User'} style="height:40px" /></a
			>
			<li class="nav-item ml-1100">
				<a class="nav-link btn btn-outline-secondary text-outline-info" href="/shop/auth/logout">Logout</a>
			</li>
		{/if}
	</div>
</nav>

<div class="container">
	<slot />
</div>
