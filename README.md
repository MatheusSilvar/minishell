# Shell Python

Um shell simples implementado em Python que suporta comandos básicos, execução paralela e redirecionamento de saída.

## Funcionalidades

- **Comandos built-in**: `pwd`, `cd`, `cat`, `ls`, `echo`, `exit`
- **Execução de comandos externos**: Qualquer comando disponível no sistema
- **Redirecionamento de saída**: Usando `>` para salvar output em arquivos
- **Execução sequencial**: Usando `;` para executar comandos em sequência
- **Execução paralela**: Usando `&` para executar comandos simultaneamente

## Como usar

### Executando o shell

```bash
python denis2.py
```

### Comandos básicos

```bash
> pwd                    # Mostra o diretório atual
> ls                     # Lista arquivos do diretório
> cd pasta               # Muda para o diretório "pasta"
> cat arquivo.txt        # Exibe o conteúdo do arquivo
> echo Hello World       # Imprime "Hello World"
> exit                   # Sai do shell
```

### Redirecionamento de saída

```bash
> ls > arquivos.txt      # Salva a lista de arquivos em "arquivos.txt"
> echo "texto" > saida.txt  # Salva "texto" no arquivo "saida.txt"
```

### Execução sequencial

```bash
> pwd; ls; echo "fim"    # Executa os comandos um após o outro
```

### Execução paralela

```bash
> sleep 3 & echo "paralelo" & ls  # Executa os três comandos simultaneamente
```

**Nota**: Os comandos `cd` e `exit` não podem ser executados em paralelo.

### Combinando funcionalidades

```bash
> echo "inicio"; sleep 2 & echo "paralelo"; echo "fim"
```

## Requisitos

- Python 3.x
- Módulos padrão: `os`, `shlex`, `subprocess`, `sys`, `multiprocessing`, `time`

## Interrompendo o shell

- `exit`: Encerra o shell
