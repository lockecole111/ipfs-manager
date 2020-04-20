# ipfs-manager
A C/S based GUI tool for manage files in ipfs or ipfs private network.


## Client Useage

Writen in PyQt5  
first of all,start ipfs daemon.  
then,in Project root directory :  
edit config.json  
Fill in  account information(username and password),If you do n’t have an account, you can register one:  
```
curl -X POST -d "username=username&password=password" http://25oh.com:28000/ipfs/register
```
then,  
```shell
python3  client.py
```
## Server Deployment

Written in Django.  
in Project **server directory**:  
```shell
python3 manage.py makemigrations
python3 manage.py migrate
```
 
## Screenshots

![](https://github.com/lockecole111/ipfs-manager/blob/master/images/screenshot.png)

