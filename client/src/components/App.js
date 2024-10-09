import '../App.css';
import Login from './Login';
import Register from './Register';
import Home from './Home';
import { BrowserRouter as Router, Routes, Route, Link, useNavigate } from "react-router-dom";
import { useEffect } from 'react';

function App() {
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      navigate('/home');
    }
  }, [navigate]);

  return (
    <Routes>
    <Route 
      path="/login" 
      element={
        <div>
          <Login />
        </div>
      } 
    />
    <Route 
      path="/register" 
      element={
        <div>
          <Register />
        </div>
      } 
    />
    <Route 
      path="/home" 
      element={
        <div>
          <Home />
        </div>
      } 
    />
    <Route 
      path="*" 
      element={
        <div>
          <nav>
            <ul>
              <li>
                <Link to="/login">Login</Link>
              </li>
              <li>
                <Link to="/register">Register</Link>
              </li>
            </ul>
          </nav>
        </div>
      } 
    />
  </Routes>
  );
}


export default App;