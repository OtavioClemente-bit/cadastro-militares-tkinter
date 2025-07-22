import json, os
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import filedialog
from PIL import Image, ImageTk

dados_arquivos = "militares.json"
militares = []
posto_graduação = ["Capitão", "1º Tenente", "2º Tenente", "Subtenente", "1º Sargento", "2º Sargento", "3º Sargento", "Cabo Efetivo Profissional", "Soldado Efetivo Profissional", "Soldado Efetivo Variável"]
bancos = ["001 - Banco do Brasil S.A", "341 - Itaú Unibanco S.A", "033 - Banco Santander (Brasil) S.A", "237 - Banco Bradesco S.A", "237 - Banco Santander (Brasil) S.A", "104 - Caixa Econômica Federal"]

def salvar_dados():
    with open(dados_arquivos, "w") as f:
        json.dump(militares, f, indent=4, ensure_ascii=True)

def carregar_dados():
    global militares
    try:
        with open(dados_arquivos, "r") as f:
            militares = json.load(f)
    except FileNotFoundError:
        pass

carregar_dados()

tooltip_foto = None

def mostrar_foto_tooltip(event, caminho_foto):
    global tooltip_foto
    if not os.path.exists(caminho_foto):
        return

    imagem = Image.open(caminho_foto)
    imagem.thumbnail((200, 200))  # Reduz o tamanho
    foto = ImageTk.PhotoImage(imagem)

    tooltip_foto = tk.Toplevel()
    tooltip_foto.wm_overrideredirect(True)
    tooltip_foto.geometry(f"+{event.x_root+20}+{event.y_root+20}")
    label = tk.Label(tooltip_foto, image=foto)
    label.image = foto  # Impede garbage collection
    label.pack()

def esconder_foto_tooltip(event):
    global tooltip_foto
    if tooltip_foto:
        tooltip_foto.destroy()
        tooltip_foto = None

def contar_militares_por_posto():
    contagem = {posto: 0 for posto in posto_graduação}

    for m in militares:
        posto = m.get("P/G", "")
        if posto in contagem:
            contagem[posto] += 1

    total = sum(contagem.values())
    return total, contagem

# Criar a janela principal
janela = tk.Tk()
janela.title("Sistema de Cadastro Militar")
janela.geometry("450x450")

frame_totais = tk.LabelFrame(janela, text="Resumo de Militares", padx=10, pady=10)
frame_totais.pack(padx=10, pady=10, fill="x")

def atualizar_resumo():
    for widget in frame_totais.winfo_children():
        widget.destroy()

    total, contagem = contar_militares_por_posto()

    tk.Label(frame_totais, text=f"Total cadastrados: {total}").pack(anchor="w")

    for posto in posto_graduação:
        qtde = contagem[posto]
        if qtde >= 0:
            tk.Label(frame_totais, text=f"{posto}: {qtde}").pack(anchor="w")

atualizar_resumo()

