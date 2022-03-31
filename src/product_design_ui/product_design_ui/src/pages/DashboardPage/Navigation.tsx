import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import Container from 'react-bootstrap/Container'


const Navigation = () => {
    return (
      <>
      <Navbar bg="dark" variant="dark" fixed="bottom">
        <Container>
        <Navbar.Brand>Product GAN Generator</Navbar.Brand>
        <Nav activeKey="/StyleGAN2" className="me-auto">
          <Nav.Link href="/StyleGAN2">StyleGAN2</Nav.Link>
          <Nav.Link href="#features">ConditionalGAN</Nav.Link>
        </Nav>
        </Container>
      </Navbar>
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
    );
  };
  
  export default Navigation;
  