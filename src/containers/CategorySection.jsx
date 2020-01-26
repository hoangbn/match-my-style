import React from 'react';
import './CategorySection.css';
import { useMediaQuery } from 'react-responsive';
import CategoryItem from '../components/CategoryItem';

const CategorySection = ({ categoryName, categoryData }) => {
    // const isMobile = useMediaQuery({ query: '(max-width: 640px)' });

    // if (isMobile) {
    //     return (
    //         <div></div>
    //     )
    // }

    const renderCategoryItems = () => {
        return categoryData.map((categoryItemData) => {
            let src = categoryItemData.src;
            let name = categoryItemData.name;
            let brand = categoryItemData.brand;
            return <CategoryItem key={name} src={src} name={name} brand={brand} />;
        });
    };

    return (
        <div className="desktopCategoryOuter">
            <p className="desktopCategoryTitle">
                {categoryName.charAt(0).toUpperCase() + categoryName.slice(1)}
            </p>
            <div className="desktopCategoryItemRow">
                {renderCategoryItems()}
            </div>
        </div>
    );
};

export default CategorySection;