import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { useMediaQuery } from 'react-responsive'
import './HomeScreen.css';
import Slider from '@material-ui/core/Slider';
import Input from '@material-ui/core/Input';

const useStyles = makeStyles({
    root: {
        width: 150,
        color: '#fff'
    },
    input: {
        width: 42,
    },
});

const HomeScreen = () => {
    const isMobile = useMediaQuery({ query: '(max-width: 640px)' });

    const classes = useStyles();
    const [value, setValue] = React.useState(30);

    const handleSliderChange = (event, newValue) => {
        setValue(newValue);
    };

    const handleInputChange = event => {
        setValue(event.target.value === '' ? '' : Number(event.target.value));
    };

    const handleBlur = () => {
        if (value < 0) {
            setValue(0);
        } else if (value > 100) {
            setValue(100);
        }
    };

    // if mobile
    if (isMobile) {
        return (
            <div className="mobileHeader">

            </div>
        );
    }
    // if desktop
    return (
        <div className="desktopHeader">
            <p className="desktopHeaderTitle">MatchMyStyle</p>
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
    );
}

export default HomeScreen;