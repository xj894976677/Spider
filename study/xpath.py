from lxml import etree
text='''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)#调用HTML类 初始化 构造一个XPath解析对象
result = etree.tostring(html)#输出 HTML代码
print(result.decode('utf-8'))#结果为bytes类型 用decode方法转化为str类型