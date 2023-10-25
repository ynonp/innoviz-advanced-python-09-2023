#include <stdio.h>
#include <time.h>
#include <utime.h>

int main(int argc, char **argv)
{
  printf("sizeof(time_t) = %lu\n", sizeof(time_t));
  printf("sizeof(int)    = %lu\n", sizeof(int));
  printf("sizeof(long)   = %lu\n", sizeof(long));

  const struct utimbuf times;
  utime("./starter.py", &times);
  printf("modtime = %ld", times.modtime);

  return 0;
}
