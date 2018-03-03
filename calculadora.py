#!/usr/bin/python3

import sys

def suma(op1,op2):
	return op1 + op2;
def resta(op1,op2):
	return op1 - op2;
def multi(op1,op2):
	return op1 * op2;
def div(op1,op2):
	try:
		return (str(op1 / op2));
	except ZeroDivisionError:
		return("No se puede dividir entre 0.");

funciones = {"suma": suma, "resta": resta, "multi": multi, "div": div}

if __name__ == "__main__":

	funcion = sys.argv[1];
	op1 = sys.argv[2];
	op2 = sys.argv[3];

	try:
		resultado = funciones[funcion](float(op1), float(op2));
	except KeyError:
		sys.exit("Funcion " + funcion + " no definida");
		print("Funcion " + funcion + " no definida");
	print(resultado);



