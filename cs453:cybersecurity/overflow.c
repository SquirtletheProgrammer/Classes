#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

void shell() {
    gid_t gid = getegid();
    setresgid(gid, gid, gid);
    system("/bin/sh -i");
}

void message(char *input) {
    char buf[16];
    int secret = 0;
    strcpy(buf, input);

    printf("You said: %s\n", buf);

    if (secret == 0x524B4348) {
        shell();
    } else {
        printf("The secret is 0x%x\n", secret);
    }
}

int main(int argc, char **argv) {
    if (argc > 1){
        message(argv[1]);
    } else {
        printf("Usage: ./overflow <message>\n");
    }
    return 0;
}
