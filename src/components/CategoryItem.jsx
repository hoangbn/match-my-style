import React from 'react';
import './CategoryItem.css';;

const CategoryItem = ({ src, name, brand }) => {
    return (
        <div className="desktopCategoryItemOuter">
            <div className="desktopCategoryItemMatch">
                <p>77%</p>
            </div>
            <img className="desktopCategoryItemSrc" src={src}  alt=""/>
            <p className="desktopCategoryName">{name}</p>
            <p className="desktopCategoryBrand">{brand}</p>
        </div>
    );
};

export default CategoryItem;