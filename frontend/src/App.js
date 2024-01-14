// src/App.js
import React from 'react';
import StaffComponent from './components/StaffComponent';
import TraineeComponent from './components/TraineeComponent';

const App = () => {
  // functions for NFT operations and smart contract interactions

  const issueNFT = (nftData) => {
    //  logic to issue NFT
    console.log('Issuing NFT:', nftData);
  };

  const optIn = (traineeData) => {
    // logic for trainee to opt-in
    console.log('Trainee opted in:', traineeData);
  };

  const checkRequestStatus = (requestData) => {
    // logic to check request status
    console.log('Checking request status:', requestData);
  };

  const approveTransfer = (requestData) => {
    // logic to approve NFT transfer
    console.log('Approving transfer:', requestData);
  };

  return (
    <div>
    <h1>NFT Management System</h1>
    <StaffComponent
      issueNFT={issueNFT}
      approveTransfer={approveTransfer}
    />
    <br />
    <TraineeComponent
      optIn={optIn}
      checkRequestStatus={checkRequestStatus}
    />
    <br />
  </div>
  );
};

export default App;
