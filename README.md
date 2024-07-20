```markdown
# Magalu Selenium Test Suite

### Descrição

Repositório para o trabalho de testes automatizados com Selenium no site da Magazine Luiza.

### Integrantes

- Andersson
- Daniel 
- Franklin 

## Requisitos

**Python**  
[Download Python](https://www.python.org/downloads/)

**Selenium**  
Instalar usando pip:  
```sh
pip install selenium
```

**WebDriver (ChromeDriver, GeckoDriver, etc.)**  
- [Baixe o ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
- Extraia o executável e adicione-o ao PATH do sistema.

## Vídeos

**Demonstração dos Testes**  
[Link para o vídeo de demonstração](https://example.com)

## Guia geral

**Links úteis**  
[Documentação do Selenium](https://www.selenium.dev/documentation/)

**Primeiros passos**

- **Clonar o repositório**, e deixar na pasta onde deseja salvar o trabalho:
  ```sh
  git clone <URL_DO_REPOSITORIO>
  ```
- **Criar uma Branch**  
  Na página principal do repositório, clique em **Branch** e depois em **New Branch**.  
  Nomeie como **Branch-seu_nome** para manter a organização.  
  No VS Code, vá no **Source Control**, clique nos três pontinhos, depois em **Fetch** para atualizar, e em seguida em **Checkout to** para escolher a branch que você criou.

- **Enviar código**:
  Para enviar sua parte do código, sempre verifique se está na branch **CORRETA**.  
  Ao editar o código, os arquivos aparecerão no **Source Control**.  
  Quando terminar, escreva o que fez na mensagem e clique em **Commit**.

  Ah, quase me esqueci... **sempre** crie uma nova branch para novas tarefas.  
  Exemplo: Fulano vai fazer a interface gráfica.  
  Então, Fulano, vai abrir uma branch nova, fazer a interface gráfica, e quando acabar, faz o commit e pronto.

  A princípio é isso. Com o tempo vamos acertando direitinho como usar isso aqui melhor, e qualquer dúvida é só chamar.  
  ![imagem_exemplo](https://i.pinimg.com/1200x/f7/c3/ca/f7c3ca6460fbc7112026e502993ac2f0.jpg)

## Estrutura do Projeto

```
Magalu_Selenium/
├── __pycache__/
├── test_login.py
├── test_search_product.py
├── webdriver_setup.py
├── main_gui.py
└── README.md
```

## Como Executar os Testes

### Executando os Testes Individualmente

1. **Teste de Login**
    ```sh
    python test_login.py
    ```

2. **Teste de Pesquisa de Produto**
    ```sh
    python test_search_product.py
    ```

### Executando Todos os Testes

1. Execute o script principal da interface gráfica:
    ```sh
    python main_gui.py
    ```

2. Use a interface gráfica para selecionar e executar os testes desejados.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.
```

Este `README.md` está estruturado para fornecer uma descrição clara do projeto, listar os integrantes, descrever os requisitos, e fornecer instruções detalhadas sobre como configurar e utilizar o repositório.
