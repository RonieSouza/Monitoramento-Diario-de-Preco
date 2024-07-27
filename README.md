# Robô de Monitoramento Diário de Preço 📉

## Descrição do Projeto 📋

Este projeto consiste em um robô desenvolvido em Python para monitorar os preços do suplemento alimentar CREATINA MONOHIDRATADA 250G em um site de e-commerce. O robô coleta o preço do produto a cada 30 minutos e atualiza uma planilha Excel com as informações coletadas.

## Funcionalidades ⚙️

1. **Consulta Automatizada:**
   - Acesso a um site de e-commerce.
   - Verificação e extração do preço atual do produto.

2. **Manipulação de Planilhas:**
   - Criação de uma planilha Excel com as seguintes colunas:
     - Produto 🛒
     - Data Atual 📅
     - Valor 💰
     - Link do Produto 🔗

3. **Automatização Recorrente:**
   - O script deve ser executado automaticamente a cada 30 minutos ⏲️.

## Configuração do Ambiente 🔧

### Requisitos

- Python 3.x 🐍
- Bibliotecas: `selenium`, `pandas`, `openpyxl`, `re`, `datetime`, `os`

### Instruções para Execução ▶️

1. Clone este repositório.
2. Instale as dependências a partir do arquivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
3. Execute o script: `python app.py`.

## Agendamento da Execução ⏰

Para garantir que o script seja executado automaticamente a cada 30 minutos, você deve configurar um agendamento usando ferramentas externas. Veja como fazer isso em diferentes sistemas operacionais:

### Configuração de Agendamento de Tarefas

#### Linux: Usando `crontab`

1. Abra o arquivo `crontab` com o comando:
    ```bash
    crontab -e
    ```

2. Adicione a seguinte linha ao arquivo `crontab`:
    ```bash
    */30 * * * * /usr/bin/python3 /caminho/para/seu/script/app.py
    ```
   Substitua `/usr/bin/python3` pelo caminho para o interpretador Python no seu sistema e `/caminho/para/seu/script/app.py` pelo caminho absoluto para o script `app.py`.

3. Salve e feche o arquivo. O `crontab` agora executará o script a cada 30 minutos.

#### Windows: Usando Agendador de Tarefas

1. Abra o Agendador de Tarefas (Task Scheduler).

2. Crie uma nova tarefa (Create Basic Task) e siga o assistente.

3. Defina o gatilho (Trigger) para "Diariamente" e configure para repetir a cada 30 minutos.

4. Defina a ação (Action) para "Iniciar um programa" e selecione o arquivo `python.exe` (geralmente encontrado em `C:\PythonXX\python.exe`).

5. No campo "Adicionar argumentos", insira o caminho para o script `app.py`.

6. Complete a configuração e salve a tarefa.

## Notas 📝

O agendamento da execução do script não está incluído diretamente no código para permitir uma maior flexibilidade e controle. Utilizar ferramentas externas para gerenciamento de tarefas recorrentes, como `crontab` no Linux e o Agendador de Tarefas no Windows, é mais eficaz para garantir que o script seja executado conforme planejado, permitindo que o sistema operacional cuide da execução do script em intervalos regulares.

## Exemplo de Uso 💡

Após configurar o agendamento, o robô começará a coletar e registrar os preços automaticamente. Você pode verificar a planilha Excel para ver as informações atualizadas a cada 30 minutos.

## Problemas Conhecidos ⚠️

- A coleta de dados pode falhar se o site alvo estiver fora do ar ou tiver mudanças significativas na estrutura da página.
- Certifique-se de que o caminho para o script e o Python estejam corretos no agendador de tarefas.

## Licença 📝

Este projeto está licenciado sob a Licença MIT - consulte o arquivo `LICENSE` para detalhes.
