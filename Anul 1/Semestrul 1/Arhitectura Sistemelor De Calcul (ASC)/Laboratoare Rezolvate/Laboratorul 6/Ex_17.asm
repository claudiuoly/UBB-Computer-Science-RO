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
    ;17)
    ;Se da un sir de dublucuvinte. Sa se ordoneze descrescator sirul cuvintelor inferioare ale acestor dublucuvinte. Cuvintele superioare raman neschimbate.
        ;Exemplu:
            ;dandu-se: sir DD 12345678h 1256ABCDh, 12AB4344h
            ;rezultatul va fi: 1234ABCDh, 12565678h, 12AB4344h.
    sir dd 12345678h, 1256ABCDh, 12AB4344h
    len equ ($ - sir) / 4 ;

; our code starts here
segment code use32 class=code
    start:
        ; ...
    
        mov ecx, len ; Initializez contorul buclei externe
        dec ecx    ; Decrementez contorul pentru indexare de la 0

    prima_bucla:
        push ecx ; Salvez contorul buclei externe pe stiva

        mov esi, sir ; Mut adresa de inceput a sirului in esi
        

    a_doua_bucla:
        mov eax, [esi] ; Incarc dublucuvantul curent in eax
        mov edx, [esi+4] ; Incarc urmatorul dublucuvant in edx

        ; Extrag cuvintele inferioare
        and eax, 0FFFFh 
        and edx, 0FFFFh

        cmp eax, edx ; Compar cuvintele inferioare
        jae nu_schimba; Daca sunt deja in ordine descrescatoare, sar peste interschimbare
        
        ; Interschimb cuvintele inferioare
        mov ax, dx ; Mut cuvantul inferior din edx in ax
        mov dx, word [esi] ; Mut cuvantul inferior din [esi] in dx
        mov word [esi], ax ; Salvez noul cuvant inferior in [esi]
        mov word [esi+4], dx ; Salvez noul cuvant inferior in [esi+4]

        nu_schimba:
        ; Mut pointerul la urmatorul dublucuvant
        add esi, 4 
        ; Repeta bucla interna
        loop a_doua_bucla 

        ; Restaurez contorul buclei externe de pe stiva
        pop ecx 
        ; Repeta bucla externa
        loop prima_bucla 
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
