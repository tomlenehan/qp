import React, {useState, useEffect} from 'react';
import {makeStyles} from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import LoadingSpinner from './LoadingSpinner';
import AppBar from "./AppBar"; // import your loading spinner component

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
    },
    card: {
        maxWidth: 345,
        margin: theme.spacing(2),
    },
    media: {
        height: 140,
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
            });
    }, []);

    return (
        <div className={classes.root}>
            <AppBar/>
            {loading ? <LoadingSpinner/> :
                <Grid container spacing={3}>
                    {members.map((member) => (
                        <Grid item xs={12} sm={4} key={member.member_id}>
                            <Card className={classes.card}>
                                <CardActionArea>
                                    <CardMedia
                                        className={classes.media}
                                        image={member.image_url}
                                        title="Member Image"
                                    />
                                    <CardContent>
                                        <Typography gutterBottom variant="h5" component="h2">
                                            {member.first_name} {member.last_name}
                                        </Typography>
                                        <Typography variant="body2" color="textSecondary" component="p">
                                            {member.email}
                                        </Typography>
                                    </CardContent>
                                </CardActionArea>
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
}

export default MembersPage;