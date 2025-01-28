export const CONTRACT_ADDRESS = "YOUR_DEPLOYED_CONTRACT_ADDRESS";

export const CONTRACT_ABI = [
  "function registerAsCreator() external",
  "function sendTip(address creator) external payable",
  "function withdrawTips() external",
  "function getCreatorBalance(address creator) external view returns (uint256)",
  "event CreatorRegistered(address creator)",
  "event TipSent(address indexed from, address indexed to, uint256 amount)",
  "event WithdrawnTips(address indexed creator, uint256 amount)"
];