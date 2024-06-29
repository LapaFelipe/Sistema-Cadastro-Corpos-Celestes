import { Sidebar, Menu, MenuItem } from 'react-pro-sidebar';
import { Link } from 'react-router-dom';

function Cadastro() {
    return (
        
            <Sidebar>
            <Menu
                menuItemStyles={{
                button: {
                    // the active class will be added automatically by react router
                    // so we can use it to style the active menu item
                    [`&.active`]: {
                    backgroundColor: '#13395e',
                    color: '#b6c8d9',
                    },
                },
                }}
            >
                <MenuItem component={<Link to="/categoria" />}>Categoria</MenuItem>
                <MenuItem component={<Link to="/cattempcor" />}>Cor da Categoria</MenuItem>
                <MenuItem component={<Link to="/compatm" />}>Composição Atmosférica</MenuItem>
                <MenuItem component={<Link to="/componente" />}>Componente Químico</MenuItem>
                <MenuItem component={<Link to="/constelacao" />}>Constelação</MenuItem>
                <MenuItem component={<Link to="/corpo" />}>Corpo</MenuItem>
                <MenuItem component={<Link to="/estrela" />}>Estrela</MenuItem>
                <MenuItem component={<Link to="/estrperiferica" />}>Estrela Periférica</MenuItem>
                <MenuItem component={<Link to="/galaxia" />}>Galáxia</MenuItem>
                <MenuItem component={<Link to="/satnatural" />}>Satélite Natural</MenuItem>
                <MenuItem component={<Link to="/planeta" />}>Planeta</MenuItem>
                <MenuItem component={<Link to="/planetatipo" />}>Tipo Planeta</MenuItem>
                <MenuItem component={<Link to="/sistema" />}>Sistema Planetário</MenuItem>
                <MenuItem component={<Link to="/tipogalax" />}>Tipo Galáxia</MenuItem>
                <MenuItem component={<Link to="/ciepesq" />}>Pesquisadores</MenuItem>
            </Menu>
            </Sidebar>
    )
}

export default Cadastro;