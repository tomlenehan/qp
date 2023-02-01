import React from "react";
import QP_America_Logo from '../../static/images/logos/QP-America-Logo-LG.png';
import QP_Text from "../../static/images/logos/QP-Text-LG.png";
import Grid from "@material-ui/core/Grid";
import {makeStyles} from '@material-ui/core/styles';
import Typography from "@material-ui/core/Typography";
import AppBar from "./AppBar";
import theme from './Theme';

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
    },
    homePageContainer: {
        textAlign: 'center',
        // backgroundColor: '#076AE0',
        // color: '#FFFFFF',
    },
    mainLogo: {
        width: '50%',
        margin: '0 auto',
        display: 'block',
    },
    smallLogo: {
        width: '30%',
        margin: '0 auto',
        display: 'block',
    },

}));

const HomePage = () => {
    const classes = useStyles();

    return (
        <div className={classes.root}>
            <AppBar/>
            <div className={classes.homePageContainer}>
                <Grid container>
                    <Grid item xs={12}>
                        <img src={QP_America_Logo} alt="QP America Logo" className={classes.mainLogo}/>
                    </Grid>
                    <Grid item xs={12}>
                        <img src={QP_Text} alt="QP America Small Logo" className={classes.smallLogo}/>
                    </Grid>
                </Grid>
            </div>
        </div>
    );
}

export default HomePage;
