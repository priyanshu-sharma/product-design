interface Props {
  interpolationMethod: string;
}

const InterpolationSelectorForm = ({interpolationMethod}:Props) => {
  return (
      <form action="">
          <div className="form-group">
            <label htmlFor="">MetaData:</label>
            <input type="text" className="form-control" placeholder="Attribute:Value;Attribute:Value;"/>
            <label htmlFor="">Select Images: </label>
            <input type="text" className="form-control" placeholder="Image1,Image2,Image3"/>
            <input type="hidden" name="" id="" value={interpolationMethod}/>
          </div>
          <button type="submit" className="btn btn-dark float-end">Interpolate</button>
      </form>
  );
};

export default InterpolationSelectorForm;
