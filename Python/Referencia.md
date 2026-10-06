# Referência Python — Scanner de Portas

## Socket / rede

- `socket.socket(socket.AF_INET, socket.SOCK_STREAM)` → cria o "telefone" pra conexão. `AF_INET` = internet/IPv4, `SOCK_STREAM` = TCP. Sempre essa receita pra porta TCP.
- `s.settimeout(1)` → quanto tempo (segundos) esperar antes de desistir. Impede travar numa porta que não responde.
- `s.connect_ex((host, porta))` → tenta conectar e **devolve um número**: 0 = conectou (aberta), outro = falhou. *Não quebra.* Use pra **testar** se está aberta.
- `s.connect((host, porta))` → tenta conectar e **quebra** se falhar. Use quando já sabe que está aberta e quer conversar.
- `s.send(b"...")` → **envia** dados pro serviço (você falando). O `b` transforma texto em bytes.
- `s.recv(1024)` → **recebe** até 1024 bytes que o serviço mandou (você ouvindo). Devolve bytes.
- `s.close()` → fecha a conexão. **Sempre com `()`** — sem os parênteses não executa.
- `socket.gethostbyname("host")` → traduz um nome ou IP no endereço IP real (resolução de nome/DNS). Devolve o IP, ou quebra com `socket.gaierror` se o host não resolve. Use pra validar host.

## Texto / string

- `texto.strip()` → remove espaços e quebras de linha das pontas. Essencial ao ler arquivo.
- `texto.split(".")` → quebra o texto numa lista pelo separador. `"1.2.3".split(".")` → `['1','2','3']`.
- `texto.split("\n")` → quebra um texto de várias linhas numa lista de linhas.
- `texto.startswith("Server:")` → devolve `True` se o texto começa com aquilo. Método embutido, não precisa importar.
- `texto.upper()` / `texto.lower()` → maiúsculas / minúsculas.
- `texto.replace(a, b)` → troca todas as ocorrências de `a` por `b`.
- `len(texto)` → quantos caracteres. Também funciona em lista (quantos itens).
- `bytes.decode(errors="ignore")` → traduz bytes (da rede) em texto. O `errors="ignore"` pula bytes estranhos sem quebrar.
- `f"... {variavel} ..."` → f-string: insere valores no texto. O `f` antes das aspas ativa as chaves.

## Conversão de tipo

- `int("80")` → texto vira número inteiro. Quebra com `ValueError` se não for número.
- `str(80)` → número vira texto.

## Entrada / saída

- `input("pergunta: ")` → mostra a pergunta, devolve o que foi digitado (**sempre texto**).
- `print(...)` → mostra na tela. Pula linha sozinho.

## Arquivos e caminhos

- `open("arq.txt")` → abre pra **ler** (padrão).
- `open("arq.txt", "w")` → abre pra **escrever**, apagando o conteúdo antigo.
- `open("arq.txt", "a")` → abre pra **adicionar** no fim, sem apagar.
- `with open(...) as f:` → abre e **fecha automaticamente** no fim do bloco. Recomendado.
- `f.write("texto\n")` → escreve no arquivo. **Não pula linha sozinho** — por isso o `\n`.
- `for linha in arquivo:` → percorre o arquivo linha por linha.
- `from pathlib import Path` + `Path(__file__).parent` → a pasta onde o script mora. Use pra abrir arquivos que ficam junto do script, de qualquer lugar que você rode. Monta caminho com barra: `pasta / "subpasta" / "arq.txt"`.

## Dicionário

- `{chave: valor}` → cria o dicionário. Ex: `{80: "HTTP"}`.
- `dic[chave]` → pega o valor pela chave. **Quebra** (`KeyError`) se não existir.
- `dic.get(chave, padrao)` → pega o valor; se não existir, devolve o padrão. Mais seguro.

## Listas e tuplas

- `[1, 2, 3]` → cria lista.
- `lista.append(x)` → adiciona `x` no fim. Não usa índice.
- `lista[0]` → acessa por posição (começa no **zero**). `lista[-1]` = último.
- `x in lista` → testa se `x` está na lista.
- `lista.sort()` → ordena a lista no lugar. Numa lista de tuplas, ordena pelo 1º item de cada.
- `(porta, servico, banner)` → tupla: agrupa valores relacionados. Desempacota com `a, b, c = tupla`.
- `[expr for item in colecao]` → list comprehension: cria lista num `for` de uma linha. Igual a um `for` com `.append`, só compacto.

## Laços e controle

- `for item in colecao:` → percorre os **itens** (o padrão).
- `for i in range(1, 1025):` → gera 1 a 1024 (vai até *um antes* do segundo). Use pra **contar/varrer**.
- `while True:` → repete pra sempre; sai com `return` ou `break`. Útil pra insistir até a entrada ser válida.
- `if / elif / else` → decisões. Para no primeiro verdadeiro.
- `and` / `or` / `not` → combina condições (todas / pelo menos uma / inverte).
- `1 <= x <= 65535` → comparação encadeada: testa os dois limites de uma vez.
- `a, b = b, a` → troca o valor de duas variáveis numa linha.

## Funções e estrutura

- `def nome(parametro):` → define função. Parâmetro = na definição; argumento = o valor passado.
- `return valor` → **devolve** pra quem chamou. Diferente de `print`, que só mostra. Também **encerra a função na hora**.
- `funcao()` → **executa** (com parênteses). `funcao` sozinho só menciona (passa a função sem executar).
- `if __name__ == "__main__":` → o bloco só roda quando o arquivo é executado direto.
- `from arquivo import funcao` → traz uma função de outro arquivo.
- Padrão de busca: `for` procurando, `return` dentro do `if` quando acha, `return padrao` **fora** do `for` como plano B.

## Threads (execução paralela)

- `from concurrent.futures import ThreadPoolExecutor`
- `with ThreadPoolExecutor(max_workers=100) as executor:` → cria uma equipe de 100 threads que trabalham ao mesmo tempo.
- `executor.submit(funcao, arg1, arg2)` → entrega a tarefa pra equipe. Função **sem parênteses** (a thread é que executa). Devolve um "futuro" (promessa de resultado).
- `futuro.result()` → cobra o resultado da tarefa; espera se ainda não terminou.
- **Padrão:** submeta TODAS as tarefas primeiro (viram paralelas), depois recolha os resultados. Inverter vira fila sequencial.
- Threads brilha quando o gargalo é **espera** (rede, timeout), não cálculo. No `localhost` o ganho é pequeno porque não há espera.
- **Zona crítica / race condition:** quando várias threads escrevem no mesmo recurso ao mesmo tempo → dados corrompidos. Soluções: proteger com `Lock` (cadeado), ou coletar tudo e escrever no fim numa thread só.

## Tratamento de erro

- `try: ... except TipoDoErro: ...` → tenta; se der o erro, faz o except em vez de quebrar.
- `except ValueError:` → captura **um tipo específico**. Use quando quer distinguir erros.
- `except socket.gaierror:` → erro de host que não resolve (resolução de nome falhou).
- `except Exception:` → captura **qualquer** erro. Use quando toda falha leva à mesma reação. Cuidado: esconde bugs.
- `except Exception as e:` → captura e guarda em `e`, pra *ver* qual foi (`print(e)`). Truque de depuração.
- `raise ValueError("msg")` → dispara um erro de propósito. Use pra bug interno; pra erro de usuário, prefira mensagem amigável.

## Comparação (pegadinhas)

- `=` → **atribui** valor. `x = 5`.
- `==` → **compara**. `x == 5` pergunta "x é igual a 5?".
- `!=` → diferente. `<` `>` `<=` `>=` → comparações.