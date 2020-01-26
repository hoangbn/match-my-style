import React, { useState } from "react";
import { Col, Form, Modal, Row } from "react-bootstrap";
import UserService from "../services/UserService";
import { useAlert } from "react-alert";
import Button from "@material-ui/core/Button";

// hardcode username for now
const USERNAME = "waduhek";

const itemTypes = [
    { name: "Pants", value: "pants" },
    { name: "Shirts", value: "shirts" },
];

export const UploadItemModal = ({ show, onHide, setJoined }) => {
    const [itemType, setItemType] = useState(itemTypes[0].value);
    const [chosenImage, setChosenImage] = useState();
    const alert = useAlert();

    const uploadImage = async () => {
        try {
            await UserService.addItem(USERNAME, itemType, itemType);
            onHide();
            // setJoined(true);
        } catch (e) {
            console.error(e);
            alert.error("Failed to upload item");
        }
    };

    return (
        <Modal show={show} onHide={onHide} centered>
            <Modal.Header closeButton>
                <Modal.Title>Upload Image</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form>
                    <Form.Group as={Row} controlId="itemType">
                        <Form.Label column={true} sm="4">
                            Item Type
                        </Form.Label>
                        <Col sm="8">
                            <Form.Control
                                as="select"
                                onChange={e =>
                                    setItemType(e.currentTarget.value)
                                }
                            >
                                {itemTypes.map(option => (
                                    <option key={option.value} value={option.value}>
                                        {option.name}
                                    </option>
                                ))}
                            </Form.Control>
                        </Col>
                    </Form.Group>
                </Form>
            </Modal.Body>
            <Modal.Footer>
                <Button text="Join" onClick={uploadImage} />
            </Modal.Footer>
        </Modal>
    );
};
