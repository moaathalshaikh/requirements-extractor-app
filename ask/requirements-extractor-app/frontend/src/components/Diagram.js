import React from 'react';
import { Chart } from 'react-google-charts';

const Diagram = ({ requirements }) => {
    const data = [
        ['Requirement Type', 'Count'],
        ['Functional', requirements.functional.length],
        ['Non-Functional', requirements.nonFunctional.length],
    ];

    const options = {
        title: 'Requirements Overview',
        pieHole: 0.4,
    };

    return (
        <div>
            <h2>Requirements Diagram</h2>
            <Chart
                chartType="PieChart"
                data={data}
                options={options}
                width={'100%'}
                height={'400px'}
                legendToggle
            />
        </div>
    );
};

export default Diagram;