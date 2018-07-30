# Lexer

## Spécifications

Fonctionnalités implémentées :  
 - affection  
 - affichage d'expressions numériques  
 - instructions conditionnelles : __if__ et __else__  
 - structures itératives : __while__ et __for__  
 - gestion des erreurs  
 - gestion du type chaîne de caractères  
 - gestion des fonctions  
 - gestion de la déclaration implicite de variable  
 - gestion de la portée des variables  
 - gestion des fonctions récursives  
 - gestion des pointeurs  

## Utilisations

### Déclaration

Deux types d'instructions pour déclarer une variable :  
 - __var__ : accès en écriture et en lecture  
 - __const__ : accès en écriture  

### Types

Types supportés :  
 - nombre (entier et flottant sous sa forme décimale)  
 - chaîne de caractères  
 - pointeur  
 - fonction  

### Expression et fonction interne

#### Nombre

| + | - | * | / | ** | % | < | <= | > | >= | == | != |
|---|---|---|---|----|---|---|----|---|----|----|----|

#### Chaîne de caractères

 - __+__ : concatène deux chaînes de caractères  
 - __*__ : répète n fois la chaîne de caractères  
 - __str[n]__ : récupère le n -ème élément de la chaîne de caractères  
 - __str[n:m]__ : récupère une sous-chaîne à partir de la chaîne caractères principale incluse n et m (exclus)  
 - __str["test"]__ : recherche l'occurrence "test" dans la chaîne de caractères et renvoie la position de la première occurrence ou -1 si elle n'est pas trouvée  

```python
var a = "Hello";
print(a * 2); # HelloHello

print(a + " " + "world"); # Hello world

print(a[0]); # H

print(a["lo"]); # 2

print(a[1:4]); # ell
print(a[:4]); # Hell
print(a[3:]); # lo
```

#### Pointeur

 - __&__ : affectation par référence  

 ```python
var a = 1;
var b = &a;
print(b); # 1

&b = 2;
print(a); # 2
print(b); # 2
 ```

 #### Fonction

 ```python
def a() do print(1); end
a(); # 1

def sum(a, b) do print(a + b);
sum(1, 4); # 5

def b(a) do if(a < 4) then print(a); b(a + 1); end end
b(1); # 1, 2, 3
```

## Gestion des erreurs

|   |                        Error object                        | Message | Filename | Lineno |
|:-:|:----------------------------------------------------------:|:-------:|:--------:|:------:|
| 0 |                          Exception                         |    X    |          |        |
| 1 |                          PlyError                          |    X    |     X    |    X   |
| 2 | PlyInternalError PlyRangeError PlySyntaxError PlyTypeError |    X    |     X    |    X   |

Le constructeur __PlyError__ crée un objet d'erreur.  

### Syntaxe

__PlyError(frame, message)__  
Paramètres :  
 - frame : informations sur le frame actuel (filename, lineno...)  
 - message : description de l'erreur sous une forme lisible par un humain  

### Type d'erreurs

En plus du constructeur __PlyError__ générique, il existe quatre autres constructeurs d'erreurs.  

| PlyInternalError |                   Crée une instance représentant une erreur se produisant en relation avec la fonction globale runtime()                   |
|:----------------:|:------------------------------------------------------------------------------------------------------------------------------------------:|
|   PlyRangeError  | Crée une instance représentant une erreur se produisant quand une variable numérique ou un paramètre est en dehors de sa plage de validité |
|  PlySyntaxError  |                Crée une instance représentant une erreur de syntaxe se produisant lors d'une analyse de code dans runtime()                |
|   PlyTypeError   |            Crée une instance représentant une erreur se produisant quand une variable ou un paramètre n'est pas d'un type valide           | 
