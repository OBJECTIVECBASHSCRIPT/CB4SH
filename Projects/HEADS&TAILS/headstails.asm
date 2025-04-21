#randomly selects either heads or tails
section .data
    heads_msg db "heads", 0xA         ; newline
    heads_len equ $ - heads_msg

    tails_msg db "tails", 0xA
    tails_len equ $ - tails_msg

section .text
    global _start

_start:
    rdtsc                              ; edx:eax = timestamp counter
    xor eax, edx                       ; mix high and low bits
    and eax, 1                         ; mask last bit

    cmp eax, 0
    je print_heads
    jmp print_tails

#prints heads or tails based on random selection


print_heads:
    mov rax, 1                         ; syscall: write
    mov rdi, 1                         ; stdout
    mov rsi, heads_msg
    mov rdx, heads_len
    syscall
    jmp exit

print_tails:
    mov rax, 1
    mov rdi, 1
    mov rsi, tails_msg
    mov rdx, tails_len
    syscall
    jmp exit

#declares that the heads or tails game is finished once heads or tails has been printed

exit:
    mov rax, 60                        ; syscall: exit
    xor rdi, rdi                       ; status 0
    syscall
