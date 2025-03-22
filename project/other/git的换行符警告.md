```
warning: in the working copy of 'project/web/python crawler/Practical project - crawling school schedule/schedule.ipynb', LF will be replaced by CRLF the next time Git touches it
```
其实核心就是LF will be replaced by CRLF the next time git touchs it <br>
所有这个是什么意思呢？其实报错的原因就是在这个文件中间，应该是有空的换行符，这样的情况下.
```
这个警告信息是告诉你， Git 在处理文件时会将行尾的换行符从 LF （Line Feed，通常在 Unix / Linux 系统中使用）替换为 CRLF （Carriage Return and Line Feed，通常在 Windows 系统中使用）
```
line feed 换行。这个要记住
carriage return and line feed 回车换行。

从这个地方其实可以看到，linux和windows中对于换行的处理其实是完全不一样的。

## liunx 和 win 中换行的区别
在Windows系统中，一个换行往往是由一个回车符和一个换行符组成的序列（"\r\n"），而在Unix/Linux系统中，只使用换行符（"\n"）

其实电脑的核心还是要存储数据的，所以文本末的换行符其实也是要被存储起来，这样的话不同的系统自然有不同的方式存储。理解上面的话其实就是转化成二进制存储的时候，对于换行的不同理解。然后git的这个警告就是告诉我们，它可以自动的处理这个区别，我们无需主动的告诉他。其实这样一看，就能理解为什么win是carriage return 回车 line feed 换行
因为 存储的方式是 \r \n