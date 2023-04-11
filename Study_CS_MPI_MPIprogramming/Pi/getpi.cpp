#define _USE_MATH_DEFINES
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<mpi.h>

int n_size_;
int n_rank_;
double eps_precision = 1e-12;

double func_integrand(double u);

int main(int argc, char* argv[]) {
    MPI_Init(&argc, &argv); // 

    MPI_Comm_size(MPI_COMM_WORLD, &n_size_);
    //printf("%d \n", n_size_);

    MPI_Comm_rank(MPI_COMM_WORLD, &n_rank_);
   // printf("%d \n", n_rank_);


    if (n_rank_ == 0) {
        fprintf(stdout, "We have %d processes.\n", n_size_);
        fprintf(stdout, "\n");
    }

    MPI_Barrier(MPI_COMM_WORLD);

    int tag;
    MPI_Status status;

    double pi_now = 0.;
    double pi_prev;
    double pi_rank = 0.;
    double pi_rank_prev;
    int converging = 0;

    unsigned long int nbin_u = 1;

    double u_min = (double)n_rank_ / (double)n_size_;
    double u_max = u_min + 1. / (double)n_size_;
    double delta_u = fabs(u_max - u_min);

    int istep = 1;

    while (converging == 0) {
        pi_prev = pi_now;

        pi_rank_prev = pi_rank;

        pi_rank = 0.;

        unsigned int iu;

        if (istep == 1) {
            for (iu = 0; iu < nbin_u; iu++) {
                double u0 = u_min + delta_u * (double)iu;
                double u1 = u0 + delta_u;
                pi_rank += 0.5 * delta_u * (func_integrand(u0) + func_integrand(u1));
            }
        }
        else {
            pi_rank = 0.5 * pi_rank_prev;
            for (iu = 0; iu <= nbin_u; iu++) {
                if (iu % 2 == 0) {
                    continue;
                }

                double u_now = u_min + delta_u * (double)iu;
                pi_rank += delta_u * func_integrand(u_now);
            }
        }

        pi_now = 0.;

        if (n_rank_ == 0) {
            pi_now = pi_rank;
            for (int irank = 1; irank < n_size_; irank++) {
                tag = 1000 + irank;
                double pi_add;
                MPI_Recv(&pi_add, 1, MPI_DOUBLE, irank, tag, MPI_COMM_WORLD, &status);
                pi_now += pi_add;
            }
            fprintf(stdout, "step %d : pi = %.12f\n", istep, pi_now);
        }
        else {
            tag = 1000 + n_rank_;
            MPI_Send(&pi_rank, 1, MPI_DOUBLE, 0, tag, MPI_COMM_WORLD);
        }

        if (n_rank_ == 0) {
            if (fabs(pi_now - pi_prev) < 0.5 * eps_precision * fabs(pi_now + pi_prev)) {
                converging = 1;
            }

            for (int irank = 1; irank < n_size_; irank++) {
                tag = 2000 + irank;
                MPI_Send(&converging, 1, MPI_INT, irank, tag, MPI_COMM_WORLD);
            }
        }
        else {
            tag = 2000 + n_rank_;
            MPI_Recv(&converging, 1, MPI_INT, 0, tag, MPI_COMM_WORLD, &status);
        }

        istep += 1;
        nbin_u = 2 * nbin_u;
        delta_u = 0.5 * delta_u;
    }

    MPI_Barrier(MPI_COMM_WORLD);

    if (n_rank_ == 0) {
        fprintf(stdout, "\n");

        fprintf(stdout, "pi from numerical integration\n");
        fprintf(stdout, "  > pi = %.12f\n", pi_now);

        fprintf(stdout, "pi from C math library\n");
        fprintf(stdout, "  > pi = %.12f\n", M_PI);
    }

    MPI_Finalize();

    return 0;
}

double func_integrand(double u) {
    return 2. / (fabs(u * u) + fabs((1. - u) * (1. - u)));
}