# python-keylogger
A minimal keylogger that accurately track keyboard strokes made in Python

Improved by Shahar Sar Shalom 

Changes: 
* Doesn't print the output to the screen
* Save the key logs to different file on every execution 
* solve crashes - now support enter keyword 


Getting started !
-----------------

Clone | Download the Repository => then open a terminal | command prompt to your project, and then run the **app.py** script and your keylogger should up spying on every keystroke you will ever write 

```bash
git clone https://github.com/Kalebu/python-keylogger
cd python-keylogger
python app.py
```

keylogs.txt
------------

A keylogger will automatically open a new file on your project directory and then start storing yours keys, to change the filename, or directory to store the logs, open the script and then adjust the filename at the bottom of script just as illustrated below;

```python
if __name__ == '__main__':
    logger = KeyLogger(filename="path-to-logs-file.txt')
    logger.main()
    input()
```

Credits
-------

All the credits to [kalebu](https://github.com/Kalebu)

