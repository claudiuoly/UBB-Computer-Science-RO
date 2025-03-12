bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ;[(e+f-g)+(b+c)*3]/5
    a db 1
    b db 1
    c db 1
    d db 1
    
    e dw 1
    f dw 1
    g dw 3
    h dw 1
; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        mov eax, 0
        mov ebx, 0
        mov ecx, 0
        mov edx, 0
        
        mov ax, [e] ;ax = 1
        mov bx, [f] ;bx = 1
        
        add ax, bx ;ax = e+f
        
        mov cx, [g]
        sub ax, cx; ax = (e+f-g)
        
        mov dl, [b] ;dl = b
        mov bx, 0 ;bx= 0
        mov bl, [c] ;bl = c
        
        add dl, bl ; dl = b+c
        
        mov ecx, eax  ;ecx = (e+f-g)
        mov eax, 0
        mov ax, dx ;ax = b+c
        mov bl, 3 ;bl = 3
        mul bl ;ax = (b+c)*3
        
        add ax, cx 
        
        mov ecx, 0
        mov edx, 0
        mov cx, 5
        div cx
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
