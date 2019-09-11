import re

content = 'Hello 123 4567 World_This is a Regex Demo'
# match函数从头开始匹配
result = re.match('Hello', content)
print(result)
# ()里面的东西时group(1)开始
result = re.match('Hello\s(\d+)\s(\d+)\sWorld', content)
print(result.group(0))
print(result.group(1))
print(result.group(2))
print(result.span())
# .匹配任意一个字符,*匹配前面字符的无限次数
# .为贪婪模式,尽可能多的匹配字符,使用.?  .*?拒绝贪婪模式,尽可能少的匹配字符
result = re.match('^Hello.*Demo$', content)
print(result)

# 加入re.S可以让.匹配换行符,加入re.I匹配对大小写不敏感
content = '''Hello 123456 World_This
is a Regex Demo'''
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
print(result.group(1))

# 要使用的匹配字符在表达式中有含义需要使用\转义



# search()匹配整个字符串,返回第一个成功匹配的结果
content = 'Auto Hello 1234567 World_This is a Regex Demo'
result = re.search('He.*?(\d+).*Demo$', content)
print(result)
# findall() 匹配整个字符串, 返回匹配规则的所有内容
# sub() 返回替换结果
strs = '123jio2j3oi21j3io12j3ioj21oi3j'
strs = re.sub('\d+','', strs)
print(strs)


html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''

result = re.findall('<li.*?>(\s<a href=".*?" singer=".*?">)?(.*?)(</a>\s)?</li>', html, re.S)
print(result)

result = re.sub('\s?<a.*?>|</a>\s?', '', html)
result = re.findall('<li.*?>(.*?)</li>', result, re.S)
print(result)


# compile() 将正则字符串编译成正则表达式对象 便以复用


# 多种匹配方式

