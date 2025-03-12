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
    ; 17) (c+d-a)-(d-c)-b
    ; a - byte, b - word, c - double word, d - qword - Interpretare cu semn
    
    a DB 31
    b DW 1241
    c DD 17128
    d DQ 12421
    
    temp1 DQ 0
    temp2 DQ 0
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
    
        ; (c + d - a)
        MOV EAX, [c] ; EAX = c
        CDQ ; Extinde semnul lui EAX în EDX:EAX
        MOV EBX, [d] ; EBX = partea inferioara a lui d
        MOV ECX, [d+4] ; ECX = partea superioara a lui d
        ADD EAX, EBX ; EAX = c + partea inferioara a lui d
        ADC EDX, ECX ; EDX:EAX = c + d
        
        MOV AL, [a] ; a (byte) in AL
        CBW ; Extinde semnul lui AL in AX
        CWDE ; Extinde semnul lui AX in EAX

        SUB EAX, EBX ; EAX = c + d - a
        SBB EDX, 0 ; EDX:EAX = c + d - a (tine cont de CF)

        ; (d - c)
        MOV EBX, [d] ; EBX = partea inferioara a lui d
        MOV ECX, [d+4] ; ECX = partea superioara a lui d
        
        MOV [temp2], EBX
        MOV [temp2+4], ECX
        
        MOV EBX, [c]
        CDQ
        
        SUB [temp2], EBX 
        SBB [temp2], ECX

        MOV EBX, 0
        MOV ECX, 0
        
        MOV EBX, [temp1]
        MOV ECX, [temp1+4]
        
        ;SUB EBX, [c] ; EBX = partea inferioara a lui d - c
        ;SBB ECX, 0 ; ECX:EBX = d - c

        ; (c + d - a) - (d - c)
        sub EAX, EBX ; Scadere partea inferioara
        sbb EDX, ECX ; Scadere partea superioara, cu împrumut 

        ; - b
        MOV [temp1], EAX
        MOV [temp1+4], EDX

        MOV EAX, [b] 
        CDQ

        SUB [temp1], EAX 
        SBB [temp1], EDX

        MOV EAX, 0
        MOV EDX, 0
        
        MOV EAX, [temp1]
        MOV EDX, [temp1+4]

        ; Rezultatul final este acum în EDX:EAX
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