def cadastrar_militar(): #Função para cadastro dos militares
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastro de Militar")
    janela_cadastro.geometry("300x450")

    tk.Label(janela_cadastro, text="Posto e Graduação").pack() #Escolha posto e graduação
    escolha_posto = ttk.Combobox(janela_cadastro, values=posto_graduação, state="readonly")
    escolha_posto.pack()

    tk.Label(janela_cadastro, text="Nome completo").pack() #Entrada para nome completo
    nome_cadastro = tk.Entry(janela_cadastro)
    nome_cadastro.pack()

    tk.Label(janela_cadastro, text="Nome de guerra").pack() #Entrada nome de guerra
    nome_de_guerra = tk.Entry(janela_cadastro)
    nome_de_guerra.pack()

    tk.Label(janela_cadastro, text="CPF").pack() #Entrada CPF
    cpf_entrada = tk.Entry(janela_cadastro)
    cpf_entrada.pack()

    tk.Label(janela_cadastro, text="PREC-CP").pack() #Entrada PREC-CP
    prec_entrada = tk.Entry(janela_cadastro)
    prec_entrada.pack()

    tk.Label(janela_cadastro, text="Idt Militar").pack() #Entrada Idt Militar
    idt_entrada = tk.Entry(janela_cadastro)
    idt_entrada.pack()

    tk.Label(janela_cadastro, text="Banco").pack() #Escolha posto e graduação
    escolha_banco = ttk.Combobox(janela_cadastro, values=bancos, state="readonly")
    escolha_banco.pack()

    tk.Label(janela_cadastro, text="Agência").pack() #Entrada Idt Militar
    agencia_entrada = tk.Entry(janela_cadastro)
    agencia_entrada.pack()

    tk.Label(janela_cadastro, text="Conta").pack() #Entrada Idt Militar
    conta_entrada = tk.Entry(janela_cadastro)
    conta_entrada.pack()

    foto_path = tk.StringVar()

    def selecionar_foto():
        caminho = filedialog.askopenfilename(title="Selecione a foto", filetypes=[("Imagens", "*.png *.jpg *.jpeg")], parent=janela_cadastro)
        if caminho:
            foto_path.set(caminho)

    tk.Button(janela_cadastro, text="Selecionar Foto", command=selecionar_foto).pack(pady=5)

    def salvar(): #Função salvar dados dos militares
        PG = escolha_posto.get()
        nome_completo = nome_cadastro.get()
        nome_guerra = nome_de_guerra.get()
        cpf = cpf_entrada.get()
        prec = prec_entrada.get()
        idt = idt_entrada.get()
        banco = escolha_banco.get()
        agencia = agencia_entrada.get()
        cc = conta_entrada.get()

        for m in militares:
            if m.get("CPF", "").replace(".", "").replace("-", "") == cpf:
                messagebox.showerror("Erro", "Já existe um militar com esse CPF.", parent=janela_cadastro)
                return
            if m.get("Idt Militar", "").replace(".", "").replace("-", "") == idt:
                messagebox.showerror("Erro", "Já existe um militar com essa Identidade Militar.", parent=janela_cadastro)
                return
            if m.get("Prec-CP", "").replace(" ", "") == prec:
                messagebox.showerror("Erro", "Já existe um militar com esse Prec-CP", parent=janela_cadastro)
                return
            
        if not PG:
            messagebox.showerror("Erro", "Posto e Graduação deve ser preenchido.", parent=janela_cadastro)
            return
        
        if not nome_completo or not nome_de_guerra:
            messagebox.showerror("Erro", "Nome completo e nome de guerra deve ser preenchido.", parent=janela_cadastro)
            return
        
        if not nome_completo.replace(" ","").isalpha():
            messagebox.showerror("Erro", "Nome completo deve ser apenas letras.", parent=janela_cadastro)
            return
        
        if not nome_guerra.isalpha():
            messagebox.showerror("Erro", "Nome de guerra deve ser apenas letras.", parent=janela_cadastro)
            return
        
        if nome_guerra not in nome_completo:
            messagebox.showerror("Erro", "Nome de guerra inválido.", parent=janela_cadastro)
            return
        
        if not cpf.isdigit() or len(cpf) != 11:
            messagebox.showerror("Erro", "CPF Inválido.", parent=janela_cadastro)
            return
        
        if not prec.isdigit() or len(prec) != 9:
            messagebox.showerror("Erro", "Prec-CP Inválido.", parent=janela_cadastro)
            return
        
        if not idt.isdigit() or len(idt) != 10:
            messagebox.showerror("Erro", "Identidade Militar Inválida.", parent=janela_cadastro)
            return
        
        if not banco:
            messagebox.showerror("Erro", "Banco não foi escolhido.", parent=janela_cadastro)
            return
        
        if not agencia:
            messagebox.showerror("Erro", "Agência em branco.", parent=janela_cadastro)
            return
        
        if not cc:
            messagebox.showerror("Erro", "Conta em branco.", parent=janela_cadastro)
            return
        
        formato_cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        formato_prec= f"{prec[:2]} {prec[2:9]}"
        formato_IDT= f"{idt[:3]}.{idt[3:6]}.{idt[6:9]}-{idt[9:]}"

        militar_cadastrado = {
            "P/G": PG, 
            "Nome": nome_completo.title(), 
            "Nome de Guerra": nome_guerra.capitalize(), 
            "CPF": formato_cpf, 
            "Prec-CP": formato_prec, 
            "Idt Militar": formato_IDT,
            "Banco": banco,
            "Agência": agencia,
            "Conta": cc,
            "Foto": foto_path.get()
            }
        
        militares.append(militar_cadastrado)
        salvar_dados()
        atualizar_resumo()
        messagebox.showinfo("Sucesso", "Militar cadastrado com sucesso!")
        janela_cadastro.destroy()

    # Botão para salvar os dados
    tk.Button(janela_cadastro, text="Salvar", command=salvar).pack(pady=10)

ordem_posto = {}
for indice, posto in enumerate(posto_graduação):
    ordem_posto[posto] = indice

