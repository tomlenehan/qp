import React from "react";
import {
  AppBar as MuiAppBar,
  Toolbar,
  Typography,
  IconButton,
  Button,
  makeStyles,
} from "@material-ui/core";
import TwitterIcon from "@material-ui/icons/Twitter";
import { Link } from "react-router-dom";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
}));

const AppBar = () => {
  const classes = useStyles();

  return (
    <MuiAppBar position="static">
      <Toolbar>
        <Typography variant="h6" className={classes.title}>
          Question Politics
        </Typography>
        <Button href="/bills" component={Link} to="/bills" >
          Bills
        </Button>
        <Button color="inherit" component={Link} to="/members">
          Members
        </Button>
      </Toolbar>
    </MuiAppBar>
  );
};

export default AppBar;
