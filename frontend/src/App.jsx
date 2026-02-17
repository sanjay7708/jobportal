import { useState } from 'react'
import { BrowserRouter,Route,Routes } from 'react-router-dom'
import { Login } from './Components/auth/Login'
import { Signup } from './Components/auth/Signup'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path='' element={<Login/>}/>
          <Route path='/signup' element={<Signup/>}/>
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
