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
import AppBar from "./AppBar";

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
        overflow: 'scroll',
    },
    card: {
        maxWidth: 345,
        margin: theme.spacing(2),
        position: 'relative',
    },
    media: {
        height: 140,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
    },
    memberName: {
        position: 'absolute',
        bottom: theme.spacing(1),
        left: theme.spacing(1),
        color: 'white',
        fontWeight: 'bold',
        textShadow: '1px 1px 2px rgba(0, 0, 0, 0.5)',
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
            {loading ? (
                <LoadingSpinner/>
            ) : (
                <Grid container spacing={3}>
                    {members.map((member) => (
                        <Grid item xs={12} sm={4} key={member.member_id}>
                            <Card className={classes.card}>
                                <CardActionArea>
                                    <CardMedia
                                        className={classes.media}
                                        image={member.img_url}
                                        title="Member Image"
                                    />
                                    <Typography
                                        className={classes.memberName}
                                        style={{
                                            backgroundColor: "white",
                                            color: "black",
                                            position: "absolute",
                                            bottom: "5%",
                                            left: "5%",
                                            padding: "5px",
                                        }}
                                    >
                                        {member.first_name} {member.last_name}
                                    </Typography>
                                </CardActionArea>
                                <CardContent>
                                    <Typography
                                        variant="body2"
                                        color="textSecondary"
                                        component="p"
                                    >
                                        {member.email}
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
            )}
        </div>
    );
}
export default MembersPage;
