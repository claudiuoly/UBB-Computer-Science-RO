bits 32
global start        
extern exit, printf, scanf
import exit msvcrt.dll  
import printf msvcrt.dll
import scanf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; Mesage generice
    msg_general db "Calculul expresiei: (a/b)*k afisat in baza 10", 10, 0
    msg_num1 db "Introduceti primul numar: ", 0
    msg_num2 db "Introduceti al doilea numar: ", 0
    msg_suma db "Rezultatul este: %d", 10, 0
    
    ;Varibile
    num1 dd 0
    num2 dd 0
    format db "%d", 0
    k dd 3
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;Afisare primul mesaj
        push dword msg_general
        call [printf]
        add esp, 4
       
        ;Afisare al doilea mesaj
        push dword msg_num1
        call [printf]
        add esp, 4
        
        ;Introdu al doilea nr
        push dword num1
        push dword format
        call [scanf]
        add esp, 4 * 2
        
        ;Afisare al doilea mesaj
        push dword msg_num2
        call [printf]
        add esp, 4
        
        ;Introdu al doilea nr
        push dword num2
        push dword format
        call [scanf]
        add esp, 4 * 2
        
        ;Solutie
        mov eax, [num1]
        mov ebx, [num2]
        mov edx, 0
        div ebx
        
        
        mov ecx, [k]
        mul ecx
        
        ;Afisare al treilea mesaj
        push eax
        push dword msg_suma
        call [printf]
        add esp, 4 * 2
      
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
