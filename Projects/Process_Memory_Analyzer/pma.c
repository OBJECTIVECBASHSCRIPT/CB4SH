#include <sys/ptrace.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

int main(int arc, char *argv[]) {
    pid_t pid = atoi(argv[1]);
    long data;

    if (ptrace(PTRACE_ATTACH, pid, NULL, NULL) == -1) {
        perror("ptrace attach");
        return 1;
    }
    waitpid(pid, NULL, 0);
    
    data = ptrace(PTRACE_PEEKDATA, pid, (void *)0xdeadbeef, NULL);
    printf("Data at address 0xdeadbeef: %lx\n", data);

    ptrace(PTRACE_DETACH, pid, NULL, NULL);
    return 0;
}
