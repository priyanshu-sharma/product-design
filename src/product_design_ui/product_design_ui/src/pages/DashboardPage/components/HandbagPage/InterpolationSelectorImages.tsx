import {useState} from 'react';
import InterpolationSelectorImageHolder from './InterpolationSelectorImageHolder';

interface data {
  id: string;
  imgId: string;
  imgPath: string;
}

interface Props {
  imageDisplay: data[];
}



const InterpolationSelectorImages = ({imageDisplay}:Props) => {
  return (
    <div className=''>
      <table className='interpolation-selector-table'>
        <tbody>
          <tr>
            {imageDisplay.map(((data)=>(
                <InterpolationSelectorImageHolder key={data.id} data={data}/>
            )))}
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default InterpolationSelectorImages;
