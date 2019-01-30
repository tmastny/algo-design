#include<stdio.h>
#include<stdlib.h>

typedef struct {
  int *array;
  int length;
  int allocated_size;
} Array;

void initArray(Array *a, int initial_size) {
  a->array = malloc(initial_size * sizeof(int));
  a->length = 0;
  a->allocated_size = initial_size;
}

void appendArray(Array *a, int i) {
  if (a->length == a->allocated_size) {
    a->allocated_size *= 2;
    a->array = realloc(a->array, a->allocated_size * sizeof(int));
    printf("resizing up: %d\n", a->allocated_size);
  }
  a->array[a->length++] = i;
}

void popArray(Array *a) {
  int index = a->length--;
  if (index < 5) return;

  if (index < a->allocated_size / 2) {
    a->allocated_size /= 2;
    a->array = realloc(a->array, a->allocated_size * sizeof(int));
    printf("resizing down: %d\n", a->allocated_size);
  }
}



void freeArray(Array *a) {
  free(a->array);
  a->array = NULL;
  a->length = a->allocated_size = 0;
}

int main() {
  Array *arr;
  initArray(arr, 5);

  for (int i = 0; i < 20; i++) {
    appendArray(arr, i);
  }

  while(arr->length > 8) {
    popArray(arr);
  }

  appendArray(arr, 0);
  appendArray(arr, 0);
  appendArray(arr, 0);


  freeArray(arr);
}
