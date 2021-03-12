#include <stdio.h>
#define N 19009
void print_array (int A[],int lenght)
{
  for (int j = 0; j < lenght; j++)
    {
      printf (" ,%d", A[j]);
    }
    puts("\n");
}

int my_sort (int A[]){
  // start 
  int tmp,max,min,j,i,counter=0;
  for (j = 0; j < (N + 1) / 2; j++){
        //find max and min of first and end element
        if(A[j] < A[N - j]){
          min = A[j];
          max = A[N - j];
        }
        else{
          min =  A[N - j];
          max =  A[j];
        }
    
        for (i = j+1; i < N - j-1; i++){ 
        	  if (max < A[N - i]){
        	      tmp = A[N - i];
        	      A[N - i] = max;
        	      max = tmp;}
        	  if (min > A[i]){
        	      tmp = A[i];
        	      A[i] = min;
        	      min = tmp;}
              	  counter++;
        } 
    	  // put  min element to the first plase max to the last plase 
        A[j] = min;
        A[N - j] = max;
    }
  //end
  print_array (A);
  return counter;
}



int main ()
{ 
  int A[N + 1] ={1, 4, 3,8,9,0,1,2,3,4,5,6,7,8,9,28,67,58,90};
  print_array(A);
  printf("array sorted by my_sort\ncount of steps: %d\n",my_sort(A));
  return 0;
}
