import React from 'react';
import './Header.css';
import { useMediaQuery } from 'react-responsive';
import { makeStyles } from '@material-ui/core/styles';
import Slider from '@material-ui/core/Slider';
import Input from '@material-ui/core/Input';
import { MatchMyStyle } from '../assets/images/';
import { ReactSVG } from 'react-svg'

const useStyles = makeStyles({
    root: {
        width: 150,
        color: '#fff'
    },
    input: {
        color: '#fff',
        marginLeft: '25px',
        marginRight: '25px',
        fontFamily: 'Futura-Medium',
        fontSize: '24px',
    },
});

const Header = ({ reloadStyles }) => {

    // https://material-ui.com/components/slider/
    const classes = useStyles();
    const [value, setValue] = React.useState(50);
    const [showReloadButton, setToggleReloadButton] = React.useState(false);

    const handleSliderChange = (event, newValue) => {
        setToggleReloadButton(true);
        setValue(newValue);
    };

    const handleInputChange = event => {
        if (event.target.value !== '') {
            let num = Number(event.target.value);
            if (num >= 0 && num <= 100) {
                setValue(num);
                console.log(num);
                setToggleReloadButton(true);
            }
        } else {
            if (event.target.value !== '-') {
                setValue('');
            }
        }
    };

    const handleBlur = () => {
        if (value < 0) {
            setValue(0);
        } else if (value > 100) {
            setValue(100);
        }
    };

    return (
        <div className="desktopHeader">
            <ReactSVG src={MatchMyStyle}
                beforeInjection={svg => {
                    svg.classList.add('desktopMatchMyStyleLogo')
                    svg.setAttribute('style',
                        'width: 300px; margin-left: 50px; margin-top: 10px;')
                }}
            
            />
            <div style={{ flex: 1 }} />
            <div className="desktopStyleMatchContainer" style={reloadStyles ? {} : {display: "none"}}>
                {showReloadButton && (
                    <button className="desktopReloadStylesButton" onClick={() => {
                        reloadStyles(value);
                        setToggleReloadButton(false)
                    }}>
                        <p>Reload</p>
                    </button>
                )}
                <div>
                    <p className="desktopStyleMatchText">Style Match</p>
                </div>
                <Slider
                    className={classes.root}
                    value={typeof value === 'number' ? value : 0}
                    onChange={handleSliderChange}
                    aria-labelledby="input-slider"
                />
                <Input
                    className={classes.input}
                    value={value}
                    margin="dense"
                    disableUnderline
                    onChange={handleInputChange}
                    onBlur={handleBlur}
                    inputProps={{
                        step: 1,
                        min: 0,
                        max: 100,
                        type: 'number',
                        'aria-labelledby': 'input-slider',
                    }}
                />
            </div>
        </div>
    );
};

export default Header;