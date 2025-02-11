import xml.etree.ElementTree as ET

#creating xml file

root = ET.Element("users")
user = ET.SubElement(root, "user",id="1")
user.text="Sanjeev"
tree = ET.ElementTree(root)





