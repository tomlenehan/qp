import React, { useState, useEffect } from "react";
import AppBar from "./AppBar";
import LoadingSpinner from "./LoadingSpinner";
import { Grid, Card, CardActionArea, CardMedia, Typography, CardContent, CardActions, Button } from "@material-ui/core";

const BillsPage = () => {
    const [bills, setBills] = useState([]);
    const [loading, setLoading] = useState(true);
    const classes = useStyles();

    useEffect(() => {
        fetch('/api/get_bills/')
        .then(res => res.json())
        .then(data => {
            setBills(data);
            setLoading(false);
        })
        .catch(error => {
            console.error(error);
            setLoading(false);
        });
    }, []);

    return (
        <div className={classes.root}>
            <AppBar/>
            {loading ? <LoadingSpinner/> :
                <Grid container spacing={3}>
                    {bills.map((bill) => (
                        <Grid item xs={12} sm={4} key={bill.bill_id}>
                            <Card className={classes.card}>
                                <CardActionArea>
                                    <Typography className={classes.billTitle}>
                                        {bill.short_title}
                                    </Typography>
                                </CardActionArea>
                                <CardContent>
                                    <Typography variant="body2" color="textSecondary" component="p">
                                        {bill.summary}
                                    </Typography>
                                </CardContent>
                                <CardActions>
                                    <Button size="small" color="primary">
                                        Learn More
                                    </Button>
                                </CardActions>
                            </Card>
                        </Grid>
                        ))}
                </Grid>
            }
        </div>
    );
};

export default BillsPage;
