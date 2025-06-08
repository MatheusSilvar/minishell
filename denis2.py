import os
import shlex
import subprocess
import sys
import multiprocessing
import time

def executar_comando(tokens):
    if not tokens:
        return

    
    if ">" in tokens:
        if tokens.count(">") != 1 or tokens[-1] == ">":
            print("Uso incorreto de redirecionamento.")
            return
        idx = tokens.index(">")
        command, filename = tokens[:idx], tokens[idx+1]
        try:
            with open(filename, "w") as f:
                proc = subprocess.Popen(command, stdout=f, stderr=subprocess.PIPE)
                proc.wait()
        except Exception as e:
            print(f"Erro ao redirecionar: {e}")
        return

    
    cmd = tokens[0]

    if cmd == "exit":
        sys.exit(0)
    elif cmd == "pwd":
        print(os.getcwd())
    elif cmd == "cd":
        if len(tokens) != 2:
            print("Uso: cd <diretório>")
        else:
            try:
                os.chdir(tokens[1])
            except FileNotFoundError:
                print("no such file or directory")
            except NotADirectoryError:
                print("Não é um diretório")
    elif cmd == "cat":
        if len(tokens) != 2:
            print("Uso: cat <arquivo>")
        else:
            try:
                with open(tokens[1], "r") as f:
                    print(f.read(), end="")
            except FileNotFoundError:
                print("Arquivo não encontrado")
    elif cmd == "ls":
        try:
            for item in os.listdir("."):
                print(item)
        except Exception as e:
            print(f"Erro ao listar diretório: {e}")
    elif cmd == "echo":
        print(" ".join(tokens[1:]))
    else:
        
        try:
            proc = subprocess.Popen(tokens)
            proc.wait()
        except FileNotFoundError:
            print(f"Comando não encontrado: {cmd}")
        except Exception as e:
            print(f"Erro ao executar comando: {e}")

def executar_comando_em_processo(tokens):
    executar_comando(tokens)

def divisao_segura(command):
    try:
        return shlex.split(command)
    except ValueError:
        
        return command.split()

def analisar_e_executar(line):
    
    comandos_sequenciais = line.split(";")
    
    for part in comandos_sequenciais:
        
        comandos_paralelos = [cmd.strip() for cmd in part.split("&") if cmd.strip()]
        
        if len(comandos_paralelos) == 1:
            
            tokens = divisao_segura(comandos_paralelos[0])
            if tokens:
                executar_comando(tokens)
        else:
            
            processos = []
            
            for cmd in comandos_paralelos:
                tokens = divisao_segura(cmd)
                if not tokens:
                    continue
                
                
                if tokens[0] in ["cd", "exit"]:
                    print(f"Aviso: comando '{tokens[0]}' não pode ser executado em paralelo")
                    continue
                
                
                processo = multiprocessing.Process(target=executar_comando_em_processo, args=(tokens,))
                processo.start()
                processos.append(processo)
            
            
            for processo in processos:
                processo.join()

def main():
    print("Shell Python - Digite 'exit' para sair")
    
    while True:
        try:
            line = input("> ").strip()
            if line:  
                analisar_e_executar(line)
        except EOFError:
            print("\nEncerrando shell.")
            break
        except KeyboardInterrupt:
            print("\nInterrompido.")
            continue

if __name__ == "__main__":
    main()