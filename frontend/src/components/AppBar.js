import React from "react";
import {AppBar as MuiAppBar, Toolbar, IconButton, Button, makeStyles, Grid, ThemeProvider,} from "@material-ui/core";
import {Link} from "react-router-dom";
import QP_Logo from "../../static/images/logos/QP-Logo.png";
import theme from "./Theme";  // Import your custom theme here

const useStyles = makeStyles((theme) => ({
    menuButton: {
        fontFamily: "BebasNeue",
        marginRight: theme.spacing(2),
    },
    title: {
        flexGrow: 1,
    },
    logo: {
        width: "50px",
        marginRight: "10px",
    },
    toolbar: {
        justifyContent: "flex-end",
    },
}));

const AppBar = () => {
    const classes = useStyles();
    const baseUrl = process.env.BASE_URL || "http://localhost:8000";

    return (
        <ThemeProvider theme={theme}>  {/* Wrap the component with the ThemeProvider */}
            <MuiAppBar position="static">
                <Toolbar className={classes.toolbar}>
                    <Grid container justifyContent="flex-start" alignItems="center">
                        <Button color="inherit" component={Link} to="/">
                            <img
                                src={QP_Logo}
                                alt="QP-Logo"
                                className={classes.logo}
                            />
                        </Button>
                    </Grid>
                    <Grid container justifyContent="flex-end" alignItems="center">
                        <Button color="inherit"
                                onClick={() => window.location.href = `${baseUrl}/accounts/twitter/login/`}>
                            Sign Up with Twitter
                        </Button>
                        <Button color="inherit" component={Link} to="/bills">
                            Bills
                        </Button>
                        <Button color="inherit" component={Link} to="/members">
                            Members
                        </Button>
                    </Grid>
                </Toolbar>
            </MuiAppBar>
        </ThemeProvider>
    );
};

export default AppBar;
