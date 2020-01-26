import React from 'react';
import './HomeScreen.css';
import { Header } from '../components';
import { useMediaQuery } from 'react-responsive';
import CategorySectionIterator from '../containers/CategorySectionIterator';

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
            <p className="desktopSubheader">{`Mens Demo Catalog > DeltaHacks 2020`}</p>
            <CategorySectionIterator />
        </>
    );
}

export default HomeScreen;