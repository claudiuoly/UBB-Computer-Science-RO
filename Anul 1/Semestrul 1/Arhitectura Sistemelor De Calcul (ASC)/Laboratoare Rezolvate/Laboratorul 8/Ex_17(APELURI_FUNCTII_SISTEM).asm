bits 32
global start
extern exit, printf, scanf
import exit msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll
segment data use32 class=data
    ;Sa se citeasca de la tastatura un numar in baza 10 si sa se afiseze valoarea acelui numar in baza 16
    n dd 0
    message db "n = ", 0  ; mesajul pentru afisare
    format db "%d", 0   ; formatul pentru scanf
    hex_format db "Hexadecimal: %X", 10, 0  ; formatul pentru afisarea in hexadecimal

segment code use32 class=code
start:
    ; Afis mesajul "n = "
    push dword message ; pun pe stiva adresa mesajului
    call [printf] ; apelez printf pentru a afisa mesajul
    add esp, 4

    ; Citesc valoarea numarului n
    push dword n ; pun pe stiva adresa variabilei n
    push dword format ; pun pe stiva formatul pentru scanf
    call [scanf] ; apelez scanf pentru a citi numarul in n
    add esp, 8

    ; Afisez valoarea in hexadecimal
    mov eax, [n] ; incarc valoarea din n în registrul EAX
    push dword eax ; pun valoarea din EAX pe stiva
    push dword hex_format ; pun formatul de afisare pe stiva
    call [printf] ;apelez printf pentru a afisa numarul in hexazecimal
    add esp, 8

    ; Exit din program
    push dword 0        ; punem 0 pe stiva (codul de iesire)
    call [exit]         ; apelăm exit pentru a închide programul
