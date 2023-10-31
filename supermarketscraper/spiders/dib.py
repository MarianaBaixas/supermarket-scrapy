from supermarketscraper.items import SupermarketItem
import datetime
import scrapy
import json

# <nome_subcategoria>?store_id=6971
categorias = ['alimentos-basicos/category/acucares-e-adocantes',
              'alimentos-basicos/category/arroz',
              'alimentos-basicos/category/cestas',
              'alimentos-basicos/category/farinaceos-e-amidos',
              'alimentos-basicos/category/feijao',
              'alimentos-basicos/category/graos',
              'alimentos-basicos/category/massas-secas',
              'alimentos-basicos/category/oleos-azeites-e-vinagres',
              'alimentos-basicos/category/ovos',
              'alimentos-basicos/category/sal',
              'bazar-e-utilidades/category/chinelos',
              'bebidas/category/aguas',
              'bebidas/category/bebidas-vegetais',
              'bebidas/category/chas-prontos',
              'bebidas/category/isotonicos-e-energeticos',
              'bebidas/category/refrigerantes',
              'bebidas/category/sucos',
              'bebidas-alcoolicas/category/cervejas',
              'bebidas-alcoolicas/category/destilados',
              'bebidas-alcoolicas/category/drinks-prontos',
              'bebidas-alcoolicas/category/vinhos',
              'biscoitos-e-salgadinhos/category/amendoins-e-cia',
              'biscoitos-e-salgadinhos/category/biscoitos-doces',
              'biscoitos-e-salgadinhos/category/biscoitos-salgados',
              'biscoitos-e-salgadinhos/category/salgadinhos-e-snacks',
              'carnes-aves-e-peixes/category/aves',
              'carnes-aves-e-peixes/category/bovinos',
              'carnes-aves-e-peixes/category/carnes-especiais',
              'carnes-aves-e-peixes/category/carnes-secas-salgadas-ou-defumadas',
              'carnes-aves-e-peixes/category/frutos-do-mar',
              'carnes-aves-e-peixes/category/linguicas-e-salsichas',
              'carnes-aves-e-peixes/category/peixes',
              'carnes-aves-e-peixes/category/suinos',
              'congelados/category/aperitivos-e-empanados',
              'congelados/category/hamburgueres',
              'congelados/category/paes-congelados',
              'congelados/category/pratos-prontos-congelados',
              'congelados/category/vegetais-congelados',
              'doces-e-sobremesas/category/balas-e-gomas',
              'doces-e-sobremesas/category/chocolates',
              'doces-e-sobremesas/category/doces-prontos',
              'doces-e-sobremesas/category/frutas-em-calda',
              'doces-e-sobremesas/category/ingredientes-culinarios',
              'doces-e-sobremesas/category/pudins-e-gelatinas',
              'doces-e-sobremesas/category/sorvetes-e-sobremesas',
              'feira/category/frutas',
              'feira/category/legumes',
              'feira/category/temperos-frescos',
              'feira/category/verduras',
              'frios-e-laticinios/category/frios',
              'frios-e-laticinios/category/laticinios',
              'frios-e-laticinios/category/massas-frescas',
              'frios-e-laticinios/category/queijos',
              'higiene-e-cuidados-pessoais/category/bebe',
              'higiene-e-cuidados-pessoais/category/cabelo',
              'higiene-e-cuidados-pessoais/category/corpo',
              'higiene-e-cuidados-pessoais/category/cuidados-com-a-saude',
              'higiene-e-cuidados-pessoais/category/higiene',
              'higiene-e-cuidados-pessoais/category/higiene-bucal',
              'higiene-e-cuidados-pessoais/category/maos-e-pes',
              'leites-e-iogurtes/category/iogurte-e-bebida-lactea',
              'leites-e-iogurtes/category/leites-em-po',
              'leites-e-iogurtes/category/leites-especiais',
              'leites-e-iogurtes/category/leites-tradicionais',
              'limpeza/category/casa-em-geral',
              'limpeza/category/desodorizadores-e-aromatizantes',
              'limpeza/category/detergentes-e-desengordurantes',
              'limpeza/category/inseticidas-e-controle-de-pragas',
              'limpeza/category/roupas',
              'limpeza/category/utensilios-de-limpeza',
              'matinais/category/achocolatados-e-cia',
              'matinais/category/aveias-e-cereais',
              'matinais/category/cafes',
              'matinais/category/chas',
              'matinais/category/mel-e-geleias',
              'matinais/category/pastas-e-cremes-doces',
              'matinais/category/torradas',
              'molhos-condimentos-e-conservas/category/alimentos-prontos-e-enlatados',
              'molhos-condimentos-e-conservas/category/conservas',
              'molhos-condimentos-e-conservas/category/maioneses-e-molhos-diversos',
              'molhos-condimentos-e-conservas/category/molhos-de-tomate',
              'molhos-condimentos-e-conservas/category/sopas-e-cremes',
              'molhos-condimentos-e-conservas/category/temperos-e-caldos',
              'padaria/category/bolos-e-tortas',
              'padaria/category/confeitaria',
              'padaria/category/fermentos',
              'padaria/category/paes',
              'utensilios-para-o-lar/category/automotivos',
              'utensilios-para-o-lar/category/churrasco',
              'utensilios-para-o-lar/category/conveniencias',
              'utensilios-para-o-lar/category/cozinha',
              'utensilios-para-o-lar/category/embalagens-e-descartaveis',
              'utensilios-para-o-lar/category/jardinagem',
              'utensilios-para-o-lar/category/utensilios-diversos']
