import { defineConfig } from 'astro/config';

// `SITE_URL` and `BASE_PATH` can be set at build time (e.g. by the GitHub Pages
// workflow). Defaults are sensible for local dev.
const siteUrl = process.env.SITE_URL || 'http://localhost:4321';
const basePath = process.env.BASE_PATH || '/';

export default defineConfig({
  site: siteUrl,
  base: basePath,
  output: 'static',
  build: {
    format: 'directory',
  },
  vite: {
    build: { sourcemap: false },
  },
});
