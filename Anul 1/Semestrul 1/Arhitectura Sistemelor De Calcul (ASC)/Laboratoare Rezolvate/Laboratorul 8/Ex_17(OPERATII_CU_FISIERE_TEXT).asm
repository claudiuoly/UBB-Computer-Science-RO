bits 32

global start
extern exit, fopen, fclose, fprintf, scanf
import exit msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import fprintf msvcrt.dll
import scanf msvcrt.dll

segment data use32 class=data
    ;Se da un nume de fisier (definit in segmentul de date). Sa se creeze un fisier cu numele dat, apoi sa se citeasca de la ;tastatura numere si sa se scrie din valorile citite in fisier numerele divizibile cu 7, pana cand se citeste de la tastatura ;valoarea 0.
    filename db "output.txt", 0
    mode db "w", 0
    format_read db "%d", 0
    format_write db `%d\n`, 0 ;sau pot pune "%d", 13, 10, 0
    input dd 0
    file_ptr dd 0

segment code use32 class=data
start:
    ; fopen(filename, mode)
    push dword mode
    push dword filename
    call [fopen]
    add esp, 8
    cmp eax, 0
    je exit_program                   ; Daca fopen esueaza, ies din program
    mov [file_ptr], eax

read_loop:
    ; scanf("%d", &input)
    push dword input
    push dword format_read
    call [scanf]
    add esp, 8
    
    ; Verific daca numarul este 0
    mov eax, [input]
    cmp eax, 0
    je close_file                     ; Ies din bucla daca se introduce 0
    
    ; Verific daca numarul este divizibil cu 7
    mov edx, 0
    mov ebx, 7
    div ebx
    cmp edx, 0
    jne read_loop                     ; Daca nu e divizibil, citesc urmatorul numar

    ; fprintf(file_ptr, "%d", input)
    push dword [input]        ; Valoarea numarului citit
    push dword format_write   ; Formatul pentru scriere
    push dword [file_ptr]
    call [fprintf]
    add esp, 12

    jmp read_loop                     ; Continui cu urmatorul numar

close_file:
    ; fclose(file_ptr)
    push dword [file_ptr]
    call [fclose]
    add esp, 4

exit_program:
    ; exit(0)
    push dword 0
    call [exit]