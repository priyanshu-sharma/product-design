import {useState} from 'react';
import JsonData from './images.json';
import ImageHolder from './ImageHolder';

interface image {
  id: string;
  path: string;
  latent_vector: number[][];
}


interface Props {
  images: image[];
  addImageToWorkSheetActive: any;
}



const ImageGallery = ({images,addImageToWorkSheetActive}:Props) => {
  return (
    <>
        {images.map(((image)=>(
          <ImageHolder key={image.id} image= {image} addImageToWorkSheetActive={addImageToWorkSheetActive}/>
          )))}
    </>
  );
};

export default ImageGallery;
