import React from 'react';
import './CategoryItem.css';;

const CategoryItem = ({ src, name, brand }) => {
    return (
        <div className="desktopCategoryItemOuter">
            <img className="desktopCategoryItemSrc" src={src} />
            <p className="desktopCategoryName">{name}</p>
            <p className="desktopCategoryBrand">{brand}</p>
            <div className="desktopCategoryItemMatch">
                <p>77%</p>
            </div>
        </div>
    );
};

export default CategoryItem;