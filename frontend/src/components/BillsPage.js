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
    Button, TextField
} from "@material-ui/core";
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import theme from "./Theme";
import PaginationControl from "./PaginationControl";
import Footer from "./Footer";

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
        overflowY: 'scroll',
        justifyContent: 'center',
        height: '100vh',
    },
    searchContainer: {
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        marginTop: '2rem',
    },
    searchBar: {
        backgroundColor: '0862CF',
        marginRight: '1rem',
        width: '50%',
        fontFamily: 'Roboto',
        boxShadow: '0px 3px 1px -2px rgb(0 0 0 / 20%), 0px 2px 2px 0px rgb(0 0 0 / 14%), 0px 1px 5px 0px rgb(0 0 0 / 12%)',
    },
    accordion: {
        margin: theme.spacing(2),
    },
    billTitle: {
        fontSize: 20,
        fontWeight: 'bold',
        fontfamily: 'Roboto',
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
    const classes = useStyles();
    const [bills, setBills] = useState([]);
    const [loading, setLoading] = useState(true);
    const [searchTerm, setSearchTerm] = useState('');
    const [currentPage, setCurrentPage] = useState(1);
    const [itemsPerPage, setItemsPerPage] = useState(20);

    const indexOfLastItem = currentPage * itemsPerPage;
    const indexOfFirstItem = indexOfLastItem - itemsPerPage;
    const currentBills = bills.slice(indexOfFirstItem, indexOfLastItem);

    const pageNumbers = [];
    for (let i = 1; i <= Math.ceil(bills.length / itemsPerPage); i++) {
        pageNumbers.push(i);
    }

    const handlePageChange = (page) => {
        setCurrentPage(page);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        setLoading(true);
        const url = `/api/get_bills/${searchTerm}`
        fetch(url)
            .then(response => response.json())
            .then(data => {
                setBills(data.bills);
                setLoading(false);
            })
            .catch(error => {
                console.error(error);
                setLoading(false);
            });
    };


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
        <ThemeProvider theme={theme}>
            <div className={classes.root}>
                <AppBar/>


                <form className={classes.searchContainer} onSubmit={handleSubmit}>
                    <TextField
                        className={classes.searchBar}
                        label="Search by Bill title"
                        variant="outlined"
                        value={searchTerm}
                        onChange={e => setSearchTerm(e.target.value)}
                    />
                    <Button variant="contained" color="primary" type="submit">
                        Search
                    </Button>
                </form>

                {loading ? (
                    <LoadingSpinner/>
                ) : (
                    <div>
                        {currentBills.map((bill) => (
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
            </div>
            <div>
                <PaginationControl
                    pageNumbers={pageNumbers}
                    currentPage={currentPage}
                    onPageChange={handlePageChange}
                />
                <Footer/>
            </div>
        </ThemeProvider>
    );
};

export default BillsPage;