bits 32

global start

extern scanf, fprintf, fopen, fclose, exit, find_max
import scanf msvcrt.dll
import fprintf msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import exit msvcrt.dll
;Se citeste de la tastatura un sir de numere in baza 10 fara semn. Sa se determine valoarea maxima din sir si
;sa se afiseze in fisierul max.txt (fisierul va fi creat) valoarea maxima, in baza 16
segment data use32 class=data
    filename db "max.txt", 0
    mode db "w", 0
    format_read db "%u", 0  ; %u pentru numere fara semn
    format_write db "%x", 0  ; %x pentru afisare in baza 16
    max_value dd 0
    temp_value dd 0 ; Variabila temporara pentru a stoca valoarea citita

   
segment code use32 class=code
start:
    ;Deschid fișierul max.txt
    push dword mode
    push dword filename
    call [fopen]
    add esp, 8
    cmp eax, 0
    je exit_program
    mov ebx, eax ;Salvam in EBX

    ;Citesc primul numar si il iau maximul initial
    push dword max_value
    push dword format_read
    call [scanf]
    add esp, 8

read_loop:
    ;Citesc urmatorul numar in variabila temporara
    push dword temp_value
    push dword format_read
    call [scanf]
    add esp, 8

    ;Elimin valoarea citita de pe stiva
    pop eax 

    ;Verific daca s-a introdus 0
    cmp dword [temp_value], 0 
    je write_max

    ;Apelez find_max
    push dword [temp_value]  ;pe stiva al doilea nr
    push dword [max_value]   ;pe stiva primul nr
    call find_max            ;apelez
    add esp, 8               ;eliberare stiva
    mov [max_value], eax     ;salvare maxim

    jmp read_loop

write_max:
    ;Scriu valoarea maxima in fisier
    push dword [max_value]
    push dword format_write
    push dword ebx
    call [fprintf]
    add esp, 12

    ;Inchid fisierul
    push dword ebx
    call [fclose]
    add esp, 4

exit_program:
    push dword 0
    call [exit]