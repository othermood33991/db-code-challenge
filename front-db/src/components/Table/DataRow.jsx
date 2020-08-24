import React from 'react';



const DataRow = (props) => {
    return (
        <tr>
            {Object.values(props.data).map(item => <td>{item}</td>)}
        </tr>
    );
};

export default DataRow;