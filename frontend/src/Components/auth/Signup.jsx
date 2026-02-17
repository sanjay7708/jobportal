import React, { useState } from 'react'
import api from '../../api';

export const Signup = () => {
  const [user,setUser]=useState({
    username:'',
    email:'',
    password:'',
    confirm_password:''
  })
  const handleSubmit=async(e)=>{
    e.preventDefault();
    try{
      const res=await api.post('auth/signup/',user)
      console.log(res)
    }
    catch{
      console.log('error')
    }
  }
  return (
    <>
      <h1>Signup</h1>
      <div>
        <form action="" method='post' onSubmit={handleSubmit}>
          <div>
            <label className=''>Username:</label>
            <input type="text" value={user.username} name='username' onChange={(e)=>setUser(prev=>({...prev,username:e.target.value}))} />
          </div>
          <div>
            <label className=''>Email:</label>
            <input type="text" value={user.email} name='email' onChange={(e)=>setUser(prev=>({...prev,email:e.target.value}))} />
          </div>
          <div>
            <label className=''>Password:</label>
            <input type="password" value={user.password} name='password' onChange={(e)=>setUser(prev=>({...prev,password:e.target.value}))} />
          </div>
          <div>
            <label className=''>Confirm_password:</label>
            <input type="password" value={user.confirm_password} name='confirm_password' onChange={(e)=>setUser(prev=>({...prev,confirm_password:e.target.value}))} />
          </div>
          <button type='submit'>Signup</button>
        </form>
      </div>
    </>
  )
}
