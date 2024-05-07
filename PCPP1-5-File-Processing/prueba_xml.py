### Pruebas con archivos XML

# import xml.etree.ElementTree as ET

# tree = ET.parse('books.xml')
# root = tree.getroot()

############ Parsear archivo xml

# import xml.etree.ElementTree as ET

# tree = ET.parse('books.xml')
# root = tree.getroot()
# print("My books:\n")
# for book in root:
#     print('Title: ', book.attrib['title'])
#     print('Author:', book[0].text)
#     print('Year: ', book[1].text, '\n')

########## Consulta como diccionario ##############

# import xml.etree.ElementTree as ET

# tree = ET.parse('books.xml')
# root = tree.getroot()
# print('The root tag is:', root.tag)
# print('The root has the following children:')
# for child in root:
#     print(child.tag, child.attrib)


####### Búsqueda recursiva para autor ############

# import xml.etree.ElementTree as ET

# tree = ET.parse('books.xml')
# root = tree.getroot()
# for author in root.iter('author'):
#     print(author.text)


######## Búsqueda de autores (por hijos, sólo un nivel por debajo) ##########################

# import xml.etree.ElementTree as ET

# tree = ET.parse('books.xml')
# root = tree.getroot()
# for author in root.findall('author'):
#     print(author.text)


########## Búsqueda de los títulos de los libros   ###############


# import xml.etree.ElementTree as ET

# tree = ET.parse('books.xml')
# root = tree.getroot()
# for book in root.findall('book'):
#     print(book.get('title'))

##### Método find() #####################
# Devuelve el primer elemento que contenga la etiqueta.

# import xml.etree.ElementTree as ET

# tree = ET.parse('books.xml')
# root = tree.getroot()
# print(root.find('book').get('title'))

########### Laboratorio con archivos XML ###############

# import xml.etree.ElementTree as ET


# class TemperatureConverter:
#     def convert_celsius_to_fahrenheit(self, temperature_in_celsius):
#         return 9.0/5.0 * temperature_in_celsius + 32


# class ForecastXmlParser:
#     def __init__(self, temperature_converter):
#         self.temperature_converter = temperature_converter

#     def parse(self, file):
#         tree = ET.parse(file)
#         root = tree.getroot()
#         for child in root:
#             day = child.find('day').text
#             temperature_in_celsius = int(child.find(
#                 'temperature_in_celsius').text)
#             temperature_in_fahrenheit = round(
#                 self.temperature_converter.convert_celsius_to_fahrenheit(
#                     temperature_in_celsius), 1)
#             print('{0}: {1} Celsius, {2} Fahrenheit'.format(
#                 day, temperature_in_celsius, temperature_in_fahrenheit))

# temperature_converter = TemperatureConverter()
# forecast_xml_parser = ForecastXmlParser(temperature_converter)
# forecast_xml_parser.parse('forecast.xml')


############# Modificar XML ####################################

# import xml.etree.ElementTree as ET

# tree = ET.parse('books.xml')
# root = tree.getroot()
# for child in root:
#     child.tag = 'movie'
#     print(child.tag, child.attrib)
#     for sub_child in child:
#         print(sub_child.tag, ':', sub_child.text)


######## Mod cont. ################

# import xml.etree.ElementTree as ET

# tree = ET.parse('books.xml')
# root = tree.getroot()
# for child in root:
#     child.tag = 'movie'
#     child.remove(child.find('author'))
#     child.remove(child.find('year'))
#     child.set('rate', '5')
#     print(child.tag, child.attrib)
#     for sub_child in child:
#         print(sub_child.tag, ':', sub_child.text)


#### cont. #####

# import xml.etree.ElementTree as ET

# tree = ET.parse('books.xml')
# root = tree.getroot()
# for child in root:
#     child.tag = 'movie'
#     child.remove(child.find('author'))
#     child.remove(child.find('year'))
#     child.set('rate', '5')
#     print(child.tag, child.attrib)
#     for sub_child in child:
#         print(sub_child.tag, ':', sub_child.text)

# tree.write('movies.xml', 'UTF-8', True)


######## Crear XML ##########################

# import xml.etree.ElementTree as ET

# root = ET.Element('data')
# movie_1 = ET.SubElement(root, 'movie', {'title': 'The Little Prince', 'rate': '5'})
# movie_2 = ET.SubElement(root, 'movie', {'title': 'Hamlet', 'rate': '5'})
# ET.dump(root)


######## Labortario. Crear XML ###########################

# import xml.etree.ElementTree as ET

# class XmlTreeHelper:
#     def add_tags_with_text(self, parent, tags):
#         elements = []
#         for tag in tags:
#             element = ET.SubElement(parent, tag)
#             element.text = tags[tag]
#             elements.append(element)
#         return elements

# root = ET.Element('shop')

# category = ET.SubElement(root, 'category', {'name': 'Vegan Products'})

# product_1 = ET.SubElement(category, 'product', {'name': 'Good Morning Sunshine'})
# product_2 = ET.SubElement(category, 'product', {'name': 'Spaghetti Veganietto'})
# product_3 = ET.SubElement(category, 'product', {'name': 'Fantastic Almond Milk'})

# xml_tree_helper = XmlTreeHelper()

# xml_tree_helper.add_tags_with_text(product_1, {
#     'type': 'cereals',
#     'producer': 'OpenEDG Foods Limited',
#     'price': '9.90',
#     'currency': 'USD'
# })

# xml_tree_helper.add_tags_with_text(product_2, {
#     'type': 'pasta',
#     'producer': 'Programmers Eat Pasta Gmbh',
#     'price': '14.49',
#     'currency': 'EUR'
# })

# xml_tree_helper.add_tags_with_text(product_3, {
#     'type': 'beverages',
#     'producer': 'Drinks4Coders Inc.',
#     'price': '19.75',
#     'currency': 'USD'
# })

# # ET.dump(root)

# tree = ET.ElementTree(root)
# tree.write('shop.xml', 'UTF-8', True)


##################################

