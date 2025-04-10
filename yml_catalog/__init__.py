from typing import Any
from dataclasses import dataclass
from lxml import etree


@dataclass
class Category:
    id: str
    parentId: str
    text: str


@dataclass
class Offer:
    id: str
    name: str
    picture: str


class YmlCatalog:
    def __init__(self, name: str, company: str, url: str, platform: str) -> None:
        self.__yml_catalog = etree.Element("yml_catalog")
        self.__shop = etree.SubElement(self.__yml_catalog, "shop")
        self.__name = self.__init_name(text=name)
        self.__company = self.__init_company(text=company)
        self.__url = self.__init_url(text=url)
        self.__platform = self.__init_platform(text=platform)
        self.__categories = etree.SubElement(self.__shop, "categories")
        self.__offers = etree.SubElement(self.__shop, "offers")

    def __init_name(self, text: str) -> Any:
        element = etree.SubElement(self.__shop, "name")
        element.text = text
        return element

    def __init_company(self, text: str) -> Any:
        element = etree.SubElement(self.__shop, "company")
        element.text = text
        return element

    def __init_url(self, text: str) -> Any:
        element = etree.SubElement(self.__shop, "url")
        element.text = text
        return element

    def __init_platform(self, text: str) -> Any:
        element = etree.SubElement(self.__shop, "platform")
        element.text = text
        return element

    def load_categories(self, categories: list[Category]) -> None:
        for _ in categories:
            attrib = {"id": _.id}
            if _.parentId:
                attrib["parentId"] = _.parentId

            category = etree.SubElement(
                self.__categories,
                "category",
                attrib=attrib,
            )
            category.text = _.text

    def load_offers(self, offers: list[Offer]) -> None:
        for _ in offers:
            attrib = {"id": _.id}
            offer = etree.SubElement(
                self.__offers,
                "offer",
                attrib=attrib,
            )
            name = etree.SubElement(offer, "name")
            name.text = _.name

    def save_to_file(self, file_name: str = "yml_catalog.xml") -> None:
        doc = etree.ElementTree(self.__yml_catalog)
        doc.write(file_name, pretty_print=True, xml_declaration=True, encoding="utf-8")
