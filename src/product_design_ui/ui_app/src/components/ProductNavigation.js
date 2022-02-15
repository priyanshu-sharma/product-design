import { Navbar, Container,Nav } from 'react-bootstrap';

const ProductNavigation = () => {
  return (
    <>
    <Navbar bg="dark" variant="dark" >
    <Container>
      <Nav activeKey="/HandBags" className="me-auto nav-fill m0 p0 no-gutters" > 
        <Nav.Link href="#Watches">Watches</Nav.Link>
        <Nav.Link href="#Shirts">Shirts</Nav.Link>
        <Nav.Link href="/HandBags">HandBags</Nav.Link>
        <Nav.Link href="#Jewellery">Jewellery</Nav.Link>
      </Nav>
      </Container>
    </Navbar>
  </>
  )
};

export default ProductNavigation;
