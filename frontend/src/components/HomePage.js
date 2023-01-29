import React from "react";
import AppBar from "./AppBar";
import QP_America_Logo from '../../static/images/QP-America-Logo.png';
import QP_Text from "../../static/images/QP-Text.png";
import Grid from "@material-ui/core/Grid";
import {makeStyles} from '@material-ui/core/styles';
import Typography from "@material-ui/core/Typography";

const useStyles = makeStyles((theme) => ({
    root: {
        textAlign: 'center',
        backgroundColor: '#076AE0',
        color: '#FFFFFF',
        fontFamily: 'BebasNeue',
    },
    mainLogo: {
        width: '50%',
        margin: '0 auto',
    },
    smallLogo: {
        width: '25%',
        margin: '0 auto',
    },
}));

const HomePage = () => {
    const classes = useStyles();

    return (
        <div className={classes.root}>
            <AppBar/>
            <Grid container>
                <Grid item xs={12}>
                    <img src={QP_America_Logo} alt="QP America Logo" className={classes.mainLogo}/>
                </Grid>
                <Grid item xs={12}>
                    <img src={QP_Text} alt="QP America Small Logo" className={classes.smallLogo}/>
                </Grid>
            </Grid>
        </div>
    );
}

export default HomePage;