# stonks-cli
Commission-free investing in stocks &amp; crypto

Hey, want to be a real sigma grinder and invest in crypto or stocks but you don't have any funds. Well you can test your speculation skills using this epic client. Powered using the newest stock tracker ever created - finance yahoo. Client offers a true linux terminal expierience so you can feel like a true hacker man then showing your m8'es your +420% portfolio.  

![Screenshot from 2022-08-13 18-56-02](https://user-images.githubusercontent.com/52932313/184501599-c2bd7f66-0646-4c51-b5cb-4fc4b4cdf0a9.png)

## Install for linux 
Make sure python is installed
```
sudo apt install python3
```
Client installation
```
cd /home/$USER && git clone https://github.com/ProfMad/stonks-cli && cd ./stonks-cli
sudo mv ./stonks-cli /usr/local/bin
```
## Usage
Basic functions:
* Add investment
* Remove investment
* Change tax procentage
* Synch investments
* Show investments from local cache

Note: Investments can be edited manually (use any editor you like)
```
sudo gedit /home/$USER/stonks-cli/stocks.json
``` 

## Uninstall
```
sudo rm "/usr/local/bin/stonks-cli" && sudo rm -rf /home/$USER/stonks-cli
```
