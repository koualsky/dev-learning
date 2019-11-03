from lxml import etree

root = etree.Element('root')
etree.SubElement(root, 'child').text = 'Child 1'
etree.SubElement(root, 'child').text = 'Child 2'
etree.SubElement(root, 'child').text = 'Child 3'

print(etree.tostring(root, pretty_print=True))