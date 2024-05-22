// src/components/Graph.js
import React from 'react';

const Graph = ({ date, onBack }) => {
    return (
        <div className="graph">
            <button onClick={onBack}>Back to Calendar</button>
            <h2>Graph for {date.toString()}</h2>
            {/* Graph rendering logic here */}
        </div>
    );
};

export default Graph;