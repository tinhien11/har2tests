# Convert .har file to unittest
## Install
```bash
pip3 install install git+https://github.com/tinhien11/har2tests.git --user
```
### Save .har file from Chrome
![](/img1.jpg?raw=true "")


### Convert .har file to test file
```bash
python3 -m har2tests localhost.har > test.py
```
### Run test case
```bash
python3 -m unittest
```