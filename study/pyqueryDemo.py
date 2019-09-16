html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
         <div>
            <a> a标签</a>
         </div>
     </ul>
 </div>
 <div id="c">
    <ul class="list">
         <li class="fd">first item</li>
    </ul>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
print(type(doc))


item = doc('li')
print(type(item))
print(item)


item = doc('#container').children()
print(item)

item = item.parent()
print(item)

print('+++++++++++++')
item = doc('.fd')
print(item)
print('________')
print(type(item.parents()))
print(item.parents())
print(')))))))))))))))))))')
print(item.parents().find('li'))
print(item.parents().find('li').text())