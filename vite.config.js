import{defineConfig}from'vite';
export default defineConfig({server:{proxy:{'/djangoapp':{target:'http://localhost:8000',changeOrigin:true}}}});
