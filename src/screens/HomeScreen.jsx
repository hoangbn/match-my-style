import React from 'react';
import { Header } from '../components';
import { Subheader } from '../components/Subheader';
import { useMediaQuery } from 'react-responsive';
import CategorySectionIterator from '../containers/CategorySectionIterator';
import { catalogData } from '../catalogData';

const HomeScreen = () => {
    //const isMobile = useMediaQuery({ query: '(max-width: 640px)' });
    const reloadStyles = (value) => {
        console.log(`reloading styles with ${value}% style match`);
    };

    // // if mobile
    // if (isMobile) {
    //     return (
    //         <div className="mobileHeader">

    //         </div>
    //     );
    // }

    // if desktop
    return (
        <>
            <Header reloadStyles={reloadStyles} />
            <Subheader text={"Men's Demo Catalog > DeltaHacks 2020"}/>
            <CategorySectionIterator itemsData={catalogData}/>
        </>
    );
};

export default HomeScreen;