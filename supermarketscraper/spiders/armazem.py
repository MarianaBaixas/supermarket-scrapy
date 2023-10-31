from supermarketscraper.items import SupermarketItem
import datetime
import scrapy
import json

# em_oferta
categorias = ['232', '233', '234', '242', '235', '236', '237',
              '3', '24', '111', '36', '14', '238', '5', '240', '239', '241']
bearer = ['M4OTksInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiODEifQ.BV0F_rG31mhr_H9YcRazBGtQcu-v5yvVF9a1oDe0M5F3uC_mKpJw1mqF90ngHGwgsi3zmodA_-fbGINrRNMPpg',
          'QzNDAsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiODEifQ.Ow84kQ3xtLGn8WCtnAk59x10A0lmCViFABGkF09DPZ3WBI5qu51E-LfsJDKtuQAhFmLrGqnsYU6IWfVi5Pmb-A',
          'Q0NTgsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiODEifQ.qLWUgPlLwcAFYy0c2uTFo0E2gTZ7ggSXCUkm1_g6-DnPB80jIhbbFI0cj2Dw1m3LhJ86inj7xS_tKuWoM8tYJg',
          'Q1MzAsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiODEifQ.5LViqtEd8a6mGDieJtDfsnso6IFN8ild7iWCfOfPR2tf4IDZLFUsZFW64kW-6PbkTd7gvXABQs7NlXVs2gNN2g',
          'Q1OTUsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiODEifQ.u9MJ2jQ943e-jeNk6lmhVvmE6Fe-ZiXkpWLsDTzqPzTPChEdDSyUVybW9M4V6mTpWJEAij1IofTyVOFXK8E0DQ',
          'M0NzUsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiODEifQ.Mr9Ld6aBrTUmrYiv0ZME7C2GNgFbMLh_xs4a4PG8fOMWlOigDgekfjhI9H2k2N8koFcqwI0hUrRtEGaRE8Wj7g',
          'Q2NjksInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiODEifQ.pknzsXK3CPxrHIe_si0edHUNVaDV_DPosJfQDu9GChubXBeTFNCRdDVvwPoknQijX5WoTJLv5R6abJjygpy86g',
          'Q3MTMsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiODEifQ.9PVVMODghO589TmY5uLLx5tfkK9xKGUZ9tH1GiNxpmF6Vm4oNEHnBi48B9ku5kB9ZdBp6QDqzAS_MRZKRbSe0g',
          'Q4MDQsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiODEifQ.9H84_WCXnggW-s8q_CH9bAjOG8Xt2PYLwPt01gubW_WBVeNKFoF0L4gZHfoh3WNB3PAdCnPwXFugkaKpA73RIg',
          'Q5MDcsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiODEifQ.5vccrTW9OnY8diathsy155RcnSGkn9WNtFtN5mSSPrA8dizhSmiO0PyRiwlLbjvAWH2eh0SwbCwm28kJ09Zp_Q',
          'Q5NzYsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiODEifQ.87CzgSzFkB6D97YA_-nd5_V5xS706JokfqWgc53FEEXsIYI--1Tmil2mzqaxxOpwUpDtYJCSl5pXgCIG8RLHcQ',
          'UxMDAsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiODEifQ.UbOxRAvcWk622VkkixL_W7v89a4NJbQonh_dEpfAl3RBQoI5Xu94eX2vgE5MBXTGuh_-FpCcl743t9rXiC20WQ',
          'UxMDMsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiODEifQ.JFDIRskx9fTKj2W0XRWWubibyBKoDJeEITKWzTKkD13HFTdzouwJqjYBsLBv5GySvFVwqOCGsPDlSbe1GCmqTA',
          'UxMDUsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiODEifQ.9JJ0LQ7pGuvgvDpgqmP14CTooydbym_LrjATiAQIw5mdR1AEbYzUiDT89sB2DY4Lc5mUI1sYM1Gstavm6tUx1w',
          'UxMDgsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiODEifQ.L7rI7w_GhwSOOu1xiare0daGg7QyHqpf_dqgnLZyzLoASWpsDH8NAO-cZTNJazMBYnFS9dYG9ujQNY9JYdDahQ',
          'UxMTAsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiODEifQ.X3eYxPkATIRDIZ_bpz37dSmYK4J9p4l_Hv_Al--n99ygEFH83V-0cKOiGQgplIVyEJ7dlc3c_DjtsUugAIAV6g',
          'UwOTcsInZlciI6MSwiY2xpZW50IjpudWxsLCJvcGVyYXRvciI6bnVsbCwib3JnIjoiODEifQ.osZEL13Wz5CTyoF_b5qzZcgkvMrZPaFsboQvWwl4wkLpJlnAxedcLOJi9Bclx4XgiMiNDlLjyfXh36BNDH5x8A']
