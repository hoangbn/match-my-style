import React from 'react';
import './CategorySection.css';
import CategoryItem from '../components/CategoryItem';
import ScrollableAnchor from 'react-scrollable-anchor';

const CategorySection = ({ categoryName, categoryData }) => {

    const renderCategoryItems = () => {
        return categoryData.map((categoryItemData) => {
            const src = categoryItemData.src ? categoryItemData.src : categoryItemData;
            const brand = categoryItemData.brand;
            const name = categoryItemData.name;
            return <CategoryItem key={name} src={src} name={name} brand={brand} />;
        });
    };

    return (
        <ScrollableAnchor id={categoryName}>
            <div className="desktopCategoryOuter">
                <p className="desktopCategoryTitle">
                    {categoryName.charAt(0).toUpperCase() + categoryName.slice(1)}
                </p>
                <div className="desktopCategoryItemRow">
                    {renderCategoryItems()}
                </div>
            </div>
        </ScrollableAnchor>
    );
};

export default CategorySection;