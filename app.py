from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, TimeoutException
from selenium.webdriver.support import expected_conditions
import pandas as pd
import re
from datetime import datetime
import os

class WebScraper:
    def __init__(self, url, output_file):
        """
        Inicializa o WebScraper com a URL do produto e o caminho do arquivo de saída.

        :param url: URL do produto para scraping.
        :param output_file: Caminho do arquivo Excel para salvar os dados.
        """
        self.url = url
        self.output_file = output_file
        self.driver, self.wait = self._configurar_driver()
        self.dados = self._obter_dados_produto()

    def _configurar_driver(self):
        """
        Configura e inicia o driver do Selenium com opções específicas.

        :return: Instância do driver e do WebDriverWait.
        """
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        chrome_options.add_argument('--window-size=1360,750')
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_experimental_option("prefs", { 
            "profile.default_content_setting_values.notifications": 2
        })
        driver = Chrome(options=chrome_options)
        wait = WebDriverWait(driver, 10, poll_frequency=1, 
                             ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
        return driver, wait

    def _verificar_elemento_existe(self, xpath):
        """
        Verifica se um elemento está presente na página.

        :param xpath: XPath do elemento a ser verificado.
        :return: True se o elemento estiver presente, False caso contrário.
        """
        try:
            self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
            return True
        except TimeoutException:
            return False

    def _obter_descricao_item(self):
        """
        Obtém a descrição do item da página.

        :return: Descrição do item.
        """
        return self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//h1[@class="topoDetalhe-boxRight-nome"]'))).text

    def _obter_preco_item(self):
        """
        Obtém o preço do item da página.

        :return: Preço do item.
        """
        return self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//span[@class="topoDetalhe-boxRight-precoDe show-for-large"]'))).text

    def _formatar_preco(self, preco):
        """
        Formata o preço removendo caracteres não numéricos e substituindo a vírgula por ponto.

        :param preco: Preço original.
        :return: Preço formatado.
        """
        return re.sub(r"[^0-9,]", "", preco).replace(',', '.')
    
    def _verificar_disponibilidade_compra(self):
        """
        Verifica a disponibilidade do produto para compra.

        :return: 'SIM' ou 'NÃO'.
        """
        return 'SIM' if self._verificar_elemento_existe('//div[@class="botao-de-compra"]//button[@class="botaoComprar"]') else 'NÃO'

    def _obter_dados_produto(self):
        """
        Obtém os dados do produto da página web.

        :return: Dicionário com os dados do produto.
        """
        self.driver.get(self.url)
        
        descricao_item = self._obter_descricao_item()
        preco_item = self._obter_preco_item()
        disponibilidade_compra = self._verificar_disponibilidade_compra()

        dados = {
            "Descrição do Item": descricao_item,
            "Preço": self._formatar_preco(preco_item),
            "Data Hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "Disponível para Compra?": disponibilidade_compra,
            "Link do Produto": self.url
        }
        return dados
    
    def salvar_dados(self):
        """
        Salva os dados coletados em um arquivo Excel. Se o arquivo já existir, os dados novos são adicionados aos existentes.
        """
        df_novo = pd.DataFrame([self.dados])
        if os.path.exists(self.output_file):
            df_existente = pd.read_excel(self.output_file)
            df_combinado = pd.concat([df_existente, df_novo], ignore_index=True)
        else:
            df_combinado = df_novo
        df_combinado.to_excel(self.output_file, index=False)

def main():
    """
    Função principal para iniciar o processo de coleta de dados e salvar os resultados.
    """
    print("\033[33m\033[1mIniciando o processo de coleta de dados...\033[0m")

    URL_PRODUTO = 'https://www.gsuplementos.com.br/creatina-monohidratada-250gr-growth-supplements-p985931'
    CAMINHO_ARQUIVO_EXCEL = os.path.join(os.getcwd(), "dados.xlsx")

    scraper = WebScraper(URL_PRODUTO, CAMINHO_ARQUIVO_EXCEL)
    scraper.salvar_dados()

    print(f"\033[32m\033[1mProcesso finalizado com sucesso. Arquivo -> {CAMINHO_ARQUIVO_EXCEL}\033[0m")

if __name__ == "__main__":
    main()
