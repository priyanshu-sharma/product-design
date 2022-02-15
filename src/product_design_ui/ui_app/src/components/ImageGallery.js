import ImageHolder from "./ImageHolder";

const ImageGallery = ({imageData}) => {
  return (
      <>
        {/* <ImageHolder/> */}
        {
          imageData.map((image) => (
            <ImageHolder image={image}/>
          ))
        }
      </>
  )
};

export default ImageGallery;
