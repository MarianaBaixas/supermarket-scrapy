# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from . import config
import psycopg2
from itemadapter.adapter import ItemAdapter
from scrapy.exceptions import DropItem


class DuplicatesPipeline:
    def __init__(self):
        self.seen_items = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        # Crie uma tupla com o nome e o preco_oferta
        item_key = (adapter["nome"], adapter["preco_oferta"])

        if item_key in self.seen_items:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.seen_items.add(item_key)
            return item


class SupermarketscraperPipeline:
    def __init__(self):
        # Use as configurações para conectar ao PostgreSQL
        POSTGRES_USER = config.POSTGRES_USER
        POSTGRES_PASSWORD = config.POSTGRES_PASSWORD
        POSTGRES_HOST = config.POSTGRES_HOST
        POSTGRES_DB = config.POSTGRES_DB

        # Create/Connect to database
        self.connection = psycopg2.connect(
            host=POSTGRES_HOST, user=POSTGRES_USER, password=POSTGRES_PASSWORD, dbname=POSTGRES_DB)

        # Create cursor, used to execute commands
        self.cur = self.connection.cursor()

    def process_item(self, item, spider):
        # Define insert statement
        self.cur.execute(
            f"INSERT INTO teste (nome, preco_original, preco_oferta, img_pequena, img_grande, departamento, mercado, url, data) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (item['nome'], item['preco_original'], item['preco_oferta'], item['img_pequena'],
                item['img_grande'], item['departamento'], item['mercado'], item['url'], item['data'])
        )

        # Execute insert of data into data base
        self.connection.commit()
        return item

    def close_spider(self, spider):
        # Close cursor & connection to database
        self.cur.close()
        self.connection.close()
