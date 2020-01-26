import React, { useEffect } from 'react';
import { catalogData, getCategoryUrls } from '../catalogData';   // REPLACE WITH API FETCH
import CategorySection from './CategorySection';
import './CategorySectionIterator.css';

const CategorySectionIterator = () => {
    const [selectedCategory, setSelectedCategory] = React.useState('');
    useEffect(() => {
        setSelectedCategory(window.location.hash);
    }, []);

    const categories = Object.keys(catalogData);
    const renderSections = () => {
        return categories.map((categoryName) => {
            return <CategorySection key={categoryName} categoryName={categoryName}
                categoryData={catalogData[categoryName]} />;
        });
    }

    window.addEventListener("hashchange", function(e) {
        setSelectedCategory(window.location.hash);
    });

    const renderScrollBarSections = () => {
        return categories.map((categoryName) => {
            let defaultTextStyle = {
                textDecoration: 'none',
                fontFamily: 'Futura-Medium',
                fontSize: 18,
                color: '#A3A3A3'
            };

            let selectedTextStyle = {
                textDecoration: 'none',
                fontFamily: 'Futura-Medium',
                fontSize: 18,
                color: '#30C2D6'
            };

            let defaultBubbleStyle = {
                height: 15,
                width: 15,
                borderRadius: 25,
                backgroundColor: '#A3A3A3'
            };

            let selectedBubbleStyle = {
                bottom: 25,
                height: 15,
                width: 15,
                borderRadius: 25,
                backgroundColor: '#30C2D6'
            };

            return (
                <a className="desktopScrollBarCategory" href={`#${categoryName}`}
                    style={selectedCategory === `#${categoryName}` ? selectedTextStyle : defaultTextStyle }>
                    <p className="desktopScrollBarSections">
                        {categoryName.charAt(0).toUpperCase() + categoryName.slice(1)}
                    </p>
                    <div className="desktopScrollBarBubbles">
                        <div style={selectedCategory === `#${categoryName}` ? selectedBubbleStyle : defaultBubbleStyle } />
                    </div>
                </a>
            );
        });
    }

    return (
        <div className="desktopCategorySectionsLayout">
            <div style={{
                display: 'flex',
                flexDirection: 'column',
            }}>
                {renderSections()}
            </div>
            <div className="desktopScrollBar">
                {renderScrollBarSections()}
            </div>
        </div>
    );
};

export default CategorySectionIterator;