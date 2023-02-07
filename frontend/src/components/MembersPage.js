import React, {useState, useEffect} from 'react';
import {
    makeStyles, ThemeProvider, Card, CardActionArea, CardActions,
    CardContent, CardMedia, Button, Typography, Grid,
} from '@material-ui/core';
import TwitterIcon from "@material-ui/icons/Twitter";
import Footer from './Footer';
import AppBar from './AppBar';
import LoadingSpinner from './LoadingSpinner';
import theme from './Theme';
import {TextField} from "@material-ui/core";
import PaginationControl from './PaginationControl';

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
        overflowY: 'scroll',
        justifyContent: 'center',
    },
    card: {
        maxWidth: 245,
        margin: theme.spacing(2),
    },
    media: {
        height: 200,
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
    },
}));

const MembersPage = (props) => {
    const classes = useStyles();
    const [members, setMembers] = useState([]);
    const [loading, setLoading] = useState(true);
    const [searchTerm, setSearchTerm] = useState('');
    const [currentPage, setCurrentPage] = useState(1);
    const [itemsPerPage, setItemsPerPage] = useState(20);

    const indexOfLastItem = currentPage * itemsPerPage;
    const indexOfFirstItem = indexOfLastItem - itemsPerPage;
    const currentMembers = members.slice(indexOfFirstItem, indexOfLastItem);

    const pageNumbers = [];
    for (let i = 1; i <= Math.ceil(members.length / itemsPerPage); i++) {
        pageNumbers.push(i);
    }

    const handlePageChange = (page) => {
        setCurrentPage(page);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        setLoading(true);
        const url = `/api/get_members/${searchTerm}`
        fetch(url)
            .then(response => response.json())
            .then(data => {
                setMembers(data.members);
                setLoading(false);
            })
            .catch(error => {
                console.error(error);
                setLoading(false);
            });
    };


    useEffect(() => {
        setLoading(true);
        fetch('/api/get_members/')
            .then(response => response.json())
            .then(data => {
                setMembers(data.members);
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
                <form className={classes.searchContainer} onSubmit={handleSubmit}>
                    <TextField
                        className={classes.searchBar}
                        label="Search by Name or State abbreviation"
                        variant="outlined"
                        value={searchTerm}
                        onChange={e => setSearchTerm(e.target.value)}
                    />
                    <Button variant="contained" color="primary" type="submit">
                        Search
                    </Button>
                </form>
                {loading ? <LoadingSpinner/> :
                    <Grid container spacing={3}>
                        {currentMembers.map((member) => (
                            <Grid item xs={12} sm={3} key={member.member_id}>
                                <Card className={classes.card}>
                                    <CardActionArea>
                                        <CardMedia
                                            className={classes.media}
                                            image={`/static/images/profile_images/${member.img_file}`}
                                            title="Member Image"
                                        />
                                        <CardContent>
                                            <Typography gutterBottom variant="h5" component="h2">
                                                {member.first_name} {member.last_name}
                                            </Typography>
                                            <Typography variant="body2" color="textSecondary" component="p">
                                                {member.title}, {member.state}
                                            </Typography>
                                        </CardContent>
                                    </CardActionArea>
                                    <CardActions>
                                        <Button size="small" color="primary">
                                            Learn More
                                        </Button>
                                        {member.twitter_account && (
                                            <Button
                                                size="small"
                                                href={"https://twitter.com/${member.twitter_account"}
                                                target="_blank"
                                                rel="noopener noreferrer">
                                                <TwitterIcon fontSize="small"/>
                                            </Button>)}
                                    </CardActions>
                                </Card>
                            </Grid>
                        ))}
                    </Grid>

                }
                <PaginationControl
                    pageNumbers={pageNumbers}
                    currentPage={currentPage}
                    onPageChange={handlePageChange}
                />
                <Footer/>
            </ThemeProvider>
        </div>
    );
};
export default MembersPage;