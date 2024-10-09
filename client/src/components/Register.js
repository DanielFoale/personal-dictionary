import '../App.css';
import react, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';


function Register() {
  const navigate = useNavigate();
  const [username, setUsername] = useState('');
  const [password, setPasssword] = useState('');

  const handleRegister = async () => {
    try {
      const response = await axios.post('/api/register', {username, password});
      if (response.data.access_token){
        localStorage.setItem('token', response.data.access_token)
        alert('Registration successful!');
        navigate('/home');
      }
      else{
        alert(response.data.message)
      }
    }
    catch (error) {
      alert(error.message);
    }
  }

  return (
    <div>
      <input type='username' value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
      <input type='password' value={password} onChange={(e) => setPasssword(e.target.value)} placeholder="Password" />
      <button onClick={handleRegister}>Register</button>
    </div>
  );
}

export default Register;