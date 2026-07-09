// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://issoft.kr',
  integrations: [
    sitemap({
      i18n: {
        defaultLocale: 'ko',
        locales: {
          ko: 'ko-KR',
          en: 'en-US',
        },
      },
    }),
  ],
  build: {
    assets: '_assets',
  },
  vite: {
    css: {
      transformer: 'lightningcss',
    },
  },
});
