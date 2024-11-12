import xml.etree.ElementTree as ET

# Load and parse each XML file
astro_tree = ET.parse('./Astro.xml')
sg_tree = ET.parse('./SG.xml')
# unifi_tree = ET.parse('./EPG/unifi.xml')
chn_tree = ET.parse('./CHN.xml')

# Get the root elements of each file
astro_root = astro_tree.getroot()
sg_root = sg_tree.getroot()
# unifi_root = unifi_tree.getroot()
chn_root = chn_tree.getroot()

# Create a new XML root for the merged document
merged_root = ET.Element('tv')

# Function to append channels and programmes to the merged root
def append_elements(src_root):
    for child in src_root:
        if child.tag in ['channel', 'programme']:
            merged_root.append(child)

# Append channels and programmes from each file
append_elements(astro_root)
append_elements(sg_root)
# append_elements(unifi_root)
append_elements(chn_root)

# Write the merged XML to a new file
merged_tree = ET.ElementTree(merged_root)
merged_tree.write('./EPG.xml', encoding='UTF-8', xml_declaration=True)
