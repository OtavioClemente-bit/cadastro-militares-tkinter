#  Sistema de Cadastro de Militares

Projeto completo em Python com Tkinter para **cadastro, gerenciamento e visualização de militares** em uma organização. Desenvolvido com foco em **usabilidade**, **validação de dados** e **organização hierárquica por posto e graduação**.

>  **Propósito real:** Este sistema substitui o uso de planilhas e automatiza a rotina administrativa de controle de militares, algo que eu realmente utilizo no meu trabalho dentro do Exército Brasileiro.

---
##  Demonstração

![Demonstração do Sistema](execução_projeto.gif)

> *A animação acima mostra o funcionamento real do sistema: cadastro com validações, contagem por posto/graduação, exibição de militares e tooltip com foto ao passar o mouse.*
##  Funcionalidades

 Cadastro completo com:
- Posto e Graduação  
- Nome completo e nome de guerra  
- CPF com validação e formatação  
- PREC-CP e Identidade Militar  
- Banco, Agência e Conta  
- Inserção de foto (opcional)

 Tela inicial com:
- Total de militares cadastrados  
- Quantidade por Posto/Graduação

 Salvamento dos dados em arquivo `.json`

---

##  Tecnologias Utilizadas

- **Python 3**
- **Tkinter (GUI)**
- **Pillow (PIL) para imagens**
- **JSON para persistência dos dados**

---

##  Motivação

Sou militar de carreira e estudante de Ciência da Computação. Desenvolvi esse projeto para **facilitar minha rotina administrativa real**. Com ele, consigo eliminar planilhas e ter uma solução visual, segura e reutilizável.

Este projeto também é parte da minha **transição de carreira para área de tecnologia** — e é um marco do meu crescimento prático em Python.

---

##  Como rodar

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/cadastro-militares.git
cd cadastro-militares
```

2. **Instale as dependências**
```bash
pip install pillow
```

3. **Execute o sistema**
```bash
python main.py
```

---

##  Estrutura

```
cadastro-militares/
├── main.py               # Código principal com interface
├── militares.json        # Banco de dados local
├── imgs/
│   └── exemplo.jpg       # Exemplo de imagem
└── README.md             # Este arquivo
```

##  Próximos passos (em andamento)

-  Tela de edição de dados  
-  Exclusão de militares  
-  Listagem completa com busca  
-  Tooltip com foto ao passar o mouse  
-  Exportação para PDF ou Excel  
-  Interface mais moderna com `ttkbootstrap`

---

##  Autor

**Otavio Clemente**  
Sargento do Exército | Estudante de Ciência da Computação  
Apaixonado por resolver problemas com código.

🔗 [GitHub](https://github.com/OtavioClemente-bit)  
🔗 [LinkedIn](https://www.linkedin.com/in/otavio-clemente-36056b2b5/)
