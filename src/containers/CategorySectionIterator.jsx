import React from 'react';
import { catalogData, getCategoryUrls } from '../catalogData';   // REPLACE WITH API FETCH
import CategorySection from './CategorySection';

const CategorySectionIterator = () => {
    const categories = Object.keys(catalogData);

    const renderSections = () => {
        return categories.map((categoryName) => {
            return <CategorySection key={categoryName} categoryName={categoryName}
                categoryData={catalogData[categoryName]} />
        });
    }

    return (
        <>
            <div>
                {renderSections()}
            </div>
        </>
    );
};

export default CategorySectionIterator;