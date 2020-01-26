import React, { useState, useEffect } from "react";
import UserService from "../services/UserService";
import { useAlert } from "react-alert";
import {Header} from "../components";
import CategorySectionIterator from "../containers/CategorySectionIterator";
import {Subheader} from "../components/Subheader";
import Button from "@material-ui/core/Button";
import { makeStyles } from "@material-ui/core/styles";
import { ButtonToolbar } from "react-bootstrap";
import { UploadItemModal } from "../components/UploadItemModal"

const useStyles = makeStyles(() => ({
    buttonWrapper: {
        position: "absolute",
        right: "40px",
        display: "flex",
        zIndex: "100"
    }
}));
// hardcoded username for now
const USERNAME = "waduhek";

export const Wardrobe = () => {
    const classes = useStyles();
    const alert = useAlert();
    const [userItems, setUserItems] = useState({});
    const [uploadItemModalShow, setUploadItemModalShow] = useState(false);
    const [updateTracker, setUpdateTracker] = useState(false);

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
        getUserItems();
    }, []);

    return (
        <>
            <Header/>
            <Subheader text={"Wardrobe"}/>
            <ButtonToolbar className={classes.buttonWrapper}>
                <Button
                variant="contained"
                size="small"
                color="primary"
                // onClick={() => setUploadItemModalShow(true)}
                >
                    Upload Image
                </Button>
                <UploadItemModal
                    show={uploadItemModalShow}
                    onHide={() => setUploadItemModalShow(false)}
                />
            </ButtonToolbar>
            <CategorySectionIterator itemsData={userItems}/>
        </>
    )
};