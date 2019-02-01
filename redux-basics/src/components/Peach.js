
import React from 'react';
import { washPeach, eatPeach, rotPeach } from './../actions';
import { bindActionCreators } from 'redux';

const Peach = ({ washPeach, eatPeach, rotPeach, dirty, remainingBites, color  }) => (
    <div>
        <p>Dirty: {dirty ? 'true' : 'false'}</p>
        <p>Remaining bites: {remainingBites}</p>
        <p>Color: {color}</p>

        <button onClick={washPeach}>Wash peach</button>
        <button onClick={eatPeach}>Eat peach</button>
        <button onClick={rotPeach}>Rot peach</button>
    </div>
);

export default Peach