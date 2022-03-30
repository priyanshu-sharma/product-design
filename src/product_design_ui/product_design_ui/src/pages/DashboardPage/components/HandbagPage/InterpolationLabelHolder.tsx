interface data {
    id: string;
    label: string;
    isActive: boolean;
}

interface Props {
    data: data;
    changeInterpolationLabelActive: any;
}

const InterpolationLabelHolder = ({data,changeInterpolationLabelActive}:Props) => {
return (
    <div className={data.isActive?"label-holder label-active":"label-holder"} onClick={() => changeInterpolationLabelActive(data.id)}>
        {data.label}
    </div>
);
};

export default InterpolationLabelHolder;