departamento = {'Bebidas': ('23', '35', '56', '59', '65', '253', '254', '255', '256', '257', '258', '259', '260', '261', '262', '263', '382', '383', '384', '385'),
                'Biscoitos, Doces e Matinais': ('28', '54', '131', '149', '264', '265', '266', '267', '268', '269', '270', '271', '272', '273', '274', '275', '318', '335', '336', '337', '338', '339', '340', '341', '342', '343', '344', '345', '346'),
                'Carnes': ('277', '278', '279', '280', '281', '282', '283', '284'),
                'Congelados': ('47', '176', '285', '286', '287', '288', '289', '290', '291', '292'),
                'Hortifruti': ('129', '313', '314', '315', '316', '317'),
                'Frios e Laticínios': ('50', '75', '120', '127', '293', '294', '295', '296', '297', '298', '299', '300', '301', '302', '303'),
                'Higiene': ('33', '97', '121', '133', '304', '305', '306', '307', '308', '309', '310', '311', '312', '319', '320', '321'),
                'Limpeza': ('16', '74', '128', '168', '322', '323', '324', '325', '326', '327', '328', '329', '330', '331', '332', '333', '334'),
                'Mercearia': ('243', '244', '245', '246', '248', '249', '250', '251', '252', '347', '348', '349', '350', '351', '352', '353', '354', '355', '356', '357', '358', '359', '360', '361', '362', '363'),
                'Padaria': ('103', '364', '365', '366', '367', '368', '369', '370', '371'),
                'Utilidades e Pet': ('203', '372', '373', '374', '376', '377', '378', '379', '380', '381')}


class ArmazemSpider(scrapy.Spider):
    name = "armazem"
    start_urls = ["https://www.armazemdograo.com.br/"]

    def parse(self, response):
        for elemento in range(len(categorias)):
            for i in range(1, 4):
                url = f"https://api-loja.armazemdograo.com.br/v1/loja/classificacoes_mercadologicas/departamentos/{categorias[elemento]}/produtos/filial/1/centro_distribuicao/3/em_oferta?page={i}"
                headers = {
                    "Accept": "application/json",
                    "Authorization": f"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJ2aXBjb21tZXJjZSIsImF1ZCI6ImFwaS1hZG1pbiIsInN1YiI6IjZiYzQ4NjdlLWRjYTktMTFlOS04NzQyLTAyMGQ3OTM1OWNhMCIsInZpcGNvbW1lcmNlQ2xpZW50ZUlkIjpudWxsLCJpYXQiOjE2OTUwNj{bearer[elemento]}",
                    "Content-Type": "application/json",
                    "Organizationid": "81",
                    "Referer": "https://www.armazemdograo.com.br/",
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
            if product['disponivel'] is True:
                valor = str(product['classificacao_mercadologica_id'])
                rotulo = self.encontrar_rotulo(valor, departamento)

                product_item['nome'] = product['descricao']
                product_item['preco_original'] = product['oferta']['preco_antigo']
                product_item['preco_oferta'] = product['oferta']['preco_oferta']
                product_item['img_pequena'] = 'https://s3.amazonaws.com/produtos.vipcommerce.com.br/144x144/' + product['imagem']
                product_item['img_grande'] = 'https://s3.amazonaws.com/produtos.vipcommerce.com.br/250x250/' + product['imagem']
                product_item['departamento'] = rotulo
                product_item['mercado'] = 'Armazém do Grão'
                product_item['url'] = 'https://www.armazemdograo.com.br/produtos/detalhe/' + \
                    str(product['produto_id']) + '/' + product['link']
                product_item['data'] = datetime.date.today()

                yield product_item

        paginas = data['paginator']['total_pages']

    def encontrar_rotulo(self, valor, departamento):
        for rotulo, valores in departamento.items():
            if valor in valores:
                return rotulo
        return None
