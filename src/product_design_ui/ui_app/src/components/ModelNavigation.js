
import { Navbar, Container,Nav } from 'react-bootstrap';

const ModelNavigation = () => {
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
    </>
  )
};

export default ModelNavigation;
