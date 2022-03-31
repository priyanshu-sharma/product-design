import ImageGallery from './ImageGallery';
import 'bootstrap/dist/css/bootstrap.min.css'
import WorkSheet from './WorkSheet';
import {useState} from 'react';
import JsonData from './images.json';
import InterpolationSelectorImages from './InterpolationSelectorImages';
import InterpolationSelectorForm from './InterpolationSelectorForm';
import InterpolationSelection from './InterpolationSelection';

interface Image {
  id: string;
  path: string;
}

interface Props {
  images: Image[];
}


const HandbagPage = ({images}: Props) => {
  // const [galleryImages, setgalleryImages] = useState(JsonData);
  
  const [workSheetActive,setworkSheetActive] = useState("A1");
  const [exprBar,setexprBar] = useState("");
  const [imageString,setimageString] = useState("");
  const [interpolationLabelActive,setinterpolationLabelActive] = useState("Linear Interpolation")


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

  const [interpolationSelectorImages,setinterpolationSelectorImages]:any = useState([]);

  const [interpolationSelectorList,setinterpolationSelectorList] = useState([
    {id:  "L1", label:"Sum", isActive: false},
    {id:  "L2", label:"Difference", isActive: false},
    {id:  "Linear Interpolation", label:"Linear-Interpolation", isActive: true},
    {id:  "L4", label:"Linear-Int", isActive: false},
    {id:  "L5", label:"Linear-Int", isActive: false},
    {id:  "L6", label:"Linear-Int", isActive: false},
    {id:  "L7", label:"Linear-Int", isActive: false},
    {id:  "L8", label:"Linear-Int", isActive: false},
    {id:  "L9", label:"Linear-Int", isActive: false},
    {id:  "L10", label:"Linear-Int", isActive: false},
  ]);

  const [interpolationResultImage,setinterpolationResultImage] = useState({
    imgId: "None", 
    imgPath: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="
  })

  const changeInterpolationLabelActive = (id:string ) => {
    setinterpolationSelectorList(interpolationSelectorList.map((data)=>(
      data.id === id ? {...data,isActive:true}:data.id ===interpolationLabelActive? {...data,isActive:false}:data
    )))
    setinterpolationLabelActive(id)
  }


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

  const interpolate = () => {
    console.log(interpolationLabelActive);
    var imageArray = imageString.split(",");
    console.log(imageArray);
    var imageIDArray = [];
    var tempInterpolationImageArray = [];
    for( var row=0;row<workSheet.length;row++ ){
      for( var col=0; col<workSheet[row].length;col++) {
        if(imageArray.includes(workSheet[row][col].id)){
          console.log(workSheet[row][col])
          imageIDArray.push(workSheet[row][col].imgId)
          tempInterpolationImageArray.push({
            imgId: workSheet[row][col].imgId,
            imgPath: workSheet[row][col].imgPath
          })
        }
      }
    } 
    console.log(imageIDArray);
    console.log(tempInterpolationImageArray);
    setinterpolationSelectorImages(tempInterpolationImageArray);
    console.log(interpolationSelectorImages);
    var payload = {
      'images': imageIDArray,
      'product_type': 'HANDBAGS',
      'interpolation_type': interpolationLabelActive
    }
    console.log(payload)
  }

  const pushToWorkSheet = () => {
    setWorkSheet(workSheet.map((row)=>(
      row.map((data)=>(
        data.isActive == true? {...data,imgId: interpolationResultImage.imgId,imgPath: interpolationResultImage.imgPath}:data
      ))
    )));
  }

  return (
    <>
      <div className='row work-space'>
        <div className='col-6 image-gallery'>
          <ImageGallery images={images} addImageToWorkSheetActive={addImageToWorkSheetActive}/>
        </div>
        <div className='col-6'>
          <WorkSheet workSheetActive={workSheetActive} workSheet={workSheet} changeWorkSheetActive={changeWorkSheetActive}/>
        </div>
      </div>
      <div className='row'>
        <div className='col-10'>

        </div>
        <div className='col-2'>
          <button type="button" className="btn btn-dark float-end" onClick={() => pushToWorkSheet()}>Push to WorkSheet</button>
        </div>
      </div>
      <div className='row mt-2 interpolation-menu'>
        <div className='col-2 interpolation-selector g-0'>
          <InterpolationSelection selectorList={interpolationSelectorList} changeInterpolationLabelActive={changeInterpolationLabelActive}/>
        </div>
        <div className='col-7'>
          <div className='row interpolation-selector-form align-items-center'>
            <InterpolationSelectorForm interpolationMethod={interpolationLabelActive} imageString={imageString} setimageString={setimageString} interpolate={interpolate}/>
          </div>
          <div className='row interpolation-selector-images align-items-center'>
            <InterpolationSelectorImages imageDisplay={interpolationSelectorImages}/>
          </div>
        </div>
        <div className='col-3 d-flex align-items-center interpolation-result'>
          <img className="mx-auto" src={interpolationResultImage.imgPath} alt="No Image" width={340} height={340}/>
        </div>
      </div>
    </>
  );
};

export default HandbagPage;
