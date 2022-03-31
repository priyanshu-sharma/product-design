import {useState} from 'react';
import InterpolationSelectorImageHolder from './InterpolationSelectorImageHolder';

interface data {
  imgId: string;
  imgPath: string;
}

interface Props {
  imageDisplay: data[];
}



const InterpolationSelectorImages = ({imageDisplay}:Props) => {
  return (
    <div className=''>
      <div className='interpolation-selected-images'>
      <table className='interpolation-selector-table'>
        <tbody>
          <tr>
            {imageDisplay.map(((data)=>(
                <InterpolationSelectorImageHolder key={data.imgId} data={data}/>
            )))}
          </tr>
        </tbody>
      </table>
      </div>
    </div>
  );
};

export default InterpolationSelectorImages;