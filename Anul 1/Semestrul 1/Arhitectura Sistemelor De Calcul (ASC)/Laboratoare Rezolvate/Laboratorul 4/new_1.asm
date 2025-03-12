bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...

    ;17) Se dau cuvantul A si octetul B. Sa se obtina dublucuvatul C:
    ;bitii 0-3 ai lui C au valoarea 1
    ;bitii 4-7 ai lui C coincid cu bitii 0-3 ai lui A
    ;bitii 8-13 ai lui C au valoarea 0
    ;bitii 14-23 ai lui C coincid cu bitii 4-13 ai lui A
    ;bitii 24-29 ai lui C coincid cu bitii 2-7 ai lui B
    ;bitii 30-31 au valoarea 1
        
   ; 1000 0101 0101 0010 0011 0000 0100 1111 = 8 5 5 2 3 0 4 F
    
   ; A = 0001 0010 0011 0100
   ; B = 0000 0000 0101 0110

    A DW 1234h      ; Cuvantul A (exemplu)
    B DB 56h        ; Octetul B (exemplu)
    C DD 0          ; Dublucuvântul C (initializat cu 0)

; our code starts here
segment code use32 class=code
    start:
        ; ...
        ; Pun in ecx valoarea lui C (initial 0)
        mov ecx, [C]
      
        ; Setez bitii 0-3 ai lui C la 1
        or ecx, 0x0000000F
        
        ; Curat registrul ebx
        xor ebx, ebx
        
        ; Mut cuvantul A in bx
        mov bx, [A]
        
        ; Extrag bitii 0-3 din A
        and bx, 0x000F
        
        ; Extind bx la 32 de biti (ebx)
        movzx ebx, bx
        
        ; Mut bitii 0-3 din A in pozitiile 4-7 din C
        shl ebx, 4
        
        ; Copiez bitii in C
        or ecx, ebx
        
        ; Curat registrul ebx
        mov bx, 0
        
        ; Mut cuvantul A in bx
        mov bx, [A]
        
        ; Extrag bitii 4-13 din A
        and bx, 0011111111110000b
        
        ; Extind bx la 32 de biti
        movzx ebx, bx
        
        ; Mut bitii 4-13 din A in pozitiile 14-23 din C
        rol ebx, 8
        
        ; Copiaz bitii in C
        or ecx, ebx
        
        ; Curat registrul ebx
        mov ebx, 0
        
        ; Mut octetul B in bx
        mov bx, [B]
        
        ; Extrag bitii 2-7 din B
        and bx, 0000000111111100b
        
        ; Extind bx la 32 de biti
        movzx ebx, bx
        
        ; Mut bitii 2-7 din B in pozitiile 24-29 din C
        rol ebx, 20
        
        ; Copiez bitii in C
        or ecx, ebx
        
        ; Setez bitii 30-31 ai lui C la 1
        mov eax, 0
        mov eax, 1000000000000000b
        rol eax, 16
        or ecx, eax
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
