import React from 'react';
import './CategoryItem.css';;

const CategoryItem = ({ src, name, brand, score_avg }) => {
    return (
        <div className="desktopCategoryItemOuter">
            <div className="desktopCategoryItemMatch" style={score_avg ? {} : {display: "none"}}>
                <p>{parseInt(score_avg * 100)}%</p>
            </div>
            <img className="desktopCategoryItemSrc" src={src}  alt=""/>
            <p className="desktopCategoryName">{name}</p>
            <p className="desktopCategoryBrand">{brand}</p>
        </div>
    );
};

export default CategoryItem;