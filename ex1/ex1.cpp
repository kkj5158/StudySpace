#include <mpi.h>
#include <stdio.h> 
int main() {
	int my_rank, p;
	int a, b; MPI_Status status;
	int source = 1, dest = 0, tag = 5;
	MPI_Init(NULL, NULL);
	MPI_Comm_size(MPI_COMM_WORLD, &p);
	MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);
	if (my_rank == 1) {
		a = 10;
		MPI_Send(&a, 1, MPI_INT, dest, tag, MPI_COMM_WORLD);
	}
	else if (my_rank == 0) {
		MPI_Recv(&b, 1, MPI_INT, source, tag, MPI_COMM_WORLD, &status);
		printf("received date=%d", b);
	}
	MPI_Finalize();
	return 0;
}
