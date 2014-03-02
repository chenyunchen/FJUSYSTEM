#FJUSYSTEM

##For Fu Jen Catholic University 
Only use in telnet://signcourse.fju.edu.tw
This is a system for student easy to get course.

## About My Code

The FJU signcouse system is base on BIG5.
So we have to make encode and decode first before typing chinese.

```python
def big5(str):
    return str.decode('utf-8', 'ignore').encode('big5', 'ignore')
```

I use "i" "m" "k" to instead up、down right.
Because there is a bug "left" in signcourse system,so I use right only.

```python
def up(num):
    for i in range(num):
        tn.write("i")
def down(num):
    for i in range(num):
        tn.write("m")
def right(num):
    for i in range(num):
        tn.write("k")
```

Python have a library to help you connect with telnet.
We can give Host to it and use some function.

```python
import telnetlib
tn = telnetlib.Telnet(HOST)
```

We have to wait for connect so use read_until to check when we get the information.
tn.read_ver_eager can return the string what you get on the page.
tn.write() can send your command to the host.

```python
tn.read_until("login",10)
tn.read_very_eager()
tn.write()
```

By the way, to avoid sending the command too fast when the page don't take back yet,
we have to make delay to stop the program to wait for the information

```python
time.sleep(0.5)
```
