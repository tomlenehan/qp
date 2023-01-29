import React from "react";
import AppBar from "./AppBar";

const BillsPage = () => {

    const className = "full-width";

    return (
        <div className={className}>
            <AppBar/>
            <p>Bills</p>
            {/* Other components and content */}
        </div>
    );
};

export default BillsPage;
