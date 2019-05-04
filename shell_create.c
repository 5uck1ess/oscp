C code to spawn shell 

int main(void) {
setgid(0); setuid(0);
execl("/bin/sh". "sh". 0);
}
