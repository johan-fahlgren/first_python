from typing import Callable

def johan() -> str:
    return "johan"

def Jocke() -> str:
    return "Jocke"

#Callable gör inget, berättar för IDE att function(variabeln) är callable.
def callback(function: Callable):
    print(function())

callback(johan)