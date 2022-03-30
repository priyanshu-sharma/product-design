
interface Props {
    interpolationMethod: string;
    imageString: string;
    setimageString: any;
    interpolate: any;
  }
  
  const InterpolationSelectorForm = ({interpolationMethod,imageString,setimageString,interpolate}:Props) => {
    return (
        <form action="">
            <div className="form-group">
              {/* <label htmlFor="">MetaData:</label>
              <input type="text" className="form-control" placeholder="Attribute:Value;Attribute:Value;"/> */}
              <label>Select Images: </label>
              <input type="text" className="form-control" placeholder="Image1,Image2,Image3" value={imageString} 
                onChange={(e) => setimageString(e.target.value)}/>
              <input type="hidden" name="" id="" value={interpolationMethod}/>
            </div>
            <button type="button" className="btn btn-dark float-end" onClick={() => interpolate()}>Interpolate</button>
        </form>
    );
  };
  
  export default InterpolationSelectorForm;