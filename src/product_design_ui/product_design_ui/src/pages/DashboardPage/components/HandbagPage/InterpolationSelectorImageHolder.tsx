interface data {
    id: string;
    imgId: string;
    imgPath: string;
  }
  
  interface Props {
    data:data;
  }
  
  
  
  const InterpolationSelectorImageHolder = ({data}:Props) => {
    return (
    <td>
        <img src={data.imgPath} alt="None" width={120} height={120}/>
    </td>
    );
  };
  
  export default InterpolationSelectorImageHolder;
  