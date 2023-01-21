import React, {Component} from "react";
import Button from "@mui/material/Button";
import Grid from "@mui/material/Grid";
import Typography from "@mui/material/Typography";
import TextField from "@mui/material/TextField";
import FormHelperText from "@mui/material/FormHelperText";
import FormControl from "@mui/material/FormControl";
import {Link} from "react-router-dom";

export default class BillsPage extends Component {
    defaultBills = 2;

    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Grid container spacing={1}>
                <Grid item xs={12} align="center">
                    <Typography component="h4" variant="h4">
                        View Bills
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">

                </Grid>
            </Grid>
        );
    }
}