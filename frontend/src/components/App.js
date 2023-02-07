import React from "react";
import {Routes, Route, BrowserRouter, createSearchParams} from "react-router-dom";
import HomePage from "./HomePage";
import BillsPage from "./BillsPage";
import MembersPage from "./MembersPage";

export default function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/bills" element={<BillsPage />} />
                <Route path="/members" element={<MembersPage />} />
            </Routes>
        </BrowserRouter>
    );
}
