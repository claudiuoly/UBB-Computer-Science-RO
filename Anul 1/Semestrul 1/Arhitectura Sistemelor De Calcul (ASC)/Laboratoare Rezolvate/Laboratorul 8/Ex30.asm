bits 32 
global start        
extern exit, printf, scanf            
import exit msvcrt.dll  
import printf msvcrt.dll
import scanf msvcrt.dll   

segment data use32 class=data
    num1 dd 0
    rezultat dd 0
    format_citire db "%d", 0
    format_afisare db "Cel mai mic numar este: %d", 10, 0
    first_number db 1     ; flag pentru primul număr

segment code use32 class=code
    start:
        mov ebx, 0      ; ebx va păstra minimul
        
    citeste:
        push dword num1
        push dword format_citire
        call [scanf]
        add esp, 4 * 2
        
        cmp dword [num1], 0   ; verificăm dacă s-a introdus 0
        je afisare
        
        cmp byte [first_number], 1  ; verificăm dacă e primul număr
        jne compara
        mov ebx, [num1]        ; dacă e primul număr, îl punem direct în ebx
        mov byte [first_number], 0   ; resetăm flag-ul
        jmp citeste
        
    compara:
        cmp ebx, [num1]        ; comparăm minimul curent cu noul număr
        jle citeste            ; dacă minimul e mai mic sau egal, citim următorul număr
        mov ebx, [num1]        ; dacă noul număr e mai mic, actualizăm minimul
        jmp citeste
        
    afisare:
        push ebx               ; punem minimul pe stivă
        push dword format_afisare
        call [printf]
        add esp, 4 * 2
        
        push dword 0      
        call [exit]