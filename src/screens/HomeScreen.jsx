import React, { useState, useEffect } from "react";
import { Header } from '../components';
import { Subheader } from '../components/Subheader';
import CategorySectionIterator from '../containers/CategorySectionIterator';
import { catalogData } from '../catalogData';
import UserService from "../services/UserService";
import {useAlert} from "react-alert";

// hardcoded username for now
const USERNAME = "waduhek"

const HomeScreen = () => {
    const alert = useAlert();
    const [filteredCatalog, setFilteredCatalog] = useState(catalogData);

    const reloadStyles = async (value) => {
        console.log(`reloading styles with ${value}% style match`);
        try {
            const data = await UserService.getMostSimilar(USERNAME, value);
            setFilteredCatalog(data);
            console.log(data);
        } catch (e) {
            alert.error("Failed to load data");
            console.error(e);
        }
    };

    return (
        <>
            <Header reloadStyles={reloadStyles} />
            <Subheader text={"Men's Demo Catalog > DeltaHacks 2020"}/>
            <CategorySectionIterator itemsData={filteredCatalog}/>
        </>
    );
};

export default HomeScreen;