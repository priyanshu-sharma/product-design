import ImageGallery from './ImageGallery';
// import 'bootstrap/dist/css/bootstrap.min.css'
import WorkSheet from './WorkSheet';
import {useState} from 'react';
import JsonData from './images.json';
import InterpolationSelectorImages from './InterpolationSelectorImages';
import InterpolationSelectorForm from './InterpolationSelectorForm';
import InterpolationSelection from './InterpolationSelection';

const HandbagPage = ({}) => {
  const [galleryImages, setgalleryImages] = useState(JsonData);
  const [workSheetActive,setworkSheetActive] = useState("D2");
  const [exprBar,setexprBar] = useState("");


  const [workSheet,setWorkSheet] = useState([
      [
        {id:  "A1", isActive: false, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
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
        {id:  "D2", isActive: true, imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
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

  const [interpolationSelectorImages,setinterpolationSelectorImages] = useState([
        {id:  "ISI1", imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "ISI2", imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "ISI3", imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "ISI4", imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "ISI5", imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "ISI6", imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
        {id:  "ISI7", imgId: "None", imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="},
  ]);

  const [interpolationSelectorList,setinterpolationSelectorList] = useState([
    {id:  "L1", label:"Linear-Int", isActive: false},
    {id:  "L2", label:"Linear-Int", isActive: false},
    {id:  "L3", label:"Linear-Int", isActive: true},
    {id:  "L4", label:"Linear-Int", isActive: false},
    {id:  "L5", label:"Linear-Int", isActive: false},
    {id:  "L6", label:"Linear-Int", isActive: false},
    {id:  "L7", label:"Linear-Int", isActive: false},
    {id:  "L8", label:"Linear-Int", isActive: false},
    {id:  "L9", label:"Linear-Int", isActive: false},
    {id:  "L10", label:"Linear-Int", isActive: false},
]);

  const [interpolationLabelActive,setinterpolationLabelActive] = useState("L3")

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

  const changeInterpolationLabelActive = (id:string ) => {
    setinterpolationSelectorList(interpolationSelectorList.map((data)=>(
      data.id === id ? {...data,isActive:true}:data.id ===interpolationLabelActive? {...data,isActive:false}:data
    )))
    setinterpolationLabelActive(id)
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
      <div className='row mt-2 interpolation-menu'>
        <div className='col-2 interpolation-selector g-0'>
          <InterpolationSelection selectorList={interpolationSelectorList} changeInterpolationLabelActive={changeInterpolationLabelActive}/>
        </div>
        <div className='col-7'>
          <div className='row interpolation-selector-form align-items-center'>
            <InterpolationSelectorForm interpolationMethod={interpolationLabelActive}/>
          </div>
          <div className='row interpolation-selector-images align-items-center'>
            <InterpolationSelectorImages imageDisplay={interpolationSelectorImages}/>
          </div>
        </div>
        <div className='col-3 d-flex align-items-center interpolation-result'>
          <img className="mx-auto" src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=" alt="" width={340} height={340}/>
        </div>
      </div>
    </>
  );
};

export default HandbagPage;
