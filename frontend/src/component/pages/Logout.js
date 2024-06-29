import React from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import Cookies from 'js-cookie';

const Logout = () => {
    const navigate = useNavigate();

    const handleLogout = async () => {
        try {
            const refreshToken = Cookies.get('refresh_token');
            if (refreshToken) {
                await axios.post('http://127.0.0.1:8000/logout/', {
                    refresh_token: refreshToken
                }, {
                    headers: {
                        'Authorization': `Bearer ${Cookies.get('access_token')}`
                    }
                });

                // Remover os tokens dos cookies
                Cookies.remove('access_token');
                Cookies.remove('refresh_token');

                // Redirecionar para a página de login
                navigate('/login');
            } else {
                console.error('No refresh token found');
            }
        } catch (error) {
            console.error('Erro no logout:', error.response ? error.response.data : error.message);
        }
    };

    return (
        <div>
            <h1>Logout</h1>
            <button onClick={handleLogout}>Logout</button>
        </div>
    );
};

export default Logout;
