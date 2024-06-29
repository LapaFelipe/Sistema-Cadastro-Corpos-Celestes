import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./NewProject.module.css";
import Cookies from 'js-cookie';
import Input from "../form/Input";
import SubmitButton from "../form/SubmitButton";
import Cadastro from "./Cadastro";

function NewProject(props) {
  const history = useNavigate();
  const accessToken = Cookies.get('access_token');
  const [categoria, setCategoria] = useState({ categoria_nome: "" });
  const api = props.api;

  const handleChange = (e) => {
    const { name, value } = e.target;
    setCategoria({ ...categoria, [name]: value });
  };

  const validateCategoria = (categoria) => {
    if (!categoria.categoria_nome || typeof categoria.categoria_nome !== 'string') {
      return "O nome da categoria é obrigatório e deve ser uma string.";
    }
    return null;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Categoria:", categoria);

    const errorMessage = validateCategoria(categoria);
    if (errorMessage) {
      console.error("Validation Error:", errorMessage);
      return;
    }

    fetch(`http://localhost:8000/api/${props.api}/`, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${accessToken}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(categoria),
    })
      .then((resp) => {
        if (!resp.ok) {
          return resp.json().then(err => { throw new Error(JSON.stringify(err)) });
        }
        return resp.json();
      })
      .then((data) => {
        console.log("Success:", data);
        history(`/${props.api}`, { message: "Categoria criada com sucesso!" });
      })
      .catch((err) => console.error("Error:", err));
  };

  return (
    <div style={{ display: "flex"}}>
      <Cadastro/>
    <form onSubmit={handleSubmit} className={styles.form}>
      <Input
        type="text"
        text="Nome da categoria"
        name="categoria_nome"
        placeholder="Insira o nome da categoria"
        handleOnChange={handleChange}
      />

      <SubmitButton text="Enviar"/>
    </form>
    </div>
  );
}

export default NewProject;
