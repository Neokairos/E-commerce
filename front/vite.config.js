import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		fs: {
			allow: ['..', 'static', 'src/routes'] // Allow serving files from one level up to the project root
		}
	}
});
