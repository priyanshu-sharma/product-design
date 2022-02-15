import 'bootstrap/dist/css/bootstrap.min.css'
import ImageGallery from './components/ImageGallery';
import ModelNavigation from './components/ModelNavigation';
import ProductNavigation from './components/ProductNavigation';
import WorkSheet from './components/WorkSheet';
import JsonData from './images.json';
import {useState} from 'react';

function App() {
  const [imageData,setImages] = useState(JsonData)

  return (
    <div className="App default-class">
      <ModelNavigation/>
      <ProductNavigation/>
      <div className="row app-row">
        <div className='col app-col border image-gallery'>
          <ImageGallery imageData={imageData}/>
        </div>
        <div className='col app-col border work-sheet'>
          <WorkSheet/>
        </div>
        <div className='col-1 app-col border work-sheet'>
        </div>
      </div>
    </div>
  );
}

export default App;