def listar_militares():
    try:
        with open(dados_arquivos, "r") as f:
            dados = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo("Aviso", "Nenhum militar cadastrado ainda.", parent=janela_lista)
        return
    
    if not dados:
        messagebox.showinfo("Aviso", "Nenhum militar cadastrado ainda.", parent=janela_lista)
        return

    militares_ordenados = sorted(militares, key=lambda m: ordem_posto.get(m.get("P/G", ""), 999))

    def excluir_militares():
        item = seçoes.selection()
        if not item:
            messagebox.showwarning("Atenção", "Selecione um militar para excluir.", parent=janela_lista)
            return
        
        resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir este militar?", parent=janela_lista)
        if resposta is True:
            index = seçoes.index(item)
            seçoes.delete(item)
            del militares[index]
            salvar_dados()
            atualizar_resumo()
            messagebox.showinfo("Excluido", "Militar excluído com sucesso.", parent=janela_lista)

    def buscar_militar(busca):
        busca =  entrada_busca.get().strip().lower()
        seçoes.delete(*seçoes.get_children()) 

        for militar in militares_ordenados:
            nome = militar.get("Nome", "").lower()
            cpf = militar.get("CPF", "").replace(".", "").replace("-", "")
            idt = militar.get("Idt Militar", "").replace(".", "").replace("-", "")

            if busca in nome or busca in cpf or busca in idt:
                seçoes.insert("", "end", values=(
                militar.get("P/G"),
                militar.get("Nome"),
                militar.get("Nome de Guerra"),
                militar.get("CPF"),
                militar.get("Prec-CP"),
                militar.get("Idt Militar"),
                militar.get("Banco"),
                militar.get("Agência"),
                militar.get("Conta"),
             ))

    def limpar_busca():
        seçoes.delete(*seçoes.get_children()) 
        for militar in militares_ordenados:
            seçoes.insert("", "end", values=(
            militar.get("P/G"),
            militar.get("Nome de Guerra"),
            militar.get("Nome"),
            militar.get("CPF"),
            militar.get("Prec-CP"),
            militar.get("Idt Militar"),
            militar.get("Banco"),
            militar.get("Agência"),
            militar.get("Conta"),
             ))
        entrada_busca.delete(0, tk.END)  # limpa o campo de texto

    def editar_militar():
        escolha = seçoes.selection()
        if not escolha:
            messagebox.showwarning("Atenção", "Selecione um militar para editar.", parent=janela_lista)
            return
        
        valores = seçoes.item(escolha)["values"]
        cpf_escolhido = valores[3]  # índice do CPF na Treeview

        for idx, m in enumerate(militares):
            if m.get("CPF", "") == cpf_escolhido:
                index = idx
                dados_militar = m
                break

        janela_editar = tk.Toplevel()
        janela_editar.title("Editar Militar")
        janela_editar.geometry("300x500")

        tk.Label(janela_editar, text="Posto e Graduação").pack()
        escolha_posto = ttk.Combobox(janela_editar, values=posto_graduação, state="readonly")
        escolha_posto.set(dados_militar["P/G"])
        escolha_posto.pack()

        tk.Label(janela_editar, text="Nome completo").pack()
        nome_cadastro = ttk.Entry(janela_editar)
        nome_cadastro.insert(0, dados_militar["Nome"])
        nome_cadastro.pack()

        tk.Label(janela_editar, text="Nome de Guerra").pack()
        nome_guerra = ttk.Entry(janela_editar)
        nome_guerra.insert(0, dados_militar["Nome de Guerra"])
        nome_guerra.pack()

        tk.Label(janela_editar, text="CPF").pack()
        cpf = ttk.Entry(janela_editar)
        cpf.insert(0, dados_militar["CPF"].replace(".", "").replace("-", ""))
        cpf.pack()

        tk.Label(janela_editar, text="Prec-CP").pack()
        prec = ttk.Entry(janela_editar)
        prec.insert(0, dados_militar["Prec-CP"].replace(" ", ""))
        prec.pack()

        tk.Label(janela_editar, text="Identidade Militar").pack()
        idt = ttk.Entry(janela_editar)
        idt.insert(0, dados_militar["Idt Militar"].replace(".", "").replace("-", ""))
        idt.pack()

        tk.Label(janela_editar, text="Banco").pack()
        banco = ttk.Combobox(janela_editar, values=bancos, state="readonly")
        banco.set(dados_militar["Banco"])
        banco.pack()

        tk.Label(janela_editar, text="Agência").pack()
        agencia = ttk.Entry(janela_editar)
        agencia.insert(0, dados_militar["Agência"])
        agencia.pack()

        tk.Label(janela_editar, text="Conta").pack()
        cc = ttk.Entry(janela_editar)
        cc.insert(0, dados_militar["Conta"])
        cc.pack()

        foto_path_edicao = tk.StringVar()
        foto_path_edicao.set(dados_militar.get("Foto", ""))

        def selecionar_nova_foto():
            caminho = filedialog.askopenfilename(title="Selecione a nova foto", filetypes=[("Imagens", "*.png *.jpg *.jpeg")], parent=janela_editar)
            if caminho:
                foto_path_edicao.set(caminho)

        tk.Button(janela_editar, text="Selecionar Nova Foto", command=selecionar_nova_foto).pack(pady=5)

        def salvar_edicao():
            formato_cpf = f"{cpf.get()[:3]}.{cpf.get()[3:6]}.{cpf.get()[6:9]}-{cpf.get()[9:]}"
            formato_prec= f"{prec.get()[:2]} {prec.get()[2:9]}"
            formato_IDT= f"{idt.get()[:3]}.{idt.get()[3:6]}.{idt.get()[6:9]}-{idt.get()[9:]}"
            militar_editado = {
            "P/G": escolha_posto.get(), 
            "Nome": nome_cadastro.get().title(), 
            "Nome de Guerra": nome_guerra.get().capitalize(), 
            "CPF": formato_cpf, 
            "Prec-CP": formato_prec, 
            "Idt Militar": formato_IDT,
            "Banco": banco.get(),
            "Agência": agencia.get(),
            "Conta": cc.get(),
            "Foto": foto_path_edicao.get()
            }
            militares[index] = militar_editado
            salvar_dados()
            messagebox.showinfo("Sucesso", "Militar editado com sucesso.", parent=janela_editar)
            janela_editar.destroy()
            janela_lista.destroy()
            listar_militares()

        tk.Button(janela_editar, text="Salvar Alterações", command=salvar_edicao).pack(pady=10)

    janela_lista = tk.Toplevel()
    janela_lista.title("Lista de Militares")
    janela_lista.state("zoomed")

    colunas = ("P/G", "Nome de Guerra", "Nome", "CPF", "Prec-CP", "Idt Militar", "Banco", "Agência", "Conta")

    frame_botoes = tk.Frame(janela_lista)
    frame_botoes.pack(side="top", pady=10, fill="x")

    tk.Label(frame_botoes, text="Buscar:").pack(side="left", padx=5)
    entrada_busca = tk.Entry(frame_botoes)
    entrada_busca.pack(side="left", padx=5)
    tk.Button(frame_botoes, text="Pesquisar", command= lambda: buscar_militar(entrada_busca.get())).pack(side="left", padx=5)
    tk.Button(frame_botoes, text="Limpar", command=limpar_busca).pack(side="left", padx=5)
    tk.Button(frame_botoes, text="Editar", command=editar_militar).pack(side="left", padx=5)
    tk.Button(frame_botoes, text="Excluir Selecionado", command=excluir_militares).pack(side="left", padx=5)
    
    seçoes = ttk.Treeview(janela_lista, columns=colunas, show="headings")
    seçoes.pack(side="left", fill="both", expand=True)

    for i, coluna in enumerate(colunas):
        seçoes.heading(coluna, text=colunas[i])
        seçoes.column(coluna, width=120)

    item_para_foto = {}

    for i, militar in enumerate(militares_ordenados):
        caminho_foto = militar.get("Foto", "")
        
        item_id = seçoes.insert("", "end", values=(
            militar.get("P/G"),
            militar.get("Nome de Guerra"),
            militar.get("Nome"),
            militar.get("CPF"),
            militar.get("Prec-CP"),
            militar.get("Idt Militar"),
            militar.get("Banco"),
            militar.get("Agência"),
            militar.get("Conta"),
        ))

        if caminho_foto:
            item_para_foto[item_id] = caminho_foto

    item_ativo = {"id": None}

    def ao_mover_mouse(event):
        region = seçoes.identify("region", event.x, event.y)
        if region != "cell":
            esconder_foto_tooltip(event)
            item_ativo["id"] = None
            return

        item_id = seçoes.identify_row(event.y)

        if item_id and item_id in item_para_foto:
            if item_id != item_ativo["id"]:
                esconder_foto_tooltip(event)
                mostrar_foto_tooltip(event, item_para_foto[item_id])
                item_ativo["id"] = item_id
        else:
            esconder_foto_tooltip(event)
            item_ativo["id"] = None

    seçoes.bind("<Motion>", ao_mover_mouse)
    seçoes.bind("<Leave>", esconder_foto_tooltip)


def pesquisar():
    print("Pesquisar clicado")

def editar():
    print("Editar clicado")

def sair():
    janela.destroy()  # Fecha a janela

# Criar os botões com espaçamento e largura total
tk.Button(janela, text="Cadastrar Militar", command=cadastrar_militar).pack(fill="x", pady=5, padx=20)
tk.Button(janela, text="Listar Militares", command=listar_militares).pack(fill="x", pady=5, padx=20)
tk.Button(janela, text="Sair", command=sair).pack(fill="x", pady=10, padx=20)

# Iniciar a interface
janela.mainloop()
