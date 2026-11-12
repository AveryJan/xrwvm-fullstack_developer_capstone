import React,{useState} from 'react';
export default function Register(){
 const [form,setForm]=useState({userName:'',firstName:'',lastName:'',email:'',password:''});
 const [message,setMessage]=useState('');
 const fields=[['userName','Username','text'],['firstName','First Name','text'],['lastName','Last Name','text'],['email','Email','email'],['password','Password','password']];
 async function submit(event){event.preventDefault();setMessage('');try{
   const response=await fetch('/djangoapp/register',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(form)});
   const result=await response.json();setMessage(response.ok?'Registration successful':result.error||'Registration failed');
 }catch(err){setMessage('Django API unavailable: '+err.message);}}
 return <form onSubmit={submit}>{fields.map(([key,label,type])=><div key={key} style={{marginBottom:12}}><label htmlFor={key}>{label}</label><input id={key} name={key} type={type} placeholder={label} value={form[key]} onChange={e=>setForm({...form,[key]:e.target.value})} required style={{display:'block',padding:10,width:'100%',boxSizing:'border-box'}}/></div>)}<button type="submit">Register</button><p role="status">{message}</p></form>;
}
