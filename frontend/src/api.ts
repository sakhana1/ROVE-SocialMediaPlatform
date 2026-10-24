const BASE = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api';
export const token = () => localStorage.getItem('rove_access') || '';
export async function api(path:string, options:RequestInit={}) {
  const isForm = typeof FormData !== 'undefined' && options.body instanceof FormData;
  const headers:Record<string,string> = {...(!isForm ? {'Content-Type':'application/json'} : {}), ...(options.headers as Record<string,string>||{})};
  if (token()) headers.Authorization = `Bearer ${token()}`;
  const res = await fetch(`${BASE}${path}`, {...options, headers});
  const data = res.status===204 ? null : await res.json().catch(()=>({detail:'Unexpected server response'}));
  if(!res.ok) throw new Error(data?.detail || data?.error || Object.values(data||{}).flat().join(' ') || `Request failed (${res.status})`);
  return data;
}
export const auth = {login:(username:string,password:string)=>api('/auth/token/',{method:'POST',body:JSON.stringify({username,password})}),register:(payload:any)=>api('/auth/register/',{method:'POST',body:JSON.stringify(payload)}),me:()=>api('/auth/me/')};
