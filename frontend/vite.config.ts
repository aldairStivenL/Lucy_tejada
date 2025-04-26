import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import tailwindcss from 'tailwindcss';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    tailwindcss() // Configuración de Tailwind CSS
  ],
  server: {
    port: 3000, // Puerto para el frontend
  },
});