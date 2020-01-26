import React, { useState, useEffect } from "react";
import UserService from "../services/UserService";

// hardcoded username for now
const USERNAME = "waduhek";

export const Wardrobe = () => {
    const [userItems, setUserItems] = useState();

    useEffect(() => {
        const getUserItems = async () => {
            try {
                await UserService.getUserItems(USERNAME);
            }
        });
            setSelectedTab(0);
            setJoinedCommunity(joinResult.data);
            setCommunityInfo(communityInfo.data);
        };
    })
};