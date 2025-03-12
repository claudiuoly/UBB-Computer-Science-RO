bits 32 
global start        
extern exit, printf, scanf            
import exit msvcrt.dll  
import printf msvcrt.dll
import scanf msvcrt.dll   

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    msg1 db "Introduceti primul numar: ", 0
    msg2 db "Introduceti al doilea numar: ", 0
    num1 dd 0
    num2 dd 0
    rezultat dd 0
    format  db "%d", 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;Afisare primul mesaj
        push dword msg1
        call [printf]
        add esp, 4
        
        ;Citire primul nr
        push dword num1
        push dword format
        call [scanf]
        add esp, 4*2
        
        ;Afisare al doilea mesaj
        push dword msg2
        call [printf]
        add esp, 4
        
        ;Citire al doilea mesaj
        push dword num2
        push dword format
        call [scanf]
        add esp, 4*2
        
        ;Operatii
        mov eax, [num1]
        add eax, [num2]
        
        mov ebx, [num1]
        sub ebx, [num2]
        
        mul ebx
        
        mov [rezultat], eax
        
        ;Afisare rezultat
        push dword [rezultat]
        push dword format
        call [printf]
        add esp, 4 * 2
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
