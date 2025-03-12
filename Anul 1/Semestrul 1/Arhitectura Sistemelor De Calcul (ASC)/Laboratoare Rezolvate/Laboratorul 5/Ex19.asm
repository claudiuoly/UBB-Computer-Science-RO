bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; Se dau 2 siruri de octeti A si B. Sa se construiasca sirul R care sa contina doar elementele pare si negative din cele 2 siruri.
    ;Exemplu:
    ;A: 2, 1, 3, -3, -4, 2, -6
    ;B: 4, 5, -5, 7, -6, -2, 1
    ;R: -4, -6, -6, -2
        
        a db 2, 1, 3, -3, -4, 2, -6
        la equ ($-a)
   
        b db 4, 5, -5, 7, -6,-2, 1
        lb equ ($-b)
        
        r times (la+lb) db 0 ;FC, FA, FA, FE
        
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        ;CONDITIE: PARE & NEGATIVE
        
        mov eax, 0
        mov ebx, 0
        mov ecx, 0
        mov edx, 0
        
        mov esi, a
        mov edi, r
        mov edx, b
        
        mov ecx, la
        add ecx, lb
        
        loopy_a:
            cmp ecx, la
            
            jbe loopy_b
            
            mov al, [esi]
            inc esi
            cmp al, 0
            jg repeta
            mov bl, al
            and bl, 00000001b
            cmp bl, 1
            je repeta
            mov [edi], al
            inc edi
            loop loopy_a
            
        jmp final
            
        loopy_b:
            mov al, [edx]
            inc edx
            cmp al, 0
            jg repeta
            mov bl, al
            and bl, 00000001b
            cmp bl, 1
            je repeta
            mov [edi], al
            inc edi
            loop loopy_a
        
        repeta:
            loop loopy_a
           
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
