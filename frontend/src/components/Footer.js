import React from 'react';
import {makeStyles, ThemeProvider} from '@material-ui/core';
import theme from './Theme';


const useStyles = makeStyles(() => ({
    footer: {
        color: 'white',
        justifyContent: 'center',
        textAlign: 'center',
    }
}));


const Footer = (props) => {
    const classes = useStyles();

    return (
        <ThemeProvider theme={theme}>
            <footer className={classes.footer}>
                <p>Copyright &copy; {new Date().getFullYear()} Question Systems </p>
            </footer>
        </ThemeProvider>
    )
};

export default Footer;
