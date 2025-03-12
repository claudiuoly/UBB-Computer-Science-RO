bits 32

global start        
extern exit, printf, scanf
import exit msvcrt.dll  
import printf msvcrt.dll
import scanf msvcrt.dll

segment data use32 class=data
    ; Sa se citeasca de la tastatura doua numere (in baza 10) si sa se calculeze produsul lor. Rezultatul inmultirii se va salva in memorie in variabila 
    ;"rezultat" (definita in segmentul de date).
    ;format db "Ana are %d mere", 0
    msg1 db "Introduceti primul numar: ", 0
    msg2 db "Introduceti al doilea numar: ", 0
    
    num1 dd 0
    num2 dd 0
    rezultat dd 0
    
    format  db "%d", 0
segment code use32 class=code
    start:
        ; ...        
        
        push dword msg1
        call [printf]
        add esp, 4
        
        push dword num1
        push dword format
        call [scanf]
        add esp, 4*2
        
        push dword msg2
        call [printf]
        add esp, 4
        
        push dword num2
        push dword format
        call [scanf]
        add esp, 4*2
        
        mov eax, [num1]
        imul dword [num2]
        
        mov [rezultat], eax
        
        
        push dword [rezultat]
        push dword format
        call [printf]
        add esp, 4 * 2
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
