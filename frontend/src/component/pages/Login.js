import Cookies from 'js-cookie';
import React, { useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useNavigate } from 'react-router-dom';
import { useAuth } from './AuthContext';


const Login = () => {
  const [nome, setNome] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const { login } = useAuth();

  const submit = async (e) => {
    e.preventDefault();
    const user = {
      username: nome,
      password: password
    }
    try {
      const { data } = await axios.post("http://127.0.0.1:8000/token/", user);
      
      // Storing Access in cookie
      Cookies.set('access_token', data.access);
      Cookies.set('refresh_token', data.refresh);
      
      // Atualiza o estado de autenticação
      login();
      
      // Redireciona para a página inicial
      navigate("/cadastro");
    } catch (error) {
      console.error("error in token fetch: ", error.message);
    }
  }
  
  return (
    <div className="Auth-form-container">
      <form className="Auth-form" onSubmit={submit}>
        <div className="Auth-form-content">
          <h3 className="Auth-form-title">Sign In</h3>
          <div className="form-group mt-3">
            <label>Username</label>
            <input
              className="form-control mt-1"
              placeholder="Enter Name"
              name='name'
              type='name'
              value={nome}
              required
              onChange={e => setNome(e.target.value)}
            />
          </div>
          <div className="form-group mt-3">
            <label>Senha</label>
            <input
              name='password'
              type="password"
              className="form-control mt-1"
              placeholder="Enter password"
              value={password}
              required
              onChange={e => setPassword(e.target.value)}
            />
          </div>
          <div className="d-grid gap-2 mt-3">
            <button type="submit" className="btn btn-primary">Submit</button>
          </div>
        </div>
      </form>
    </div>
  )
};

export default Login;