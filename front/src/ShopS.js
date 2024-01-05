import { writable } from "svelte/store";  

export const ShopS = writable([])
export const isLoggedIn = writable(false);
export const isLoggedOut = writable(true);