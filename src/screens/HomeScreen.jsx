import React from 'react';
import './HomeScreen.css';
import { Header } from '../components';
import { useMediaQuery } from 'react-responsive';

const HomeScreen = () => {
    const isMobile = useMediaQuery({ query: '(max-width: 640px)' });
    const reloadStyles = (value) => {
        console.log(`reloading styles with ${value}% style match`);
    };

    // if mobile
    if (isMobile) {
        return (
            <div className="mobileHeader">

            </div>
        );
    }

    // if desktop
    return (
        <>
            <Header reloadStyles={reloadStyles} />
            <p className="subheader">Mens Demo Catalog > DeltaHacks 2020</p>
        </>
    );
}

export default HomeScreen;