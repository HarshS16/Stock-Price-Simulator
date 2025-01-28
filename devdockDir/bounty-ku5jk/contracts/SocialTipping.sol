// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract SocialTipping {
    mapping(address => uint256) public creatorBalance;
    mapping(address => bool) public isCreator;
    
    event CreatorRegistered(address creator);
    event TipSent(address indexed from, address indexed to, uint256 amount);
    event WithdrawnTips(address indexed creator, uint256 amount);
    
    function registerAsCreator() external {
        require(!isCreator[msg.sender], "Already registered as creator");
        isCreator[msg.sender] = true;
        emit CreatorRegistered(msg.sender);
    }
    
    function sendTip(address creator) external payable {
        require(isCreator[creator], "Not a registered creator");
        require(msg.value > 0, "Tip amount must be greater than 0");
        
        creatorBalance[creator] += msg.value;
        emit TipSent(msg.sender, creator, msg.value);
    }
    
    function withdrawTips() external {
        require(isCreator[msg.sender], "Not a registered creator");
        uint256 amount = creatorBalance[msg.sender];
        require(amount > 0, "No tips to withdraw");
        
        creatorBalance[msg.sender] = 0;
        (bool success, ) = payable(msg.sender).call{value: amount}("");
        require(success, "Transfer failed");
        
        emit WithdrawnTips(msg.sender, amount);
    }
    
    function getCreatorBalance(address creator) external view returns (uint256) {
        return creatorBalance[creator];
    }
}