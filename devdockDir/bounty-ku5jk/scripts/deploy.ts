import { ethers } from "hardhat";

async function main() {
  const SocialTipping = await ethers.getContractFactory("SocialTipping");
  const socialTipping = await SocialTipping.deploy();
  await socialTipping.deployed();

  console.log(`SocialTipping deployed to ${socialTipping.address}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});