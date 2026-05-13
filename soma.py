import argparse

parser = argparse.ArgumentParser()

parser.add_argument("binario_1")
parser.add_argument("binario_2")

args = parser.parse_args()

print(args.nome)
print(args.idade)

