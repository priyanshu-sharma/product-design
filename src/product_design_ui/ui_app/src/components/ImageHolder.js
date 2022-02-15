const ImageHolder = ({image}) => {
  return (
    <div className="image-holder">
        <img src={image.path} alt="" width={"96px"} height={"96px"}/>
    </div>
  )
}

export default ImageHolder