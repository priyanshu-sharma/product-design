import ImageGallery from './ImageGallery';
import 'bootstrap/dist/css/bootstrap.min.css'
import WorkSheet from './WorkSheet';
import {useState} from 'react';
import JsonData from './images.json';

const HandbagPage = ({}) => {
  const [galleryImages, setgalleryImages] = useState(JsonData);
  const [workSheetActive,setworkSheetActive] = useState("A1");
  const [exprBar,setexprBar] = useState("");


  const [workSheet,setWorkSheet] = useState([
      [
        {id:  "A1", isActive: true, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "B1", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "C1", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "D1", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "E1", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "F1", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "G1", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "H1", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "I1", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "J1", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "K1", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "L1", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "M1", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
      ],
      [
        {id:  "A2", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "B2", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "C2", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "D2", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "E2", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "F2", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "G2", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "H2", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "I2", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "J2", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "K2", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "L2", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "M2", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
      ],
      [
        {id:  "A3", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "B3", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "C3", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "D3", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "E3", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "F3", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "G3", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "H3", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "I3", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "J3", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "K3", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "L3", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "M3", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
      ]
  ]);

  const changeWorkSheetActive = (id:string) => {
    setWorkSheet(workSheet.map((row)=>(
      row.map((data)=>(
        data.id ===id? {...data,isActive: true}:data.id === workSheetActive? {...data,isActive: false}:data
      ))
    )));
    setworkSheetActive(id);
  }

  const addImageToWorkSheetActive = (id:string,path:string) => {
    setWorkSheet(workSheet.map((row)=>(
      row.map((data)=>(
        data.id === workSheetActive? {...data,imgId:id,imgPath:path}:data
      ))
    )));
  }

  return (
    <>
      <div className='row work-space'>
        <div className='col-6 image-gallery'>
          <ImageGallery images={galleryImages} addImageToWorkSheetActive={addImageToWorkSheetActive}/>
        </div>
        <div className='col-6'>
          <WorkSheet workSheetActive={workSheetActive} workSheet={workSheet} changeWorkSheetActive={changeWorkSheetActive}/>
        </div>
      </div>
      <div className='row'>
        <div className='col-6'>

        </div>
        <div className='col-5'>
          <input type="text" className="form-control" placeholder="Write commands here."/>
        </div>
        <div className='col-1'>
          <button type="button" className="btn btn-dark">Execute</button>
        </div>
      </div>
    </>
  );
};

export default HandbagPage;
