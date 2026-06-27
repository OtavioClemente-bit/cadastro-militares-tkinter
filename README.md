# Sistema de Cadastro de Militares

Sistema desktop desenvolvido em **Python** com **Tkinter** para cadastro, organização e consulta de militares em uma rotina administrativa.

O projeto nasceu de uma necessidade real: substituir controles manuais e planilhas por uma ferramenta simples, visual e mais organizada.

> Observação: o repositório não deve conter dados reais de militares. Qualquer dado utilizado em demonstrações deve ser fictício.

---

## Objetivo

Criar uma aplicação local para apoiar o controle de efetivo, permitindo registrar informações essenciais, consultar dados rapidamente e manter uma base organizada para tarefas administrativas.

Este projeto representa minha evolução prática em desenvolvimento: comecei com scripts simples em Python e fui avançando para interfaces gráficas, validações, persistência local e organização de funcionalidades.

---

## Funcionalidades

- Cadastro de militares com dados básicos
- Organização por posto/graduação
- Nome completo e nome de guerra
- Validação e formatação de CPF
- Registro de PREC-CP e identidade militar
- Campos bancários e dados administrativos
- Inclusão opcional de foto
- Tela inicial com resumo do efetivo
- Contagem por posto/graduação
- Persistência local em arquivo JSON

---

## Demonstração

![Demonstração do Sistema](execução_projeto.gif)

A demonstração apresenta o fluxo principal do sistema: cadastro, validação, visualização e organização das informações cadastradas.

---

## Tecnologias utilizadas

- **Python 3**
- **Tkinter** para interface gráfica
- **Pillow** para manipulação de imagens
- **JSON** para persistência local
- **Git e GitHub** para versionamento

---

## O que este projeto demonstra

- Criação de interfaces gráficas desktop
- Organização de dados locais
- Validação de entrada do usuário
- Separação de responsabilidades em uma aplicação simples
- Capacidade de transformar uma necessidade real em solução funcional
- Evolução prática em desenvolvimento de software

---

## Como executar

1. Clone o repositório:

```bash
git clone https://github.com/OtavioClemente-bit/cadastro-militares-tkinter.git
cd cadastro-militares-tkinter
```

2. Instale a dependência necessária:

```bash
pip install pillow
```

3. Execute o projeto:

```bash
python main.py
```

---

## Estrutura básica

```text
cadastro-militares-tkinter/
├── main.py
├── militares.json
├── imgs/
└── README.md
```

---

## Melhorias futuras

- Migração para SQLite
- Tela de edição mais completa
- Exportação para PDF ou Excel
- Busca avançada por nome, posto/graduação e outros campos
- Interface mais moderna
- Separação do projeto em camadas
- Testes automatizados para validações principais

---

## Autor

Desenvolvido por **Otavio Clemente**  
Estudante de Ciência da Computação e desenvolvedor em formação, com foco em Python, automação e sistemas administrativos.

- GitHub: [@OtavioClemente-bit](https://github.com/OtavioClemente-bit)
- LinkedIn: [Otavio Clemente](https://www.linkedin.com/in/otavio-clemente-36056b2b5/)
