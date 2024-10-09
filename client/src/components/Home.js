import '../App.css';
import { jwtDecode } from 'jwt-decode';
import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Home() {
    const navigate = useNavigate();
    const [username, setUsername] = useState('');

    useEffect(() => {
        const token = localStorage.getItem('token');

        if (token) {
            try {
                const decodedToken = jwtDecode(token);
                setUsername(decodedToken.sub);
                console.log('Username from token:', decodedToken.sub);
            } catch (error) {
                console.error('Invalid token:', error);
                navigate('/');
            }
        } else {
            console.log('No token found. Redirecting to the main App route.');
            navigate('/');
        }
    }, [navigate]);

    return (
        <div>
            <h1>Welcome, {username}!</h1>
        </div>
    );
}

export default Home;