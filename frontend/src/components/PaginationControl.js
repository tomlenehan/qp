import React, {useState, useEffect} from 'react';
import {Pagination} from '@material-ui/lab';
import {makeStyles} from "@material-ui/core";
import theme from './Theme';

const useStyles = makeStyles(() => ({
    paginateContainer: {
        flexGrow: 1,
        justifyContent: 'center',
    }
}));

const PaginationControl = (props) => {
    const classes = useStyles();
    const [currentPage, setCurrentPage] = useState(1);


    const handleChange = (event, value) => {
        setCurrentPage(value);
        props.onPageChange(value);
    };

    return (

        <div className={classes.paginateContainer}>
            <Pagination
                size="large"
                count={props.pageNumbers.length}
                page={currentPage}
                onChange={handleChange}
            />
        </div>
    );
};

export default PaginationControl;
