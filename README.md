UPDATE - Lottery results available
==================================

Dear everyone in the IoP Community. This is the moment all of you have been waiting for. We have now uploaded both the final registration data and the lottery results. The registration data is found [here](src/data/registration.json) and is sorted by IOP address, so you can easily verify that your addresses have been properly registered. Using the signatures, everyone can verify that all IOP addresses were actually registered by none other than their owner.

The results of the lottery are found [here](src/data/lottery_results.json). These results can also be reproduced by everyone using [this Python3 script](src/data/hydra_lottery.py). We congratulate the owner of the ETH address `0xc61A15639602e0BfD3d79E699001A03b734d179d`, who has won the incredible amount of 15710 HYD (you seem to have a lot of addresses). Everyone else can be happy as the average winning was 2283.11 HYD and no one won less than 7 HYD. The median amount was 2167 HYD.

For everyone interested in the inner workings of our lottery, we give here a short description of the system we are modeling: 

Imagine walking up to a ticket booth for the lottery. A ticket costs 2 IOP, and no one is allowed to buy more than 250 tickets at a time. As a bonus, everyone buying tickets is awarded 1 HYD immediately. Of course, if you come back later with a fake moustache and sunglasses, or buy tickets at another booth, you succesfully tricked the system. Shame on you! On each ticket you buy is written a number, and the tickets are ordered. So if you buy 35 tickets, and your first ticket is no. 439, your last ticket will be no. 473. 

Now comes the day of the lottery drawing and the booths are all closed. For every ticket sold, a corresponding numbered ball is thrown into a big bowl and mixed wildly. Now, a random ball is drawn from the bowl. The owner of the corresponding ticket is awarded 1 HYD (someone writes this down, of course), and the ticket is thrown back into the bowl, which is then again mixed randomly (this rewards participants with fewer IOP, as their chances would shrink dramatically by losing one ticket, while people with hundreds of tickets could care less about one of them). This is repeated for all of the remaining Hydra---remember, a few hundred of the 500k HYD have already been given out to the participants when registering.


UPDATE - Registration closed
============================

The registration for the Hydra Lottery closed as planned on Friday, December 22, 2:00 PM UTC. Thank you all for participating. After we extract all relevant information from the registration database, we will present the registration data together with the lottery results.

Stay tuned!


First Hydra Airdrop
===================

Dear IOP Community,

Registration for the first Hydra airdrop has opened on Sunday, December 17, 2:00 PM UTC. To give everyone in the community a fair chance to get some Hydra, we are not distributing a fixed amount of Hydra per IOP.

Instead, we’re running a lottery.

