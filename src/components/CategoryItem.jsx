import React from 'react';
import './CategoryItem.css';;

const CategoryItem = ({ src, name, brand }) => {
    return (
        <div className="desktopCategoryItemOuter">
            <img className="desktopCategoryItemSrc" src={src} />
            <p>{name}</p>
            <p>{brand}</p>
        </div>
    );
};

export default CategoryItem;