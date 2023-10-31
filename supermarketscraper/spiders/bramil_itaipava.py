from supermarketscraper.items import SupermarketItem
import datetime
import scrapy
import json

# em_oferta
categorias = ['19', '1', '46', '53', '78', '98',
              '113', '136', '157', '179', '194', '205', '216']
bearer = ['M4NDQsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiNTMifQ.oZ2mzPPfw-zccpHylJNmx72UEfTeD_ZEkTEmf45LwQPYlbvUP3jVd8e8FLwTqkOMUujPAK4jTRjyAsgzdhFKeQ',
          'QyNDgsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiNTMifQ.gOWEJcM63JlwbAMvPsuUVkBND0Ax_d6nFb7lLcpzVV4io-hejpc8vS46-ApXLE1sIvjVFs-1X9FKGYQT4O4T9A',
          'M4OTksInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiNTMifQ.LFkyrBW73mcpikbV48MzklPkeCztHtqKKkESsD71k5q-TidZswUcXOAmEG5eIuaQghVw0RFi6ykxnbha8v5R6w',
          'M5MTYsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiNTMifQ.94fUJ3VOCs4D1IxLRmggQ8ZHpJ3rWzkFd5AIxY3NL8FDJthb8sL5z9LkXn2LrtESNwkAfBy8XtYFX-55J0_Tow',
          'M5MjksInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiNTMifQ.rGkQXDAuPe2yBXjcazYgSyrTPka0O4Sy4MxuFhl_sfP0rePB0XRbLPwhh9cGeKdJRglyWxG2GIOiYOHglgXP_g',
          'M5MzcsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiNTMifQ.7gzg7o7DwBpPFq7MYC2euopb-5tB9V5JrJpdWSLL0ROz2l3JfkjKyVESXnyFCv40iWwNLk2napWk_UoyER_Q5g',
          'M5NDEsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiNTMifQ.4Mf1kcrx0nW3ttQiUF0BjmeS3mwSJYxnn_h9vBlvdY8IOzi_-x5HJ8J3txWdtyTEqLAsAx6EeRomeX3c68nEIw',
          'M5NTMsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiNTMifQ.2WTOc9ImhsppKtXkq3nT-WCSdrp1LYhllngll8cK-l7J2rRPUvGge6FD2jCExm9jsi121g6Lapd6ucToHWhoMA',
          'M5NTYsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiNTMifQ.e6zYofejkHCHbP3VhIapGjrL_lTbc8v6cRFA4dKlzfcthruJEY7xO566GiZTJFS7qFgptTIwh-kWVcTizV6HLQ',
          'M5NjYsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiNTMifQ.u07dMBn7z32_Ig8AHRIuiVt9Cj4EN2QVo80eMVeDm9mAQWY_NlAMoYhpw7ZrTycBJz3WHVbwCsiucGPhMLCuXQ',
          'M5NzAsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiNTMifQ.X3nutGcKD39OblO3S8UQeTPBPbHTdo2SdP-xl96ckrPSgDyIUyDcFLz2-xQUHzvFmJ8OLgzh3Yrisf0Mvd3wXw',
          'M5NzgsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiNTMifQ.ZSDFhlE6fE4Tb8Qo-QOn-q4rpxbmpKm4fDxPfUMRHc8RNNdMJi6QWCSYEmGdJ1yOJhgiXoXAhNqhOkE4rSrMGg',
          'M5ODQsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiNTMifQ.vFP2JWOyU3KqOW-411NtKbfgls_hPu4QkUhixmrpmLdAuFhqtbLHJafEqUoH5Id3zH82YRcUTEnxQFrFal6fXg']
departamento = {'Bebidas': ('79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97'),
                'Biscoitos, Doces e Matinais': ('137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '175', '176', '177', '178'),
                'Carnes': ('206', '207', '208', '209', '210', '211', '212', '213', '214', '215'),
                'Congelados': ('195', '196', '197', '198', '199', '200', '201', '202', '203', '204'),
                'Hortifruti': ('217', '218', '219', '220', '221'),
                'Frios e Laticínios': ('180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '193'),
                'Higiene': ('20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '36', '37', '38', '39', '40', '41', '42', '43', '44'),
                'Limpeza': ('2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18'),
                'Mercearia': ('99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135'),
                'Utilidades e Pet': ('47', '48', '49', '50', '51', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77')}


class BramilItaipavaSpider(scrapy.Spider):
    name = "bramil_itaipava"
    start_urls = ["https://www.bramilemcasa.com.br/"]

    def parse(self, response):
        for elemento in range(len(categorias)):
            for pagina in range(1, 4):
                url = f"https://api-loja.bramilemcasa.com.br/v1/loja/classificacoes_mercadologicas/departamentos/{categorias[elemento]}/produtos/filial/1/centro_distribuicao/15/em_oferta?page={pagina}"
                headers = {
                    "Accept": "application/json",
                    "Authorization": f"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJ2aXBjb21tZXJjZSIsImF1ZCI6ImFwaS1hZG1pbiIsInN1YiI6IjZiYzQ4NjdlLWRjYTktMTFlOS04NzQyLTAyMGQ3OTM1OWNhMCIsInZpcGNvbW1lcmNlQ2xpZW50ZUlkIjpudWxsLCJpYXQiOjE2OTUwNz{bearer[elemento]}",
                    "Content-Type": "application/json",
                    "Organizationid": "53",
                    "Referer": "https://www.bramilemcasa.com.br/",
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

        for product in data['data']:
            if product["disponivel"] == True:
                valor = str(product['classificacao_mercadologica_id'])
                rotulo = self.encontrar_rotulo(valor, departamento)

                product_item['nome'] = product['descricao']
                product_item['preco_original'] = product['oferta']['preco_antigo']
                product_item['preco_oferta'] = product['oferta']['preco_oferta']
                product_item['img_pequena'] = 'https://s3.amazonaws.com/produtos.vipcommerce.com.br/144x144/' + product['imagem']
                product_item['img_grande'] = 'https://s3.amazonaws.com/produtos.vipcommerce.com.br/250x250/' + product['imagem']
                product_item['departamento'] = rotulo
                product_item['mercado'] = 'Bramil Itaipava'
                product_item['url'] = 'https://www.bramilemcasa.com.br/produtos/detalhe/' + \
                    str(product['produto_id']) + '/' + product['link']
                product_item['data'] = datetime.date.today()

                yield product_item

        paginas = data['paginator']['total_pages']

    def encontrar_rotulo(self, valor, departamento):
        for rotulo, valores in departamento.items():
            if valor in valores:
                return rotulo
        return None
