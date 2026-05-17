# Pensamentos, Ideia, Linhas de Raciocínio

## Ideia do mini projeto

Estudando sobre como realmente funcionam memórias e o computador em si (estudo esse mais voltado para PWN, já que acredito ser um processo importante para quem quer entender o quão baixo nível um computador realmente é), me passou uma questão que nunca tinha parado realmente para pensar. Isso aconteceu enquanto eu voltava a revisar sobre portas lógicas.

A questão é a seguinte: somas binárias e operações básicas feitas por computadores não são realizadas exatamente como uma soma comum do dia a dia. Por se tratarem de binários, não precisamos — e nem usamos diretamente — operadores aritméticos como o `+`.

---

## E como isso é possível?

Imagine que temos uma soma simples:

```text
5 + 3
```

Em binário, teremos:

```text
0101 + 0011
```

Para fazer essa soma, basicamente precisamos de:

* uma variável para guardar o carry (o famoso “vai um” da matemática tradicional);
* e operações lógicas, principalmente o operador XOR (`⊕`).

O XOR (“OU exclusivo”) retorna `True` apenas quando os dois valores comparados são diferentes.

### Tabela verdade do XOR

| A | B | A ⊕ B |
| - | - | ----- |
| 0 | 0 | 0     |
| 0 | 1 | 1     |
| 1 | 0 | 1     |
| 1 | 1 | 0     |

---

Agora imagine que vamos comparar os bits da direita para a esquerda.

Temos:

```text
0101
0011
```

### Primeiro bit

```text
1 ⊕ 1 = 0
```

Como tivemos `1` e `1`, o resultado será `0`, mas geramos um carry (`vai um`).

Resultado atual:

```text
0
```

Carry:

```text
1
```

---

### Segundo bit

Agora temos:

* `0` vindo do primeiro número;
* `1` vindo do segundo número;
* e `1` vindo do carry.

Primeiro fazemos:

```text
1 ⊕ 0 = 1
```

Mas ainda precisamos considerar o carry:

```text
1 ⊕ 1 = 0
```

Então o resultado final desse bit continua sendo `0`, e ainda mantemos `1` no carry.

Resultado atual:

```text
00
```

Carry:

```text
1
```

---

### Terceiro bit

Agora temos novamente:

* `1` do primeiro número;
* `0` do segundo;
* `1` no carry.

Ou seja, exatamente o mesmo cenário anterior.

Resultado:

```text
0
```

E continuamos com carry `1`.

Resultado atual:

```text
000
```

---

### Último bit

Agora temos:

```text
0 ⊕ 0 = 0
```

Diferente do caso `1 ⊕ 1`, aqui não geramos novo carry.

Mas ainda existe o carry anterior guardado.

Então fazemos:

```text
1 ⊕ 0 = 1
```

Resultado final:

```text
1000
```

Que representa `8` em decimal.

---

## Montando o código

* Primeiro precisamos receber os valores propostos pelo usuário. Pensei inicialmente em utilizar `input()`, mas acabei preferindo `argparse`, já que isso facilita bastante testar diretamente pela CLI.

* Depois de receber os valores via argumentos da linha de comando (como strings), transformei os dois em listas usando `list()`. Isso me ajudaria na validação, na inversão da ordem dos bits e na iteração durante os loops.

* Após isso, fiz uma validação para garantir que os valores fossem compostos apenas por `0` e `1`.

* Depois da validação, parti para uma feature que achei interessante: mostrar também o valor decimal dos binários inseridos. Assim nasceu a função `binary_array_to_decimal`, que percorre os bits e soma `2^index` sempre que encontra um bit igual a `1`.

* Antes de criar a função `binary_sum` (responsável por realizar a soma sem usar operadores aritméticos), percebi a necessidade de garantir que os dois binários possuíssem o mesmo tamanho. Afinal, a lógica da soma depende da comparação entre os bits de cada posição. Assim nasceu a função `make_binary_arrays_has_the_same_length`.

* Durante os testes, precisei corrigir a função `binary_array_to_decimal`, porque ela fazia `.reverse()` no array, mas não revertia novamente antes de sair da função. Inicialmente imaginei que o `reverse()` afetaria apenas o escopo interno da função, mas descobri que ele modifica diretamente a lista original.

* Durante a criação da função `binary_sum`, percebi também que a função de equalização precisava garantir espaço suficiente para possíveis carries finais. Sem isso, somas como:

```text
111 + 111
```

poderiam gerar problemas.

Por isso, caso os binários começassem com `1`, adicionei um `0` extra na frente dos dois números para prevenir overflow de tamanho:

```text
0111 + 0111 = 1110
```

Assim, tanto os operandos quanto o resultado continuam compatíveis em tamanho.

* A lógica principal por trás da função `binary_sum` foi explicada anteriormente na seção “E como isso é possível?”.

* Um bug lógico importante foi encontrado dentro da função `make_binary_arrays_has_the_same_length`. Ele aparecia quando os dois binários tinham tamanhos diferentes e o maior terminava com bit `1`.

Exemplo:

```text
Menor: 0101
Maior: 11011
```

O problema acontecia porque a lógica responsável por adicionar um `0` extra no início do binário maior não estava revertendo corretamente a lista antes do `append("0")`.

Isso fazia com que:

```text
11011
```

se transformasse em:

```text
110110
```

quando o correto seria:

```text
011011
```

* Outro erro corrigido foi dentro da função `binary_sum`, onde eu acabava comparando o bit atual com `0` (inteiro) ao invés de `"0"` (string), já que os bits estavam armazenados dentro de listas de strings.

