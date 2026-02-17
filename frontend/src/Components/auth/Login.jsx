import React, { useState } from 'react'
import api from '../../api';
import axios from 'axios';

export const Login = () => {

    const [user,setUser]=useState({
        username:'',
        password:'',
    })

  const handleSubmit=async(e)=>{
    e.preventDefault();
    try{
      const res=await api.post('auth/login/',user)
      console.log(res)
      localStorage.setItem('access',res.data.access);
      localStorage.setItem('refresh',res.data.refresh)
      
    }
    catch(error){
      console.log(error)
    }
  }
  console.log(user)
  return (
    <>
        <h1 className='text-center mx-auto mt-10 text-3xl text-teal-500 font-bold'>Login</h1>
        <div>
          <form action="" method='post' onSubmit={handleSubmit}>
            <div>
              <label className=''>Username:</label>
              <input type="text" className='' value={user.username} name='username' placeholder='username' onChange={(e)=>setUser(prev=>({...prev,username:e.target.value}))} />
            </div>
            <div>
              <label className=''>password:</label>
              <input type="password" className='' value={user.password} name='password' placeholder='Enter Your password' onChange={(e)=>setUser(prev=>({...prev,password:e.target.value}))} />
            </div>
          <button type='submit'>Login</button>
          </form>
          
        </div>
        
    </>
  )
}
