import React from 'react';import{createRoot}from'react-dom/client';import Register from './components/Register/Register.jsx';
function App(){return <main style={{fontFamily:'system-ui',maxWidth:540,margin:'2rem auto'}}><h1>Best Cars — Sign-up</h1><p>Register to review dealerships.</p><Register/><p><a href="http://localhost:8000">Open Django dealership directory</a></p></main>}
createRoot(document.getElementById('root')).render(<App/>);
