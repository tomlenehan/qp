import React, {useState, useEffect} from 'react';
import {
    makeStyles, ThemeProvider, Card, CardActionArea, CardActions,
    CardContent, CardMedia, Button, Typography, Grid
} from '@material-ui/core';
import TwitterIcon from "@material-ui/icons/Twitter";
import AppBar from './AppBar';
import LoadingSpinner from './LoadingSpinner';
import theme from './Theme';


const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
        overflowY: 'scroll',
    },
    card: {
        maxWidth: 245,
        margin: theme.spacing(2),
    },
    media: {
        height: 200,
    },
}));

const MembersPage = (props) => {
    const classes = useStyles();
    const [members, setMembers] = useState([]);
    const [loading, setLoading] = useState(true);

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
                {loading ? <LoadingSpinner/> :
                    <Grid container spacing={3}>
                        {members.map((member) => (
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
                                                {member.short_title} {member.first_name} {member.last_name}
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
                                        {member.twitter_account &&
                                            <Button size="small" href={`https://twitter.com/${member.twitter_account}`}
                                                    target="_blank" rel="noopener noreferrer">
                                                <TwitterIcon fontSize="small"/>
                                            </Button>}
                                    </CardActions>
                                </Card>
                            </Grid>
                        ))}
                    </Grid>
                }
            </ThemeProvider>
        </div>
    );
}

export default MembersPage;