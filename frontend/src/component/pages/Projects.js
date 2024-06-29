import { useEffect, useState } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  IconButton,
} from '@mui/material';

import { BsPencil, BsFillTrashFill } from "react-icons/bs";
import Container from "../layout/Container";
import LinkButton from "../layout/LinkButton";
import Message from "../layout/Message";
import Loading from "../layout/Loading";
import Cookies from 'js-cookie';
import Cadastro from "./Cadastro";

import styles from "./Projects.module.css";

function categorias(props) {
  const [categorias, setCategorias] = useState([]);
  const [removeLoading, setRemoveLoading] = useState(false);
  const [categoriaMessage, setCategoriaMessage] = useState("");
  const accessToken = Cookies.get('access_token');

  const navigate = useNavigate();
  const location = useLocation();
  let message = "";

  const name_api = props.api

  if (location.state) {
    message = location.state.message;
  }

  useEffect(() => {
    setTimeout(() => {
      fetch(`http://localhost:8000/api/${props.api}/`, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${accessToken}`,
          "Content-Type": "application/json",
        },
      })
        .then((resp) => {
          if (!resp.ok) {
            throw new Error("Erro na requisição GET");
          }
          return resp.json();
        })
        .then((data) => {
          console.log("Dados recebidos:", data); // Adicionando log para verificar os dados recebidos
          setCategorias(data);
          setRemoveLoading(true);
        })
        .catch((err) => {
          console.error("Erro ao buscar categorias:", err);
          setRemoveLoading(true); // Para garantir que a tela de carregamento saia em caso de erro
        });
    }, 500);
  }, [props.api, accessToken]);

  function removeCategoria(id) {
    fetch(`http://localhost:8000/api/${props.api}/${id}/`, {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${accessToken}`,
        "Content-Type": "application/json",
      },
    })
      .then((resp) => {
        if (!resp.ok) {
          throw new Error("Erro na requisição DELETE");
        }
        return resp.json();
      })
      .then(() => {
        setCategorias(categorias.filter((categoria) => categoria.cod_categoria !== id));
        setCategoriaMessage("Removido com sucesso!");
      })
      .catch((err) => console.error("Erro ao remover categoria:", err));
  }

  return (
    <div style={{ display: "flex"}}>
      <Cadastro/>
    <div className={styles.categoria_container}>
      <div className={styles.title_container}>
        <h1>{name_api}</h1>
        <LinkButton to="/newcategoria" text="Criar categoria" />
      </div>
      {message && <Message msg={message} type="success" />}
      {categoriaMessage && <Message msg={categoriaMessage} type="success" />}

      <Container>
            <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>{name_api}</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {categorias.map((categoria) => (
            <TableRow
              key={categoria.id}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
              </TableCell>
              <TableCell align="right">{categoria.cod_categoria}</TableCell>
              <TableCell align="right">{categoria.categoria_nome}</TableCell>
              <TableCell align="right">
              <button >
          <BsFillTrashFill /> Excluir
        </button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>

        {!removeLoading && <Loading />}

        {removeLoading && categorias.length === 0 && (
          <p>Não há itens cadastrados!</p>
        )}
      </Container>
    </div>
    </div>
  );
}

export default categorias;
