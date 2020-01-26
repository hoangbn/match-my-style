import React from "react";
import { usePromiseTracker } from "react-promise-tracker";
import Loader from "react-loader-spinner";
import styled from "styled-components";
import "react-loader-spinner/dist/loader/css/react-spinner-loader.css";

export const LoadingComponent = () => {
    const { promiseInProgress } = usePromiseTracker();
    return !promiseInProgress ? (
        <div />
    ) : (
        <Wrapper>
            <Loader type="Plane" height={100} width={100} />
        </Wrapper>
    );
};

const Wrapper = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1000;
`;
