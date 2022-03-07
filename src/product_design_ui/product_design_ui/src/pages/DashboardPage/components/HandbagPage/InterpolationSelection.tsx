
import InterpolationLabelHolder from './InterpolationLabelHolder';

interface data {
    id: string;
    label: string;
    isActive: boolean;
  }
  
  interface Props {
    selectorList: data[];
    changeInterpolationLabelActive: any;
  }

const InterpolationSelection= ({selectorList,changeInterpolationLabelActive}:Props) => {
    return (
        <>
            {selectorList.map(((data)=>(
                <InterpolationLabelHolder key={data.id} data={data} changeInterpolationLabelActive={changeInterpolationLabelActive}/>
              )))}
        </>
    );
  };
  
  export default InterpolationSelection;
  