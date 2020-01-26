import React, { useState, useEffect } from "react";
import UserService from "../services/UserService";
import { useAlert } from "react-alert";
import {Header} from "../components";
import CategorySectionIterator from "../containers/CategorySectionIterator";
import {catalogData} from "../catalogData";
import {Subheader} from "../components/Subheader";

// hardcoded username for now
const USERNAME = "waduhek";

export const Wardrobe = () => {
    const alert = useAlert();
    const [userItems, setUserItems] = useState({});

    useEffect(() => {
        const getUserItems = async () => {
            try {
                const items = await UserService.getUserItems(USERNAME);
                setUserItems(items);
            } catch (e) {
                alert.error("Failed to load data");
                console.error(e);
            }
        };
        getUserItems().then(r => {});
    });

    return (
        <>
            <Header/>
            <Subheader text={"Wardrobe"}/>
            <CategorySectionIterator itemsData={userItems}/>
        </>
    )
};