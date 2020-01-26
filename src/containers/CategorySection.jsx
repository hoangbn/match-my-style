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
            const score_avg = categoryItemData.score_avg;
            return <CategoryItem key={name} src={src} name={name} brand={brand} score_avg={score_avg} />;
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