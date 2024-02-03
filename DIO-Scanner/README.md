**README - DIOScanner**

## Descrição
Bem-vindo ao DIOScanner, uma ferramenta simples de varredura de portas usando a biblioteca Nmap em Python. Este script permite realizar varreduras em diferentes tipos, fornecendo informações sobre o status das portas e protocolos disponíveis em um determinado endereço IP.

## Requisitos
- Python instalado (recomendado Python 3.x)
- Biblioteca Nmap (`python-nmap`)

Você pode instalar a biblioteca Nmap executando o seguinte comando:
```bash
pip install python-nmap
```

## Uso
1. Execute o script `dioscanner.py`.
2. Insira o endereço IP que deseja varrer quando solicitado.
3. Escolha o tipo de varredura desejado:
   - 1: Varredura do Tipo SYN
   - 2: Varredura do Tipo UDP
   - 3: Varredura do Tipo Intensa

O script exibirá informações sobre o status do IP, protocolos e portas abertas com base na opção escolhida.

## Exemplo de Uso
```bash
python dioscanner.py
```

## Observações
- Certifique-se de ter permissões adequadas para realizar varreduras no IP especificado.
- Este script usa a biblioteca Nmap, portanto, é necessário que o Nmap esteja instalado no sistema.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar solicitações de pull (pull requests) para melhorar este projeto.

Divirta-se explorando e utilizando o DIOScanner!