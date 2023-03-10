# Вам дано описание пирамиды из кубиков в формате XML.
# Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
# Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

# Пример:

# <cube color="blue">
#   <cube color="red">
#     <cube color="green">
#     </cube>
#   </cube>
#   <cube color="red">
#   </cube>
# </cube>
 
# Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1. Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д.

# Ценность цвета равна сумме ценностей всех кубиков этого цвета.

# Выведите через пробел три числа: ценности красного, зеленого и синего цветов.

# Sample Input:

# <cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>

# Sample Output:

# 4 3 1

  
  
from xml.etree import ElementTree


def getChild(root, lvl):
    lvl += 1
    for child in root:
        colors[child.attrib['color']] = colors.get(child.attrib['color']) + lvl
        getChild(child, lvl)


root = ElementTree.fromstring(input())

colors = {'blue': 0, 'red': 0, 'green': 0}
level = 1
colors_str = []

colors[root.attrib['color']] = colors.get(root.attrib['color']) + 1

getChild(root, level)
colors = sorted(colors.items(), key=lambda x: x[0],  reverse=True)

for elem in colors:
    print(elem[1], end=' ')
