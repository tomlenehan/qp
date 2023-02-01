import React, {useState, useEffect} from "react";
import AppBar from "./AppBar";
import LoadingSpinner from "./LoadingSpinner";
import {
    makeStyles,
    ThemeProvider,
    Accordion,
    AccordionSummary,
    AccordionDetails,
    Typography,
    Button
} from "@material-ui/core";
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import theme from "./Theme";

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
        overflowY: 'scroll',
    },
    accordion: {
        margin: theme.spacing(2),
    },
    billTitle: {
        fontSize: 20,
        fontWeight: 'bold',
    },
    summary: {
        fontSize: 16,
        color: 'gray',
    },
    accordionDetails: {
        display: 'block',
    },
}));

const BillsPage = () => {
    const [bills, setBills] = useState([]);
    const [loading, setLoading] = useState(true);
    const classes = useStyles();

    useEffect(() => {
        fetch('/api/get_bills/')
            .then(response => response.json())
            .then(data => {
                setBills(data.bills);
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
            <ThemeProvider theme={theme}>
                {loading ? (
                    <LoadingSpinner/>
                ) : (
                    <div>
                        {bills.map((bill) => (
                            <Accordion key={bill.bill_id} className={classes.accordion}>
                                <AccordionSummary
                                    expandIcon={<ExpandMoreIcon/>}
                                    aria-controls="panel1a-content"
                                    id="panel1a-header"
                                >
                                    <Typography className={classes.billTitle}>{bill.short_title}</Typography>
                                </AccordionSummary>
                                <AccordionDetails className={classes.accordionDetails}>
                                    <Typography className={classes.summary}>{bill.summary}</Typography>
                                    <Button size="small" color="primary">
                                        Learn More
                                    </Button>
                                </AccordionDetails>
                            </Accordion>
                        ))}
                    </div>
                )}
            </ThemeProvider>
        </div>
    );
};

export default BillsPage;