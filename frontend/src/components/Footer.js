import React from 'react';
import { ThemeProvider } from '@material-ui/core';
import theme from './Theme';

const Footer = (props) => {
    return (
        <ThemeProvider theme={theme}>
            <footer style={{color: 'white', padding: '1rem', justifyContent: 'center'}}>
                <p>Copyright &copy; {new Date().getFullYear()} Question Systems </p>
            </footer>
        </ThemeProvider>
    )
};

export default Footer;
