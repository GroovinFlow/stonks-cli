# stonks-cli
Commission-free investing in stocks &amp; crypto

Hey, want to be a real sigma grinder and invest in crypto or stocks but you don't have any funds. Well you can test your speculation skills using this epic client. Powered using the newest stock tracker ever created - finance yahoo. Client offers a true linux terminal expierience so you can feel like a true hacker man then showing your m8'es your +420% portfolio.  

![Screenshot from 2022-07-27 01-41-22](https://user-images.githubusercontent.com/52932313/181632683-b06b14cf-ea9a-46ca-84ee-1e9794d1fe6f.png)

## Install
Beware this only works for linux 
```
sudo apt install python3
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
sudo rm "/usr/local/bin/stonks-cli" && sudo rmdir /home/$USER/stonks-cli
```
