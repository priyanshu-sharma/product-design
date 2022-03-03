interface data {
  id: string;
  isActive: boolean;
  imgId: string;
  imgPath: string;
}

interface Props {
  data: data;
  workSheetActive: string;
  changeWorkSheetActive: any;
}

const WorksheetSegment = ({ data, workSheetActive , changeWorkSheetActive}:Props) => {
  return (
    <td>
      <div className={data.isActive?"work-sheet-segment active":"work-sheet-segment"}>
          <img src={data.imgPath} alt="None" width={96} height={96} onClick={() => changeWorkSheetActive(data.id)}/>
      </div>
    </td>
  );
};

export default WorksheetSegment;