To take part, you need a valid Ethereum address **that you have the private key for** to receive your Hydra tokens. You can register for the lottery using the IoPCommunityBot in our official [Telegram Channel](https://t.me/IoPofficial). It is best to talk to the bot using private messages, so people can use the channel for asking questions. The command used for registering an IOP address is `/%register YOUR_IOP_ADDRESS YOUR_ETH_ADDRESS SIGNATURE`. In this, `YOUR_IOP_ADDRESS` is the IOP address you want to register and `YOUR_ETH_ADDRESS` is the address you want to receive the Hydra on. `SIGNATURE` is generated by using the *Sign Message* function of your IoP Core wallet. Enter your Ethereum address in the message field, without any other symbols or whitespace. Choose the IOP address you want to register and click *Sign*. Copy the resulting signature into the command for the telegram bot. This is used to verify that you indeed own the IOP address you want to register.

A very helpful videos has been uploaded to our official Internet of People YouTube Channel, explaining how to [register for the first Hydra Airdrop](https://youtu.be/hvMySKfQZ7Q).

When you register one of your IOP addresses for the lottery, you will be credited 1 ticket for every 2 full IOP in your account when we took the snapshot on Sunday, December 10, 7:00 PM UTC at Block 71417, up to a maximum of 250 tickets per IOP address. 

If you find an address is credited with fewer tickets than expected, please remember that your wallet generates change addresses everytime you send a transaction. Depending on their balance, these addresses might also be eligible. You can get a list of all addresses in your wallet--including change addresses--by running `listaddressgroupings` in the console found in your IOP Core Wallet under *Help->Debug Window->Console*. To find out which of these is eligible for registration, you can compare them against the snapshot data [here](src/data/snapshot.json). 

Registration will be open until Friday, December 22, 2:00 PM UTC. After registration closes, we will update this repository with the full registration data. 

The code for the lottery is already online and can be used by everyone to validate the result. Please be aware that the results of the lottery will only be fixed once registration is complete.

# FAQ

If you still have questions, you should be able to find the answers here.

**Q**: What is an airdrop?
**A**: An airdrop is a distribution of free cryptocurrency to holders of a different currency. It’s a way to establish a broad base of token holders, reward a certain group of people or just generate buzz for a new token.

**Q**: Does it cost anything?
**A**: No, an airdrop is a free gift.

**Q**: Why is this airdrop happening? Who is it for?
**A**: To celebrate the long-standing partnership between IoP and Libertaria, Libertaria is rewarding members of the IoP community with a free gift of Hydra, Libertaria’s new cryptotoken.

**Q**: What is Hydra?
**A**: Hydra is Libertaria’s new cryptotoken. Eventually it will run on Libertaria’s new Hydra blockchain protocol, but for now it is an ERC20 token on the Ethereum blockchain. The address of the contract is 0xd233495c48eb0143661ffc8458eafc21b633f97f, the Token symbol is **HYD**.

**Q**: How many Hydra tokens are being airdropped?
**A**: 500,000 Hydra tokens are being distributed in this airdrop.

**Q**: Is everyone eligible to receive free Hydra tokens?
**A**: No, only IOP addresses containing 2 IOP or more as of block 71417 (Sunday, December 10, 7:00 PM UTC) are eligible for this airdrop. However, more airdrops are planned for the near future, so keep hodling!

**Q**: Will every eligible address receive free Hydra tokens?
**A**: No, tokens will be distributed via a random lottery. However, the chance to go empty-handed is almost zero.

**Q**: So everyone has the same chance of receiving tokens?
**A**: Not exactly. The airdrop is being run as a lottery. You can receive tickets based on the number of IOP tokens you own. IOP holders are eligible for one lottery entry for every 2 IOP they hold, up to a maximum of 250 tickets (per address).

**Q**: Can I do anything to increase my chances?
**A**: Not any more. The distribution of tickets will be based on a snapshot of the IoP blockchain taken at block 71417 and is now fixed.

**Q**: Can I receive Hydra from my IOP on Bittrex?
**A**: No, you cannot receive Hydra tokens based on Bittrex holdings. Only IOP addresses for which you own the private keys are eligible to register for the lottery.

**Q**: What do I need to register my address?
**A**: You’ll need an eligible IOP address, an Ethereum wallet address for a wallet supporting ERC20 tokens and an IOP wallet capable of signing a message using the private key for the eligible IOP address. The official IoP Core wallet is perfect for this, exchange addresses are NOT :)

**Q**: Which wallets support ERC20 tokens?
**A**: There are several options, but we recommend MyEtherWallet.com. We have created a short instruction video explaining how to set up a wallet address in MEW.

**Q**: How do I register my address?
**A**: You can register your address in our official IoP Token telegram channel by messaging our bot. The bot also accepts direct messages.

**Q**: The bot says I need a signature. What’s that?
**A**: We need a cryptographic signature to verify that you own the IoP address you’re trying to register. In your IoP core wallet, select “Sign Message” from the File menu. Paste the eligible IoP address in the top bar and your ETH address in the message box. Click the Sign Message button and the signature will be generated. You can use the Copy button to the right of the signature to copy it to the clipboard.

**Q**: I’m pretty sure I had an eligible amount of tokens in an eligible IOP address at the time of 71417. However, when I try to register the address with the bot I get a message saying “That IoP address isn't on the list of IoP addresses eligible for this airdrop. Sorry.” Why am i getting that message?

**A**: First check [this list](src/data/snapshot.json) for the address. If it’s not in the list, don’t worry. It may have been stored in a different address than you think. Go to *Help->Debug Window->Console*, enter `listaddressgroupings` and hit return. In the console window you will see all the addresses that the wallet used for your transactions. Check that list against the first list and you should find the tokens you’re looking for.gi
