bits 32
segment code use32 public code
global find_max

;find_max primeste doua numere ca parametri pe stiva
;si returneaza maximul dintre ele in EAX
find_max:
    mov eax, [esp+4]  ;primul nr
    cmp eax, [esp+8]  ;comparam cu al doilea nr
    jge end_find_max  ;daca primul este mai mare sau egal, gata
    mov eax, [esp+8]  ;altfel, maximul este al doilea nr
end_find_max:
    ret 8             ; Eliberam 8 bytes de pe stiva (doi parametri)