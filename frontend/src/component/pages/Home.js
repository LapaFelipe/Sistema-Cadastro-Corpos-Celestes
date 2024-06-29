import styles from "./Home.module.css";
import space from "../../img/solar-system.png";
import LinkButton from "../layout/LinkButton";

function Home() {
  return (
    <section className={styles.home_container}>
      <h1>
        Bem-vindo ao Sistema de Cadastro Planetário
      </h1>
      <p>Comece a gerenciar o espaço!</p>
      <LinkButton to="/login" text="Realize o Login!" />
      <img src={space} alt="Costs" />
    </section>
  );
}

export default Home;
