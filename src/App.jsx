import React from 'react';
import { Route, Switch } from "react-router-dom";
import HomeScreen from './screens/HomeScreen';
import { Wardrobe } from "./screens/Wardrobe";
import { LoadingComponent } from "./LoadingComponent";

export const App = () => {
    return (
        <div>
            <LoadingComponent />
            <Switch>
                <Route path={"/home"}>
                    <HomeScreen />
                </Route>
                <Route path={"/my-wardrobe"}>
                    <Wardrobe />
                </Route>
            </Switch>
        </div>
    )
};