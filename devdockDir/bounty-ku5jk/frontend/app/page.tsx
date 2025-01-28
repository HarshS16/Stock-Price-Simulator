"use client";

import { useState } from 'react';
import { useAccount, useContractWrite, useContractRead } from 'wagmi';
import { parseEther } from 'viem';
import { CONTRACT_ADDRESS, CONTRACT_ABI } from '../config/constants';

export default function Home() {
  const [tipAmount, setTipAmount] = useState('');
  const [creatorAddress, setCreatorAddress] = useState('');
  const { address } = useAccount();

  const { write: registerAsCreator } = useContractWrite({
    address: CONTRACT_ADDRESS,
    abi: CONTRACT_ABI,
    functionName: 'registerAsCreator',
  });

  const { write: sendTip } = useContractWrite({
    address: CONTRACT_ADDRESS,
    abi: CONTRACT_ABI,
    functionName: 'sendTip',
  });

 useContractRead({
    address: CONTRACT_ADDRESS,
    abi: CONTRACT_ABI,
    functionName: 'getCreatorBalance',
    args: [address],
  });

  return (
    <div className="min-h-screen bg-gray-100 py-6 flex flex-col justify-center sm:py-12">
      <div className="relative py-3 sm:max-w-xl sm:mx-auto">
        <div className="relative px-4 py-10 bg-white shadow-lg sm:rounded-3xl sm:p-20">
          <div className="max-w-md mx-auto">
            <div className="divide-y divide-gray-200">
              <div className="py-8 text-base leading-6 space-y-4 text-gray-700 sm:text-lg sm:leading-7">
                <h2 className="text-2xl font-bold mb-8">Social Tipping Platform</h2>
                
                <button
                  onClick={() => registerAsCreator()}
                  className="bg-blue-500 text-white px-4 py-2 rounded"
                >
                  Register as Creator
                </button>

                <div className="mt-8">
                  <input
                    type="text"
                    placeholder="Creator Address"
                    value={creatorAddress}
                    onChange={(e) => setCreatorAddress(e.target.value)}
                    className="w-full p-2 border rounded"
                  />
                  <input
                    type="number"
                    placeholder="Tip Amount (ETH)"
                    value={tipAmount}
                    onChange={(e) => setTipAmount(e.target.value)}
                    className="w-full p-2 border rounded mt-2"
                  />
                  <button
                    onClick={() => sendTip({
                      args: [creatorAddress],
                      value: parseEther(tipAmount),
                    })}
                    className="bg-green-500 text-white px-4 py-2 rounded mt-2"
                  >
                    Send Tip
                  </button>
                </div>

                {creatorBalance && (
                  <div className="mt-4">
                    <p>Your Creator Balance: {creatorBalance.toString()} ETH</p>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}