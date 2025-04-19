const solanaWeb3 = require('@solana/web3.js');
const fs = require('fs');


const secretKey = new Uint8Array([
    ##,###,###,###,###,###, ###, ###
]);

const wallet = solanaWeb3.Keypair.fromSecretKey(secretKey);

console.log(' Public Key:', wallet.publicKey.toString());

const connection = new solanaWeb3.Connection(
    solanaWeb3.clusterApiUrl('devnet'),
    'confirmed'
);

async function getBalance() {
    const balance = await connection.getBalance(wallet.publicKey);
    console.log(' Wallet Balance:', balance / solanaWeb3.LAMPORTS_PER_SOL, 'SOL');
}


async function airdrop() {
    const latestBlockhash = await connection.getLatestBlockhash();

    const airdropSignature = await connection.requestAirdrop(
        wallet.publicKey,
        solanaWeb3.LAMPORTS_PER_SOL * 2
    );

    await connection.confirmTransaction(
        {
            signature: airdropSignature,
            blockhash: latestBlockhash.blockhash,
            lastValidBlockHeight: latestBlockhash.lastValidBlockHeight
        },
        'confirmed'
    );

    console.log(' Airdrop successful! Signature:', airdropSignature);
}


async function main() {
    await airdrop();
    await getBalance();
}

main();