departamento = {'Bebidas': ('Bebidas', 'Bebidas Alcoólicas'),
                'Biscoitos, Doces e Matinais': ('Biscoitos e Salgadinhos', 'Doces e Sobremesas', 'Matinais'),
                'Carnes': ('Carnes, Aves e Peixes'),
                'Congelados': ('Congelados e Resfriados'),
                'Hortifruti': ('Feira'),
                'Frios e Laticínios': ('Frios e Laticínios', 'Leites e Iogurtes'),
                'Higiene': ('Higiene e Cuidados Pessoais'),
                'Limpeza': ('Limpeza'),
                'Mercearia': ('Alimentos Básicos', 'Molhos, Condimentos e Conservas'),
                'Padaria': ('Padaria'),
                'Utilidades e Pet': ('Bazar e Utilidades', 'Utensílios para o Lar')}

class DibSpider(scrapy.Spider):
    name = "dib"
    start_urls = [
        "https://www.sitemercado.com.br/dibsupermercados/petropolis-dib-supermercados-castelanea-r-olavo-bilac"]

    def parse(self, response):
        for elemento in range(len(categorias)):
            url = f"https://ecommerce-backend-wl.sitemercado.com.br/api/b2c/product/department/{categorias[elemento]}?store_id=6971"
            headers = {
                "Accept": "application/json, text/plain, */*",
                "Hosturl": "www.sitemercado.com.br",
                "Sec-Ch-Ua": "'Google Chrome';v='117', 'Not;A=Brand';v='8', 'Chromium';v='117'",
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": "Windows",
                "Sm-Token": "{'Location':{'Latitude':-22.4289697,'Longitude':-42.9821471},'IdClientAddress':0,'IsDelivery':false,'IdLoja':6971,'IdRede':2291,'DateBuild':'2023-09-15T10:30:20.9639004'}",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
            }
            yield scrapy.Request(url, callback=self.parse_api, headers=headers)

    def parse_api(self, response):
        data = json.loads(response.body)
        product_item = SupermarketItem()

        for product in data['products']:
            if product['price_old'] != 0:
                valor = str(product['department'])
                rotulo = self.encontrar_rotulo(valor, departamento)

                product_item['nome'] = product['excerpt']
                product_item['preco_original'] = product['price_old']
                product_item['preco_oferta'] = product['prices'][0]['price']
                product_item['img_pequena'] = product['image']
                product_item['img_grande'] = product['imageFull']
                product_item['departamento'] = rotulo
                product_item['mercado'] = 'Dib'
                product_item['url'] = 'https://www.sitemercado.com.br/dibsupermercados/petropolis-dib-supermercados-castelanea-r-olavo-bilac/produto/' + product['url']
                product_item['data'] = datetime.date.today()

                yield product_item

    def encontrar_rotulo(self, valor, departamento):
        for rotulo, valores in departamento.items():
            if valor in valores:
                return rotulo
        return None
