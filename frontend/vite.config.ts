// import Vite config helper
import { defineConfig } from 'vite'

// React plugin for Vite
// Enable React Fast Refresh and JSX support
import react from '@vitejs/plugin-react'

// Tailwind CSS v4 Vite integration plugin
import tailwindcss from '@tailwindcss/vite'


// https://vite.dev/config/

// Export Vite configuration
export default defineConfig({
  // Register plugins used during development/build
  plugins: [
    react(),  // enables React support
    tailwindcss() // enables Tailwind CSS processing 
    ],
  })
   
