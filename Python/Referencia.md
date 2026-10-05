# Referência Python — Scanner de Portas

## Socket / rede

- `socket.socket(socket.AF_INET, socket.SOCK_STREAM)` → cria o "telefone" pra conexão. `AF_INET` = internet/IPv4, `SOCK_STREAM` = TCP. Sempre essa receita pra porta TCP.
- `s.settimeout(1)` → quanto tempo (segundos) esperar antes de desistir. Impede travar numa porta que não responde.
- `s.connect_ex((host, porta))` → tenta conectar e **devolve um número**: 0 = conectou (aberta), outro = falhou. *Não quebra.* Use pra **testar** se está aberta.
- `s.connect((host, porta))` → tenta conectar e **quebra** se falhar. Use quando já sabe que está aberta e quer conversar.
- `s.send(b"...")` → **envia** dados pro serviço (você falando). O `b` transforma texto em bytes.
- `s.recv(1024)` → **recebe** até 1024 bytes que o serviço mandou (você ouvindo). Devolve bytes.
- `s.close()` → fecha a conexão. **Sempre com `()`** — sem os parênteses não executa.

## Texto / string

- `texto.strip()` → remove espaços e quebras de linha das pontas. Essencial ao ler arquivo.
- `texto.split(".")` → quebra o texto numa lista pelo separador. `"1.2.3".split(".")` → `['1','2','3']`.
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

## Arquivos

- `open("arq.txt")` → abre pra **ler** (padrão).
- `open("arq.txt", "w")` → abre pra **escrever**, apagando o conteúdo antigo.
- `open("arq.txt", "a")` → abre pra **adicionar** no fim, sem apagar.
- `with open(...) as f:` → abre e **fecha automaticamente** no fim do bloco. Recomendado.
- `f.write("texto\n")` → escreve no arquivo. **Não pula linha sozinho** — por isso o `\n`.
- `for linha in arquivo:` → percorre o arquivo linha por linha.

## Dicionário

- `{chave: valor}` → cria o dicionário. Ex: `{80: "HTTP"}`.
- `dic[chave]` → pega o valor pela chave. **Quebra** (`KeyError`) se não existir.
- `dic.get(chave, padrao)` → pega o valor; se não existir, devolve o padrão. Mais seguro.

## Listas

- `[1, 2, 3]` → cria lista.
- `lista.append(x)` → adiciona `x` no fim. Não usa índice.
- `lista[0]` → acessa por posição (começa no **zero**). `lista[-1]` = último.
- `x in lista` → testa se `x` está na lista.

## Laços e controle

- `for item in colecao:` → percorre os **itens** (o padrão).
- `for i in range(1, 1025):` → gera 1 a 1024 (vai até *um antes* do segundo). Use pra **contar/varrer**.
- `while condicao:` → repete enquanto for verdadeira.
- `if / elif / else` → decisões. Para no primeiro verdadeiro.
- `and` / `or` / `not` → combina condições (todas / pelo menos uma / inverte).

## Funções e estrutura

- `def nome(parametro):` → define função. Parâmetro = na definição; argumento = o valor passado.
- `return valor` → **devolve** pra quem chamou. Diferente de `print`, que só mostra.
- `funcao()` → **executa** (com parênteses). `funcao` sozinho só menciona.
- `if __name__ == "__main__":` → o bloco só roda quando o arquivo é executado direto.
- `from arquivo import funcao` → traz uma função de outro arquivo.

## Tratamento de erro

- `try: ... except TipoDoErro: ...` → tenta; se der o erro, faz o except em vez de quebrar.
- `except ValueError:` → captura **um tipo específico**. Use quando quer distinguir erros.
- `except Exception:` → captura **qualquer** erro. Use quando toda falha leva à mesma reação. Cuidado: esconde bugs.
- `except Exception as e:` → captura e guarda em `e`, pra *ver* qual foi (`print(e)`). Truque de depuração.

## Comparação (pegadinhas)

- `=` → **atribui** valor. `x = 5`.
- `==` → **compara**. `x == 5` pergunta "x é igual a 5?".
- `!=` → diferente. `<` `>` `<=` `>=` → comparações.