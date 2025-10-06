import yaml
import xml.etree.ElementTree as ET

with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)
    rss_element = ET.Element('rss', version='2.0')