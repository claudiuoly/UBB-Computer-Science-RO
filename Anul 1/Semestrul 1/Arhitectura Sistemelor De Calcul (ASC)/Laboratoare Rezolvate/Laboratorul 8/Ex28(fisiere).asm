bits 32 

global start

extern exit, printf, fgets
import exit msvcrt.dll
import printf msvcrt.dll
import fgets msvcrt.dll

segment data use32 class=data
    mesaj_introducere db 'Introduceti cuvintele (introduceti "$" pentru a termina): ', 0
    lungime_mesaj_introducere equ $-mesaj_introducere
    format_cuvant db '%s', 0

segment bss use32 class=data
    cuvinte resb 1024 ; spatiu pentru maxim 1024 caractere (inclusiv '\n' si '\0')
    contor resd 1

segment code use32 class=code
    start:

        ; afisam mesajul de introducere
        push dword lungime_mesaj_introducere 
        push dword mesaj_introducere
        push dword 1
        push dword 4
        call [printf]
        add esp, 16

        mov edi, cuvinte ; edi va pointa catre inceputul buffer-ului de cuvinte
        mov dword [contor], 0 ; initializam contorul

    citire_cuvant:
        ; citim un cuvant de la tastatura (maxim 255 caractere)
        push dword 0 ; stdin
        push dword 255
        push edi
        call [fgets]
        add esp, 12

        ; verificam daca primul caracter este '$'
        cmp byte [edi], '$'
        je afisare_cuvinte

        ; incrementam contorul de cuvinte
        inc dword [contor]

        ; avansam pointerul edi la urmatorul spatiu disponibil in buffer
        mov esi, edi
        cautare_sfarsit_cuvant:
            cmp byte [esi], 0
            je gasit_sfarsit_cuvant
            inc esi
            jmp cautare_sfarsit_cuvant
        gasit_sfarsit_cuvant:
            inc esi ; trecem peste terminatorul null
            mov edi, esi

        jmp citire_cuvant

    afisare_cuvinte:
        mov esi, cuvinte
        mov ecx, dword [contor]

    afisare_cuvant:
        cmp ecx, 0
        je final

        ; afisam cuvantul curent
        push esi
        push dword format_cuvant
        push dword 1
        push dword 4
        call [printf]
        add esp, 16

        ; avansam pointerul esi la urmatorul cuvant
        cautare_sfarsit_cuvant_2:
            cmp byte [esi], 0
            je gasit_sfarsit_cuvant_2
            inc esi
            jmp cautare_sfarsit_cuvant_2
        gasit_sfarsit_cuvant_2:
            inc esi ; trecem peste terminatorul null

        dec ecx
        jmp afisare_cuvant

    final:
        ; iesim din program
        push dword 0
        call [exit]