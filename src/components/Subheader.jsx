import React from 'react';
import styled from 'styled-components'

export const Subheader = ({text}) => {
    return <Wrapper>{text}</Wrapper>
};

const Wrapper = styled.p`
    font-family: 'Futura-Medium', sans-serif;
    font-size: 16px;
    color: #A3A3A3;
    margin-left: 50px;
`;