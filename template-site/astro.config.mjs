import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://example.com',
  output: 'static',
  build: {
    format: 'directory',
  },
  vite: {
    build: { sourcemap: false },
  },
});
