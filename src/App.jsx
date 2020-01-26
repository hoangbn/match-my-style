import React from 'react';
import { Route, Switch } from "react-router-dom";
import HomeScreen from './screens/HomeScreen';
import { Wardrobe } from "./screens/Wardrobe";

export const App = () => {
    return (
        <Switch>
            <Route path={"/home"}>
                <HomeScreen />
            </Route>
            <Route path={"/my-wardrobe"}>
                <Wardrobe />
            </Route>
        </Switch>
    )
};