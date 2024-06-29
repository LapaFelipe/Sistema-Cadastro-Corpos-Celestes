import { Link } from "react-router-dom";

import Container from "./Container";

import styles from "./Navbar.module.css";
import logo from "../../img/saturn.png";
import React, {useContext} from 'react';
import { useAuth } from '../pages/AuthContext'; // Importando o hook useAuth corretamente

// function Navbar() {
//   return (
//     <nav className={styles.navbar}>
//       <Container>
//         <Link to="/">
//           <img src={logo} alt="Costs" />
//         </Link>

//         <ul className={styles.list}>
//           <li className={styles.item}>
//             <Link to="/">Home</Link>
//           </li>
//           {/* <li className={styles.item}>
//             <Link to="/categorias">Categorias</Link>
//           </li> */}
//           <li className={styles.item}>
//             <Link to="/company">Empresa</Link>
//           </li>
//           <li className={styles.item}>
//             <Link to="/contact">Contato</Link>
//           </li>
//           <li className={styles.item}>
//             <Link to="/login">Login</Link>
//           </li>
//           <li className={styles.item}>
//             <Link to="/logout">Logout</Link>
//           </li>
//           <li className={styles.item}>
//             <Link to="/registrar">Registrar</Link>
//           </li>
//         </ul>
//       </Container>
//     </nav>
//   );
// }



const Navbar = () => {
  const { isAuthenticated, logout } = useAuth();
  console.log(isAuthenticated) // Utilizando o hook useAuth

  return (
    <nav className={styles.navbar}>
       <Container>
        <Link to="/">
           <img src={logo} style={{width:55}} alt="Costs" />
         </Link>

        <ul className={styles.list}>
           <li className={styles.item}>
             <Link to="/">Home</Link>
          </li>
           {isAuthenticated ? (
              <li className={styles.item}>
                <Link className="nav-link" to="/cadastro">Cadastro</Link>
              </li>
            ) : null}

            
            {!isAuthenticated && (
              <li className={styles.item}>
                <Link to="/registrar">Registrar</Link>
              </li>
            )}
          {isAuthenticated ? (
            <button className="btn btn-outline-danger" onClick={logout}>Logout</button>
          ) : (
            <li className={styles.item}><Link className={styles.item} to="/login">Login</Link></li>
          )}
          
          </ul>
      </Container>
    </nav>
  );
};

export default Navbar;
