import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from "./component/pages/Home";
import Cadastro from "./component/pages/Cadastro";
import Company from "./component/pages/Company";
import Contact from "./component/pages/Contact";
import NewProject from "./component/pages/NewProject";

import Container from "./component/layout/Container";
import Navbar from "./component/layout/Navbar";
import Footer from "./component/layout/Footer";
import Projects from "./component/pages/Projects";
import Login from './component/pages/Login';
import Logout from './component/pages/Logout';
import ProtectedRoute from './component/pages/ProtectedRoute';
import { AuthProvider } from './component/pages/AuthContext';
import { NavbarCollapse } from 'react-bootstrap';



const App = () => {
    return (
        <AuthProvider>
        <Router>
            <Navbar/>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/login" element={<Login/>} />
                <Route path="/logout" element={<Logout />} />
                
                <Route element={<ProtectedRoute />}>
                    <Route path="/categoria" element={<Projects api="categoria"/>} />
                    <Route path="/ciepesq" element={<Projects api="ciepesq"/>} />
                    <Route path="/cattempcor" element={<Projects api="cattempcor"/>} />
                    <Route path="/compatm" element={<Projects api="compatm"/>} />
                    <Route path="/componente" element={<Projects api="componente"/>} />
                    <Route path="/constelacao" element={<Projects api="constelacao"/>} />
                    <Route path="/corpo" element={<Projects api="corpo"/>} />
                    <Route path="/estrela" element={<Projects api="estrela"/>} />
                    <Route path="/estrperiferica" element={<Projects api="estrperiferica"/>} />
                    <Route path="/galaxia" element={<Projects api="galaxia"/>} />
                    <Route path="/planeta" element={<Projects api="planeta"/>} />
                    <Route path="/planetatipo" element={<Projects api="planetatipo"/>} />
                    <Route path="/satnatural" element={<Projects api="satnatural"/>} />
                    <Route path="/sistema" element={<Projects api="sistema"/>} />
                    <Route path="/tipogalax" element={<Projects api="tipogalax"/>} />
                    <Route path="/cadastro" element={<Cadastro/>} />

                    <Route path="/newcategoria" element={<NewProject api="categoria"/>} />
                    <Route path="/newciepesq" element={<NewProject api="ciepesq"/>} />
                    <Route path="/newcattempcor" element={<NewProject api="cattempcor"/>} />
                    <Route path="/newcompatm" element={<NewProject api="compatm"/>} />
                    <Route path="/newcomponente" element={<NewProject api="componente"/>} />
                    <Route path="/newconstelacao" element={<NewProject api="constelacao"/>} />
                    <Route path="/newcorpo" element={<NewProject api="corpo"/>} />
                    <Route path="/newestrela" element={<NewProject api="estrela"/>} />
                    <Route path="/newestrperiferica" element={<NewProject api="estrperiferica"/>} />
                    <Route path="/newgalaxia" element={<NewProject api="galaxia"/>} />
                    <Route path="/newplaneta" element={<NewProject api="planeta"/>} />
                    <Route path="/newplanetatipo" element={<NewProject api="planetatipo"/>} />
                    <Route path="/newsatnatural" element={<NewProject api="satnatural"/>} />
                    <Route path="/newsistema" element={<NewProject api="sistema"/>} />
                    <Route path="/newtipogalax" element={<NewProject api="tipogalax"/>} />
                </Route>
            </Routes>
        
        </Router >
        </AuthProvider>
        
    );
}
export default App;