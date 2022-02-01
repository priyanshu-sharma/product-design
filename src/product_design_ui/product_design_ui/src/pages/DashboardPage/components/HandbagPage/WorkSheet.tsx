import {useState} from 'react';
import WorksheetSegment from './WorksheetSegment';

interface data {
  id: string;
  isActive: boolean;
  imgId: string;
  imgPath: string;
}

interface Props {
  workSheetActive: string;
  workSheet: data[][];
  changeWorkSheetActive: any;
}



const WorkSheet = ({workSheetActive,workSheet, changeWorkSheetActive}:Props) => {

  const formTextInput = ""

  let rowCount = 1;

  return (
    <div className='work-sheet'>
      <table>
        <thead>
          <tr>
            <td></td>
            <td>A</td>
            <td>B</td>
            <td>C</td>
            <td>D</td>
            <td>E</td>
            <td>F</td>
            <td>G</td>
            <td>H</td>
            <td>I</td>
            <td>J</td>
            <td>K</td>
            <td>L</td>
            <td>M</td>
          </tr>
        </thead>
        <tbody>
          {workSheet.map(((row)=>(
            <>
              <tr>
                <th scope="row">{rowCount++}</th>
                  {row.map(((data)=>(
                    <WorksheetSegment key={data.id} data={data} workSheetActive={workSheetActive} changeWorkSheetActive={changeWorkSheetActive}/>
                  )))}
              </tr>
            </>
          )))}
        </tbody>
      </table>
    </div>
  );
};

export default WorkSheet;
