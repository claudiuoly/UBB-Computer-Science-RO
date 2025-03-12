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
    ;17) h/a + (2 + b) + f/d – g/c
    ;a,b,c,d-byte, e,f,g,h-word\
    
    a db 5 ;exemplu de valoare pentru a (byte)
    b db 3 ;exemplu de valoare pentru b (byte)
    c db 4 ;exemplu de valoare pentru c (byte)
    d db 2 ;exemplu de valoare pentru d (byte)
    h dw 100 ;exemplu de valoare pentru h (word)
    f dw 50 ;exemplu de valoare pentru f (word)
    g dw 40 ;exemplu de valoare pentru g (word)

; our code starts here
segment code use32 class=code
    start:
    
    ; (h/a)
    MOV AX, [h] ; AX = 100
    MOV BL, [a] ; BL = 5
    DIV BL ; AX = AX / BL {AX = AL - partea intreaga & AH - restul}
    MOV CX, AX ; CX = AX

    ; (2 + b)
    MOV AL, [b] ; AL = 3
    ADD AL, 2    ; AL = 2 + b
    ADD CX, AX   ; CX = (h/a) + (2 + b)

    ; f/d
    MOV AX, [f] ; AX = 50
    MOV BL, [d] ; BL = 2
    DIV BL       ; AX = AX / BL {AX = AL - partea intreaga & AH - restul}
    ADD CX, AX   ; CX = (h/a) + (2 + b) + (f/d)

    ; g/c
    MOV AX, [g] ; AX = 40
    MOV BL, [c] ; BL = 4
    DIV BL       ; AX = AX / BL {AX = AL - partea intreaga & AH - restul}
    SUB CX, AX   ; cx = (h/a) + (2 + b) + (f/d) - (g/c)
    
    ;REZULTATUL ESTE IN CX
        
    ; exit(0)
    push    dword 0      ; push the parameter for exit onto the stack
    call    [exit]       ; call exit to terminate the program
