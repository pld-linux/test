#include <fcntl.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define BUF_SIZE 1048576

int write_all(int fd, void* buf, size_t count) {
  int ret;
  int to_write = count;
  do {
    ret = write(fd, buf, to_write);
  } while (ret >= 0 && (to_write -= ret) > 0);

  return ret < 0 ? ret : count;
}

void write_file(char* name, int adflags) {
  char *buf;
  posix_memalign((void**)&buf, 4096, BUF_SIZE);
  memset(buf,0xff,BUF_SIZE);
  int fd = open(name, O_CREAT|O_TRUNC|O_WRONLY, S_IRUSR|S_IWUSR);
  for (int i = 0; i < 8; i++) {
    write_all(fd, buf, BUF_SIZE);
  }
  close(fd);
  fd = open(name, O_WRONLY|adflags);
  lseek(fd, BUF_SIZE, SEEK_SET);
  memset(buf,0,BUF_SIZE);
  write_all(fd, buf, BUF_SIZE);
  close(fd);
}

int main() {
  write_file("file-normal", 0);
  write_file("file-direct-io", O_DIRECT);
}
