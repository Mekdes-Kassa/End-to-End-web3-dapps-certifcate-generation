// src/components/TraineeComponent.js
import React, { useState } from 'react';

const TraineeComponent = ({ optIn, checkRequestStatus }) => {
  const [requestStatus, setRequestStatus] = useState('');

  const handleOptIn = () => {
    // Call the function to opt-in to NFT certificate
    optIn(/* pass necessary data */);
  };

  const handleCheckRequestStatus = () => {
    // Call the function to check request status
    checkRequestStatus(/* pass necessary data and update requestStatus state */);
  };

  return (
    <div>
      <h2>Trainee Role</h2>
      <button onClick={handleOptIn}>Opt-In to NFT</button>
      <button onClick={handleCheckRequestStatus}>Check Request Status</button>

      {/* Display request status */}
      <p>Request Status: {requestStatus}</p>
    </div>
  );
};

export default TraineeComponent;
