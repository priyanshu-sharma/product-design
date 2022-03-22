interface image {
  id: string;
  path: string;
}

interface Props {
    image: image;
    addImageToWorkSheetActive: any;
}

const ImageHolder = ({image,addImageToWorkSheetActive}:Props) => {
  return (
    <div className="image-holder">
      <img src={image.path} alt="None" width={105} height={105} onClick={() => addImageToWorkSheetActive(image.id,image.path)}/>
    </div>
  );
};

export default ImageHolder;
